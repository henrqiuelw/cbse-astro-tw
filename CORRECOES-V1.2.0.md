# Correções Visuais v1.2.0

**Data:** 2025-02-22  
**Deploy:** 4b025447  
**Tag:** v1.2.0  
**Commit:** 98aa1e0

---

## 🎯 Objetivo

Corrigir diferenças visuais críticas vs v2.0-reference.html identificadas nas seções:
- Método (layout)
- Como Funciona (ícones accordion)

---

## ✅ Correções Aplicadas

### 1. Metodo.astro — Layout Refatorado

#### Problema
**v2.0 Reference:**
```
[Imagem laptop    ]  [Card 1: Método Estruturado        ]
[à esquerda       ]  [Card 2: Mudança de Fundamento     ]
[(320px desktop)  ]  [Card 3: Sequência Progressiva     ]
                     [Card 4: Autonomia Alimentar       ]
                     [Card 5: Flexível ao Desenvolvimento]
```

**v1.1.0 (ERRADO):**
```
Grid 3×2:
[Card 1] [Card 2] [Card 3]
[Card 4] [Card 5] [Imagem]
```

#### Solução
- Mudado de `display: grid` para `display: flex` com 2 colunas
- Imagem à esquerda (320px, desktop only)
- 5 cards empilhados verticalmente à direita
- Mobile/tablet: imagem esconde, cards em coluna

#### Código
```astro
<div class="metodo-content">
  <!-- Left: image -->
  <div class="metodo-img-col">
    <img src="/img/083313-copy.webp" ... />
  </div>
  
  <!-- Right: 5 cards vertical -->
  <div class="metodo-cards-col">
    {diferenciais.map((d) => (
      <div class="metodo-card">...</div>
    ))}
  </div>
</div>
```

```css
.metodo-content {
  display: flex;
  flex-direction: row;
  gap: 40px;
}
.metodo-img-col {
  flex: 0 0 auto;
  width: 320px;
}
.metodo-cards-col {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 30px;
}
```

### 2. Metodo.astro — Hover Effect Adicionado

#### Problema
v2.0 tem ícones que rotacionam 136° no hover. v1.1 não tinha.

#### Solução
```css
.metodo-icon {
  transition: transform 0.3s ease;
}
.metodo-card:hover .metodo-icon {
  transform: rotate(136deg);
}
```

### 3. ComoFunciona.astro — Ícones Accordion Corrigidos

#### Problema
**v2.0 (Elementor accordion):**
- Fechado: seta direita →
- Aberto: seta baixo ↓

**v1.1 (native `<details>`):**
- Fechado: seta baixo ↓ ❌
- Aberto: seta direita → ❌

#### Solução
Trocados os SVGs:

**Fechado (seta direita →):**
```html
<svg class="caret-closed" viewBox="0 0 192 512">
  <path d="M0 384.662V127.338c0-17.818 21.543-26.741 34.142-14.142l128.662 128.662c7.81 7.81 7.81 20.474 0 28.284L34.142 398.804C21.543 411.404 0 402.48 0 384.662z"/>
</svg>
```

**Aberto (seta baixo ↓):**
```html
<svg class="caret-open" viewBox="0 0 320 512">
  <path d="M31.3 192h257.3c17.8 0 26.7 21.5 14.1 34.1L174.1 354.8c-7.8 7.8-20.5 7.8-28.3 0L17.2 226.1C4.6 213.5 13.5 192 31.3 192z"/>
</svg>
```

---

## 📊 Comparação Antes/Depois

### Build
- **Tempo:** 483ms (consistente)
- **Arquivos modificados:** 2 (Metodo.astro, ComoFunciona.astro)
- **Erros:** 0 ✅

### Deploy
- **v1.1.0:** a019e7a5
- **v1.2.0:** 4b025447
- **Upload:** 2 arquivos novos, 46 em cache
- **Tempo:** 1.02s

### Visual
| Seção | v1.1.0 | v1.2.0 |
|-------|--------|--------|
| **Método (layout)** | Grid 3×2 ❌ | 2-column ✅ |
| **Método (hover)** | Sem hover ❌ | Rotação 136° ✅ |
| **Accordion (ícones)** | Invertidos ❌ | Corretos ✅ |

---

## 🔗 Links

- **Deploy v1.2.0:** https://4b025447.cbse-site-tw.pages.dev
- **Produção:** https://cbse-site-tw.pages.dev
- **v1.1.0 (anterior):** https://a019e7a5.cbse-site-tw.pages.dev
- **Reference (mirror):** https://cbse-mirrorclean.pages.dev

---

## 📋 Arquivos Modificados

```
src/components/ComoFunciona.astro    — Ícones accordion corrigidos
src/components/Metodo.astro          — Layout 2-column + hover effect
```

---

## 🎯 Status das Seções

### ✅ Pixel Perfect Confirmadas
- Hero
- Comparação
- Depoimentos
- Bônus (estrutura)

### ✅ Corrigidas em v1.2.0
- Método (layout + hover)
- Como Funciona (ícones)

### ⏳ Pendente Verificação
- GradientBar
- Problemas
- Fases
- Pricing
- SobreFlavia
- FAQ
- Footer

---

## 🚀 Próximos Passos

1. ✅ Deploy v1.2.0
2. ✅ Tag criada
3. ✅ Commit feito
4. ⏳ Validação visual (comparar lado a lado)
5. ⏳ Verificar seções restantes
6. ⏳ Planejar v1.3.0 (se necessário)

---

**Versão:** 1.2.0  
**Status:** ✅ Deployada e pronta para validação
