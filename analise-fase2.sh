#!/bin/bash

echo "=== ANÁLISE FASE 2: CORREÇÕES CRÍTICAS ==="
echo ""

# 1. Contagem de fetchpriority
echo "1. FETCHPRIORITY:"
echo "   v2.0 reference:"
grep -c 'fetchpriority="high"' v2.0-reference.html || echo "   0 occurrences"
echo "   Astro renderizado:"
grep -c 'fetchpriority="high"' /tmp/cbse-astro-rendered.html || echo "   0 occurrences"
echo ""

# 2. Contagem de loading="lazy"
echo "2. LOADING LAZY:"
echo "   v2.0 reference:"
grep -c 'loading="lazy"' v2.0-reference.html || echo "   0 occurrences"
echo "   Astro renderizado:"
grep -c 'loading="lazy"' /tmp/cbse-astro-rendered.html || echo "   0 occurrences"
echo ""

# 3. Imagens sem lazy loading (exceto hero)
echo "3. IMAGENS SEM OTIMIZAÇÃO:"
echo "   Procurando <img> sem loading='lazy' (exceto hero)..."
grep -n '<img' /tmp/cbse-astro-rendered.html | grep -v 'loading=' | head -5
echo ""

# 4. Swiper config
echo "4. SWIPER CONFIG:"
if grep -q "swiper" /tmp/cbse-astro-rendered.html; then
  echo "   Swiper encontrado no HTML"
  grep -A 5 "new Swiper" /tmp/cbse-astro-rendered.html | head -10
else
  echo "   Swiper NÃO encontrado no HTML renderizado"
fi
echo ""

# 5. FAQ accordion
echo "5. FAQ ACCORDION:"
if grep -q "accordion" /tmp/cbse-astro-rendered.html; then
  echo "   Accordion encontrado"
else
  echo "   Verificando <details> tags..."
  grep -c "<details" /tmp/cbse-astro-rendered.html || echo "   0 occorrências"
fi
echo ""

# 6. Lottie
echo "6. LOTTIE:"
if grep -q "lottie" /tmp/cbse-astro-rendered.html; then
  echo "   Lottie encontrado"
  grep -B 2 -A 2 "lottie" /tmp/cbse-astro-rendered.html | head -10
else
  echo "   Lottie NÃO encontrado"
fi
echo ""

# 7. Textos da seção MÉTODO - Card 1
echo "7. TEXTOS SEÇÃO MÉTODO - Card 1:"
echo "   === v2.0 reference ===" 
grep -A 15 "Método Estruturado" v2.0-reference.html | grep -E "(Método|nutricionista|opiniões)" | head -3

echo ""
echo "   === Astro renderizado ==="
grep -A 15 "Método Estruturado" /tmp/cbse-astro-rendered.html | grep -E "(Método|nutricionista|opiniões)" | head -3
echo ""

