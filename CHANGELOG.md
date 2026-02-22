# Changelog - CBSE Astro+Tailwind

Todas as mudanças notáveis neste projeto serão documentadas aqui.

---

## [1.0.0] - 2026-02-22

### ✨ Lançamento Inicial

Migração completa do site CBSE de WordPress/Elementor para Astro+Tailwind.

### 🎯 Funcionalidades Principais

- **Hero Section:** Vídeo VSL + CTA Hotmart + Lottie animation (mobile)
- **Seção Problemas:** Lista de dores + card com background blur
- **Seção Método:** Grid 3×2 com 6 cards explicativos
- **Seção Comparação:** Antes/depois com ícones X/Check
- **Seção Fases:** Grid 2×2 das 4 fases do método
- **Sobre Flávia:** Bio + foto em 2 colunas
- **Como Funciona:** Accordion com 4 semanas de conteúdo
- **Bônus:** 3 cards com gradientes verdes
- **Depoimentos:** Swiper carousel com 13 depoimentos
- **Pricing:** Oferta 12x + bônus + garantia
- **FAQ:** 9 perguntas com `<details>` nativo

### ⚡ Performance

- ✅ PageSpeed mobile ≥ 75
- ✅ Fetchpriority em imagens críticas (2)
- ✅ Loading lazy apenas em imagens não-críticas (5)
- ✅ HTML minificado: 55 linhas (vs 439 no v2.0)
- ✅ Build time: ~430ms

### 🎨 Visual

- ✅ Fidelidade 100% ao design v2.0 (WordPress/Elementor)
- ✅ Responsivo: mobile (375px), tablet (768px), desktop (1024px+)
- ✅ Cores customizadas (creme, verde, dourado)
- ✅ Fontes: Factul (custom) + Inter + Nunito (Google Fonts)

### 🔧 Stack Técnico

- **Framework:** Astro 5.17.3
- **CSS:** Tailwind CSS 4
- **Carousel:** Swiper 11 (CDN)
- **Animation:** Lottie Web 5.12.2
- **Deploy:** Cloudflare Pages
- **Build:** Vite 6

### 📦 Componentes

```
src/components/
├── Hero.astro          ← Logo + VSL + CTA + Lottie
├── Problemas.astro     ← Dores + card blur
├── Metodo.astro        ← Grid 3×2 cards
├── Comparacao.astro    ← Antes/depois
├── Fases.astro         ← 4 fases (grid 2×2)
├── SobreFlavia.astro   ← Bio 2 colunas
├── ComoFunciona.astro  ← Accordion 4 semanas
├── Bonus.astro         ← 3 bônus
├── Depoimentos.astro   ← Swiper 13 items
├── Pricing.astro       ← Oferta + garantia
├── FAQ.astro           ← 9 perguntas
└── Footer.astro        ← Rodapé
```

### 🐛 Bug Fixes

- Swiper implementado (não existia na base inicial)
- Fetchpriority adicionado ao poster do vídeo
- Loading lazy otimizado (hero sem lazy)
- FAQ com transição suave

### 📊 Métricas

| Métrica | v2.0 (WordPress) | v1.0 (Astro) |
|---------|------------------|--------------|
| HTML size | 439 linhas | 55 linhas |
| Build time | Manual | 430ms |
| Fetchpriority | 2 | 2 |
| PageSpeed mobile | 75 | ≥ 75 |
| Components | 1 (monolítico) | 12 (modulares) |

### 🚀 Deploy

- **URL:** <https://cbse-site-tw.pages.dev>
- **Deploy ID:** df9283fd
- **Provider:** Cloudflare Pages
- **Branch:** main

### 📝 Documentação

- [x] PLANO-MIGRACAO.md
- [x] VALIDACAO-FASE1.md
- [x] CORRECOES-FASE2.md
- [x] FASE2-IMPLEMENTADO.md
- [x] RESUMO-FASE2.md
- [x] FASE3-TESTES.md
- [x] CHECKLIST-VALIDACAO.md
- [x] RESUMO-EXECUTIVO.md
- [x] CHANGELOG.md
- [x] VERSION.md

### 🙏 Créditos

- **Desenvolvedor:** OpenClaw Mini (AI)
- **Cliente:** Henrique Weber
- **Design original:** Flávia Andrade (WordPress/Elementor)
- **Produto:** Comer Bem Sem Estresse (CBSE)

---

## [Unreleased]

Nenhuma mudança pendente no momento.

---

**Formato:** Baseado em [Keep a Changelog](https://keepachangelog.com/)  
**Versionamento:** [Semantic Versioning](https://semver.org/)
