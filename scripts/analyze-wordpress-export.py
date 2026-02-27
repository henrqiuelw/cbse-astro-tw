#!/usr/bin/env python3
"""
Analisa export XML do WordPress para extrair dados do Elementor.
"""

import xml.etree.ElementTree as ET
import json
import gzip
import sys
import os
from collections import defaultdict

def analyze_xml_file(xml_file):
    """Analisa arquivo XML do WordPress export."""
    print(f"📂 Analisando: {xml_file}")
    print(f"📏 Tamanho: {os.path.getsize(xml_file) / 1024 / 1024:.2f} MB")
    
    try:
        # Tentar parsear o XML
        print("🔍 Parseando XML...")
        tree = ET.parse(xml_file)
        root = tree.getroot()
        
        # Namespace do WordPress
        ns = {'wp': 'http://wordpress.org/export/1.2/',
              'excerpt': 'http://wordpress.org/export/1.2/excerpt/'}
        
        # Estatísticas
        stats = defaultdict(int)
        elementor_pages = []
        all_meta = []
        
        # Encontrar todos os itens (posts/pages)
        for item in root.findall('.//item'):
            stats['total_items'] += 1
            
            # Tipo de post
            post_type = item.find('wp:post_type', ns)
            if post_type is not None:
                stats[f'type_{post_type.text}'] += 1
            
            # Status
            status = item.find('wp:status', ns)
            if status is not None:
                stats[f'status_{status.text}'] += 1
            
            # Coletar metadados
            for meta in item.findall('wp:postmeta', ns):
                meta_key = meta.find('wp:meta_key', ns)
                meta_value = meta.find('wp:meta_value', ns)
                
                if meta_key is not None and meta_value is not None:
                    key = meta_key.text
                    value = meta_value.text
                    
                    stats['total_meta'] += 1
                    stats[f'meta_{key}'] = stats.get(f'meta_{key}', 0) + 1
                    
                    # Verificar se é Elementor data
                    if key == '_elementor_data':
                        stats['has_elementor_data'] += 1
                        
                        # Tentar parsear JSON
                        try:
                            elementor_json = json.loads(value)
                            page_title = item.find('title').text if item.find('title') is not None else 'Sem título'
                            page_id = item.find('wp:post_id', ns)
                            page_id = page_id.text if page_id is not None else 'N/A'
                            
                            elementor_pages.append({
                                'id': page_id,
                                'title': page_title,
                                'elementor_data': elementor_json,
                                'meta_value_length': len(value)
                            })
                            
                            print(f"   ✅ Página {page_id}: '{page_title[:50]}...' - Elementor data: {len(value):,} chars")
                            
                        except json.JSONDecodeError as e:
                            print(f"   ❌ Erro ao parsear JSON Elementor: {e}")
                            stats['elementor_json_errors'] += 1
                    
                    # Coletar amostra de metadados
                    if stats['total_meta'] <= 10:  # Primeiros 10
                        all_meta.append({
                            'key': key,
                            'value_preview': str(value)[:100] + ('...' if len(str(value)) > 100 else '')
                        })
        
        # Exibir estatísticas
        print("\n📊 ESTATÍSTICAS:")
        print(f"   Total de itens: {stats['total_items']}")
        
        # Tipos de conteúdo
        print("   Tipos de conteúdo:")
        for key, count in stats.items():
            if key.startswith('type_'):
                print(f"     - {key[5:]}: {count}")
        
        # Status
        print("   Status:")
        for key, count in stats.items():
            if key.startswith('status_'):
                print(f"     - {key[7:]}: {count}")
        
        # Metadados
        print(f"\n   Total de metadados: {stats['total_meta']}")
        print("   Metadados mais comuns:")
        meta_counts = [(k[5:], v) for k, v in stats.items() if k.startswith('meta_') and k != 'meta_total']
        meta_counts.sort(key=lambda x: x[1], reverse=True)
        for key, count in meta_counts[:10]:
            print(f"     - {key}: {count}")
        
        # Elementor
        print(f"\n   🎨 Elementor:")
        print(f"     - Páginas com _elementor_data: {stats.get('has_elementor_data', 0)}")
        if stats.get('elementor_json_errors', 0) > 0:
            print(f"     - Erros no JSON: {stats['elementor_json_errors']}")
        
        # Amostra de metadados
        print(f"\n   📋 Amostra de metadados (primeiros 10):")
        for meta in all_meta:
            print(f"     - {meta['key']}: {meta['value_preview']}")
        
        # Salvar dados do Elementor se encontrados
        if elementor_pages:
            output_file = 'elementor-data-extracted.json'
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(elementor_pages, f, indent=2, ensure_ascii=False)
            print(f"\n💾 Dados do Elementor salvos em: {output_file}")
            
            # Analisar estrutura do Elementor
            analyze_elementor_structure(elementor_pages)
        
        return True, elementor_pages
        
    except ET.ParseError as e:
        print(f"❌ Erro ao parsear XML: {e}")
        return False, None
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        return False, None

def analyze_elementor_structure(elementor_pages):
    """Analisa a estrutura dos dados do Elementor."""
    print("\n🔬 ANÁLISE DA ESTRUTURA DO ELEMENTOR:")
    
    for page in elementor_pages:
        print(f"\n   📄 Página: {page['title'][:50]}... (ID: {page['id']})")
        elementor_data = page['elementor_data']
        
        if isinstance(elementor_data, list):
            print(f"     - Tipo: Lista com {len(elementor_data)} elementos")
            
            # Analisar primeiros elementos
            for i, element in enumerate(elementor_data[:3]):
                if isinstance(element, dict):
                    print(f"     - Elemento {i}: {element.get('elType', 'N/A')} - {element.get('widgetType', 'N/A')}")
                    
                    # Verificar estilos
                    if 'settings' in element:
                        settings = element['settings']
                        if isinstance(settings, dict):
                            style_keys = [k for k in settings.keys() if 'style' in k.lower() or 'padding' in k or 'margin' in k]
                            if style_keys:
                                print(f"       Estilos encontrados: {', '.join(style_keys[:5])}")
                                if len(style_keys) > 5:
                                    print(f"       ... e mais {len(style_keys) - 5}")
        
        elif isinstance(elementor_data, dict):
            print(f"     - Tipo: Dicionário")
            print(f"     - Keys: {list(elementor_data.keys())}")
        
        # Verificar tamanho
        data_str = json.dumps(elementor_data)
        print(f"     - Tamanho JSON: {len(data_str):,} chars")

def main():
    if len(sys.argv) < 2:
        print("Uso: python analyze-wordpress-export.py <arquivo-xml>")
        print("Exemplo: python analyze-wordpress-export.py wordpress-export.xml")
        sys.exit(1)
    
    xml_file = sys.argv[1]
    
    if not os.path.exists(xml_file):
        print(f"❌ Arquivo não encontrado: {xml_file}")
        sys.exit(1)
    
    success, elementor_data = analyze_xml_file(xml_file)
    
    if success and elementor_data:
        print("\n✅ Análise concluída com sucesso!")
        print("📋 Próximos passos:")
        print("   1. Os dados do Elementor foram extraídos e salvos")
        print("   2. Podemos começar a mapear estilos → Tailwind")
        print("   3. Criar componentes Astro seção por seção")
    else:
        print("\n⚠️  Nenhum dado do Elementor encontrado no XML.")
        print("📋 Alternativas:")
        print("   1. Verificar se export incluiu metadados")
        print("   2. Tentar export com plugin 'All-in-One WP Migration'")
        print("   3. Capturar dados via browser (DevTools)")

if __name__ == "__main__":
    main()