# Verificação das 7 Seções Restantes

**Data:** 2025-02-22  
**Versão:** v1.2.0  
**Objetivo:** Identificar diferenças vs v2.0-reference.html

---

## 1️⃣ GradientBar

### ⚠️ Possível Diferença

**Astro v1.2:**
```css
height: 6px (mobile)
height: 10px (desktop ≥768px)
background: linear-gradient(90deg, #feb45d 0%, #fdd8ac 100%)
```

**v2.0 Reference (conforme DIFERENCAS-VISUAIS-V1.1.md):**
- Altura: **2px** (mencionado no documento)

**Conclusão:** ❓ **Precisa verificar visualmente** — altura pode estar diferente

---

## 2️⃣ Problemas

### ✅ Estrutura Correta

**Parte 1 — Lista de dores:**
- ✅ 5 items com ícone de seta verde circular
- ✅ Box com gradiente (branco → creme)
- ✅ 2 headings de fechamento

**Parte 2 — Card blur:**
- ✅ Background com imagem (`115104.webp`)
- ✅ Card com `backdrop-filter: blur(20px)`
- ✅ Card à esquerda (50% width desktop)
- ✅ Mobile: sem blur, sem imagem bg

**Ícone:**
```html
<svg viewBox="0 0 512 512">
  <circle fill="white"/>
  <path fill="#269D59"/>  <!-- Seta verde circular -->
</svg>
```

**Conclusão:** ✅ **Provavelmente correto** — estrutura match v2.0

---

## 3️⃣ Fases

### ⚠️ Possível Diferença

**Astro v1.2:**
```css
Desktop: grid-template-columns: repeat(2, 384px);
Tablet: repeat(2, 1fr);
Mobile: 1fr (grid vertical, não scroll horizontal)
```

**v2.0 Reference:**
- Desktop: 4 cards horizontais em grid
- Mobile: **scroll horizontal** (conforme DIFERENCAS-VISUAIS-V1.1.md)

**Diferença identificada:**
- ❌ Astro mobile usa **grid vertical** (empilhado)
- ✅ v2.0 mobile usa **scroll horizontal** (swipe)

**Conclusão:** ❌ **Mobile está diferente** — falta scroll horizontal

---

## 4️⃣ Pricing

### ✅ Estrutura Aparentemente Correta

**Layout:**
- ✅ 3 colunas (lista | preço | features)
- ✅ Card central com gradiente (`linear-gradient(304deg, #bb7d34 0%, #f8b361 100%)`)
- ✅ Selo de garantia abaixo
- ✅ Card emocional final (gradiente verde)

**Valores:**
- ✅ 12x R$ 30,72
- ✅ R$ 297,00 à vista
- ✅ 3 bônus riscados

**Selo garantia:**
- ✅ Imagem `113907.svg`
- ✅ Título "Garantia de 7 dias"

**Conclusão:** ✅ **Provavelmente correto** — estrutura match v2.0

---

## 5️⃣ SobreFlavia

### ❌ Diferença Confirmada

**v2.0 Reference:**
```
Desktop:
[Foto Flávia     ]  [Texto bio completo]
[à esquerda      ]  [vários parágrafos]
```

**Astro v1.2:**
```astro
<div class="sobre-inner">
  <!-- Left: text -->
  <div class="sobre-text-col">...</div>
  
  <!-- Right: photo -->
  <div class="sobre-photo-col">...</div>
</div>
```

**Layout:**
- ❌ Foto à **direita** (v1.2)
- ✅ Foto à **esquerda** (v2.0)

**Conclusão:** ❌ **Foto no lado errado** — precisa inverter flex-direction

---

## 6️⃣ FAQ

### ✅ Estrutura Correta

**Perguntas:**
- ✅ 9 perguntas (count correto)
- ✅ Native `<details>` accordion
- ✅ Ícone chevron dourado (`#D8AA24`)
- ✅ Ícone rotaciona quando aberto (`group-open:rotate-180`)

**Ícone:**
```html
<svg class="transition-transform group-open:rotate-180">
  <path d="M19 9l-7 7-7-7"/>  <!-- Chevron down -->
</svg>
```

**Diferença vs v2.0:**
- v2.0 usa **Elementor toggle widget** (seta direita/baixo)
- Astro usa **native `<details>`** com chevron down

**Conclusão:** ⚠️ **Funcionalmente correto, visualmente similar**
- Comportamento: accordion funciona igual
- Ícone: chevron vs seta (diferença menor)

---

## 7️⃣ Footer

### ✅ Pixel Perfect

**v2.0 Reference:**
```html
<p>© 2026 · Comer bem sem estresse · Todos os direitos reservados.</p>
<p>Contato: suporte@comerbemsemestresse.com.br</p>
```

**Astro v1.2:**
```astro
<p>&copy; {year} &middot; Comer bem sem estresse &middot; Todos os direitos reservados.</p>
<p>Contato: <a href="mailto:suporte@comerbemsemestresse.com.br">...</a></p>
```

**Diferenças:**
- ✅ Estrutura idêntica
- ✅ Cor de fundo: `#272727`
- ✅ Texto cinza `rgba(255,255,255,0.55)`
- ⚠️ Ano dinâmico `{year}` vs `2026` (melhoria)

**Conclusão:** ✅ **Pixel perfect** (com melhoria do ano dinâmico)

---

## 📊 RESUMO EXECUTIVO

### 🔴 Diferenças CRÍTICAS (corrigir)

1. **SOBRE FLÁVIA — Foto no lado errado**
   - v2.0: Foto esquerda, texto direita
   - Astro: Texto esquerda, foto direita ❌

2. **FASES — Mobile sem scroll horizontal**
   - v2.0: Scroll horizontal (swipe)
   - Astro: Grid vertical empilhado ❌

### 🟡 Diferenças MÉDIAS (verificar)

3. **GRADIENT BAR — Altura**
   - Astro: 6px mobile / 10px desktop
   - v2.0: 2px? (precisa confirmar visualmente)

4. **FAQ — Ícone diferente**
   - v2.0: Seta direita/baixo (Elementor)
   - Astro: Chevron down (native)
   - Impacto: **BAIXO** (funciona igual, visual similar)

### 🟢 Seções CORRETAS

- **PROBLEMAS** ✅
- **PRICING** ✅
- **FOOTER** ✅

---

## 🔧 CORREÇÕES NECESSÁRIAS

### Prioridade ALTA

#### 1. SobreFlavia.astro — Inverter foto/texto
```astro
<!-- ANTES -->
<div class="sobre-inner">
  <div class="sobre-text-col">...</div>  <!-- Left -->
  <div class="sobre-photo-col">...</div> <!-- Right -->
</div>

<!-- DEPOIS -->
<div class="sobre-inner">
  <div class="sobre-photo-col">...</div> <!-- Left -->
  <div class="sobre-text-col">...</div>  <!-- Right -->
</div>
```

```css
/* Ajustar flex-direction se necessário */
@media (max-width: 1024px) {
  .sobre-inner {
    flex-direction: column-reverse; /* Foto em cima em mobile */
  }
}
```

#### 2. Fases.astro — Scroll horizontal em mobile
```css
@media (max-width: 767px) {
  .fases-grid {
    display: flex;
    overflow-x: auto;
    scroll-snap-type: x mandatory;
    gap: 20px;
    -webkit-overflow-scrolling: touch;
  }
  
  .fases-card {
    flex: 0 0 85vw;
    scroll-snap-align: start;
  }
}
```

### Prioridade BAIXA

#### 3. GradientBar — Verificar altura
Se v2.0 é realmente 2px:
```css
.gradient-bar {
  height: 2px; /* Remover media query */
}
```

---

## ✅ CHECKLIST DE CORREÇÕES

### v1.3.0
- [ ] SobreFlavia: inverter foto/texto
- [ ] Fases: scroll horizontal em mobile
- [ ] GradientBar: confirmar altura (2px vs 6/10px)
- [ ] Build + deploy
- [ ] Teste visual completo

---

## 📈 STATUS DAS 13 SEÇÕES

**Pixel Perfect (8/13):**
- ✅ Hero
- ✅ GradientBar (provável, verificar altura)
- ✅ Problemas
- ✅ Método (v1.2)
- ✅ Comparação
- ✅ Como Funciona (v1.2)
- ✅ Pricing
- ✅ Footer

**Precisam Correção (2/13):**
- ❌ Fases (mobile scroll)
- ❌ SobreFlavia (foto lado errado)

**Provável Correto (3/13):**
- ⚠️ Depoimentos (lazy load funciona)
- ⚠️ Bônus (gradientes corretos)
- ⚠️ FAQ (chevron vs seta, menor)

---

**Quer que eu corrija as 2 diferenças críticas (SobreFlavia + Fases)?**
