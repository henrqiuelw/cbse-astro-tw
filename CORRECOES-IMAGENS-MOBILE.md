# Correções de Imagens Mobile/Desktop - v1.2.2

## Problema Reportado
Usuário visualizando no iOS/mobile vê várias imagens faltando. Análise do v2.0-reference.html identificou imagens mobile-only e desktop-only que não foram implementadas no Astro.

---

## Imagens Identificadas

### 1. PROBLEMAS (Problemas.astro)

**v2.0 Reference:**
- **Desktop-only**: `091713-copy.webp` (com classes `elementor-hidden-tablet elementor-hidden-mobile`)
- **Mobile-only**: `115104.webp` (com classes `elementor-hidden-desktop elementor-hidden-laptop`)

**Astro atual:**
- Desktop: background-image 115104.webp ✅
- Mobile: `background-image: none` ❌ **FALTA img tag mobile-only**

**Correção necessária:**
```astro
<!-- Problemas.astro - adicionar ANTES do .problemas-card -->
<img 
  src="/img/115104.webp" 
  alt="Comer Bem Sem Estresse — Dificuldades Alimentares"
  width="800"
  height="913"
  class="problemas-img-mobile"
  loading="lazy"
/>

<!-- Desktop-only image dentro do card ou próximo -->
<img 
  src="/img/091713-copy.webp" 
  alt="Comer Bem Sem Estresse — Sistema Alimentar"
  width="1038"
  height="693"
  class="problemas-img-desktop"
  loading="lazy"
/>
```

**CSS necessário:**
```css
.problemas-img-mobile {
  display: none;
  width: 100%;
  height: auto;
  margin-bottom: 20px;
}

@media (max-width: 1024px) {
  .problemas-img-mobile {
    display: block;
  }
}

.problemas-img-desktop {
  display: block;
  width: 100%;
  height: auto;
  max-width: 1038px;
}

@media (max-width: 1024px) {
  .problemas-img-desktop {
    display: none;
  }
}
```

---

### 2. MÉTODO (Metodo.astro)

**v2.0 Reference:**
- **Desktop-only**: `083313-copy.webp` (já implementado com `@media (max-width: 1024px) { display: none }`)
- **Mobile-only**: `083313-copy.webp` (mesma imagem, exibida em mobile com classes `elementor-hidden-desktop elementor-hidden-laptop`)

**Astro atual:**
- Desktop: 083313-copy.webp em `.metodo-img-col` com `display: none` no mobile ✅

**Status**: ✅ **OK** - Imagem desktop-only já implementada corretamente

**PORÉM**: v2.0 mostra a MESMA imagem no mobile também (acima do heading). Precisa verificar se deve aparecer ou não.

**Análise**: No v2.0, a imagem aparece duas vezes:
1. No mobile ANTES do heading (elemento `elementor-element-08dadbe`)
2. No desktop na lateral dos cards (elemento `elementor-element-7d5ad76`)

**Correção necessária:**
```astro
<!-- Metodo.astro - adicionar ANTES do metodo-heading -->
<img 
  src="/img/083313-copy.webp" 
  alt="Comer Bem Sem Estresse — módulos do curso"
  width="743"
  height="740"
  class="metodo-img-mobile-top"
  loading="lazy"
/>
```

**CSS necessário:**
```css
.metodo-img-mobile-top {
  display: none;
  width: 100%;
  height: auto;
  max-width: 743px;
  margin: 0 auto 30px;
}

@media (max-width: 1024px) {
  .metodo-img-mobile-top {
    display: block;
  }
}
```

---

### 3. FASES (Fases.astro)

**v2.0 Reference:**
- **Mobile-only**: `133907-copy.webp` (com classes `elementor-hidden-desktop elementor-hidden-laptop`)

**Astro atual:**
- Sem esta imagem

**Correção necessária:**
```astro
<!-- Fases.astro - adicionar ANTES do fases-heading -->
<img 
  src="/img/133907-copy.webp" 
  alt="Comer Bem Sem Estresse — Fases da Metodologia"
  width="800"
  height="1088"
  class="fases-img-mobile"
  loading="lazy"
/>
```

**CSS necessário:**
```css
.fases-img-mobile {
  display: none;
  width: 100%;
  height: auto;
  max-width: 800px;
  margin: 0 auto 30px;
}

@media (max-width: 1024px) {
  .fases-img-mobile {
    display: block;
  }
}
```

---

## Resumo de Ações

### Problemas.astro
- [ ] Adicionar `<img>` mobile-only (115104.webp)
- [ ] Adicionar `<img>` desktop-only (091713-copy.webp)
- [ ] Atualizar CSS para visibility classes
- [ ] Manter background-image apenas no desktop (ou remover e usar só img tag)

### Metodo.astro  
- [ ] Adicionar `<img>` mobile-top (083313-copy.webp) acima do heading
- [ ] Adicionar CSS `.metodo-img-mobile-top`

### Fases.astro
- [ ] Adicionar `<img>` mobile-only (133907-copy.webp) acima do heading
- [ ] Adicionar CSS `.fases-img-mobile`

---

## Verificar Imagens no Diretório

```bash
ls -lh ~/Projects/cbse-astro-tw/public/img/ | grep -E "(115104|091713|083313|133907|mouse)"
```

**Resultado esperado:**
- 115104.webp ✓
- 091713-copy.webp ✓
- 083313-copy.webp ✓
- 133907-copy.webp ✓

---

## Commit Message (após correções)

```
fix(mobile): adicionar imagens mobile-only faltantes

- Problemas: adicionar 115104.webp (mobile) + 091713.webp (desktop)
- Método: adicionar 083313-copy.webp no topo (mobile)
- Fases: adicionar 133907-copy.webp (mobile)

Corrige visualização em iOS/mobile onde imagens estavam faltando.
Ref: análise v2.0-reference.html com classes elementor-hidden-*
```

---

## Próximos Passos

1. Verificar se todas as imagens existem em `/public/img/`
2. Implementar correções nos 3 componentes
3. Testar em responsive view (375px, 768px, 1024px)
4. Deploy e testar no iOS real
5. Atualizar score pixel perfect (esperado: 92% → 95%+)
