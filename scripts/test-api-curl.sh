#!/bin/bash
# Teste de API usando curl (não precisa de Python requests)

SITE_URL="https://comerbemsemestresse.com.br"

echo "🚀 Testando API do WordPress.com"
echo "🌐 Site: $SITE_URL"
echo "=" * 60

test_endpoint() {
    local endpoint=$1
    local description=$2
    local url="${SITE_URL}${endpoint}"
    
    echo -e "\n🔍 Testando: $description"
    echo "   URL: $url"
    
    # Usar curl com timeout
    response=$(curl -s -w "%{http_code}" -o /tmp/curl_output.txt --max-time 10 "$url")
    http_code=${response: -3}
    body=$(cat /tmp/curl_output.txt)
    
    echo "   Status: $http_code"
    
    if [ "$http_code" = "200" ]; then
        echo "   ✅ OK"
        
        # Tentar parsear JSON se possível
        if command -v python3 &> /dev/null; then
            echo "$body" | python3 -m json.tool 2>/dev/null | head -20
        elif command -v jq &> /dev/null; then
            echo "$body" | jq '.' 2>/dev/null | head -20
        else
            echo "   📄 Resposta (primeiras 500 chars):"
            echo "$body" | head -c 500
            echo "..."
        fi
        
        # Salvar resposta se for páginas
        if [[ "$endpoint" == *"wp/v2/pages"* ]]; then
            echo "$body" > "api-pages.json"
            echo "   💾 Dados salvos em api-pages.json"
            
            # Contar páginas
            if command -v python3 &> /dev/null; then
                count=$(echo "$body" | python3 -c "import sys,json; print(len(json.load(sys.stdin)))" 2>/dev/null || echo "?")
                echo "   📄 Páginas encontradas: $count"
            fi
        fi
        
        return 0
    elif [ "$http_code" = "401" ]; then
        echo "   🔒 Acesso não autorizado"
    elif [ "$http_code" = "403" ]; then
        echo "   🚫 Acesso proibido"
    elif [ "$http_code" = "404" ]; then
        echo "   ❌ Endpoint não encontrado"
    elif [ "$http_code" = "000" ]; then
        echo "   ⏰ Timeout ou erro de conexão"
    else
        echo "   ⚠️  Status inesperado: $http_code"
    fi
    
    return 1
}

# Testar endpoints
test_endpoint "/wp-json/wp/v2/pages" "Lista de páginas"
test_endpoint "/wp-json/wp/v2/pages?per_page=10&status=publish" "Páginas publicadas"
test_endpoint "/wp-json/elementor/v1/globals" "Dados globais do Elementor"
test_endpoint "/wp-json/" "Discovery (todos endpoints)"

echo -e "\n" && echo "=" * 60
echo "📊 Teste completo. Verifique os resultados acima."

# Verificar se temos dados
if [ -f "api-pages.json" ]; then
    echo -e "\n📋 Páginas disponíveis para migração:"
    if command -v python3 &> /dev/null; then
        python3 -c "
import json
with open('api-pages.json', 'r') as f:
    pages = json.load(f)
for page in pages[:5]:
    print(f'  - ID: {page.get(\"id\")}, Title: {page.get(\"title\", {}).get(\"rendered\", \"N/A\")[:50]}..., Slug: {page.get(\"slug\")}')
if len(pages) > 5:
    print(f'  ... e mais {len(pages) - 5} páginas')
" 2>/dev/null || echo "  (Não foi possível parsear JSON)"
    fi
fi