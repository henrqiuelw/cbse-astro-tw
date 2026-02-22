# Diferenças Visuais — v1.1 vs v2.0 Reference

**Tag:** v1.1.0  
**Score:** 81 (mobile)  
**Status:** Hero confirmado como pixel perfect ✅

---

## Metodologia de Análise

Vou comparar cada seção exceto Hero (já confirmado como pixel perfect) e documentar:
- Layout/estrutura
- Cores e tipografia
- Espaçamentos
- Componentes interativos
- Responsividade

---

## 🔍 Seções Analisadas

### 1. ✅ GradientBar
**Status:** Precisa verificar visualmente

**v2.0 Reference:**
- Gradiente verde → dourado → verde
- Altura: 2px

**Astro v1.1:**
- Verificar se gradiente está idêntico
- Verificar altura

### 2. 🔄 Problemas (Lista com 5 problemas)
**Status:** Precisa verificar

**v2.0 Reference:**
```html
- Repertório alimentar restrito
- Negociação constante
- Faz tudo certo mas não vê evolução
- Falta clareza sobre quando insistir
- Alimentação ocupa energia mental excessiva
```

**Astro v1.1:**
- Componente: `Problemas.astro`
- Verificar se tem 5 ou 6 items
- Verificar ícones (setas verdes)
- Verificar textos

### 3. 🔄 Método (Sistema alimentar favorável)
**Status:** Precisa verificar

**v2.0 Reference:**
- 5 cards com ícones de ovo/folha
- Títulos: Método Estruturado, Mudança de Fundamento, Sequência Progressiva, Autonomia Alimentar, Flexível ao Desenvolvimento
- Ícone rotativo no hover

**Astro v1.1:**
- Componente: `Metodo.astro`
- Verificar se tem 5 cards
- Verificar ícones e hover

### 4. 🔄 Comparacao (Com CBSE vs Sem CBSE)
**Status:** Precisa verificar

**v2.0 Reference:**
- 2 colunas (vermelho vs verde)
- X vermelho vs ✓ verde
- 4 items cada lado

**Astro v1.1:**
- Componente: `Comparacao.astro`
- Verificar cores
- Verificar ícones

### 5. 🔄 Fases (4 fases do método)
**Status:** Precisa verificar

**v2.0 Reference:**
- 4 cards horizontais com gradiente verde
- Ícones de ovo numerados (1, 2, 3, 4)
- Títulos: Diagnóstica, Estruturação, Alimentar, Consolidação
- Mobile: scroll horizontal

**Astro v1.1:**
- Componente: `Fases.astro`
- Verificar layout mobile
- Verificar ícones

### 6. 🔄 ComoFunciona (Accordion de 4 semanas)
**Status:** Precisa verificar

**v2.0 Reference:**
- Card creme de fundo
- Hint "Clique nos módulos para saber mais"
- 4 accordions com ícones de seta
- Listas de módulos com checkmarks verdes
- Semana 1 tem 2 módulos, Semana 2 tem 1, Semana 3 tem 1, Semana 4 tem 2

**Astro v1.1:**
- Componente: `ComoFunciona.astro`
- Verificar quantidade de módulos por semana
- Verificar ícones de seta (direita fechado, baixo aberto)
- Verificar checkmarks

### 7. ✅ Bonus
**Status:** Provável pixel perfect

**v2.0 Reference:**
- 3 cards com gradiente verde
- Alternância de layout (reverse)
- Badges "BÔNUS 01/02/03"
- Divisor decorativo

**Astro v1.1:**
- Componente: `Bonus.astro`
- Verificar alternância

### 8. ✅ Depoimentos
**Status:** Funcionando com lazy load

**v2.0 Reference:**
- Swiper carousel Elementor
- 13 slides
- Autoplay 5s
- Paginação dourada

**Astro v1.1:**
- Lazy loading implementado ✅
- 13 slides ✅
- Autoplay 5s ✅
- Bullets dourados ✅

### 9. 🔄 Pricing/Oferta
**Status:** Precisa verificar

**v2.0 Reference:**
- 3 colunas (lista | preço | CTA)
- Selo de garantia 7 dias
- Preço riscado vs atual
- Badge desconto
- 12x R$ 30,72
- R$ 297 à vista

**Astro v1.1:**
- Componente: `Pricing.astro`
- Verificar layout de 3 colunas
- Verificar selo de garantia
- Verificar valores

### 10. 🔄 SobreFlavia
**Status:** Precisa verificar

**v2.0 Reference:**
- Foto circular da Flávia (lado esquerdo em desktop)
- Título "Quem criou o Comer bem sem estresse?"
- Nome "Flávia Andrade"
- Bio longa (vários parágrafos)
- CRN mencionado implicitamente

**Astro v1.1:**
- Componente: `SobreFlavia.astro`
- Verificar layout foto + texto
- Verificar bio completa

### 11. 🔄 FAQ
**Status:** Precisa verificar

**v2.0 Reference:**
- 9 perguntas com Elementor accordion
- Ícones de seta (direita fechado, baixo aberto)
- Perguntas listadas no HTML

**Astro v1.1:**
- Componente: `FAQ.astro`
- Usa `<details>` nativos
- Verificar quantidade (9)
- Verificar ícones

### 12. ✅ Footer
**Status:** Provável pixel perfect

**v2.0 Reference:**
```
© 2026 · Comer bem sem estresse · Todos os direitos reservados.
Contato: suporte@comerbemsemestresse.com.br
```

**Astro v1.1:**
- Componente: `Footer.astro`
- Verificar copyright
- Verificar email de contato

---

## ⚠️ Diferenças Potenciais Identificadas

### Tipografia
- v2.0 usa Factul (custom font) + Inter
- v1.1 deve usar as mesmas fontes
- **Verificar:** Pesos de fonte (regular, light, medium, bold)

### Cores
- Verde principal: `#269D59` (v2.0) vs `#6bb577` (Astro checkmarks)
- Dourado: `#f89a2b` (v2.0 pricing) vs `#DBB953` (Astro pagination)
- Creme: `#ECE1C9` / `#FDF6EC` / `#F0EADF`
- **Verificar:** Consistência de cores

### Ícones
- v2.0 usa SVGs inline customizados
- Astro pode usar os mesmos ou similares
- **Verificar:** Checkmarks verdes, Xs vermelhos, setas de accordion

### Espaçamentos
- v2.0 usa Elementor com espaçamentos específicos
- **Verificar:** Padding/margin de seções

---

## 📋 Checklist de Verificação Visual

Para cada seção (exceto Hero):

1. Abrir v2.0-reference.html no navegador
2. Abrir https://cbse-site-tw.pages.dev lado a lado
3. Comparar em desktop (1280px+)
4. Comparar em mobile (375px)
5. Anotar diferenças encontradas

**Ferramentas:**
- Screenshots lado a lado
- DevTools para inspecionar espaçamentos
- Color picker para cores

---

## 🎯 Próxima Ação

1. **Método sugerido:** Usar browser automation para tirar screenshots de cada seção
2. **Alternativa manual:** Abrir ambas as versões e comparar visualmente
3. **Ferramentas úteis:** 
   - PixelSnap para medir espaçamentos
   - ColorSnapper para verificar cores exatas
   - Responsively App para múltiplos viewports

**Quer que eu:**
- A) Abra ambas as versões no browser e tire screenshots automatizados?
- B) Você prefere fazer a comparação visual manualmente e me avisar das diferenças?
- C) Focar nas seções específicas que você já sabe que têm diferenças?
