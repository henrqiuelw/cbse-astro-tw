#!/bin/bash
# Testar endpoints do Jetpack/WordPress.com API

SITE_URL="https://comerbemsemestresse.com.br"
PAGE_ID="11724"  # Página principal CBSE

echo "🚀 Testando API Jetpack/WordPress.com"
echo "🌐 Site: $SITE_URL"
echo "📄 Página ID: $PAGE_ID"
echo "=" * 60

test_endpoint() {
    local endpoint=$1
    local description=$2
    local url="${SITE_URL}${endpoint}"
    
    echo -e "\n🔍 Testando: $description"
    echo "   URL: $url"
    
    response=$(curl -s -w "%{http_code}" -o /tmp/curl_output.txt --max-time 10 "$url")
    http_code=${response: -3}
    body=$(cat /tmp/curl_output.txt)
    
    echo "   Status: $http_code"
    
    if [ "$http_code" = "200" ]; then
        echo "   ✅ OK"
        
        # Verificar se tem _elementor_data
        if echo "$body" | grep -q "_elementor_data"; then
            echo "   🎨 ENCONTRADO: _elementor_data no response!"
            
            # Extrair e salvar
            echo "$body" > "api-page-${PAGE_ID}-full.json"
            echo "   💾 Dados completos salvos em api-page-${PAGE_ID}-full.json"
            
            # Tentar extrair apenas elementor_data
            if command -v python3 &> /dev/null; then
                python3 -c "
import json, sys
try:
    with open('api-page-${PAGE_ID}-full.json', 'r') as f:
        data = json.load(f)
    
    # Procurar _elementor_data em diferentes lugares
    elementor_data = None
    
    if 'meta' in data and '_elementor_data' in data['meta']:
        elementor_data = data['meta']['_elementor_data']
        print('   📍 Encontrado em data[\"meta\"][\"_elementor_data\"]')
    elif 'acf' in data and '_elementor_data' in data['acf']:
        elementor_data = data['acf']['_elementor_data']
        print('   📍 Encontrado em data[\"acf\"][\"_elementor_data\"]')
    else:
        # Procurar recursivamente
        import json
        data_str = json.dumps(data)
        if '\"_elementor_data\"' in data_str:
            print('   🔎 _elementor_data encontrado no JSON, mas não parseado')
            # Salvar resposta completa para análise
            with open('api-page-${PAGE_ID}-raw.txt', 'w') as f:
                f.write(data_str[:5000])
                f.write('\\n... [truncated]')
    
    if elementor_data:
        # Salvar elementor_data separadamente
        with open('elementor-data-${PAGE_ID}.json', 'w') as f:
            if isinstance(elementor_data, str):
                # Pode ser JSON stringificado
                try:
                    parsed = json.loads(elementor_data)
                    json.dump(parsed, f, indent=2)
                    print(f'   💾 Elementor data parseado e salvo ({len(json.dumps(parsed)):,} chars)')
                except:
                    f.write(elementor_data)
                    print(f'   💾 Elementor data salvo como string ({len(elementor_data):,} chars)')
            else:
                json.dump(elementor_data, f, indent=2)
                print(f'   💾 Elementor data salvo ({len(json.dumps(elementor_data)):,} chars)')
                
except Exception as e:
    print(f'   ❌ Erro ao processar: {e}')
" 2>/dev/null || echo "   ⚠️  Não foi possível processar JSON"
            fi
        else
            echo "   ❌ NÃO contém _elementor_data"
            
            # Verificar estrutura
            echo "   📋 Estrutura do response (primeiros 2KB):"
            echo "$body" | head -c 2000
            echo "..."
        fi
        
        return 0
    elif [ "$http_code" = "401" ] || [ "$http_code" = "403" ]; then
        echo "   🔒 Acesso não autorizado - precisa de autenticação"
    elif [ "$http_code" = "404" ]; then
        echo "   ❌ Endpoint não encontrado"
    else
        echo "   ⚠️  Status: $http_code"
    fi
    
    return 1
}

# Testar diferentes endpoints
echo "📋 Testando endpoints disponíveis:"

# 1. Página normal
test_endpoint "/wp-json/wp/v2/pages/${PAGE_ID}" "Página normal (view)"

# 2. Página com context=edit (pode mostrar mais dados)
test_endpoint "/wp-json/wp/v2/pages/${PAGE_ID}?context=edit" "Página edit mode"

# 3. Jetpack API
test_endpoint "/wp-json/jetpack/v4/" "Jetpack API root"

# 4. Site health (pode dar informações)
test_endpoint "/wp-json/wp-site-health/v1/tests" "Site health"

# 5. Custom fields
test_endpoint "/wp-json/wp/v2/pages/${PAGE_ID}?_fields=id,title,meta" "Apenas meta fields"

echo -e "\n" && echo "=" * 60
echo "📊 Teste completo."

# Verificar se conseguimos dados
if [ -f "elementor-data-${PAGE_ID}.json" ]; then
    echo -e "\n🎉 SUCESSO! Dados do Elementor extraídos!"
    echo "   Arquivo: elementor-data-${PAGE_ID}.json"
    echo "   Próximo passo: Analisar estrutura do Elementor"
elif [ -f "api-page-${PAGE_ID}-full.json" ]; then
    echo -e "\n⚠️  Temos dados da página, mas não extraímos _elementor_data"
    echo "   Próximo passo: Analisar manualmente o JSON"
else
    echo -e "\n❌ Não conseguimos dados via API pública"
    echo "   Próximas opções:"
    echo "   1. Export XML do WordPress (já temos)"
    echo "   2. Autenticação OAuth na API"
    echo "   3. Captura via browser"
fi