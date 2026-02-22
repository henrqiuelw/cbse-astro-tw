# Diferenças Críticas — Seções 3, 4, 6 e Bônus

**Análise:** v1.1.0 Astro vs v2.0 Reference  
**Seções:** Método, Comparação, Como Funciona, Bônus Exclusivos

---

## 3️⃣ Seção MÉTODO (Sistema alimentar estruturado)

### ❌ Diferenças Encontradas

#### Layout
**v2.0 Reference:**
- Imagem decorativa (laptop/criança) à **esquerda** em desktop
- 5 cards verticais em **coluna única** à direita
- Mobile: imagem some, cards em coluna

**Astro v1.1:**
- Grid **3×2** (6 espaços)
- 5 cards + imagem decorativa no **6º espaço** (canto inferior direito)
- Imagem some em tablet/mobile

**Impacto:** **ALTO** — layout completamente diferente

#### Cards
**v2.0:**
- Ícones de ovo/folha dourados **rotacionam no hover** (transform)
- Cards sem bordas visíveis
- Ícone: `141704.svg` (ovo/folha)

**Astro:**
- Ícones de checkmark verde (não rotacionam)
- Cards com `box-shadow` pronunciada
- Ícone: mesmo `141704.svg` mas sem hover effect

**Impacto:** **MÉDIO** — ícone e interatividade

#### Tipografia
**v2.0:**
- Título bold/italic com borda verde à esquerda
- Descrição regular

**Astro:**
- Título regular (não bold/italic)
- Borda verde à esquerda na descrição bold
- Descrição regular separada

**Impacto:** **BAIXO** — estrutura similar

---

## 4️⃣ Seção COMPARAÇÃO (Sem vs Com)

### ✅ Estrutura Correta

**v2.0 Reference:**
- Fundo gradiente dourado/laranja ✅
- Card branco central com gradiente radial ✅
- 2 listas (Sem = X vermelho, Com = ✓ verde) ✅
- Divisor entre listas ✅
- CTA verde ao final ✅

**Astro v1.1:**
- Tudo idêntico ✅

### ⚠️ Diferenças Menores

#### Quantidade de items
**v2.0:**
- 4 items "Sem" (X vermelho)
- 4 items "Com" (✓ verde)

**Astro v1.1:**
- 4 items "Sem" ✅
- 4 items "Com" ✅

**Impacto:** **NENHUM** — perfeito

#### Underline
**v2.0:**
- `box-shadow: inset 0 -7px 0 0 #ff0b00;` (vermelho)
- `box-shadow: inset 0 -7px 0 0 #25a75c;` (verde)

**Astro:**
- `.underline-red`: `box-shadow: inset 0 -7px 0 0 #ff0b00;` ✅
- `.underline-verde`: `box-shadow: inset 0 -7px 0 0 #25a75c;` ✅

**Impacto:** **NENHUM** — cores corretas

---

## 6️⃣ Seção COMO FUNCIONA (Accordion 4 semanas)

### ✅ Estrutura Correta

**v2.0 Reference:**
- Fundo gradiente verde escuro ✅
- Card creme com bordas arredondadas ✅
- Hint "Clique nos módulos" ✅
- 4 accordions ✅
- Headers laranja com gradiente ✅

**Astro v1.1:**
- Tudo idêntico ✅

### ⚠️ Diferenças Encontradas

#### Ícones de seta
**v2.0 (Elementor accordion):**
- Fechado: seta para **direita** →
- Aberto: seta para **baixo** ↓

**Astro (native `<details>`):**
- Fechado: seta para **baixo** ↓ (`.caret-closed`)
- Aberto: seta para **direita** → (`.caret-open`)

**❌ INVERTIDO!**

**Impacto:** **ALTO** — ícones estão ao contrário

#### Quantidade de módulos por semana
**v2.0:**
- Semana 1: 2 módulos ✅
- Semana 2: 1 módulo ✅
- Semana 3: 1 módulo ✅
- Semana 4: 2 módulos ✅

**Astro:**
- Semana 1: 2 módulos ✅
- Semana 2: 1 módulo ✅
- Semana 3: 1 módulo ✅
- Semana 4: 2 módulos ✅

**Impacto:** **NENHUM** — perfeito

#### Badge "Semana X"
**v2.0:**
- Badge branco com fundo laranja
- Texto laranja

**Astro:**
- Badge branco com fundo do header
- Texto laranja `#c47519`

**Impacto:** **NENHUM** — visual idêntico

---

## 🎁 Seção BÔNUS EXCLUSIVOS

### ✅ Estrutura Correta

**v2.0 Reference:**
- 3 cards com gradiente verde ✅
- Alternância de layout (reverse) ✅
- Badges dourados "BÔNUS 01/02/03" ✅
- Divisor decorativo branco ✅

**Astro v1.1:**
- Tudo idêntico ✅

### ⚠️ Diferenças Menores

#### Gradientes
**v2.0:**
- Bônus 01: `linear-gradient(103deg, #244030 0%, #4e8867 100%)` ✅
- Bônus 02: `linear-gradient(180deg, #244030 0%, #4e8867 100%)` ✅
- Bônus 03: `linear-gradient(103deg, #244030 0%, #4e8867 100%)` ✅

**Astro:**
- Exatamente iguais ✅

**Impacto:** **NENHUM**

#### Badge dourado
**v2.0:**
- Background: (não especificado, assumindo dourado)

**Astro:**
- Background: `#DBB953` (dourado)

**Impacto:** **BAIXO** — precisa verificar se cor exata

#### Mobile behavior
**v2.0:**
- Reverse se mantém em mobile? (precisaria testar)

**Astro:**
- `flex-direction: column !important;` em mobile (sempre imagem em cima)

**Impacto:** **MÉDIO** — mobile pode estar diferente

---

## 📊 RESUMO EXECUTIVO

### 🔴 Diferenças CRÍTICAS (necessário corrigir)

1. **MÉTODO — Layout completamente diferente**
   - v2.0: Imagem à esquerda, 5 cards verticais à direita
   - Astro: Grid 3×2 com imagem no canto

2. **COMO FUNCIONA — Ícones de accordion invertidos**
   - v2.0: Fechado = direita →, Aberto = baixo ↓
   - Astro: Fechado = baixo ↓, Aberto = direita →

### 🟡 Diferenças MÉDIAS (verificar)

3. **MÉTODO — Hover effect nos ícones**
   - v2.0: Ícones rotacionam no hover
   - Astro: Sem hover effect

4. **BÔNUS — Mobile layout**
   - Precisa verificar se reverse se mantém em mobile no v2.0

### 🟢 Seções CORRETAS

- **COMPARAÇÃO** — Pixel perfect ✅
- **BÔNUS (estrutura)** — Quase perfeito ✅

---

## 🔧 CORREÇÕES NECESSÁRIAS

### Prioridade ALTA

1. **Refazer layout do MÉTODO**
   ```
   - Mudar de grid 3×2 para layout 2-column
   - Imagem à esquerda (desktop)
   - 5 cards verticais à direita
   - Mobile: imagem some, cards em coluna
   ```

2. **Inverter ícones do accordion**
   ```css
   /* Fechado: seta direita */
   .caret-closed {
     /* Usar ícone de seta direita */
   }
   /* Aberto: seta baixo */
   .caret-open {
     /* Usar ícone de seta baixo */
   }
   ```

### Prioridade MÉDIA

3. **Adicionar hover effect nos ícones do MÉTODO**
   ```css
   .metodo-icon {
     transition: transform 0.3s ease;
   }
   .metodo-card:hover .metodo-icon {
     transform: rotate(136deg);
   }
   ```

### Prioridade BAIXA

4. **Verificar badge dourado do Bônus**
   - Confirmar se `#DBB953` é a cor exata

---

## ✅ CHECKLIST DE CORREÇÕES

- [ ] Refazer Metodo.astro (layout 2-column)
- [ ] Inverter ícones do accordion (ComoFunciona.astro)
- [ ] Adicionar hover rotation aos ícones (Metodo.astro)
- [ ] Testar mobile do Bônus (comparar reverse)
- [ ] Build + deploy
- [ ] Comparação visual final

**Quer que eu comece pelas correções de prioridade ALTA?**
