# Análise Seção MÉTODO - Mobile v2.0 vs Astro

## Estrutura v2.0 (elementor-element-3704ea8)

### Desktop (> 1024px)
1. **Heading** (elementor-element-03949ff): "O Comer bem sem estresse é um método estruturado para sair do improviso e construir autonomia alimentar:"
2. **Grid 2 colunas**:
   - **Coluna 1** (elementor-element-7d5ad76): Imagem 083313-copy.webp (class `elementor-hidden-tablet elementor-hidden-mobile`)
   - **Coluna 2**: 5 cards verticais (grid 1×5)

### Mobile (≤ 1024px)
1. **Imagem mobile-top** (elementor-element-08dadbe): 083313-copy.webp (class `elementor-hidden-desktop elementor-hidden-laptop`)
2. **Heading**: mesmo texto
3. **Grid vertical**: 5 cards empilhados (sem imagem lateral)

---

## Astro Atual (v1.2.2)

### Desktop
✅ Imagem lateral 083313-copy.webp (display: none no mobile)
✅ 2 colunas: imagem esquerda + cards direita
✅ 5 cards verticais

### Mobile
✅ Imagem mobile-top 083313-copy.webp adicionada
✅ Heading
✅ 5 cards empilhados

---

## Possíveis Problemas Identificados

### 1. **Largura da imagem mobile-top**
**v2.0**:
```html
<img 
  sizes="(max-width: 743px) 100vw, 743px" 
  width="743" 
  height="740"
  class="elementor-widget-mobile__width-initial"
/>
```

**Astro atual**:
```css
.metodo-img-mobile-top {
  max-width: 743px;
  margin: 0 auto 30px;
}
```

**Problema**: No mobile, a imagem pode estar menor do que deveria (max-width limita o crescimento).

**Solução**: Remover `max-width` e usar `width: 100%` no mobile.

---

### 2. **Espaçamento do heading**
**v2.0**:
```css
margin: 0 0 40px 0;
```

**Astro atual**:
```css
margin: 0 0 40px 0;
```

✅ **OK**

---

### 3. **Grid layout dos cards**
**v2.0**: Usa `e-grid` com `e-con-full`
**Astro atual**: Usa `flexbox` com `flex-direction: column`

Ambos produzem resultado visual similar, mas podem ter diferenças sutis de gap.

---

## Checklist de Correções

- [ ] Ajustar largura da imagem mobile-top para 100% (sem max-width no mobile)
- [ ] Verificar espaçamento entre imagem e heading (atual: 30px, v2.0: verificar)
- [ ] Verificar gap entre cards (atual: 30px, v2.0: verificar)
- [ ] Comparar padding do `.metodo-inner` no mobile

---

## Próximos Passos
1. Abrir https://517f27ac.cbse-site-tw.pages.dev no mobile (375px)
2. Abrir https://cbse-mirrorclean.pages.dev no mobile (375px)
3. Comparar lado a lado:
   - Largura da imagem mobile-top
   - Espaçamento imagem → heading
   - Espaçamento heading → cards
   - Espaçamento entre cards
   - Padding lateral do container
