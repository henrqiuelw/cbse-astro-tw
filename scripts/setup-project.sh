#!/bin/bash
# Setup do projeto CBSE Migração 3.0

echo "🚀 Configurando projeto CBSE Migração 3.0"
echo "=========================================="

# Criar estrutura de diretórios
echo "📁 Criando estrutura de diretórios..."
mkdir -p scripts data/elementor-json data/screenshots data/assets docs src/components src/layouts src/pages

# Verificar dependências
echo "🔧 Verificando dependências..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 não encontrado. Instale com: brew install python"
    exit 1
fi

# Verificar módulos Python
echo "📦 Verificando módulos Python..."
python3 -c "import xml.etree.ElementTree" 2>/dev/null || echo "⚠️  xml.etree.ElementTree disponível"
python3 -c "import json" 2>/dev/null || echo "✅ json disponível"

# Tornar scripts executáveis
echo "🔧 Configurando scripts..."
chmod +x scripts/*.py scripts/*.sh 2>/dev/null || true

# Criar arquivos de configuração
echo "📝 Criando arquivos de configuração..."

# .gitignore
cat > .gitignore << EOF
# Dados temporários
data/screenshots/*
data/elementor-json/*.json
!data/elementor-json/README.md

# Python
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
env/
venv/

# Node/Astro
node_modules/
dist/
*.log
.DS_Store
EOF

# requirements.txt (se precisarmos)
cat > requirements.txt << EOF
# Python dependencies for CBSE migration
# Install with: pip3 install -r requirements.txt

# XML/JSON processing
# (built-in: xml.etree.ElementTree, json)

# HTTP requests (for API calls)
# requests==2.31.0

# Image processing (for screenshot analysis)
# Pillow==10.1.0

# Optional: for better XML parsing
# lxml==4.9.3
EOF

echo "✅ Setup completo!"
echo ""
echo "📋 Próximos passos:"
echo "   1. Colocar o XML export do WordPress em data/"
echo "   2. Executar: python3 scripts/analyze-wordpress-export.py data/export.xml"
echo "   3. Analisar dados do Elementor extraídos"
echo "   4. Começar migração seção por seção"
echo ""
echo "📁 Estrutura criada:"
find . -type d -not -path "./.*" | sort