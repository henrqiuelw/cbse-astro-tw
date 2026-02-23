# 📱 Teste Mobile - v1.3.1 vs v2.0 Reference

## URLs para Comparação

- **v2.0 Reference (Mirror):** https://cbse-mirrorclean.pages.dev
- **v1.3.1 Astro:** https://44f9c676.cbse-site-tw.pages.dev

## Como Testar

### Opção 1: No Celular Real
1. Abra ambas URLs no Safari/Chrome mobile
2. Role até a seção **PROBLEMAS** (card branco com blur + imagem)
3. Compare visualmente

### Opção 2: No DevTools (Desktop)
1. Abra Chrome/Edge
2. Pressione **F12** → **Toggle Device Toolbar** (Ctrl+Shift+M)
3. Selecione **iPhone 12 Pro** (390x844) ou **iPhone SE** (375x667)
4. Abra ambas URLs em abas separadas
5. Role até seção PROBLEMAS e compare

## ✅ Estrutura DOM Renderizada (Após v1.3.1)

### v2.0 Reference
```html
<div class="e-con-inner">
  <!-- 1. Card -->
  <div class="e-con-child">
    <h1>Quando não existe...</h1>
    <p>Isso gera desgaste...</p>
    <p>Famílias que alcançam...</p>
  </div>
  
  <!-- 2. Mobile Image (visível mobile, hidden desktop) -->
  <div class="elementor-widget 
       elementor-hidden-desktop 
       elementor-hidden-laptop">
    <img src="115104.webp" />
  </div>
  
  <!-- 3. Desktop Image (hidden mobile) -->
  <div class="elementor-widget
       elementor-hidden-tablet
       elementor-hidden-mobile">
    <img src="091713-copy.webp" />
  </div>
</div>
```

### v1.3.1 Astro
```html
<div class="problemas-section-2-inner">
  <!-- 1. Card -->
  <div class="problemas-card">
    <h1>Quando não existe...</h1>
    <p>Isso gera desgaste...</p>
    <p>Famílias que alcançam...</p>
  </div>
  
  <!-- 2. Mobile Image (visível mobile, hidden desktop) -->
  <div class="problemas-img-mobile-wrap">
    <img class="problemas-img-mobile" 
         src="115104.webp" />
  </div>
  
  <!-- 3. Desktop Image (hidden mobile) -->
  <div class="problemas-img-desktop-wrap">
    <img class="problemas-img-desktop" 
         src="091713-copy.webp" />
  </div>
</div>
```

## 🎯 CSS Aplicado no Mobile (max-width: 767px)

### Container
```css
.problemas-section-2-inner {
  display: flex;
  flex-direction: column;  /* Empilha verticalmente */
  padding: 10% 5%;
}
```

### Wrappers das Imagens
```css
/* Mobile wrapper - VISÍVEL */
.problemas-img-mobile-wrap {
  display: block;
  margin: 20px 0 0 0;  /* Espaço após o card */
}

/* Desktop wrapper - OCULTO */
.problemas-img-desktop-wrap {
  display: none;
}
```

## 📊 Checklist de Verificação

No **mobile (< 767px)**, deve aparecer nesta ordem:

1. ✅ **Card branco** (blur background)
   - Heading: "Quando não existe um sistema alimentar..."
   - 2 parágrafos de texto

2. ✅ **Imagem vertical** (800×913)
   - Arquivo: 115104.webp
   - Mãe + criança
   - Margin-top: 20px (espaço após card)

3. ❌ **Imagem horizontal NÃO deve aparecer**
   - Arquivo: 091713-copy.webp
   - Display: none no mobile

## 🐛 Se ainda houver problemas

Compare especificamente:

1. **Ordem dos elementos:** Card → Imagem vertical → (nada)
2. **Espaçamento:** 20px entre card e imagem
3. **Largura da imagem:** 100% do container
4. **Alinhamento:** Centralizado ou à esquerda?
5. **Background do card:** Blur branco funcionando?

## 📸 Tire Screenshots

Se possível, tire screenshots de ambos e me envie para comparação visual exata.
