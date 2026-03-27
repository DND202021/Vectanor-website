# spatium-iot.com — Statut

## Stack Technique

| Element | Detail |
|---------|--------|
| CMS | WordPress + Elementor |
| Theme | Hello Elementor |
| Multilingual | Polylang (EN/FR/ES) |
| SEO | Yoast SEO |
| Cache | Autoptimize |
| File Manager | File Manager Advanced (elFinder) |
| Forms | WPForms |

## Pages cles (IDs)

| Page | EN | FR | ES |
|------|----|----|-----|
| Homepage | 10 | 259 | 260 |
| Key Differentiators | 17 | — | — |
| Benefits | 19 | — | — |
| Indoor/Outdoor Parking | 20 | (pas encore) | (pas encore) |
| Curbside Parking | 21 | (pas encore) | (pas encore) |
| MPS Sensor | 23 (noindex, obsolete) | — | — |
| M1 Gateway | 24 | — | — |
| Get a Demo | 25 | — | — |

## Adresse officielle
410-1015 ave. Wilfrid-Pelletier, Quebec, QC, Canada G1W 0C4

## Projets completes

### AEO/GEO Audit (~216/300)
- **Date**: 2026-03-27
- **Score initial**: 151/300
- **Score final**: ~216/300 (SEO 65, AEO 78, GEO 73)
- **Deploye**: 1 mu-plugin consolide + llms.txt + noindex 3 pages + titres raccourcis
- **Remaining**: TTFB (1841ms target <800ms), citations externes — IT items
- **Details**: voir `audits/Audit-AEO-GEO-Spatium.md`

### Prototype Integration (Phases 1, 2, 4 complete)
- **Date**: 2026-03-27
- **Objectif**: Integrer les meilleures idees du prototype produit dans spatium-iot.com
- **Phase 1**: COMPLETE — CSS modernisation + homepage stats/temoignages/logos/CTA
- **Phase 2**: COMPLETE — Pages Indoor/Outdoor + Curbside avec contenu complet
- **Phase 3**: PARTIEL — Calculateur ROI sur homepage seulement
- **Phase 4**: COMPLETE — Trust badges, section About, FAQ avec schema
- **Details**: voir `docs/Plan-Prototype-Integration.md`

## mu-plugins deployes (3 actifs)

| Fichier | Taille | Role |
|---------|--------|------|
| spatium-seo-aeo-geo.php | 12,430 B | Schemas (Organization, Product, SoftwareApp), entity-first, Q&A, comparison table, published_time |
| spatium-design-upgrade.php | ~30,000 B | Phase 1: CSS moderne, homepage stats/temoignages/logos/ROI/CTA (EN/FR/ES) |
| spatium-pages-phase2-4.php | ~41,000 B | Phase 2: contenu Indoor/Outdoor + Curbside, Phase 4: trust badges, about, FAQ + schema |

## Contraintes techniques

- **mu-plugins folder hash** (elFinder): `l1_d3AtY29udGVudC9tdS1wbHVnaW5z`
- **elFinder instance**: `jQuery('.elfinder').elfinder('instance')`
- **Polylang detection**: `pll_current_language('slug')` avec URI fallback
- **Base64 chunking**: Fichiers >10KB doivent etre split en chunks ~9100 chars pour elFinder
- **Yoast llms.txt**: Peut etre regenere par cron — desactiver dans Yoast > Settings > Crawl

## A faire

- Creer traductions Polylang FR/ES pour pages 20 (Indoor/Outdoor) et 21 (Curbside)
- Optimisation TTFB (1841ms cible <800ms) — IT
- Liens de citations externes dans contenu Elementor — IT

## Derniere mise a jour
2026-03-27
