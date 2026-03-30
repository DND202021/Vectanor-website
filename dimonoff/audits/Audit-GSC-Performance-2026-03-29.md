# Audit Google Search Console — dimonoff.com
**Date**: 2026-03-29
**Periode analysee**: 3 derniers mois (dec 2025 — mars 2026)
**Source**: Google Search Console (CrUX data)

---

## 1. Metriques Globales

| Metrique | Valeur | Evaluation |
|----------|--------|------------|
| Total clicks (3 mois) | 1,830 | Faible pour un leader de marche |
| Total impressions | 241,000 | Bon potentiel, mal exploite |
| CTR moyen | 0.8% | CRITIQUE (industrie 2-5%) |
| Position moyenne | 10.1 | Page 2 en moyenne |
| Pages indexees | 815 | |
| Pages non indexees | 1,920 | 70% non indexe |
| Total queries | 1,000 | Principalement branded |

---

## 2. Page Indexing

### Repartition
- **Indexed**: 815 pages
- **Not indexed**: 1,920 pages (12 raisons)

### Raisons de non-indexation

| Raison | Pages | Severite | Action |
|--------|-------|----------|--------|
| Page with redirect | 713 | HIGH | Nettoyer chaines de redirects, supprimer de sitemap |
| Alternate page with proper canonical tag | 257 | NORMAL | Polylang FR/ES — comportement attendu |
| Excluded by 'noindex' tag | 244 | MEDIUM | Verifier si intentionnel, certaines pourraient etre utiles |
| Duplicate without user-selected canonical | 81 | CRITICAL | Ajouter canonical tags explicites |
| Not found (404) | 77 | CRITICAL | Identifier et rediriger ou supprimer |
| Soft 404 | 22 | HIGH | Pages vides/thin — ajouter contenu ou noindex |
| Blocked by robots.txt | 19 | MEDIUM | Verifier si intentionnel |
| Blocked due to access forbidden (403) | 9 | MEDIUM | Verifier permissions serveur |
| Server error (5xx) | 2 | HIGH | Corriger erreurs serveur |
| Blocked due to other 4xx issue | 1 | LOW | Verifier |

---

## 3. Core Web Vitals

### Mobile
| Statut | URLs |
|--------|------|
| Poor | 0 |
| Need improvement | 206 |
| Good | 31 |

### Desktop
| Statut | URLs |
|--------|------|
| **Poor** | **237** |
| Need improvement | 0 |
| Good | 0 |

### Issues Desktop (2 issues)

| Issue | Severite | URLs | Cause probable |
|-------|----------|------|----------------|
| CLS issue: more than 0.25 (desktop) | Poor | 237 | Elementor rendering pipeline (meme probleme que Spatium) |
| LCP issue: longer than 4s (desktop) | Poor | 237 | Images lourdes, CSS render-blocking, TTFB serveur (4200ms) |

**Note**: Le TTFB de 4200ms (identifie dans l'audit AEO/GEO precedent) est un facteur majeur du LCP > 4s. C'est un probleme d'hebergement HostGator.

---

## 4. Top Queries (3 mois)

| Query | Clicks | Impressions | CTR | Type |
|-------|--------|-------------|-----|------|
| dimonoff | 656 | 1,213 | 54% | Branded |
| dimonoff inc | 26 | 49 | 53% | Branded |
| diminoff (faute) | 20 | 35 | 57% | Branded |
| dimonoff quebec | 10 | 54 | 19% | Branded |
| bernard tetu | 8 | 48 | 17% | Person |
| dimonof (faute) | 8 | 20 | 40% | Branded |
| dimonoff lighting control | 7 | 19 | 37% | Branded |
| spatium | 5 | 532 | 0.9% | Branded (autre produit) |
| daniel noiseux | 5 | 100 | 5% | Person |
| sensores para estacionamiento inteligente | 5 | 53 | 9% | Non-branded ES |

**Constat critique**: 95%+ du trafic est branded. Quasi zero trafic non-branded pour "smart street lighting", "IoT lighting platform", etc.

---

## 5. Top Pages (3 mois)

| Page | Clicks | Impressions | CTR |
|------|--------|-------------|-----|
| / (homepage) | 469 | 10,267 | 4.6% |
| /fr/ | 310 | 1,192 | 26% |
| /fr/carrieres/ | 63 | 967 | 6.5% |
| /careers/ | 62 | 1,683 | 3.7% |
| /fr/nouvelles/panneaux-signalisation-dynamiques...laval/ | 41 | 5,094 | 0.8% |
| **/solutions/smart-lighting-control/** | **37** | **35,911** | **0.1%** |
| /solutions/.../rme-external-controller/ | 34 | 5,968 | 0.6% |
| /es/ | 29 | 128 | 23% |
| /solutions/.../wireless-nodes/ | 27 | 3,046 | 0.9% |
| /about-us/ | 25 | 2,813 | 0.9% |

**Observation critique**: /solutions/smart-lighting-control/ a 35,911 impressions mais seulement 37 clicks (CTR 0.1%). Le title tag et la meta description ne convainquent pas les utilisateurs de cliquer.

---

## 6. Sitemap Analysis

- 3 sitemaps (posts, pages, categories) via Yoast SEO
- **497 posts** dans post-sitemap.xml (mars 2022 — aout 2025)
- **Dernier post**: aout 2025 (7 mois sans nouveau contenu)
- Contenu en 3 langues: EN (/news/), FR (/nouvelles/), ES (/noticias/)

---

## 7. Comparaison avec Spatium-iot.com

| Metrique | dimonoff.com | spatium-iot.com |
|----------|-------------|-----------------|
| CWV Desktop | 237 poor, 0 good | Meme probleme CLS Elementor |
| Indexed pages | 815 | ~21 |
| CTR | 0.8% | N/A (trop petit) |
| Impressions | 241K | ~5K |
| Theme | The7 | Hello Elementor |
| CLS fix applicable | Oui (meme approche) | Deja applique |
| TTFB | 4200ms | ~1800ms |

---

## Recommandations Prioritaires

1. **URGENCE**: Fixer CWV Desktop (CLS + LCP) — impact direct sur ranking de 237 URLs
2. **URGENCE**: Recrire title tag de /solutions/smart-lighting-control/ (35K impressions gaspillees)
3. **HIGH**: Nettoyer les 77 erreurs 404 et les 81 canonical duplicates
4. **HIGH**: Ecrire meta descriptions uniques pour les 10 top pages
5. **MEDIUM**: Investiguer les 713 redirects et 244 noindex pages
6. **MEDIUM**: Relancer la publication de contenu (blog mort depuis 7 mois)
