# Debug: PROBLEMAS Section 2 Mobile

## Imagens Enviadas pelo Usuário

### Imagem 1 (ERRADA - v1.2.7)
- Imagem da mãe com bebê MUITO GRANDE
- Ocupa quase toda a tela
- Pouco texto visível embaixo

### Imagem 2 (CERTA - v2.0)
- Imagem da mãe com bebê MENOR
- Mais texto visível
- Melhor proporção

## v2.0 CSS Mobile Image (elementor-element-d7394c9)

### Desktop
```css
width: 43%;
max-width: 43%;
```

### Tablet (max-width: 1024px, min-width: 768px)
```css
width: 100%;
max-width: 100%;
margin: -50% -13% -26% -13%; /* ⚠️ Margin MUITO negativo */
```

### Mobile (max-width: 767px)
```css
width: 100%;
max-width: 100%;
margin: -26% -7% -14% -6%; /* ⚠️ Margin negativo menor */
```

## v2.0 Container (elementor-element-9881de1)

### Desktop
```css
flex-direction: row;
padding: 0;
```

### Tablet
```css
flex-direction: column-reverse; /* ⚠️ Inverte ordem */
margin-top: -51px;
padding: 10% 5% 17% 5%;
```

### Mobile
```css
flex-direction: column-reverse; /* ⚠️ Inverte ordem */
padding: 10% 5%;
```

---

## Problemas.astro Atual (v1.2.7)

### Mobile Image
```css
@media (max-width: 1024px) {
  .problemas-img-mobile {
    display: block;
    margin: -26% -7% -14% -6%; /* ✅ Correto para mobile */
  }
}
```

**Falta:** Margin diferente para tablet!

### Container
```css
.problemas-section-2-inner {
  display: flex;
  /* ❌ Falta flex-direction: column-reverse no mobile! */
}

@media (max-width: 767px) {
  .problemas-section-2-inner {
    padding: 10% 5%;
  }
}
```

**Falta:** `flex-direction: column-reverse` no mobile/tablet!

---

## Correções Necessárias

### 1. Adicionar flex-direction: column-reverse
```css
@media (max-width: 1024px) {
  .problemas-section-2-inner {
    flex-direction: column-reverse;
  }
}
```

### 2. Separar margins tablet vs mobile
```css
/* Tablet (768px - 1024px) */
@media (min-width: 768px) and (max-width: 1024px) {
  .problemas-img-mobile {
    margin: -50% -13% -26% -13%;
  }
}

/* Mobile (< 768px) */
@media (max-width: 767px) {
  .problemas-img-mobile {
    margin: -26% -7% -14% -6%;
  }
}
```

### 3. Remover margin negativo no mobile? (TESTE)
Talvez o margin negativo esteja fazendo a imagem parecer maior do que deveria.

**Hipótese:** Margin negativo no mobile pode estar aumentando visualmente o tamanho da imagem.

**Teste:** Remover ou reduzir margin negativo no mobile puro (< 768px).

---

## Próxima Ação

1. Adicionar `flex-direction: column-reverse` no tablet/mobile
2. Separar tablet margin (-50%) do mobile margin (-26%)
3. Testar se remover margin negativo no mobile < 768px melhora
