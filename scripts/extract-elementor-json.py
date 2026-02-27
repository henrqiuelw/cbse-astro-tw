#!/usr/bin/env python3
"""
Extrai JSON do Elementor do XML do WordPress.
"""

import re
import json
import sys
import os

def extract_elementor_data(xml_content):
    """Extrai dados do Elementor do conteúdo XML."""
    print("🔍 Procurando _elementor_data no XML...")
    
    # Padrão para encontrar _elementor_data
    pattern = r'<wp:meta_key><!\[CDATA\[_elementor_data\]\]></wp:meta_key>\s*<wp:meta_value><!\[CDATA\[(.*?)\]\]></wp:meta_value>'
    
    matches = re.findall(pattern, xml_content, re.DOTALL)
    
    if not matches:
        print("❌ Nenhum _elementor_data encontrado no XML")
        return None
    
    print(f"✅ Encontrados {len(matches)} blocos de _elementor_data")
    
    elementor_data_list = []
    
    for i, match in enumerate(matches[:5]):  # Limitar a 5 para análise
        print(f"\n📦 Processando bloco {i+1}...")
        
        # O conteúdo pode estar truncado no print, mas vamos tentar parsear
        json_str = match
        
        print(f"   Tamanho do JSON: {len(json_str):,} caracteres")
        print(f"   Primeiros 200 chars: {json_str[:200]}...")
        
        try:
            # Tentar parsear o JSON
            elementor_json = json.loads(json_str)
            print(f"   ✅ JSON parseado com sucesso")
            print(f"   Tipo: {type(elementor_json)}")
            
            if isinstance(elementor_json, list):
                print(f"   Elementos na lista: {len(elementor_json)}")
                if elementor_json:
                    first_item = elementor_json[0]
                    print(f"   Primeiro elemento - elType: {first_item.get('elType', 'N/A')}, id: {first_item.get('id', 'N/A')}")
            
            elementor_data_list.append({
                'index': i,
                'size': len(json_str),
                'data': elementor_json,
                'type': type(elementor_json).__name__
            })
            
            # Salvar em arquivo separado
            output_file = f"data/elementor-json/page-{i+1}.json"
            os.makedirs(os.path.dirname(output_file), exist_ok=True)
            
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(elementor_json, f, indent=2, ensure_ascii=False)
            
            print(f"   💾 Salvo em: {output_file}")
            
        except json.JSONDecodeError as e:
            print(f"   ❌ Erro ao parsear JSON: {e}")
            print(f"   Posição do erro: {e.pos}")
            print(f"   Linha: {e.lineno}, coluna: {e.colno}")
            
            # Tentar encontrar onde está o problema
            if e.pos < len(json_str):
                context_start = max(0, e.pos - 50)
                context_end = min(len(json_str), e.pos + 50)
                print(f"   Contexto do erro: ...{json_str[context_start:context_end]}...")
    
    return elementor_data_list

def analyze_elementor_structure(elementor_data):
    """Analisa a estrutura dos dados do Elementor."""
    print("\n🔬 ANÁLISE DA ESTRUTURA DO ELEMENTOR:")
    
    if not elementor_data:
        print("   Nenhum dado para analisar")
        return
    
    for item in elementor_data:
        print(f"\n   📄 Bloco {item['index'] + 1} (tipo: {item['type']}, tamanho: {item['size']:,} chars)")
        
        data = item['data']
        
        if isinstance(data, list):
            print(f"   📋 Lista com {len(data)} elementos (containers/seções)")
            
            # Analisar cada container/seção
            for i, element in enumerate(data[:3]):  # Analisar apenas 3 primeiros
                if isinstance(element, dict):
                    el_type = element.get('elType', 'N/A')
                    widget_type = element.get('widgetType', 'N/A')
                    element_id = element.get('id', 'N/A')
                    
                    print(f"   ├── Elemento {i}: id={element_id}, elType={el_type}, widgetType={widget_type}")
                    
                    # Verificar settings (onde estão os estilos)
                    if 'settings' in element:
                        settings = element['settings']
                        if isinstance(settings, dict):
                            # Contar quantos estilos temos
                            style_keys = [k for k in settings.keys() if any(style_word in k.lower() for style_word in ['style', 'padding', 'margin', 'color', 'font', 'size', 'width', 'height'])]
                            print(f"   │   ├── Settings: {len(settings.keys())} propriedades")
                            print(f"   │   ├── Estilos encontrados: {len(style_keys)}")
                            
                            # Mostrar alguns estilos importantes
                            important_styles = []
                            for key in style_keys[:10]:  # Limitar a 10
                                value = settings[key]
                                if isinstance(value, dict) and 'unit' in value and 'size' in value:
                                    important_styles.append(f"{key}: {value.get('size')}{value.get('unit')}")
                                elif isinstance(value, (str, int, float)):
                                    important_styles.append(f"{key}: {value}")
                            
                            if important_styles:
                                print(f"   │   └── Exemplos: {', '.join(important_styles[:5])}")
                            
                            # Verificar breakpoints (mobile, tablet)
                            has_mobile = any('mobile' in k.lower() for k in settings.keys())
                            has_tablet = any('tablet' in k.lower() for k in settings.keys())
                            print(f"   │   └── Breakpoints: mobile={has_mobile}, tablet={has_tablet}")
                    
                    # Verificar elementos filhos
                    if 'elements' in element and element['elements']:
                        print(f"   │   └── Elementos filhos: {len(element['elements'])}")
            
            if len(data) > 3:
                print(f"   └── ... e mais {len(data) - 3} elementos")
        
        elif isinstance(data, dict):
            print(f"   📋 Dicionário com keys: {list(data.keys())}")

def main():
    if len(sys.argv) < 2:
        print("Uso: python extract-elementor-json.py <arquivo-xml>")
        print("Exemplo: python extract-elementor-json.py wordpress-export.xml")
        sys.exit(1)
    
    xml_file = sys.argv[1]
    
    if not os.path.exists(xml_file):
        print(f"❌ Arquivo não encontrado: {xml_file}")
        sys.exit(1)
    
    print(f"📖 Lendo arquivo: {xml_file}")
    print(f"📏 Tamanho: {os.path.getsize(xml_file) / 1024 / 1024:.2f} MB")
    
    try:
        with open(xml_file, 'r', encoding='utf-8') as f:
            xml_content = f.read()
    except UnicodeDecodeError:
        with open(xml_file, 'r', encoding='latin-1') as f:
            xml_content = f.read()
    
    print(f"📄 Conteúdo lido: {len(xml_content):,} caracteres")
    
    # Extrair dados do Elementor
    elementor_data = extract_elementor_data(xml_content)
    
    if elementor_data:
        print(f"\n🎉 SUCESSO! Extraídos {len(elementor_data)} blocos de dados do Elementor")
        
        # Analisar estrutura
        analyze_elementor_structure(elementor_data)
        
        print("\n📋 PRÓXIMOS PASSOS:")
        print("   1. Os dados do Elementor foram salvos em data/elementor-json/")
        print("   2. Podemos começar a mapear estilos → Tailwind")
        print("   3. Criar componentes Astro seção por seção")
        
        # Criar resumo
        with open('data/elementor-summary.md', 'w', encoding='utf-8') as f:
            f.write("# Resumo dos Dados do Elementor\n\n")
            f.write(f"**Total de páginas com dados:** {len(elementor_data)}\n\n")
            
            for i, item in enumerate(elementor_data):
                f.write(f"## Página {i+1}\n")
                f.write(f"- **Tipo:** {item['type']}\n")
                f.write(f"- **Tamanho:** {item['size']:,} caracteres\n")
                
                data = item['data']
                if isinstance(data, list):
                    f.write(f"- **Elementos:** {len(data)} containers/seções\n")
                    
                    # Contar tipos de elementos
                    el_types = {}
                    for element in data[:10]:  # Apenas 10 primeiros
                        el_type = element.get('elType', 'desconhecido')
                        el_types[el_type] = el_types.get(el_type, 0) + 1
                    
                    if el_types:
                        f.write("- **Distribuição:**\n")
                        for el_type, count in el_types.items():
                            f.write(f"  - {el_type}: {count}\n")
                
                f.write("\n")
        
        print("   📝 Resumo salvo em: data/elementor-summary.md")
        
    else:
        print("\n⚠️  Não foi possível extrair dados do Elementor")
        print("📋 Possíveis problemas:")
        print("   1. O XML pode estar malformado")
        print("   2. O export não incluiu metadados do Elementor")
        print("   3. O conteúdo está truncado")
        print("\n💡 Sugestões:")
        print("   1. Verificar se o export inclui 'Todos os conteúdos'")
        print("   2. Tentar export com plugin 'All-in-One WP Migration'")
        print("   3. Usar captura via browser como fallback")

if __name__ == "__main__":
    main()