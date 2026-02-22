# Lazy Load do Swiper — Implementação

**Versão:** 1.2.0  
**Deploy:** 4113c030  
**URL:** https://4113c030.cbse-site-tw.pages.dev  
**Data:** 2025-02-22

---

## 🎯 Objetivo

Eliminar **750ms de render blocking** removendo Swiper CSS/JS do caminho crítico.

---

## ✅ O que foi feito

### 1. Removido do `<head>` (Layout.astro)
```diff
- <!-- Swiper CSS -->
- <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css" />
- 
- <!-- Swiper JS -->
- <script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js" defer></script>
```

### 2. Lazy loading no componente Depoimentos
- **Intersection Observer:** Detecta quando seção entra no viewport (50px antes)
- **Carregamento dinâmico:** CSS + JS adicionados sob demanda
- **Fallback:** Navegadores sem IntersectionObserver carregam no DOMContentLoaded
- **Idempotência:** Evita reinicialização dupla

---

## 📊 Impacto Esperado

| Métrica | Antes | Depois | Economia |
|---------|-------|--------|----------|
| **Render blocking CSS** | 5.7 KiB (750ms) | 0 | -750ms |
| **Desempenho (mobile)** | 78 | 80-82 | +2-4 pts |
| **FCP** | 2.6s | ~2.3-2.4s | -200-300ms |

---

## 🧪 Como Testar

### Verificar lazy loading no DevTools:
1. Abrir https://cbse-site-tw.pages.dev
2. DevTools → Network → Filtrar "swiper"
3. Rolar até seção Depoimentos
4. ✅ Swiper CSS/JS deve aparecer SÓ quando rolar até lá

### Verificar funcionamento:
1. Rolar até seção "Veja os resultados de mães e alunas"
2. ✅ Carrossel deve funcionar normalmente
3. ✅ Autoplay de 5s
4. ✅ Paginação clicável

---

## 🔄 Como Reverter (se der problema)

```bash
cd ~/Projects/cbse-astro-tw

# Reverter arquivos
git checkout src/layouts/Layout.astro src/components/Depoimentos.astro

# Rebuild
npm run build

# Deploy
CLOUDFLARE_API_TOKEN=$(security find-generic-password -a "openclaw" -s "cloudflare-api-token" -w) \
  npx wrangler pages deploy dist --project-name cbse-site-tw
```

---

## 📦 Arquivos Modificados

```
src/layouts/Layout.astro          — Removido Swiper do <head>
src/components/Depoimentos.astro  — Lazy loading com IntersectionObserver
```

---

## 🔗 Links

- **Deploy atual:** https://4113c030.cbse-site-tw.pages.dev
- **Produção:** https://cbse-site-tw.pages.dev
- **PageSpeed (testar):** <https://pagespeed.web.dev/analysis?url=https://cbse-site-tw.pages.dev>

---

## ✅ Checklist Pós-Deploy

- [ ] Rodar PageSpeed Insights (mobile)
- [ ] Verificar score ≥ 80
- [ ] Confirmar FCP < 2.5s
- [ ] Testar carrossel funcionando normalmente
- [ ] Verificar autoplay de 5s
- [ ] Confirmar paginação clicável
