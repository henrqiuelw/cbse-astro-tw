# Referência CSS v2.0 — Seção PROBLEMAS (9881de1)

Extraído de: ~/Documents/cbse/mirror-clean/css/elementor-inline.css

## Elementos

| Elementor ID | Função | Equivalente Astro |
|---|---|---|
| 9881de1 | Section container | .problemas-section-2 |
| 5acd04f | Card (inner container) | .problemas-card |
| 5a31cf3 | Heading widget | .problemas-card-heading |
| 3cc8c10 | Text widget 1 (p1) | .problemas-card-p1 |
| 1aa2be7 | Text widget 2 (p2) | .problemas-card-p2 |
| d7394c9 | Mobile image | .problemas-img-mobile |
| 4297d9a | Desktop image | .problemas-img-desktop |

## Desktop (min-width: 768px)

### Section (9881de1)
- --content-width: 1140px
- --width: 44% (for 5acd04f)

### Card (5acd04f)
- --width: 44%
- backdrop-filter: blur(20px)

## Laptop (max-width: 1366px)

### Section (9881de1)
- --gap: 0px
- --padding: 0px 0px 0px 0px → override to 40px lateral
- Actually: --padding-top:0px; --padding-bottom:0px; --padding-left:40px; --padding-right:40px

### Desktop Image (4297d9a)
- margin: 0 -62% -1% -15%

## Tablet (max-width: 1024px)

### Section (9881de1)
- --min-height: 0px
- --flex-direction: **column-reverse**
- --container-widget-width: 100%
- --margin: 0px all
- --padding: 10% 5% 10% 5%

### Card (5acd04f)
- --width: 100% (tablet-specific via 768-1024 media)
- border-width: 0
- --padding: 0px all

### Mobile Image (d7394c9)
- width: 100%
- margin: -50% -13% -26% -13%

## Mobile (max-width: 767px)

### Section (9881de1)
- --flex-direction: **column-reverse**
- --align-items: center
- --gap: 20px
- border-width: 1px 0 0 0 (border-top only!)
- **--margin-top: -51px**
- --margin-bottom/left/right: 0
- **--padding-top: 10%**
- **--padding-bottom: 17%**
- --padding-left: 5%
- --padding-right: 5%

### Card (5acd04f)
- border-width: 0
- --padding: 0px all

### Heading (5a31cf3)
- width: 100%; max-width: 100%
- text-align: center
- font-size: **4.4vw**
- line-height: **1.3em**
- **margin: 0 -20px 0 -20px** (via .elementor-widget-container)

### P1 — "Isso gera desgaste..." (3cc8c10)
- width: 100%; max-width: 100%
- text-align: center
- **font-size: 20px**
- **line-height: 1.4em**
- font-weight: 600 (from base CSS)
- margin: 0

### P2 — "Famílias que alcançam..." (1aa2be7)
- width: 100%; max-width: 100%
- text-align: center
- **font-size: 16px** ← NÃO 20px!
- **line-height: 1.4em**
- **font-weight: 400** ← NÃO 600!
- margin: 0

### Mobile Image (d7394c9) — mobile viewport
- margin: **-26% -7% -14% -6%**

### Desktop Image (4297d9a) — mobile viewport (hidden but has rules)
- margin: -26% -7% -14% -6%
- width: 100%
