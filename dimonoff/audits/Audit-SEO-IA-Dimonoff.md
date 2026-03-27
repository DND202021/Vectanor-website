# Audit SEO et Preparation IA — dimonoff.com

**Date :** 2026-03-24
**Site audite :** https://www.dimonoff.com
**CMS :** WordPress 6.9.4 + Elementor Pro + The7 theme
**Plugins SEO :** Yoast SEO Premium, SmartCrawl Pro
**Multilingue :** Polylang (EN / FR / ES)

---

## Resume executif

Le site dimonoff.com presente une base SEO correcte grace a Yoast SEO (schema Article, Open Graph, hreflang) mais souffre de lacunes significatives en SEO technique, en optimisation on-page et surtout en preparation pour les agents IA. Les recommandations ci-dessous sont classees par priorite et impact estimé.

**Score global estime : 55/100**

| Categorie | Note | Commentaire |
|-----------|------|-------------|
| SEO Technique | 5/10 | robots.txt minimal, sitemap polluee, pas de sitemap dans robots.txt |
| Performance | 6/10 | DOM raisonnable (1771 noeuds), mais 40 JS + 10 CSS render-blocking |
| Contenu & On-page | 5/10 | Pas de H1 sur homepage, titres generiques, meta desc FR en anglais |
| Schema / Structured Data | 6/10 | Article schema present mais Organisation incomplete, pas de LocalBusiness |
| Preparation IA | 2/10 | Pas de llms.txt, pas de directives AI bots, contenu non structure pour LLM |
| Accessibilite | 4/10 | viewport bloque le zoom, 115 images sans alt sur une seule page |

---

## 1. SEO Technique

### 1.1 robots.txt — CRITIQUE

**Etat actuel :**
```
User-agent: *
Disallow: /wp-admin/
Allow: /wp-admin/admin-ajax.php
```

**Problemes :**
- Aucune reference au sitemap dans le robots.txt
- Aucune directive pour les bots IA (GPTBot, ClaudeBot, etc.)
- Trop minimaliste — pas de blocage des parametres de recherche, feeds inutiles, etc.

**Recommandation :**
```
User-agent: *
Disallow: /wp-admin/
Allow: /wp-admin/admin-ajax.php
Disallow: /*?s=
Disallow: /*?p=
Disallow: /wp-json/
Allow: /wp-json/wp/v2/
Disallow: /tag/
Disallow: /author/
Disallow: /feed/

# AI Crawlers — autorises pour la visibilite dans les reponses LLM
User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

Sitemap: https://www.dimonoff.com/sitemap_index.xml
```

### 1.2 Sitemap XML — IMPORTANT

**Etat actuel :** 8 sitemaps via Yoast, ~340+ URLs dans post-sitemap, 141 dans page-sitemap.

**Problemes :**
- Le sitemap n'est PAS reference dans robots.txt (les moteurs le trouvent via Search Console, mais c'est une mauvaise pratique)
- Le `dt_portfolio-sitemap.xml` et `dt_portfolio_category-sitemap.xml` contiennent probablement des URLs de contenus depublies (derniere modification dec 2024 = avant la migration parking)
- `post_tag-sitemap.xml` et `author-sitemap.xml` indexent des pages a faible valeur SEO
- Pas de verification si les URLs depubliees (articles parking) ont ete retirees du sitemap

**Recommandations :**
1. Ajouter `Sitemap: https://www.dimonoff.com/sitemap_index.xml` dans robots.txt
2. Verifier et nettoyer le sitemap portfolio (dt_portfolio) pour retirer les URLs 404
3. Desactiver l'indexation des archives auteur et des tags dans Yoast > Reglages > Taxonomies
4. Soumettre le sitemap mis a jour dans Google Search Console et Bing Webmaster Tools

### 1.3 Canonical et Hreflang — CORRECT avec reserves

**Etat actuel :**
- Canonical present sur toutes les pages testees
- Hreflang EN/FR/ES present sur les pages principales (homepage, solutions)
- `og:locale:alternate` present pour ES (`es_MX`)

**Problemes potentiels :**
- Verifier que le hreflang FR pointe vers `/fr/` et non vers la version EN (erreur frequente avec Polylang)
- `og:locale:alternate` ne liste que `es_MX`, pas `fr_FR` — possible oubli dans la config Yoast
- Le contenu parking migre vers spatium-iot.com n'a probablement plus de hreflang coherent

**Recommandation :** Audit croise des hreflang sur un echantillon de 10 pages EN/FR/ES pour verifier la coherence bidirectionnelle.

### 1.4 HTTPS et securite — BON

- HTTPS actif sur tout le site
- Pas de mixed content detecte
- Cloudflare en frontal (protection DDoS, CDN)

---

## 2. Performance

### 2.1 Metriques mesurees (depuis le navigateur)

| Metrique | Valeur | Seuil Google | Verdict |
|----------|--------|-------------|---------|
| TTFB | 20ms | < 800ms | Excellent |
| DOM Content Loaded | 161ms | < 1500ms | Excellent |
| Load Complete | 522ms | < 2500ms | Excellent |
| DOM Interactive | 127ms | < 3000ms | Excellent |
| CLS | 0.0000 | < 0.1 | Excellent |
| DOM Nodes | 1771 | < 1500 | Leger exces |
| Total Transfer | 0.56 MB | < 3 MB | Bon |

**Note :** Ces metriques sont mesurees depuis un navigateur local avec cache. Les vrais Core Web Vitals sur mobile seront differents. Un test PageSpeed Insights est fortement recommande.

### 2.2 Ressources — AMELIORABLE

| Type | Nombre | Recommande |
|------|--------|------------|
| Fichiers CSS | 10 | < 5 |
| Fichiers JS externes | 35 | < 15 |
| Scripts inline | 26 | Minimiser |
| Images | 29 | OK |
| Preconnect hints | 3 | OK |
| Polices preloadees | 0 | Ajouter |

**Problemes :**
- **35 fichiers JavaScript externes** : excessif, impacte le Time to Interactive sur mobile
- **9 CSS render-blocking** : bloquent le rendu initial
- **0 images en format moderne** : toutes en JPG/PNG, aucune en WebP ou AVIF
- **0 polices preloadees** : les Google Fonts (Nunito, Poppins, Roboto) sont chargees sans preload
- **141 elements avec style inline** : Elementor genere beaucoup de CSS inline

**Recommandations :**
1. **HAUTE** : Convertir les images en WebP (gain 25-35% sur le poids des images)
2. **HAUTE** : Activer le preload des polices critiques : `<link rel="preload" href="font.woff2" as="font" crossorigin>`
3. **MOYENNE** : Concatener/minifier les CSS et JS avec un plugin de cache (WP Rocket, Autoptimize, ou LiteSpeed Cache)
4. **MOYENNE** : Differer le chargement des JS non critiques avec `defer` ou `async`
5. **BASSE** : Reduire les styles inline en utilisant les classes CSS du theme

---

## 3. Contenu et SEO On-Page

### 3.1 Page d'accueil (Homepage) — PROBLEMATIQUE

| Element | Etat | Probleme |
|---------|------|----------|
| Title | `Home \| Dimonoff` | Generique, manque de mots-cles (smart city, IoT, etc.) |
| Meta description | "Leader supplier for smart city products..." | Correcte mais pourrait etre plus percutante |
| H1 | **ABSENT** | Critique : pas de H1 sur la homepage |
| H2 (premier) | "Smart Control Solutions to ManageStreetlights & City Assets" | Bon contenu mais devrait etre H1 |
| og:title | "Home" | Generique, devrait inclure le nom de marque et les mots-cles |
| og:description | Tronquee, commence par du contenu HTML brut | Bug Yoast/Elementor |

**Recommandations :**
1. **CRITIQUE** : Ajouter un H1 avec les mots-cles principaux, ex: "Smart City & IoT Solutions — Connected Asset Management"
2. **HAUTE** : Changer le title en : `Dimonoff | Smart City IoT Solutions — Connected Lighting & Asset Management`
3. **HAUTE** : Corriger le og:title pour correspondre au title
4. **MOYENNE** : Revoir la meta description pour inclure un appel a l'action

### 3.2 Pages interieures — AMELIORABLE

**Page Solutions :**
- Title : `Solutions | Dimonoff` — trop generique
- H1 : "Solutions" — manque de contexte et mots-cles
- Meta desc : Correcte mais pas optimisee pour le CTR
- Contenu : seulement 327 mots (trop mince pour un bon classement)
- Recommandation : enrichir a 800+ mots avec du contenu descriptif

**Page Contact :**
- Title : `Contact Us | Dimonoff` — OK
- Meta desc : Correcte
- Pas de schema LocalBusiness (adresse, horaires, telephone)
- Pas de Google Maps embed
- Pas de numero de telephone affiche

**Articles de blog :**
- Title : Bien structure (titre article + Dimonoff)
- Schema Article : present et assez complet
- Meta desc FR en contenu FR meme sur page EN (bug Polylang/Yoast detecte sur l'article Naomih Dalpe)
- Keywords et description manquants dans le schema Article

### 3.3 Images — CRITIQUE

| Metrique | Valeur |
|----------|--------|
| Format images | 100% JPG/PNG (0% WebP/AVIF) |
| Alt tags manquants | ~70% des images (115/163 sur un echantillon de page) |
| Lazy loading | Non verifie en detail |
| Tailles responsives | srcset present (via WordPress) |

**Recommandations :**
1. **CRITIQUE** : Ajouter des alt tags descriptifs a TOUTES les images (impact SEO image + accessibilite)
2. **HAUTE** : Convertir en WebP avec un plugin comme ShortPixel, Imagify ou EWWW
3. **MOYENNE** : Verifier que le lazy loading est actif sur les images below-the-fold

### 3.4 Viewport et accessibilite — CRITIQUE

```html
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=0">
```

`user-scalable=0` et `maximum-scale=1` **bloquent le zoom sur mobile**. C'est une violation WCAG 2.1 niveau AA et Google penalise ce comportement dans les audits d'accessibilite.

**Recommandation CRITIQUE :** Changer en :
```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

---

## 4. Preparation pour les agents IA (GEO - Generative Engine Optimization)

C'est la section la plus faible du site. En 2026, une part croissante du trafic web vient des reponses generees par les agents IA (ChatGPT, Perplexity, Claude, Google AI Overviews). Il est essentiel d'optimiser le site pour etre cite par ces agents.

### 4.1 llms.txt — ABSENT

Le fichier `llms.txt` est un standard emergent (propose par Jeremy Howard) permettant aux LLMs de comprendre rapidement le contenu et la structure d'un site. Dimonoff n'a ni `llms.txt`, ni `llms-full.txt`, ni `ai.txt`.

**Recommandation HAUTE — Creer `/llms.txt` :**
```
# Dimonoff

> Dimonoff is a smart city technology company specializing in IoT-based
> remote control and management of connected infrastructure assets,
> including streetlights, environmental sensors, and urban equipment.

## Company Overview

Dimonoff designs, manufactures, and deploys Smart City Management
Systems (SCMS) that enable municipalities and utilities to monitor and
control their connected assets remotely. The company is part of Groupe
Vectanor, alongside Spatium (smart parking), Amotus (IoT engineering),
and Vigilia (critical infrastructure monitoring).

## Products & Platforms

- **SCMS Platform**: Cloud-based smart city management system for
  lighting, environment, and asset control
- **DOO Express**: Simplified platform for smaller deployments
- **RME / RTM / LNLV**: Smart wireless lighting control nodes
- **Gateway G3+**: Communication gateway for IoT device networks
- **Mobile Application**: Field technician tools for maintenance

## Key Use Cases

- Municipal street lighting remote control and dimming
- Energy savings through intelligent lighting schedules
- Environmental monitoring (air quality, noise, weather)
- Connected infrastructure lifecycle management
- Smart city data analytics and dashboards

## Industries Served

Municipalities, utilities, transportation agencies, commercial
property managers, university campuses

## Location

Quebec City, QC, Canada

## Links

- Website: https://www.dimonoff.com
- Solutions: https://www.dimonoff.com/solutions/
- Products: https://www.dimonoff.com/solutions/ (SCMS, DOO Express, hardware)
- News: https://www.dimonoff.com/news/
- Contact: https://www.dimonoff.com/contact/
- Sister companies: https://spatium-iot.com (parking), https://amotus.com (IoT engineering)
- Parent group: https://vectanor.com
```

### 4.2 Directives robots.txt pour les bots IA — ABSENT

Aucune directive dans robots.txt pour GPTBot, ClaudeBot, PerplexityBot, Google-Extended.

**Impact :** Sans directives explicites, les crawlers IA appliquent leurs regles par defaut. En l'absence de blocage explicite, la plupart crawleront le site, mais il est recommande d'etre explicite pour deux raisons :
1. Confirmer que vous AUTORISEZ le crawl IA (certaines entreprises bloquent par defaut)
2. Controler QUELLES sections sont accessibles (ex: bloquer /wp-admin mais autoriser le contenu)

**Recommandation :** Voir la section 1.1 pour le robots.txt recommande.

### 4.3 Schema markup pour les agents IA — AMELIORABLE

**Ce qui est present :**
- Organization schema (Yoast) : nom, logo, telephone, email, reseaux sociaux (5 liens sameAs)
- Article schema sur les blog posts : headline, auteur, dates, publisher
- WebPage, BreadcrumbList, WebSite : basiques mais presents

**Ce qui manque (et qui aide les LLMs a mieux comprendre le site) :**

1. **`LocalBusiness` ou `Corporation` schema** avec adresse physique complete, horaires, zone de service — ceci est critique pour apparaitre dans les reponses locales des agents IA

2. **`Product` schema** sur les pages produits (SCMS, DOO Express, RME, etc.) avec :
   - name, description, brand, manufacturer
   - category, offers (si applicable)

3. **`Service` schema** pour les services offerts (design IoT, integration, etc.)

4. **`FAQPage` schema** : Ajouter des sections FAQ sur les pages cles (les agents IA adorent les FAQ structurees car elles repondent directement aux questions des utilisateurs)

5. **`HowTo` schema** : Pour les guides et tutoriels

6. **`keywords` dans Article schema** : Le champ keywords est vide sur les articles

7. **`description` manquante** sur l'un des deux blocs Article schema

### 4.4 Contenu structure pour les LLMs — FAIBLE

Les agents IA preferent du contenu :
- Clairement structure avec des headings hierarchiques (H1 > H2 > H3)
- Avec des definitions explicites (qu'est-ce que le SCMS? qu'est-ce qu'un noeud RME?)
- Avec des donnees chiffrees (nombre de villes servies, economies d'energie, etc.)
- Avec des FAQ qui repondent aux questions courantes

**Problemes actuels :**
- La homepage n'a PAS de H1
- Les pages produits ont peu de contenu textuel (327 mots sur /solutions/)
- Pas de page "A propos" ou "Notre technologie" facilement crawlable avec du contenu riche
- Pas de glossaire des termes (SCMS, LNLV, RME, etc.)
- Les articles de blog sont bien structures (H2 pour les questions) mais manquent de donnees chiffrees

**Recommandations :**
1. **HAUTE** : Creer une page `/about/` ou `/company/` avec un contenu riche, structure, et crawlable (histoire, mission, chiffres cles, equipe, partenaires)
2. **HAUTE** : Enrichir les pages produits avec 800+ mots de contenu descriptif structure
3. **MOYENNE** : Ajouter des sections FAQ sur les pages cles (/solutions/, /contact/, pages produits)
4. **MOYENNE** : Creer un glossaire `/glossary/` ou `/resources/glossary/` pour les termes techniques
5. **BASSE** : Ajouter des "entity definitions" dans le contenu (phrases de type "SCMS (Smart City Management System) is Dimonoff's cloud-based platform for...")

### 4.5 Signaux E-E-A-T (Experience, Expertise, Authoritativeness, Trust) — MOYEN

Les agents IA (et Google) accordent une importance croissante aux signaux E-E-A-T.

**Present :**
- Schema auteur (Person) sur les articles
- Profils sociaux dans le schema Organization (sameAs)
- Articles demontrant l'expertise (conferences, etudes de cas)

**Manquant :**
- Pas de pages auteur enrichies (bio, photo, credentials)
- Pas de page "About/Team" avec les profils d'expertise
- Pas de certifications/awards visibles dans le schema
- Pas de temoignages clients structures
- Pas de lien vers des publications externes (presse, etudes)

---

## 5. Plan d'action priorise

### Priorite CRITIQUE (faire cette semaine)

| # | Action | Impact SEO | Impact IA | Effort |
|---|--------|-----------|-----------|--------|
| 1 | Ajouter un H1 sur la homepage | Eleve | Moyen | 5 min |
| 2 | Corriger viewport (retirer user-scalable=0) | Moyen | Faible | 2 min |
| 3 | Ajouter alt text aux images (commencer par homepage et pages produits) | Eleve | Moyen | 2h |
| 4 | Corriger les redirections 301 parking (non fonctionnelles) | Eleve | Faible | 30 min |

### Priorite HAUTE (faire dans les 2 semaines)

| # | Action | Impact SEO | Impact IA | Effort |
|---|--------|-----------|-----------|--------|
| 5 | Creer le fichier `/llms.txt` | Faible | Eleve | 30 min |
| 6 | Mettre a jour le robots.txt (sitemap + directives IA) | Moyen | Moyen | 15 min |
| 7 | Optimiser le title de la homepage et des pages cles | Eleve | Moyen | 30 min |
| 8 | Ajouter le schema LocalBusiness/Corporation sur /contact/ | Moyen | Eleve | 1h |
| 9 | Convertir les images en WebP | Moyen | Faible | 1h (avec plugin) |
| 10 | Nettoyer le sitemap (retirer URLs 404, tags, auteurs) | Moyen | Faible | 30 min |

### Priorite MOYENNE (faire dans le mois)

| # | Action | Impact SEO | Impact IA | Effort |
|---|--------|-----------|-----------|--------|
| 11 | Enrichir le contenu des pages produits (800+ mots) | Eleve | Eleve | 4h par page |
| 12 | Ajouter des FAQ structurees (FAQPage schema) sur pages cles | Moyen | Eleve | 2h par page |
| 13 | Creer une page /about/ ou /company/ riche | Moyen | Eleve | 3h |
| 14 | Ajouter Product schema sur les pages produits | Moyen | Eleve | 2h |
| 15 | Optimiser le chargement JS/CSS (defer, concatener) | Moyen | Faible | 2h |
| 16 | Preload des polices critiques | Faible | Faible | 15 min |
| 17 | Corriger la meta description FR sur les articles EN (bug Polylang) | Moyen | Faible | 1h |

### Priorite BASSE (planifier)

| # | Action | Impact SEO | Impact IA | Effort |
|---|--------|-----------|-----------|--------|
| 18 | Creer un glossaire technique | Faible | Eleve | 3h |
| 19 | Enrichir les pages auteurs (bio, photo, expertise) | Faible | Moyen | 2h |
| 20 | Ajouter des temoignages clients structures | Faible | Moyen | 3h |
| 21 | Audit hreflang croise complet (10 pages EN/FR/ES) | Moyen | Faible | 2h |
| 22 | Desactiver l'indexation des archives tag/auteur dans Yoast | Faible | Faible | 5 min |

---

## 6. Notes specifiques a la migration parking

La migration du contenu parking vers spatium-iot.com a un impact SEO direct sur dimonoff.com :

1. **Les redirections 301 ne fonctionnent pas** — Les URLs parking retournent 404 au lieu de rediriger vers spatium-iot.com. Cela cause une perte de link equity et une mauvaise experience utilisateur. A corriger en urgence.

2. **Le sitemap contient probablement encore des URLs parking** — Les fichiers dt_portfolio-sitemap.xml et post-sitemap.xml n'ont pas ete verifies apres la depublication des articles.

3. **Les liens internes dans le mega menu** pointent encore vers des pages parking locales (`/resources/`, `/news/` avec contexte parking).

4. **Le cross-linking avec spatium-iot.com** est bien en place via la barre Vectanor et le menu SPATIUM.

---

## 7. Checklist de verification rapide

Apres implementation des recommandations, verifier avec :

- [ ] Google Search Console : Soumettre le sitemap, verifier les erreurs d'indexation
- [ ] Bing Webmaster Tools : Meme verification
- [ ] PageSpeed Insights : Tester mobile et desktop (viser 90+)
- [ ] Rich Results Test (search.google.com/test/rich-results) : Valider les schemas
- [ ] Schema.org Validator : Verifier la syntaxe JSON-LD
- [ ] Screaming Frog : Crawl complet pour detecter les 404 et les redirections cassees
- [ ] Ahrefs/SEMrush : Verifier les positions avant/apres pour les mots-cles cibles
- [ ] ChatGPT/Perplexity : Tester "What is Dimonoff?" et "smart city IoT solutions Quebec" pour voir si le site est cite

---

*Rapport genere le 2026-03-24. Les donnees sont basees sur l'analyse du frontend et des fichiers techniques du site a cette date.*
