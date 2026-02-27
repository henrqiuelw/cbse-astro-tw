#!/usr/bin/env python3
"""
Teste de acesso à API do WordPress.com para extrair dados do Elementor.
"""

import requests
import json
import sys
from urllib.parse import urljoin

SITE_URL = "https://comerbemsemestresse.com.br"

# Endpoints para testar
ENDPOINTS = [
    "/wp-json/wp/v2/pages",           # Lista de páginas
    "/wp-json/wp/v2/pages?per_page=10&status=publish",  # Páginas publicadas
    "/wp-json/elementor/v1/globals",  # Dados globais do Elementor
    "/wp-json/",                      # Discovery (lista todos endpoints)
]

def test_endpoint(endpoint):
    """Testa um endpoint da API."""
    url = urljoin(SITE_URL, endpoint)
    print(f"\n🔍 Testando: {url}")
    
    try:
        response = requests.get(url, timeout=10)
        print(f"   Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            
            if endpoint == "/wp-json/wp/v2/pages":
                print(f"   📄 Páginas encontradas: {len(data)}")
                for page in data[:3]:  # Mostrar apenas 3
                    print(f"      - ID: {page.get('id')}, Title: {page.get('title', {}).get('rendered', 'N/A')}, Slug: {page.get('slug')}")
                if len(data) > 3:
                    print(f"      ... e mais {len(data) - 3} páginas")
            
            elif endpoint == "/wp-json/elementor/v1/globals":
                print(f"   🎨 Dados Elementor globais: {len(data) if isinstance(data, dict) else 'N/A'}")
                if data:
                    print(f"      Keys: {list(data.keys())}")
            
            elif endpoint == "/wp-json/":
                print(f"   📋 Endpoints disponíveis:")
                if 'routes' in data:
                    elementor_routes = [k for k in data['routes'].keys() if 'elementor' in k.lower()]
                    print(f"      Routes Elementor: {len(elementor_routes)}")
                    for route in elementor_routes[:5]:
                        print(f"        - {route}")
                    if len(elementor_routes) > 5:
                        print(f"        ... e mais {len(elementor_routes) - 5}")
            
            return True, data
            
        elif response.status_code == 401:
            print("   🔒 Acesso não autorizado - API pode exigir autenticação")
        elif response.status_code == 403:
            print("   🚫 Acesso proibido - WordPress.com bloqueando")
        elif response.status_code == 404:
            print("   ❌ Endpoint não encontrado")
        else:
            print(f"   ⚠️  Status inesperado: {response.status_code}")
            
        return False, None
        
    except requests.exceptions.Timeout:
        print("   ⏰ Timeout - Site pode estar lento ou bloqueando")
        return False, None
    except requests.exceptions.ConnectionError:
        print("   🔌 Erro de conexão - Site pode não estar acessível")
        return False, None
    except Exception as e:
        print(f"   ❌ Erro: {e}")
        return False, None

def main():
    print("🚀 Testando API do WordPress.com")
    print(f"🌐 Site: {SITE_URL}")
    print("=" * 60)
    
    results = {}
    any_success = False
    
    for endpoint in ENDPOINTS:
        success, data = test_endpoint(endpoint)
        results[endpoint] = success
        if success:
            any_success = True
            
            # Salvar dados se for útil
            if endpoint == "/wp-json/wp/v2/pages" and data:
                with open("api-pages.json", "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                print("   💾 Dados salvos em api-pages.json")
    
    print("\n" + "=" * 60)
    print("📊 Resumo dos testes:")
    
    for endpoint, success in results.items():
        status = "✅ OK" if success else "❌ Falhou"
        print(f"  {status} {endpoint}")
    
    if not any_success:
        print("\n⚠️  Nenhum endpoint acessível via API pública.")
        print("📋 Próximas opções:")
        print("   1. Export via WordPress.com Tools (XML)")
        print("   2. Captura via browser (DevTools + JavaScript)")
        print("   3. Plugin de export Elementor (se permitido)")
    
    return any_success

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)