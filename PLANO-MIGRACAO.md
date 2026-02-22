# PLANO DE MIGRAÇÃO CBSE v2.0 → Astro+Tailwind

## Executive Summary
- Decisão: CONTINUAR — base Astro modular já implementada (13 componentes), assets copiados e stack moderna (Astro 5 + Tailwind 4).
- Status atual: ~80% estruturalmente completo; fidelidade de conteúdo e performance ainda não validadas.
- Tempo total estimado para finalização: 5h–8h.

---

## Análise de Gaps

### 1. Divergências de Conteúdo
- Necessário comparar `v2.0-reference.html` (linha 274+ início hero) com `src/components/Hero.astro` — título principal e subtítulo devem ser idênticos ao OG title/description (linhas 1–1 do HTML).
- Validar todos os CTAs Hotmart (mín. 6 ocorrências no projeto) vs links reais no HTML v2.0.
- Conferir textos das seções: Problemas, Método, Comparação, Fases, SobreFlavia, ComoFunciona, Bonus, Depoimentos, Pricing, FAQ — 1:1 com HTML.
- Garantir mesma ordem de seções do v2.0 (confirmar contra DOM após `<body>` linha 274).

### 2. Funcionalidades Interativas
- Swiper: v2.0 usa CDN + init custom (linhas 276–321). Verificar implementação equivalente em `src/components/Depoimentos.astro`.
- FAQ accordion: lógica custom com aria + animação suave (linhas 324–406). Conferir se `src/components/FAQ.astro` replica comportamento e transições.
- Lottie: script defer (linha 265) + init (411–439). Validar se Hero usa `lottie-web` com `defer` e mesma config (loop/autoplay).

### 3. Performance e Otimizações
- v2.0 usa `fetchpriority="high"` no hero (linha 1) → validar imagem principal no `Hero.astro`.
- Lazy loading explícito (`loading="lazy"`) em imagens não críticas — revisar todos `<img>` nos componentes.
- CSS crítico inline no v2.0 — avaliar extração de critical CSS via Astro build.
- Scripts com `defer` (Swiper + Lottie) — confirmar em `Layout.astro`.
- Preload de fontes Factul — validar equivalência com `global.css`.

### 4. Responsividade
- Breakpoints v2.0: 767px (mobile), 1024px (tablet), 1366px (laptop) — ver config em Tailwind (`tailwind.config`).
- Conferir se layouts mobile-first replicam Elementor spacing.
- Validar grids (ex: Pricing e Comparação) em 320px, 768px, 1024px, 1366px.

---

## Plano de Ação

### Fase 1: Validação (1–2h)

- 🔴 Build local: `npm run build && npm run preview` — validar console sem erros.
  - Dependência: Node/npm ok.
- 🔴 Comparar DOM renderizado vs `v2.0-reference.html` usando DevTools (Elements tab).
- 🔴 Verificar todos os textos e CTAs manualmente seção por seção.
- 🟡 Mapear divergências em checklist (arquivo temporário ou issues).
- 🟢 Conferir meta tags SEO em `src/layouts/Layout.astro` vs OG tags do HTML (linha 1).

Entrega: lista fechada de divergências críticas.

---

### Fase 2: Correções Críticas (2–3h)

- 🔴 Ajustar textos divergentes diretamente nos componentes afetados.
  - Ex: `src/components/Hero.astro`, `src/components/Pricing.astro`, `src/components/FAQ.astro`.
- 🔴 Corrigir todos links Hotmart (garantir `target` e `rel` corretos).
- 🔴 Implementar `loading="lazy"` e `decoding="async"` em imagens não críticas.
- 🔴 Garantir `fetchpriority="high"` apenas na imagem hero.
- 🟡 Revisar Swiper breakpoints para equivalência (0, 768, 1024).
- 🟡 Ajustar animação FAQ para transição suave (max-height + opacity).
- 🟢 Reduzir CSS custom redundante se não impactar fidelidade.

Dependência: conclusão da Fase 1.

---

### Fase 3: Testes (1–2h)

- 🔴 Testes responsivos manuais (Chrome DevTools):
  - 375px (mobile)
  - 768px (tablet)
  - 1024px (desktop pequeno)
  - 1366px (laptop)
- 🔴 Testar Swiper (loop, autoplay, pagination).
- 🔴 Testar FAQ (abrir/fechar múltiplos itens).
- 🟡 Validar Lottie carregando corretamente sem bloquear render.
- 🟡 Rodar PageSpeed Insights (mobile + desktop) e comparar com baseline 75.
- 🟢 Lighthouse local via DevTools para diagnóstico rápido.

Critério de aceite: PageSpeed ≥ 75 mobile.

---

### Fase 4: Deploy (30min)

- 🔴 Build produção: `npm run build`.
- 🔴 Deploy Cloudflare Pages (branch main).
- 🔴 Validar produção (mobile real + desktop).
- 🟡 Rodar PageSpeed na URL pública.
- 🟢 Ajustes rápidos pós-deploy se necessário.

Dependência: Fase 3 concluída.

---

## Próximos Passos Imediatos (30min)

1. Rodar `npm run build && npm run preview`.
2. Abrir v2.0-reference.html e site preview lado a lado.
3. Validar Hero (título, subtítulo, CTA, imagem).
4. Validar Pricing (preço, bônus, garantias, CTA).
5. Validar FAQ (perguntas idênticas e ordem correta).

---

## Riscos e Mitigações

- Conteúdo divergente → Mitigação: comparação manual linha a linha.
- Performance inferior ao v2.0 → Mitigação: auditoria Lighthouse + otimizações específicas (lazy, preload, defer).
- Quebra em mobile → Mitigação: testes sistemáticos por breakpoint.
- Scripts duplicados ou bloqueantes → Mitigação: garantir `defer` e evitar múltiplas instâncias.

---

Conclusão: Estrutura sólida. Foco agora é fidelidade absoluta ao v2.0 (conteúdo + performance). Após validação, deploy seguro.
