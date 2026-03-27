# Rapport Phase 2 — SEO Technique & Préparation IA
## dimonoff.com | 25 mars 2026

---

## Résumé exécutif

La Phase 2 du plan d'amélioration SEO/IA de dimonoff.com est **complétée à 100%**. Toutes les tâches prévues ont été réalisées, incluant le bonus de la Phase 1 (robots.txt).

| Tâche | Statut |
|-------|--------|
| 2.1 Vérifier/personnaliser llms.txt | ✅ Vérifié — mode Automatique conservé |
| 2.2 Optimiser meta titles/descriptions | ✅ 12 pages mises à jour (EN/FR/ES) |
| 2.3 Nettoyer le sitemap XML | ✅ Portfolios, tags, auteurs désactivés |
| 2.4 Ajouter schema LocalBusiness/Corporation | ✅ mu-plugin JSON-LD déployé |
| 2.5 Corriger bug meta FR sur articles EN | ✅ 1 article corrigé, aucun autre cas |
| Bonus Phase 1 — robots.txt | ✅ Mis à jour avec directives AI bots |

---

## 2.1 — Vérification llms.txt

**Action :** Vérifié les paramètres Yoast SEO → Site features → llms.txt

**Constat :** Yoast SEO Premium v27.1.1 génère automatiquement le fichier llms.txt (5799 caractères). Le mode Automatique inclut pages, articles, portfolios, catégories et tags.

**Décision :** Conserver le mode Automatique. Le contenu s'améliorera au fil des optimisations de metadata. Un passage en mode Manuel pourra être envisagé plus tard pour cibler les pages stratégiques.

---

## 2.2 — Meta titles & descriptions optimisés

**Méthode :** Mise à jour via les champs cachés Yoast (`#yoast_wpseo_title` / `#yoast_wpseo_metadesc`) dans l'éditeur Gutenberg, suivie de `wp.data.dispatch('core/editor').savePost()`.

### Homepage (3 langues)

| Langue | ID | Nouveau titre |
|--------|-----|---------------|
| EN | 48318 | Dimonoff \| Smart City IoT Solutions — Connected Lighting & Asset Management |
| FR | 48499 | Dimonoff \| Solutions IoT Ville Intelligente — Éclairage & Gestion d'actifs connectés |
| ES | 74058 | Dimonoff \| Soluciones IoT Ciudad Inteligente — Iluminación & Gestión de activos conectados |

### Solutions (3 langues)

| Langue | ID | Nouveau titre |
|--------|-----|---------------|
| EN | 24 | Dimonoff Solutions \| SCMS Platform — Smart Lighting, IoT & Asset Management |
| FR | 4950 | Solutions Dimonoff \| Plateforme SCMS — Éclairage intelligent, IoT & Gestion d'actifs |
| ES | 74278 | Soluciones Dimonoff \| Plataforma SCMS — Iluminación inteligente, IoT & Gestión de activos |

### About (3 langues)

| Langue | ID | Nouveau titre |
|--------|-----|---------------|
| EN | 3958 | About Dimonoff \| Smart City IoT Company — Quebec, Canada |
| FR | 60677 | À propos de Dimonoff \| Entreprise IoT Ville Intelligente — Québec, Canada |
| ES | 74215 | Sobre Dimonoff \| Empresa IoT Ciudad Inteligente — Quebec, Canadá |

### Contact (3 langues)

| Langue | ID | Nouveau titre |
|--------|-----|---------------|
| EN | 17 | Contact Dimonoff \| Smart City IoT Solutions — Get a Quote |
| FR | 4954 | Contactez Dimonoff \| Solutions IoT Ville Intelligente — Demandez une soumission |
| ES | 74091 | Contacte a Dimonoff \| Soluciones IoT Ciudad Inteligente — Solicite un presupuesto |

**Toutes les 12 pages** ont été vérifiées via l'API REST (`yoast_head_json`).

---

## 2.3 — Nettoyage du sitemap XML

**Éléments désactivés dans Yoast SEO → Settings :**

| Élément | Section Yoast | Ancien état | Nouveau état |
|---------|--------------|-------------|-------------|
| Portfolio (projects) | Content types → Portfolio | Show in search | **Noindex** |
| Tags (posts) | Categories & tags → Tags | Show in search | **Noindex** |
| Portfolio Categories | Categories & tags → Project-category | Show in search | **Noindex** |
| Portfolio Tags | Categories & tags → Project-tag | Show in search | **Noindex** |
| Author archives | Advanced → Author archives | Show in search | **Noindex** |

**Impact :** Le sitemap XML ne contient plus les URLs inutiles (portfolios, tags, pages d'auteurs). Les crawlers se concentrent sur le contenu pertinent.

---

## 2.4 — Schema LocalBusiness/Corporation (JSON-LD)

**Fichier créé :** `wp-content/mu-plugins/dimonoff-local-business-schema.php`

**Type :** mu-plugin WordPress (chargé automatiquement, sans activation requise)

**Données du schema :**

- **@type :** LocalBusiness + Corporation
- **Adresse :** 2820, rue Einstein, Quebec City, QC G1X 4B7, CA
- **Téléphone :** +1-418-877-7555
- **Email :** info@dimonoff.com
- **Coordonnées GPS :** 46.7737, -71.3080
- **Fondation :** 2008
- **Organisation parente :** Groupe Vectanor (vectanor.com)
- **Zone desservie :** Canada, États-Unis
- **Réseaux sociaux :** Facebook, LinkedIn, X, YouTube, Instagram
- **Domaines d'expertise :** Smart City, IoT, Connected Lighting, Asset Management, SCMS

**Vérification :** Le schema est visible dans le code source de la homepage (`application/ld+json` avec `LocalBusiness`). Le site fonctionne normalement après déploiement.

**Note :** Ce schema complète celui de Yoast (Organization) sans conflit. Les deux coexistent.

---

## 2.5 — Bug meta description FR sur articles EN

**Diagnostic :** Scan de ~100 articles EN (5 pages API, 20 articles/page) pour détecter des meta descriptions en français sur des URLs anglaises.

**Résultat :** 1 seul article affecté trouvé :

| Article | ID | Problème | Correction |
|---------|----|----------|------------|
| Naomih Dalpé Joins Dimonoff... | 391978 | Description FR au lieu de EN | ✅ Corrigée |

**Ancienne description (FR) :** *"Naomih Dalpé est la nouvelle directrice de développement d'affaires de Dimonoff pour SCMS..."*

**Nouvelle description (EN) :** *"Naomih Dalpé joins Dimonoff as Director of Business Development for SCMS, the smart lighting management platform. Accelerating smart city growth across North America."*

**Cause probable :** L'article a été rédigé d'abord en FR, puis traduit en EN via Polylang, mais la meta description Yoast n'a pas été traduite.

---

## Bonus Phase 1 — robots.txt

**Complété dans cette session.** Le fichier physique `robots.txt` a été mis à jour via le plugin File Manager :

- Sitemap déclaré (`sitemap_index.xml`)
- AI crawlers autorisés : GPTBot, ClaudeBot, PerplexityBot, Google-Extended
- Scrapers agressifs bloqués : CCBot, anthropic-ai, Bytespider
- Vérifié live à `https://www.dimonoff.com/robots.txt`

---

## Prochaines étapes — Phase 3

Selon le plan d'amélioration, la Phase 3 couvre la **performance & images** :

- 3.1 Convertir les images en WebP
- 3.2 Ajouter alt text aux images critiques
- 3.3 Optimiser le chargement CSS/JS
- 3.4 Preload des polices critiques

Puis la Phase 4 couvre le **contenu, enrichissement & maillage inter-sites** :

- 4.1 Enrichir la page Solutions (800+ mots)
- 4.2 Ajouter des sections FAQ structurées
- 4.3 Enrichir la page About/Company
- 4.4 Ajouter Product schema sur les pages produits
- 4.5 Créer un glossaire technique
- 4.6 Ajouter des liens croisés inter-sites (Dimonoff ↔ Spatium, Dimonoff ↔ Amotus)

---

*Rapport généré le 25 mars 2026*
