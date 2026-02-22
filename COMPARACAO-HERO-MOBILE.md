# Comparação Hero Mobile: v2.0 vs Hero.astro

## Breakpoints Elementor
- **Mobile:** `@media (max-width: 767px)` e `@media (max-width: 1024px)`
- **Tablet:** `@media (max-width: 1024px) and (min-width: 768px)`
- **Desktop:** padrão (sem media query)

---

## 1. LOGO (elementor-element-a413a28)

### v2.0 Desktop
```css
width: var(--container-widget-width, 201px);
max-width: 201px;
text-align: start;
margin: -20px 0 20px 0; /* widget-container */
--align-self: center;
```

### v2.0 Mobile/Tablet
```css
width: var(--container-widget-width, 40.888%);
max-width: 40.888%;
text-align: center; ⚠️ DIFERENÇA
margin: 0 0 5% 0; /* widget-container */
--align-self: center;
```

### Hero.astro Atual
```astro
<div class="hero-logo-wrap">
  <img src="/img/095704.svg" alt="..." width="222" height="167" />
</div>
```

**CSS provável:** (precisa verificar em styles)
- Não tem `text-align: center` no mobile
- Width provavelmente fixo ou auto

---

## 2. TÍTULO (elementor-element-b5e6d6b)

### v2.0 Desktop
```css
width: 100%;
max-width: 100%;
text-align: center;
font-family: Factul, Sans-serif;
font-size: 43px;
font-weight: 400;
line-height: 1.1em;
color: #3b3b3b;
padding: 0;
```

### v2.0 Tablet
```css
font-size: 36px;
```

### v2.0 Mobile
```css
font-size: 6.3vw; ⚠️ RESPONSIVO
line-height: 1.2em; ⚠️ DIFERENTE DO DESKTOP (1.1em)
margin: 0 -4% -3% -4%; /* widget-container */
text-wrap: balance !important;
```

### Hero.astro Atual
```astro
<div class="hero-heading-wrap">
  <p class="hero-heading">
    Leve o seu filho de um repertório alimentar restrito para 
    <span class="underline-inner">uma alimentação variada e saudável</span>
  </p>
</div>
```

**Problemas prováveis:**
- Line-height pode estar como 1.1em em todos os breakpoints
- Font-size mobile pode não ser 6.3vw
- Falta margin negativo no mobile

---

## 3. SUBTÍTULO (elementor-element-864af24)

### v2.0 Desktop
```css
width: var(--container-widget-width, 683px);
max-width: 683px;
text-align: center;
font-family: Inter, Sans-serif;
font-size: 20px;
font-weight: 400;
line-height: 1.4em;
color: #0f0f0f;
padding: 0;
```

### v2.0 Tablet
```css
width: 100%;
max-width: 100%;
margin: 0 0 -8px 0; /* widget-container */
```

### v2.0 Mobile
```css
width: 100%;
max-width: 100%;
font-size: 4.1vw; ⚠️ RESPONSIVO
line-height: 1.4em;
margin: 0; /* widget-container */
```

### Hero.astro Atual
```astro
<div class="hero-subtitle-wrap">
  <p class="hero-subtitle">
    um método estruturado para famílias que querem resultados consistentes
  </p>
</div>
```

**Problemas prováveis:**
- Font-size mobile pode não ser 4.1vw
- Width pode não ser 100% no mobile

---

## 4. BOTÃO (elementor-element-14f4e7e)

### v2.0 Desktop
```css
font-family: Inter, Sans-serif;
font-size: 18px; ⚠️
font-weight: 600;
text-transform: uppercase;
letter-spacing: 0.9px;
border-radius: 1000px;
padding: 20px 40px;
--align-self: center;
```

### v2.0 Mobile
```css
font-size: 16px; ⚠️ DIFERENÇA
line-height: 1.2em;
letter-spacing: 0.9px;
border-radius: 100px;
padding: 20px 40px;
```

### Hero.astro Atual
```astro
<a href={HOTMART} class="btn-grad animation-grow" 
   style="font-family: 'Inter', sans-serif; font-size: 18px; font-weight: 600; letter-spacing: 0.9px; padding: 20px 40px;">
  Quero iniciar o acompanhamento
</a>
```

**Problema identificado:**
✅ **Font-size fixo em 18px** - deveria ser **16px no mobile**

---

## Resumo de Diferenças Identificadas

### 1. Logo
- ❌ Falta `text-align: center` no mobile
- ❌ Width mobile deveria ser `40.888%` (não fixo)
- ❌ Margin mobile deveria ser `0 0 5% 0`

### 2. Título
- ❌ Font-size mobile deveria ser `6.3vw` (responsivo)
- ❌ Line-height mobile deveria ser `1.2em` (não 1.1em)
- ❌ Falta margin negativo mobile: `0 -4% -3% -4%`

### 3. Subtítulo
- ❌ Font-size mobile deveria ser `4.1vw` (responsivo)
- ❌ Width mobile deveria ser `100%` (sem constraint de 683px)

### 4. Botão
- ✅ **CONFIRMADO:** Font-size mobile deveria ser `16px` (não 18px)

---

## Próximos Passos

1. Verificar CSS atual do Hero.astro (arquivo de estilos)
2. Aplicar correções mobile:
   - Logo: adicionar `text-align: center` + width + margin
   - Título: ajustar font-size (6.3vw), line-height (1.2em), margin
   - Subtítulo: ajustar font-size (4.1vw), width (100%)
   - Botão: mudar font-size de 18px → 16px no mobile
3. Testar no mobile (iOS/Android)
4. Deploy v1.2.5
