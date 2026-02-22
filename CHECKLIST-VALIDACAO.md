# ✅ CHECKLIST DE VALIDAÇÃO - CBSE Astro+Tailwind

**Preview:** <http://localhost:4321/>  
**Data:** 2026-02-22

---

## 🎯 CRÍTICO (Testar Primeiro)

### 1. Swiper de Depoimentos ⏱️ 2min

**Localização:** Role até "Veja os resultados de mães e alunas"

- [ ] Autoplay funciona (troca automática a cada 5s)
- [ ] Pagination (bolinhas) é clicável
- [ ] Loop infinito (volta ao início sem quebrar)
- [ ] Mobile (375px): 2 slides visíveis
- [ ] Desktop (1024px+): 5 slides visíveis

**Como testar mobile:**
1. F12 → Toggle device toolbar (Ctrl+Shift+M)
2. Selecionar "iPhone SE" ou "Responsive" e ajustar para 375px

---

### 2. FAQ Accordion ⏱️ 1min

**Localização:** Role até "Perguntas frequentes"

- [ ] Clique abre/fecha suavemente
- [ ] Seta gira 180° ao abrir
- [ ] Não há "pulos" ao expandir conteúdo

---

### 3. Lottie Ovo (Mobile) ⏱️ 30s

**Localização:** Hero (topo da página), apenas em mobile

- [ ] Em mobile (375px): ovo animado aparece abaixo do botão CTA
- [ ] Em desktop (1024px+): ovo NÃO aparece

---

## 📱 RESPONSIVIDADE (Opcional mas Recomendado)

### Breakpoints para Testar

- [ ] **Mobile (375px):** Layout vertical, texto legível
- [ ] **Tablet (768px):** Grid 2-3 colunas
- [ ] **Desktop (1024px):** Grid completo (5 colunas no Swiper)
- [ ] **Large (1366px):** Sem overflow horizontal

**Seções críticas:**
- Hero (título + vídeo)
- Método (grid 3×2 com 6 cards)
- Depoimentos (Swiper)
- Pricing (oferta)

---

## 🚀 DEPLOY (Quando Tudo Estiver OK)

### Pré-Deploy Checklist

- [ ] Todos os testes acima passaram
- [ ] Build local sem erros (`npm run build`)
- [ ] Preview local funcional

### Deploy para Cloudflare Pages

```bash
npm run build

CLOUDFLARE_API_TOKEN=$(security find-generic-password -a "openclaw" -s "cloudflare-api-token" -w) \
npx wrangler pages deploy dist --project-name cbse-site-tw
```

### Pós-Deploy

- [ ] Testar URL pública (cbse-site-tw.pages.dev)
- [ ] PageSpeed Insights mobile ≥ 70
- [ ] Testar em mobile real (iPhone/Android)

---

## 🐛 Se Algo Não Funcionar

### Swiper não aparece / não funciona
1. Verificar console do browser (F12 → Console)
2. Procurar erro "Swiper library not loaded!"
3. Se aparecer: limpar cache do browser (Ctrl+Shift+R)

### FAQ não abre
1. Verificar se está clicando na seta OU no texto
2. Ambos devem funcionar (são parte do `<summary>`)

### Lottie não aparece
1. Normal em desktop (só aparece em mobile < 768px)
2. Se não aparece em mobile: verificar console por erros

---

## 📊 Critérios de Aprovação

### Mínimo para Deploy (MVP)
- ✅ Swiper com autoplay + pagination
- ✅ FAQ abrindo/fechando
- ✅ Sem erros no console

### Ideal (Nice to Have)
- ✅ Swiper responsivo em todos os breakpoints
- ✅ FAQ com transição suave
- ✅ Lottie funcionando em mobile
- ✅ PageSpeed ≥ 75 mobile

---

**Tempo estimado:** 5-10 minutos para validação completa

**Status Atual:**
- ✅ Código implementado
- ✅ Build passando
- ⏳ **Aguardando validação visual**
- ⏳ Aguardando deploy

**Próximo passo:** Validar visualmente → Deploy → PageSpeed test
