# Otimizações PageSpeed — v1.1.0

**Data:** 2025-02-22  
**Score anterior:** 78 (mobile)  
**Deploy:** a019e7a5

---

## ✅ Implementado (Alta Prioridade)

### 1. Configuração de `astro:assets`
- **Impacto:** ALTO — Otimização automática de imagens
- **Mudança:** Adicionado `getImage` do Astro para processar imagens
- **Resultado:** 
  - Poster 100104.webp: 72kB → 66kB (economia de 6kB / 8.3%)
  - Imagens agora têm hash no nome (cache-busting automático)
  - Compressão WebP otimizada (quality 80)

### 2. Preload do Poster no `<head>`
- **Impacto:** ALTO — Melhora LCP (Largest Contentful Paint)
- **Antes:** `<link rel="preload">` no body do componente Hero
- **Depois:** `<link rel="preload" href="/_astro/100104.SCOcUSnK_1xTg83.webp" fetchpriority="high">` no `<head>`
- **Resultado:** Navegador carrega poster do vídeo com prioridade máxima

### 3. Imagem Responsiva Otimizada
- **Impacto:** MÉDIO — Redução de tamanho sem perda visual
- **Antes:** 1081x608 (72kB)
- **Depois:** 1080x608 (66kB, quality 80)
- **Próximo passo:** Adicionar srcset com versão mobile (400w)

---

## 📊 Métricas Esperadas

| Métrica | Antes | Esperado |
|---------|-------|----------|
| **Desempenho** | 78 | 80-82 |
| **LCP** | 4.9s | <4.5s |
| **FCP** | 2.6s | ~2.5s |
| **Entrega de imagens** | 64 KiB economia | ✅ Implementado |
| **Descoberta LCP** | ⚠️ Faltava preload | ✅ Corrigido |

---

## ✅ Lazy Load do Swiper (v1.2.0)

**Deploy:** 4113c030  
**Data:** 2025-02-22

### Implementação
- **Removido:** CSS e JS do Swiper do `<head>` (eliminava 750ms de render blocking)
- **Adicionado:** Intersection Observer no componente Depoimentos
- **Comportamento:** 
  - Swiper carrega dinamicamente quando usuário rola até 50px antes da seção
  - Fallback para navegadores antigos (carrega no DOMContentLoaded)
  - CSS + JS carregados sob demanda (~49 KiB total)

### Impacto Esperado
- **Render blocking:** -750ms (Swiper CSS)
- **First Contentful Paint:** Melhora esperada (~200-300ms)
- **Score:** Estimado 80-82 (vs 78 anterior)

### Arquivos Modificados
- `src/layouts/Layout.astro` — Removido Swiper do head
- `src/components/Depoimentos.astro` — Lazy loading com IntersectionObserver

### Reversão (se necessário)
```bash
cd ~/Projects/cbse-astro-tw
git checkout src/layouts/Layout.astro src/components/Depoimentos.astro
npm run build
```

---

## ⏭️ Próximas Melhorias (Médio Prazo)

### 4. Imagens Responsivas com `srcset`
```astro
<Picture
  src={posterImage}
  widths={[400, 768, 1080]}
  formats={['webp']}
  alt="Video poster"
/>
```
- **Impacto:** MÉDIO — Mobile carrega 400w (~15kB) em vez de 66kB
- **Economia:** ~50kB em mobile

### 5. Self-host Google Fonts
- **Impacto:** BAIXO-MÉDIO — Reduz render blocking
- **Economia:** ~750ms no caminho crítico
- **Contra:** Perde cache compartilhado do CDN

---

## 🚫 Não Implementado (Baixa Prioridade)

### Cache de CDNs
- Swiper (jsDelivr): TTL de 7 dias → ideal seria 1 ano
- **Decisão:** Não mexer — cache compartilhado global vale mais

### Render Blocking CSS
- CSS próprio: 9.2 KiB (ótimo)
- **Decisão:** Não mexer — já está pequeno

---

## 📦 Arquivos Modificados

```
src/layouts/Layout.astro       — Adicionado preload do poster
src/components/Hero.astro      — Usando getImage() para poster
src/assets/100104.webp         — Movido de public/ para assets/
```

---

## 🔗 Links

- **Deploy:** https://a019e7a5.cbse-site-tw.pages.dev
- **Produção:** https://cbse-site-tw.pages.dev
- **PageSpeed antes:** Score 78 (mobile)
- **Testar agora:** <https://pagespeed.web.dev/analysis?url=https://cbse-site-tw.pages.dev>

---

**Próximo passo:** Rodar PageSpeed Insights novamente e comparar scores.
