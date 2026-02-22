# Correção Estrutura PROBLEMAS - v1.3.0

## Problema Identificado

A **ordem do HTML** e o uso de `flex-direction: column-reverse` estavam causando problemas de posicionamento das imagens no mobile.

### Estrutura INCORRETA (v1.2.9)

```html
<div class="problemas-section-2-inner">
  <!-- Imagem mobile -->
  <img src="115104.webp" class="problemas-img-mobile" />
  
  <!-- Imagem desktop -->
  <img src="091713-copy.webp" class="problemas-img-desktop" />
  
  <!-- Card com textos -->
  <div class="problemas-card">...</div>
</div>
```

**CSS problemático:**
```css
@media (max-width: 1024px) {
  .problemas-section-2-inner {
    flex-direction: column-reverse; /* ❌ Invertendo ordem */
  }
}
```

---

## Solução Aplicada (v1.3.0)

### Estrutura CORRETA (conforme v2.0)

```html
<div class="problemas-section-2-inner">
  <!-- Card primeiro -->
  <div class="problemas-card">...</div>
  
  <!-- Imagem mobile depois -->
  <img src="115104.webp" class="problemas-img-mobile" />
  
  <!-- Imagem desktop por último -->
  <img src="091713-copy.webp" class="problemas-img-desktop" />
</div>
```

**CSS correto:**
```css
@media (max-width: 767px) {
  .problemas-section-2-inner {
    padding: 10% 5%;
    flex-direction: column; /* ✅ Ordem natural */
  }
}
```

---

## Mudanças Principais

### 1. Ordem HTML
- ✅ **Card vem primeiro** no código
- ✅ **Imagem mobile depois** (hidden desktop/laptop)
- ✅ **Imagem desktop por último** (hidden tablet/mobile)

### 2. CSS Container
- ❌ Removido `flex-direction: column-reverse` no tablet
- ✅ Mantido `flex-direction: column` apenas no mobile < 767px
- ✅ Ordem visual controlada por visibilidade CSS

### 3. Margem Imagem Mobile
**Antes:**
```css
margin: 0 0 20px 0; /* Antes do card */
```

**Depois:**
```css
margin: 20px 0 0 0; /* Depois do card */
```

---

## Resultado Esperado

### Desktop (> 1024px)
- Card 44% à esquerda
- Imagem desktop 54% à direita (visível)
- Imagem mobile hidden

### Tablet (768-1024px)
- Card 55% width
- Imagem mobile visível com margens negativas
- Imagem desktop hidden

### Mobile (< 768px)
- Card width 100%, sem blur
- Imagem mobile 100% width, margin-top 20px
- Imagem desktop hidden

---

## Benefícios

✅ **Estrutura idêntica ao v2.0** - elementos irmãos diretos  
✅ **Sem hacks de flex-direction** - ordem natural  
✅ **Controle via CSS puro** - classes de visibilidade  
✅ **Posicionamento correto** - mobile e desktop  
✅ **Código mais limpo** - menos complexidade  

---

## Deploy

- **URL:** <https://31674ab3.cbse-site-tw.pages.dev>
- **Commit:** 9905d98
- **Tag:** v1.3.0
- **Build time:** 478ms ✅
