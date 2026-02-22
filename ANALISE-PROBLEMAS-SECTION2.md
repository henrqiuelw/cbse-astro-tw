# Análise: Seção PROBLEMAS Part 2 - v2.0 vs Problemas.astro

## Problema Identificado

**v1.2.6 (errado):** Imagem ocupando 100% da largura  
**v2.0 (certo):** Imagem 54% width + Card 44% width lado a lado (flexbox)

---

## v2.0 Structure

### Container (elementor-element-239a7bd)
```css
/* Desktop */
display: flex;
align-items: center;
content-width: 1140px;
padding: 40px 0 60px 0;
background-color: #fff;
```

### Imagem Desktop (elementor-element-4297d9a)
```css
/* Desktop */
width: 54%;
max-width: 54%;
margin: 0 -32% -1% -15%; /* ⚠️ Margens negativas para sobrepor */

/* Tablet */
margin: 0 -62% -1% -15%;

/* Mobile */
width: 100%;
max-width: 100%;
margin: -26% -7% -14% -6%;
```

### Card (elementor-element-5acd04f)
```css
/* Desktop */
width: 44%;
padding: 40px;
border: 1px solid #00000024;
border-radius: 10px;
background-color: #FFFFFF0D;
backdrop-filter: blur(20px);
-webkit-backdrop-filter: blur(20px);
z-index: 99;

/* Tablet/Mobile */
width: 100%;
border: 0;
padding: 0;
```

---

## Problemas.astro Atual

### Container
```css
.problemas-section-2-inner {
  max-width: 1280px; /* ❌ Deveria ser 1140px */
  padding: 60px 40px; /* ❌ Deveria ser 40px 0 60px 0 */
  display: flex;
  align-items: flex-start; /* ❌ Deveria ser center */
}
```

### Imagem Desktop
```css
.problemas-img-desktop {
  display: block;
  width: 100%; /* ❌ Deveria ser 54% */
  height: auto;
  max-width: 1038px; /* ❌ Deveria ser 54% */
}
```
**Falta:** Margens negativas para sobrepor!

### Card
```css
.problemas-card {
  background: rgba(255, 255, 255, 0.85); /* ⚠️ Deveria ser 0D (mais transparente) */
  backdrop-filter: blur(20px); /* ✅ */
  border: 1px solid rgba(0, 0, 0, 0.14); /* ✅ ~#00000024 */
  border-radius: 10px; /* ✅ */
  padding: 40px; /* ✅ */
}
```
**Falta:** Width 44% desktop, z-index: 99

---

## Plano de Correção

### 1. Container Width + Padding
```css
.problemas-section-2-inner {
-  max-width: 1280px;
+  max-width: 1140px;
-  padding: 60px 40px;
+  padding: 40px 0 60px 0;
-  align-items: flex-start;
+  align-items: center;
}

@media (max-width: 767px) {
  .problemas-section-2-inner {
+    padding: 10% 5%;
  }
}
```

### 2. Imagem Desktop - Width 54% + Margin Negativo
```css
.problemas-img-desktop {
  display: block;
-  width: 100%;
+  width: 54%;
-  max-width: 1038px;
+  max-width: 54%;
+  margin: 0 -32% -1% -15%;
}

@media (min-width: 768px) and (max-width: 1024px) {
  .problemas-img-desktop {
+    margin: 0 -62% -1% -15%;
  }
}

@media (max-width: 1024px) {
  .problemas-img-desktop {
    display: none;
  }
}
```

### 3. Card - Width 44% + Z-index + Background
```css
.problemas-card {
-  background: rgba(255, 255, 255, 0.85);
+  background: rgba(255, 255, 255, 0.05); /* #FFFFFF0D */
+  width: 44%;
+  z-index: 99;
  backdrop-filter: blur(20px);
  border: 1px solid rgba(0, 0, 0, 0.14);
  border-radius: 10px;
  padding: 40px;
}

@media (max-width: 1024px) {
  .problemas-card {
+    width: 100%;
+    border: 0;
+    padding: 0;
+    background: transparent;
  }
}
```

### 4. Imagem Mobile - Margin Negativo
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
+    margin: -26% -7% -14% -6%;
  }
}
```

---

## Resultado Esperado

✅ **Desktop:** Imagem 54% + Card 44% lado a lado (flexbox)  
✅ **Imagem:** Margens negativas para criar sobreposição visual  
✅ **Card:** Z-index 99 para ficar "por cima"  
✅ **Container:** 1140px (não 1280px)  
✅ **Mobile:** Imagem com margin negativo + card sem borda  

**Meta:** 100% pixel perfect desktop + mobile para seção PROBLEMAS part 2
