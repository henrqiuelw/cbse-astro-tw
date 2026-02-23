# Correções v1.3.2: PROBLEMAS Mobile - Exact v2.0 CSS Match

**Data:** 2026-02-22  
**Commit:** 8ca950d  
**Deploy:** https://7ee1472c.cbse-site-tw.pages.dev

## Método de Análise

Usado **browser headless** pra extrair **computed CSS** exato de ambas versões (viewport 375px):

- **v2.0:** https://cbse-mirrorclean.pages.dev  
- **v1.3.1:** https://2e77af7d.cbse-site-tw.pages.dev

## Diferenças Encontradas

### 1. Section (.problemas-section-2)

| Propriedade | v2.0 Reference | v1.3.1 Antes | v1.3.2 Corrigido |
|-------------|----------------|--------------|------------------|
| `padding` | `0px 18.75px` (5%) | `37.5px 18.75px` ❌ | `0 5%` ✅ |
| `margin` | `-51px 0 0` | `0` ❌ | `-51px 0 0` ✅ |
| `display` | `flex` | `block` ❌ | `flex` ✅ |

### 2. Container (.problemas-section-2-inner)

| Propriedade | v2.0 Reference | v1.3.1 Antes | v1.3.2 Corrigido |
|-------------|----------------|--------------|------------------|
| `padding` | `33.75px 0 57.375px` | `33.75px 16.875px` ❌ | `9% 0 15.3%` ✅ |
| **`flex-direction`** | **`column-reverse`** 🔥 | `column` ❌ | `column-reverse` ✅ |

**CRÍTICO:** v2.0 usa `column-reverse` pra inverter ordem visual (imagem → card → imagem). HTML mantém ordem natural (card → mobile img → desktop img) mas CSS inverte no mobile.

### 3. Card (.problemas-card)

| Propriedade | v2.0 Reference | v1.3.1 Antes | v1.3.2 Corrigido |
|-------------|----------------|--------------|------------------|
| `width` | `337.5px` (90%) | `303.75px` (81%) ❌ | `90%` ✅ |
| `background` | `rgba(255,255,255,0.05)` | `transparent` ❌ | `rgba(255,255,255,0.05)` ✅ |

### 4. Heading (.problemas-card-heading)

| Propriedade | v2.0 Reference | v1.3.1 Antes | v1.3.2 Corrigido |
|-------------|----------------|--------------|------------------|
| `width` | `377.5px` (100.67%) | `303.75px` (81%) ❌ | `100.67%` ✅ |
| `margin` | `0` | `0 -20px 20px` ❌ | `0` ✅ |

### 5. P1 (.problemas-card-p1)

| Propriedade | v2.0 Reference | v1.3.1 Antes | v1.3.2 Corrigido |
|-------------|----------------|--------------|------------------|
| `width` | `337.5px` (90%) | `303.75px` (81%) ❌ | `100%` ✅ |
| `margin` | `0` | `0 0 20px` ❌ | `0` ✅ |

### 6. P2 (.problemas-card-p2)

| Propriedade | v2.0 Reference | v1.3.1 Antes | v1.3.2 Corrigido |
|-------------|----------------|--------------|------------------|
| `width` | `337.5px` (90%) | `303.75px` (81%) ❌ | `100%` ✅ |
| `font-size` | `20px` | `16px` ❌ | `20px` ✅ |
| `font-weight` | `600` | `400` ❌ | `600` ✅ |

## Mudanças Aplicadas (CSS)

### Section Mobile

```css
@media (max-width: 767px) {
  .problemas-section-2 {
-   padding: 10% 5%;
+   padding: 0 5%;
+   margin: -51px 0 0;
+   display: flex;  /* Adicionado */
  }
}
```

### Container Mobile

```css
@media (max-width: 767px) {
  .problemas-section-2-inner {
-   padding: 10% 5%;
-   flex-direction: column;
+   padding: 9% 0 15.3%;
+   flex-direction: column-reverse;  /* CRÍTICO! */
  }
}
```

### Card Mobile

```css
@media (max-width: 1024px) {
  .problemas-card {
-   width: 100%;
-   background: transparent;
+   width: 90%;
+   background: rgba(255, 255, 255, 0.05);
  }
}
```

### Heading Mobile

```css
@media (max-width: 767px) {
  .problemas-card-heading {
-   width: 100%;
-   margin: 0 -20px 20px -20px;
+   width: 100.67%;
+   margin: 0;
  }
}
```

### P1 Mobile

```css
@media (max-width: 1024px) {
  .problemas-card-p1 {
    width: 100%;
    text-align: center;
+   margin: 0;  /* Removido margin-bottom */
  }
}
```

### P2 Mobile

```css
@media (max-width: 1024px) {
  .problemas-card-p2 {
    width: 100%;
-   font-size: 16px;
+   font-size: 20px;
+   font-weight: 600;
    text-align: center;
  }
}
```

## Validação Visual

Verificar **v1.3.2** no mobile (375px):

- ✅ Margin negativo -51px cria overlap com seção anterior
- ✅ Card 90% width (mais largo que v1.3.1)
- ✅ Textos P1/P2 em 20px bold (antes P2 era 16px regular)
- ✅ Heading sem margin negativo lateral
- ✅ Background rgba(255,255,255,0.05) no card
- ✅ Ordem visual correta via column-reverse

## Deploy URL

**v1.3.2:** https://7ee1472c.cbse-site-tw.pages.dev

Teste no celular real e compare com v2.0!
