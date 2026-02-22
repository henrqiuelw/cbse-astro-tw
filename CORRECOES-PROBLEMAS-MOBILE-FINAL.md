# Correções PROBLEMAS Mobile Final - Widths + Font-Sizes

## Problemas Identificados

### 1. Heading do Card (.problemas-card-heading)

**Desktop:**
- width: 100%
- font-size: 32px

**Tablet:**
- width: 516px
- text-align: center
- font-size: 36px

**Mobile:**
- width: 100%
- text-align: center
- font-size: 4.4vw ⚠️
- line-height: 1.3em ⚠️
- margin: 0 -20px 0 -20px ⚠️

### 2. Primeiro Parágrafo (.problemas-card-p1)

**Desktop:**
- width: 683px
- font-size: 20px
- font-weight: 600

**Tablet + Mobile:**
- width: 100%
- text-align: center
- font-size: 20px (mantém)

### 3. Segundo Parágrafo (.problemas-card-p2)

**Desktop:**
- width: 683px
- font-size: 18px
- font-weight: 400

**Tablet + Mobile:**
- width: 100%
- text-align: center
- font-size: 16px ⚠️ (reduz de 18px → 16px)

---

## Correções Necessárias

### Arquivo: `src/components/Problemas.astro`

#### 1. Heading do Card
```css
.problemas-card-heading {
  font-family: 'Factul', sans-serif;
  font-size: 32px;
  font-weight: 400;
  line-height: 1.2em;
  color: #1c3124;
  text-align: start;
  text-wrap: balance;
  margin: 0 0 20px 0;
}

/* Tablet */
@media (min-width: 768px) and (max-width: 1024px) {
  .problemas-card-heading {
    width: 516px;
    text-align: center;
    font-size: 36px;
  }
}

/* Mobile */
@media (max-width: 767px) {
  .problemas-card-heading {
    width: 100%;
    text-align: center;
    font-size: 4.4vw;
    line-height: 1.3em;
    margin: 0 -20px 0 -20px;
  }
}
```

#### 2. Primeiro Parágrafo
```css
.problemas-card-p1 {
  font-family: 'Inter', sans-serif;
  font-size: 20px;
  font-weight: 600;
  line-height: 1.4em;
  color: #0f0f0f;
  margin: 0 0 20px 0;
  width: 683px;
}

/* Tablet + Mobile */
@media (max-width: 1024px) {
  .problemas-card-p1 {
    width: 100%;
    text-align: center;
  }
}
```

#### 3. Segundo Parágrafo
```css
.problemas-card-p2 {
  font-family: 'Inter', sans-serif;
  font-size: 18px;
  font-weight: 400;
  line-height: 1.4em;
  color: #0f0f0f;
  margin: 0;
  width: 683px;
}

/* Tablet + Mobile */
@media (max-width: 1024px) {
  .problemas-card-p2 {
    width: 100%;
    text-align: center;
    font-size: 16px;
  }
}
```

---

## Resultado Esperado

✅ **Heading mobile**: width 100%, font-size 4.4vw, margin negativo -20px  
✅ **P1 mobile**: width 100%, font-size 20px (mantém)  
✅ **P2 mobile**: width 100%, font-size 16px (reduz)  
✅ **Tablet heading**: width 516px, font-size 36px  

**Meta:** Textos do card com widths e font-sizes corretos em todos os breakpoints
