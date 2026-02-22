#!/bin/bash

echo "=== VALIDAÇÃO FASE 3: TESTES ==="
echo ""
echo "Data: $(date '+%Y-%m-%d %H:%M:%S')"
echo ""

# Fetch HTML from preview
curl -s http://localhost:4321/ > /tmp/cbse-fase3.html

echo "## 1. SWIPER - Validação de Código"
echo ""
echo "✓ Swiper CDN presente:"
grep -c "swiper@11" /tmp/cbse-fase3.html
echo ""

echo "✓ Swiper container presente:"
grep -c "depoimentos-swiper" /tmp/cbse-fase3.html
echo ""

echo "✓ Swiper slides (13 depoimentos esperados):"
grep -c "swiper-slide" /tmp/cbse-fase3.html
echo ""

echo "✓ Swiper pagination:"
grep -c "swiper-pagination" /tmp/cbse-fase3.html
echo ""

echo "✓ Swiper init script:"
grep -c "new Swiper" /tmp/cbse-fase3.html
echo ""

echo "## 2. LOADING LAZY - Imagens Críticas (Above the Fold)"
echo ""
echo "⚠️ Imagens no HERO (não devem ter lazy):"
grep -A 10 "hero-bg" /tmp/cbse-fase3.html | grep -c "loading=\"lazy\""
echo "(0 = correto, >0 = problema)"
echo ""

echo "✓ Total de imagens com loading='lazy':"
grep -c "loading=\"lazy\"" /tmp/cbse-fase3.html
echo ""

echo "## 3. FETCHPRIORITY - Imagens Críticas"
echo ""
echo "✓ Imagens com fetchpriority='high':"
grep -c "fetchpriority=\"high\"" /tmp/cbse-fase3.html
echo "(esperado: 2)"
echo ""

echo "✓ Quais imagens têm fetchpriority:"
grep "fetchpriority=\"high\"" /tmp/cbse-fase3.html | grep -o 'href="[^"]*"' | head -5
echo ""

echo "## 4. FAQ ACCORDION - Estrutura"
echo ""
echo "✓ Details tags (FAQ items):"
grep -c "<details" /tmp/cbse-fase3.html
echo ""

echo "✓ Summary tags:"
grep -c "<summary" /tmp/cbse-fase3.html
echo ""

echo "## 5. LOTTIE - Validação"
echo ""
echo "✓ Lottie CDN presente:"
grep -c "lottie" /tmp/cbse-fase3.html
echo ""

echo "✓ Lottie container (ovo mobile):"
grep -c "lottie-ovo" /tmp/cbse-fase3.html
echo ""

echo ""
echo "=== FIM DA VALIDAÇÃO AUTOMATIZADA ==="
echo ""
echo "⚠️ TESTES MANUAIS NECESSÁRIOS:"
echo "1. Abrir http://localhost:4321/ no navegador"
echo "2. Testar Swiper: autoplay, pagination, loop, responsividade"
echo "3. Testar FAQ: abrir/fechar suave, múltiplos itens"
echo "4. Verificar se Lottie (ovo) aparece em mobile"
echo "5. Validar responsividade em 375px, 768px, 1024px, 1366px"

