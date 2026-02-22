# Correções Hero Mobile - v1.2.5

## Problemas Identificados

### ✅ Corretos (não precisam mudar)
- Logo width mobile: `40.888%` ✅
- Título font-size mobile: `6.3vw` ✅
- Subtítulo font-size mobile: `4.1vw` ✅

### ❌ Precisam Correção

#### 1. Logo (`.hero-logo-wrap`)
**Problema:** Falta centralizar no mobile
```css
/* Atual */
.hero-logo-wrap {
  margin-bottom: 20px;
}

/* Deveria ser (mobile) */
@media (max-width: 767px) {
  .hero-logo-wrap {
    text-align: center;
    margin: 0 0 5% 0;
  }
}
```

#### 2. Título (`.hero-heading`)
**Problema 1:** Line-height mobile incorreto (1.3 vs 1.2)
```css
/* Atual */
@media (max-width: 767px) {
  .hero-heading {
    font-size: 6.3vw;
    line-height: 1.3; /* ❌ deveria ser 1.2 */
  }
}

/* Correto */
@media (max-width: 767px) {
  .hero-heading {
    font-size: 6.3vw;
    line-height: 1.2em; /* ✅ */
  }
}
```

**Problema 2:** Falta margin negativo mobile
```css
/* Deveria adicionar (mobile) */
@media (max-width: 767px) {
  .hero-heading-wrap {
    margin: 0 -4% -3% -4%; /* ✅ */
  }
}
```

#### 3. Subtítulo (`.hero-subtitle-wrap`)
**Problema:** Max-width desktop muito pequeno (370px vs 683px)
```css
/* Atual */
.hero-subtitle-wrap {
  margin-bottom: 20px;
  max-width: 370px; /* ❌ deveria ser 683px */
  width: 100%;
}

/* Correto */
.hero-subtitle-wrap {
  margin-bottom: 20px;
  max-width: 683px; /* ✅ */
  width: 100%;
}
```

#### 4. Botão (inline style em Hero.astro)
**Problema:** Font-size fixo em 18px (deveria ser 16px no mobile)
```astro
<!-- Atual -->
<a ... style="font-family: 'Inter', sans-serif; font-size: 18px; ...">

<!-- Solução: mover para CSS com media query -->
```

Adicionar no global.css:
```css
.btn-hero-mobile {
  font-family: 'Inter', sans-serif;
  font-size: 18px;
  font-weight: 600;
  letter-spacing: 0.9px;
  padding: 20px 40px;
}

@media (max-width: 767px) {
  .btn-hero-mobile {
    font-size: 16px; /* ✅ */
  }
}
```

---

## Plano de Aplicação

### Arquivo 1: `src/styles/global.css`

**Linha ~173 - Logo:**
```css
.hero-logo-wrap {
  margin-bottom: 20px;
}
+
+@media (max-width: 767px) {
+  .hero-logo-wrap {
+    text-align: center;
+    margin: 0 0 5% 0;
+  }
+}
```

**Linha ~193 - Título heading-wrap:**
```css
@media (max-width: 767px) {
  .hero-heading-wrap {
-    margin-bottom: 20px;
-    padding: 7px 0 8px 0;
+    margin: 0 -4% -3% -4%;
+    padding: 0;
  }
}
```

**Linha ~213 - Título heading:**
```css
@media (max-width: 767px) {
  .hero-heading {
    font-size: 6.3vw;
-    line-height: 1.3;
+    line-height: 1.2em;
  }
}
```

**Linha ~220 - Subtítulo wrap:**
```css
.hero-subtitle-wrap {
  margin-bottom: 20px;
-  max-width: 370px;
+  max-width: 683px;
  width: 100%;
}
```

**Adicionar após .btn-grad (depois da linha ~295):**
```css
/* Hero CTA com responsive font-size */
.btn-hero-cta {
  font-family: 'Inter', sans-serif;
  font-size: 18px;
  font-weight: 600;
  letter-spacing: 0.9px;
  padding: 20px 40px;
}

@media (max-width: 767px) {
  .btn-hero-cta {
    font-size: 16px;
  }
}
```

### Arquivo 2: `src/components/Hero.astro`

**Linha ~56 - Botão CTA:**
```astro
<a
  href={HOTMART}
  target="_blank"
  rel="noopener noreferrer"
-  class="btn-grad animation-grow"
+  class="btn-grad animation-grow btn-hero-cta"
  id="cta_inic_fin_compra"
-  style="font-family: 'Inter', sans-serif; font-size: 18px; font-weight: 600; letter-spacing: 0.9px; padding: 20px 40px;"
>
  Quero iniciar o acompanhamento
</a>
```

---

## Resultado Esperado

✅ Logo centralizado no mobile  
✅ Título com line-height correto (1.2em) e margin negativo  
✅ Subtítulo com max-width desktop correto (683px)  
✅ Botão com font-size 16px no mobile (18px desktop)  

**Meta:** 100% pixel perfect desktop + mobile
