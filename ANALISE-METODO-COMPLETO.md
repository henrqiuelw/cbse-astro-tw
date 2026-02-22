# Análise Completa: Seção MÉTODO - v2.0 vs Metodo.astro

## Container Principal (.metodo-section / elementor-element-3704ea8)

### v2.0 Desktop
```css
--padding-top: 60px;
--padding-bottom: 200px;
--padding-left: 0px;
--padding-right: 0px;
--content-width: 1140px; /* ⚠️ NÃO 1280px! */
background-color: #fef4df;
border-top: 1px solid #FFFFFF0F;
--gap: 20px 20px;
```

### v2.0 Tablet (max-width: 1024px)
```css
--padding-top: 10%;
--padding-bottom: 10%;
--padding-left: 5%;
--padding-right: 5%;
--gap: 30px 30px;
```

### v2.0 Mobile (max-width: 767px)
```css
--padding-top: 10%;
--padding-bottom: 10%;
--padding-left: 10%;
--padding-right: 10%;
```

### Metodo.astro Atual
```css
.metodo-inner {
  max-width: 1280px; /* ❌ Deveria ser 1140px */
  padding: 60px 0 200px 0; /* ✅ Desktop correto */
}

@media (max-width: 1024px) {
  padding: 60px 40px 120px 40px; /* ❌ Deveria ser 10% 5% */
}

@media (max-width: 767px) {
  padding: 10% 5% 15% 5%; /* ❌ Deveria ser 10% 10% */
}
```

---

## Heading (.metodo-heading / elementor-element-03949ff)

### v2.0 CSS
```css
/* Desktop */
font-family: Factul, Sans-serif;
font-size: 32px;
line-height: 1.2em;
color: #1c3124;
text-align: center;
width: 100%;
max-width: 100%;

/* Tablet */
font-size: 36px;

/* Mobile */
font-size: 6.1vw;
margin: 0 0 30px 0;
```

### Metodo.astro Atual
```css
.metodo-heading {
  font-family: 'Factul', sans-serif;
  font-size: 32px; /* ✅ */
  line-height: 1.2em; /* ✅ */
  color: #1c3124; /* ✅ */
  text-align: center; /* ✅ */
  margin: 0 0 40px 0; /* ❌ Deveria ser 30px no mobile */
}

@media (min-width: 768px) and (max-width: 1024px) {
  font-size: 36px; /* ✅ */
}

@media (max-width: 767px) {
  font-size: 6.1vw; /* ✅ */
  margin-bottom: 30px; /* ✅ */
}
```

---

## Grid de Cards (.metodo-cards-col / elementor-element-ebff15c)

### v2.0 Desktop Structure
```html
<div class="e-con-full e-grid e-con e-child"> <!-- Grid container -->
  <div class="e-con-full e-flex e-con e-child"> <!-- Card 1 -->
    <div class="elementor-widget-image"> <!-- Icon -->
    <div class="elementor-widget-text-editor"> <!-- Title -->
    <div class="elementor-widget-text-editor"> <!-- Bold desc -->
    <div class="elementor-widget-text-editor"> <!-- Regular desc -->
  </div>
  <!-- ... 4 more cards ... -->
  <div class="elementor-widget-image"> <!-- Decorative image desktop -->
</div>
```

### v2.0 CSS
```css
/* Grid parent */
.elementor-element-ebff15c {
  --display: grid;
  --grid-template-columns: repeat(2, 1fr); /* ⚠️ 2 colunas no desktop */
  --grid-template-rows: repeat(3, 1fr);
  --gap: 30px 30px;
}

/* Individual card */
.e-con-full.e-flex {
  background-color: #fffefb;
  border-radius: 10px;
  padding: 40px;
  box-shadow: 0 34.319px 44.764px 0 rgba(0, 0, 0, 0.06);
}
```

### Metodo.astro Atual
```css
/* Right column: cards vertical */
.metodo-cards-col {
  flex: 1;
  display: flex; /* ❌ Deveria ser GRID */
  flex-direction: column; /* ❌ Grid, não flexbox */
  gap: 30px; /* ✅ */
}

/* Card */
.metodo-card {
  background-color: #fffefb; /* ✅ */
  border-radius: 10px; /* ✅ */
  padding: 40px; /* ✅ */
  box-shadow: 0 34.319px 44.764px 0 rgba(0, 0, 0, 0.06); /* ✅ */
}
```

---

## Imagem Lateral (.metodo-img / elementor-element-7d5ad76)

### v2.0 Desktop
```css
/* Desktop only - fica no final do grid */
.elementor-element-7d5ad76 {
  width: initial; /* Não tem constraint fixo */
  display: block; /* Visível desktop */
}

/* Mobile/Tablet */
.elementor-hidden-tablet,
.elementor-hidden-mobile {
  display: none;
}
```

### v2.0 Mobile Top Image (elementor-element-08dadbe)
```css
/* Mobile/Tablet only */
.elementor-element-08dadbe {
  display: block;
}

/* Desktop */
.elementor-hidden-desktop {
  display: none;
}
```

### Metodo.astro Atual
```css
/* Desktop image column */
.metodo-img-col {
  flex: 0 0 auto;
  width: 320px; /* ⚠️ Width fixo, não é do v2.0 */
}

/* Mobile top image */
.metodo-img-mobile-top {
  display: none;
  margin: 0 0 30px 0; /* ✅ */
}
```

---

## Principais Problemas Identificados

### 1. **Container Width** ❌ CRÍTICO
```css
/* Atual */
max-width: 1280px;

/* v2.0 */
--content-width: 1140px;
```

### 2. **Layout dos Cards** ❌ CRÍTICO
```css
/* Atual: Flexbox vertical (1 coluna) */
.metodo-cards-col {
  display: flex;
  flex-direction: column;
}

/* v2.0: Grid 2×3 (2 colunas, 3 rows) */
.metodo-cards-col {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-template-rows: repeat(3, 1fr);
  gap: 30px;
}
```

### 3. **Imagem Decorativa** ⚠️
```css
/* Atual: Left column com width fixo 320px */
.metodo-img-col {
  width: 320px;
}

/* v2.0: Imagem dentro do grid (último item) */
/* Sem width constraint fixo */
```

### 4. **Padding Mobile** ❌
```css
/* Atual */
padding: 10% 5% 15% 5%;

/* v2.0 */
padding: 10% 10% 10% 10%;
```

---

## Plano de Correção

### Arquivo: `src/components/Metodo.astro`

#### 1. Container Width
```astro
<style>
  .metodo-inner {
-    max-width: 1280px;
+    max-width: 1140px;
  }
</style>
```

#### 2. Layout - Grid 2×3 Desktop
```astro
<style>
  .metodo-content {
-    display: flex;
-    flex-direction: row;
+    display: grid;
+    grid-template-columns: 1fr 1fr;
+    grid-template-rows: auto auto auto auto;
    gap: 30px;
  }

  .metodo-cards-col {
-    flex: 1;
-    display: flex;
-    flex-direction: column;
+    display: contents; /* Para permitir que os cards sejam filhos diretos do grid */
  }
</style>
```

#### 3. Padding Mobile
```astro
<style>
  @media (max-width: 767px) {
    .metodo-inner {
-      padding: 10% 5% 15% 5%;
+      padding: 10% 10% 10% 10%;
    }
  }
</style>
```

#### 4. Imagem Lateral Desktop
```astro
<style>
  .metodo-img-col {
-    flex: 0 0 auto;
-    width: 320px;
+    grid-column: 1 / 2;
+    grid-row: 1 / 4;
  }

  .metodo-img {
    width: 100%;
    height: auto;
  }
</style>
```

---

## Resultado Esperado

✅ Container: 1140px (não 1280px)  
✅ Cards: Grid 2×3 desktop (não coluna única)  
✅ Imagem lateral: Dentro do grid (não coluna left fixa)  
✅ Padding mobile: 10% (não 5% left/right)  

**Meta:** 100% pixel perfect desktop + mobile para seção MÉTODO
