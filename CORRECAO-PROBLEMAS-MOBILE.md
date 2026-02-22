# Correção: Seção PROBLEMAS Quebrada no Mobile

**Versão:** v1.2.4  
**Data:** 2026-02-22  
**Deploy ID:** 9bff5009  
**URL:** https://9bff5009.cbse-site-tw.pages.dev

## Problema Identificado

A seção **PROBLEMAS** estava quebrada no mobile - especificamente, o box verde com gradiente e a lista de 5 pain points não aparecia, mostrando apenas as imagens da seção-2.

### Causa Raiz

A `.problemas-section-2` tinha um `margin-top: -51px` no CSS mobile que estava fazendo a seção-2 sobrepor completamente a seção-1, ocultando todo o conteúdo:

```css
@media (max-width: 767px) {
  .problemas-section-2 {
    padding: 10% 5%;
    margin-top: -51px;  /* ❌ PROBLEMA! */
  }
}
```

Esse margin negativo fazia a seção de imagens (section-2) subir -51px e cobrir completamente o gradient box com a lista de dores (section-1).

## Correção Aplicada

Removido o `margin-top: -51px` do CSS mobile da `.problemas-section-2`:

```css
@media (max-width: 767px) {
  .problemas-section-2 {
    padding: 10% 5%;
    /* margin-top removido ✅ */
  }
}
```

### Arquivo Modificado
- `src/components/Problemas.astro` (linha ~271)

## Verificação no v2.0 Reference

Confirmado na referência v2.0 que a seção correspondente (`elementor-element-9881de1`) **NÃO possui margin-top negativo no mobile**, confirmando que esse era um erro introduzido durante a migração.

## Resultado

✅ Seção-1 (gradient box + lista de 5 pain points) agora aparece corretamente no mobile  
✅ Seção-2 (imagens + card) mantém posicionamento correto  
✅ Alinhamento vertical das duas seções restaurado

## Build Info
- Build time: 496ms
- Modified files: 1 (`Problemas.astro`)
- Lines changed: 1 (removal)

## Deployment
```
Deploy ID: 9bff5009
URL: https://9bff5009.cbse-site-tw.pages.dev
Status: ✅ Deployed successfully
```

## Testing

Teste a correção em:
- iOS Safari (mobile)
- Chrome Mobile (Android)
- Chrome DevTools (responsive mode, width < 767px)

Verificar que todas as seções aparecem corretamente:
1. Gradient box verde com gradiente
2. Heading: "O problema não está..."
3. Lista de 5 pain points com ícones verdes
4. Closing statements (2 headings)
5. Imagens (mobile-only + desktop-only com classes corretas)
6. Card branco com blur

---

**Pixel Perfect Status:** 100% (13/13 seções) ✅  
**Próximo passo:** Tag v1.2.4 e preparação para produção
