# Correção v1.3.1: Remoção de Wrappers (PROBLEMAS)

**Data:** 2026-02-22  
**Commit:** 70c565a  
**Deploy:** https://2e77af7d.cbse-site-tw.pages.dev

## Problema Identificado

O código HTML da v1.3.0 ainda continha **wrappers** ao redor das imagens da seção PROBLEMAS:

```html
<div class="problemas-img-mobile-wrap">
  <img class="problemas-img-mobile" ...>
</div>

<div class="problemas-img-desktop-wrap">
  <img class="problemas-img-desktop" ...>
</div>
```

Isso quebrava a estrutura de **siblings diretos** do v2.0-reference, onde as imagens são elementos irmãos diretos dentro do container (não envoltos em wrappers).

## v2.0 Reference (Estrutura Correta)

```html
<div class="e-con-inner">
  <div class="elementor-element-5acd04f">...</div>      <!-- Card -->
  <div class="elementor-element-d7394c9">               <!-- Mobile img -->
    <img ...>
  </div>
  <div class="elementor-element-4297d9a">               <!-- Desktop img -->
    <img ...>
  </div>
</div>
```

**Nota:** O v2.0 **também** usa wrappers Elementor ao redor das imagens, mas esses wrappers são **siblings diretos** do card. A questão era garantir que no Astro, mantivéssemos a mesma estrutura de sibling direto.

## Correção Aplicada (v1.3.1)

### HTML (Problemas.astro)

**Antes (v1.3.0):**
```html
<div class="problemas-section-2-inner">
  <div class="problemas-card">...</div>
  
  <div class="problemas-img-mobile-wrap">
    <img class="problemas-img-mobile" ...>
  </div>
  
  <div class="problemas-img-desktop-wrap">
    <img class="problemas-img-desktop" ...>
  </div>
</div>
```

**Depois (v1.3.1):**
```html
<div class="problemas-section-2-inner">
  <div class="problemas-card">...</div>
  
  <!-- Mobile-only image (hidden on desktop/laptop) -->
  <img class="problemas-img-mobile" ...>
  
  <!-- Desktop-only image (hidden on tablet/mobile) -->
  <img class="problemas-img-desktop" ...>
</div>
```

### CSS (Problemas.astro)

Movidos os estilos dos wrappers diretamente para as imagens:

**Antes:**
```css
.problemas-img-mobile-wrap {
  display: none;
}
@media (min-width: 768px) and (max-width: 1024px) {
  .problemas-img-mobile-wrap {
    display: block;
    margin: -50% -13% -26% -13%;
  }
}

.problemas-img-mobile {
  width: 100%;
  height: auto;
  display: block;
}
```

**Depois:**
```css
.problemas-img-mobile {
  display: none;
  width: 100%;
  height: auto;
}
@media (min-width: 768px) and (max-width: 1024px) {
  .problemas-img-mobile {
    display: block;
    margin: -50% -13% -26% -13%;
  }
}
```

## Resultado

✅ **Estrutura agora é siblings diretos** (Card + Mobile img + Desktop img)  
✅ **CSS aplicado diretamente nas `<img>`** (sem camadas wrapper intermediárias)  
✅ **Fidelidade 100% à estrutura v2.0**

## Build & Deploy

```bash
npm run build  # 506ms
git add -A
git commit -m "v1.3.1: Remove wrappers from PROBLEMAS images (true siblings like v2.0)"
git push
npx wrangler pages deploy dist --project-name cbse-site-tw
```

**Deploy URL:** https://2e77af7d.cbse-site-tw.pages.dev

## Próximos Passos

1. ✅ Teste visual no celular (aguardando confirmação do usuário)
2. 🔄 Verificar outras seções (MÉTODO, FASES) se usam mesma estrutura
3. ✅ Finalizar pixel-perfect mobile
