# dimonoff.com — Statut

## Stack Technique

| Element | Detail |
|---------|--------|
| CMS | WordPress + Elementor Pro |
| Theme | The7 |
| Multilingual | Polylang (EN/FR/ES) |
| Hosting | HostGator + Cloudflare CDN |
| SEO | Yoast SEO + SmartCrawl Pro |
| Cache | Hummingbird + Autoptimize |
| Security | ModSecurity WAF (HostGator) |
| File Manager | File Manager Advanced (elFinder) |
| Forms | WPForms |
| GDPR | Complianz |
| Backup | Snapshot Pro |
| Mega Menu | Max Mega Menu Pro |

## Pages cles (IDs)

| Page | EN | FR | ES |
|------|----|----|-----|
| Homepage | 48318 | — | — |
| Solutions | 24 | 4950 | 74278 |
| About | 3958 | 60677 | 74215 |
| Smart Lighting Control | 79360 | 79365 | 79372 |
| Glossary | 399000 | 399002 | 399004 |
| Services | 80440 (vide) | 80469 | — |

## Projets completes

### SEO/CWV Execution Plan (7 phases)
- **Date**: 2026-03-30
- **Base**: Audit GSC Performance 2026-03-29
- **Phases completees**:
  - Phase 1: CWV Desktop fix (CLS + LCP) — 3 mu-plugins deployes
  - Phase 2: Title tags + meta descriptions — 2 mu-plugins (bypass SmartCrawl via pre_get_document_title)
  - Phase 3: 301 redirects pour 404 — mu-plugin pattern-based
  - Phase 4: Canonical duplicates — identifie comme issue Artifactory (IT, hors scope WP)
  - Phase 5: Hero image LCP fix (a3 Lazy Load images desactive, WP Core Lazy Load active) + a11y mu-plugin
  - Phase 6: Cross-Vectanor backlinks — verifies bidirectionnels (dimonoff, spatium, amotus, vectanor)
  - Phase 7: Validation finale
- **Changement a3 Lazy Load**: Images lazy-load desactive, WP Core Lazy Load active (WordPress natif gere above/below fold correctement)
- **Details**: voir `docs/Plan-Execution-SEO-CWV-2026-03.md` et `audits/Audit-GSC-Performance-2026-03-29.md`

### SEO Plan (score final: 100/100)
- **Dates**: Mars 2025 — Mars 2026
- **Score initial**: 55/100
- **Score final**: 100/100 (PageSpeed SEO)
- **Phases**: 5 phases (Technical SEO, On-page, Schema, Content, Validation)
- **Details**: voir `docs/Plan-Ameliorations-Dimonoff.md`

### AEO/GEO Audit — Smart Lighting Control (242/300)
- **Date**: 2026-03-26
- **Score initial**: 184/300
- **Score final**: 242/300 (SEO 69, AEO 86, GEO 87)
- **Deploye**: 4 mu-plugins + llms.txt + doc IT
- **Remaining**: TTFB (4200ms target <800ms), alt text, H2 duplicates — IT items
- **Details**: voir `audits/Audit-AEO-GEO-Smart-Lighting.md`

### Migration Amotus (EN/FR complete)
- **Date**: 2026-03-26
- **Objectif**: Retirer le contenu detaille Amotus de dimonoff.com, garder liens courts
- **Statut**: EN/FR 5 phases COMPLETE + Services EN vide + footer cards removed
- **ES**: En attente de amotus.com/es/
- **Details**: voir `docs/Plan-Migration-Amotus.md`

### Sourcewell Badge
- **Date**: 2026-03-26
- **Contrat**: #041525-DIMN (valide jusqu'au 2029-07-22)
- **Pages**: Smart Lighting Control EN/FR/ES + schema JSON-LD

## mu-plugins deployes (21 actifs)

| Fichier | Taille | Role |
|---------|--------|------|
| dimonoff-faq-schema.php | 10,268 B | FAQ schema sur /solutions/ |
| dimonoff-product-schema.php | 5,104 B | Product schema par sous-page produit |
| dimonoff-glossary-schema.php | 12,361 B | DefinedTermSet sur /glossary/ |
| dimonoff-crosslinks.php | 4,042 B | Liens Vectanor/Spatium/Amotus en footer |
| dimonoff-local-business-schema.php | 3,452 B | LocalBusiness + Corporation |
| dimonoff-font-preload.php | 1,340 B | Preload fonts critiques |
| dimonoff-counter-fix.php | 878 B | Fix compteurs Elementor (Hummingbird conflict) |
| dimonoff-about-glossary-link.php | 1,204 B | Cross-link About vers Glossary |
| dimonoff-vectanor-banner.php | 1,577 B | CSS Groupe Vectanor footer bar |
| dimonoff-sourcewell-schema.php | 3,772 B | Schema Sourcewell cooperative purchasing |
| dimonoff-seo-schemas.php | 15,719 B | FAQ + Product + HowTo schemas EN/FR/ES |
| dimonoff-entity-first.php | 2,317 B | Entity-first paragraph EN/FR/ES |
| dimonoff-compare-table.php | 4,541 B | 6-product comparison table EN/FR/ES |
| dimonoff-qa-headings.php | 3,934 B | Q&A headings + "Last updated" EN/FR/ES |
| dimonoff-aeo-fixes.php | 12,751 B | published_time + alt text + H2 dedup |
| dimonoff-cls-stabilize.php | 750 B | CLS containment CSS pour Elementor sections (desktop) |
| dimonoff-lcp-fix.php | 697 B | Preload hero image + Google Fonts display=optional |
| dimonoff-seo-titles.php | 1,399 B | Override title tags (pre_get_document_title, bypass SmartCrawl) |
| dimonoff-seo-descs.php | 1,131 B | Meta descriptions custom (chr(60/62) WAF bypass) |
| dimonoff-301-redirects.php | 1,381 B | Pattern-based 301 redirects pour anciennes URLs |
| dimonoff-a11y-fixes.php | 1,236 B | WCAG AA contrast + aria-labels pour inputs |

> Note: 5 mu-plugins sont dans le repo (faq-schema, product-schema, glossary-schema, crosslinks, font-preload). Les 16 autres sont sur le serveur dimonoff.com uniquement — a extraire via cPanel File Manager et ajouter dans un commit ulterieur.

## Contraintes techniques

- **elFinder stripslashes()**: Les fichiers PHP deployes via elFinder ne doivent contenir ZERO backslash
- **WAF HostGator**: Bloque `$_SERVER['REQUEST_URI']` dans les requetes PUT
- **Elementor cache**: `files_manager->clear_cache()` est le seul moyen fiable de purger le cache de rendu
- **Hummingbird**: Casse les compteurs Elementor (lazy handler chain)

## Produits references

| Designation | Description |
|-------------|-------------|
| SCMS | Smart City Management System (plateforme Dimonoff) |
| RME | Smart Wireless Lighting Node (controleur externe) |
| RTM | Smart Wireless Lighting Node (controleur interne) |
| LNLV | Smart Wireless Lighting Node (controleur basse tension) |
| DOO Express | Controleur d'eclairage |
| G3+ | Controleur d'eclairage |

> RME, RTM, LNLV sont des designations de lettres, PAS des acronymes.

## Changements a3 Lazy Load (2026-03-30)
- **Images lazy-load**: DESACTIVE (etait active, causait lazy_placeholder.gif sur hero = LCP degradé)
- **WordPress Core Lazy Load**: ACTIVE (WP natif gere loading="lazy" seulement sous le fold)
- **Videos/iframes lazy-load**: toujours actif via a3

## Recommandation IT (hors scope)
- **Artifactory**: 70+ URLs sous `artifactory.dimonoff.com` apparaissent comme 404/canonical duplicates dans GSC
- **Action requise**: Ajouter header `X-Robots-Tag: noindex` sur le serveur Artifactory
- **TTFB**: 4200ms (HostGator) — target <800ms, necessite migration hebergement

## Derniere mise a jour
2026-03-30
