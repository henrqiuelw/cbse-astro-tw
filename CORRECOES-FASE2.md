# CORREÇÕES FASE 2: Otimizações Críticas

**Data:** 2026-02-22  
**Status:** Em andamento

---

## 📊 Diagnóstico

### 1. Fetchpriority (CRÍTICO)
- **v2.0:** 2 imagens com `fetchpriority="high"`
- **Astro:** 1 imagem com `fetchpriority="high"`
- **Ação:** ✅ Verificar qual imagem está faltando e adicionar

### 2. Loading Lazy
- **v2.0:** 1 imagem com `loading="lazy"`
- **Astro:** 6 imagens com `loading="lazy"`
- **Ação:** ⚠️ Validar se não há lazy loading em imagens críticas (above the fold)

### 3. Swiper (CRÍTICO ❌)
- **v2.0:** Swiper implementado via CDN + init
- **Astro:** Swiper NÃO encontrado no HTML renderizado
- **Ação:** 🚨 **ALTA PRIORIDADE** - Implementar Swiper para depoimentos

### 4. Lottie (✅)
- **Status:** Encontrado e funcionando
- **Ação:** Validar script está com `defer`

### 5. FAQ Accordion (✅)
- **Status:** Implementado com `<details>`
- **Ação:** Validar animação suave (transition)

---

## 🎯 Prioridades

### ALTA (fazer primeiro)
1. **Implementar Swiper** - depoimentos não funcionam sem ele
2. **Corrigir fetchpriority** - impacta PageSpeed mobile

### MÉDIA
3. **Revisar loading="lazy"** - garantir imagens críticas sem lazy
4. **Validar FAQ transitions** - UX importante

### BAIXA
5. **Validar Lottie defer** - já está funcionando

---

## 📝 Plano de Ação

### Correção 1: Swiper (URGENTE)
**Arquivo:** `src/components/Depoimentos.astro`

**Problema:** Swiper não está sendo carregado/inicializado

**Solução:**
```astro
<!-- Adicionar CDN no <head> via Layout -->
<script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js" defer></script>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css">

<!-- Init script no componente -->
<script>
document.addEventListener('DOMContentLoaded', () => {
  new Swiper('.depoimentos-swiper', {
    slidesPerView: 2,
    spaceBetween: 15,
    loop: true,
    autoplay: { delay: 5000 },
    pagination: { el: '.swiper-pagination', clickable: true },
    breakpoints: {
      768: { slidesPerView: 3, spaceBetween: 20 },
      1024: { slidesPerView: 5, spaceBetween: 20 }
    }
  });
});
</script>
```

### Correção 2: Fetchpriority
**Arquivo:** `src/components/Hero.astro`

**Verificar:**
- Logo SVG do hero precisa de `fetchpriority="high"`? (provavelmente não, é SVG)
- Background image do hero (093713-copy.webp) - já tem preload no <head>
- Imagem do vídeo poster (100104.webp) - candidata a fetchpriority="high"

**Ação:**
Adicionar `fetchpriority="high"` no poster do vídeo se não tiver.

### Correção 3: Loading Lazy
**Verificar imagens above-the-fold:**
- Logo hero
- Poster do vídeo
- Primeira seção de ícones (setas verdes)

**Ação:**
Remover `loading="lazy"` de qualquer imagem visível no primeiro viewport.

### Correção 4: FAQ Transitions
**Arquivo:** `src/components/ComoFunciona.astro`

**Validar CSS:**
```css
details {
  transition: all 0.3s ease-out;
}

.accordion-content {
  transition: max-height 0.4s ease-out, opacity 0.3s ease-out;
}
```

---

## 🧪 Testes Necessários

Após implementar correções:

1. **Build + preview** local
2. **Testar Swiper:**
   - Autoplay funciona?
   - Pagination clickável?
   - Breakpoints respondem corretamente?
3. **PageSpeed mobile:**
   - Métrica LCP (Largest Contentful Paint)
   - Verificar se fetchpriority ajudou
4. **FAQ accordion:**
   - Abrir/fechar suave
   - Múltiplos itens simultaneamente

---

## 📈 Métricas de Sucesso

- [ ] Swiper carregando e funcional
- [ ] 2 imagens com `fetchpriority="high"`
- [ ] Nenhuma imagem crítica com `loading="lazy"`
- [ ] PageSpeed mobile ≥ 75
- [ ] FAQ com transição suave (visual)

---

**Próximo passo:** Implementar correções na ordem de prioridade.
