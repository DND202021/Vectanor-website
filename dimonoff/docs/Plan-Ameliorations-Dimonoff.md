# Plan d'exécution — Améliorations dimonoff.com

**Date :** 2026-03-25
**Score actuel :** 55/100
**Objectif :** 80+/100
**Responsable :** Daniel Noiseux + Claude

---

## Contraintes et prérequis

| Contrainte | Impact | Solution |
|------------|--------|----------|
| Accès wp-admin dimonoff.com requis | Bloque la majorité du travail | Daniel doit se connecter et garder la session active |
| Cloudflare en frontal | Peut cacher des changements / servir des 404 en cache | Purger le cache après chaque lot de modifications |
| Elementor Pro + The7 theme | Le H1 est probablement dans un widget Elementor | Modifier via l'éditeur Elementor, pas le code |
| Polylang (EN/FR/ES) | Chaque modif doit être faite 3x | Commencer par EN, puis dupliquer FR/ES |

---

## Phase 1 — Corrections critiques et quick wins (Session 1)

*Durée estimée : 1-2h | Prérequis : accès wp-admin dimonoff.com*
*Impact : +10 à +15 points sur le score global*

### 1.1 Corriger les redirections 301 parking
- **Pourquoi :** Les anciennes URLs parking retournent 404 → perte de link equity SEO
- **Comment :** Yoast SEO > Redirections > Vérifier que les 86 redirections sont actives
- **Diagnostic :** Tester format URL (avec/sans www, avec/sans slash initial)
- **Alternatives si Yoast échoue :** Redirections via .htaccess ou plugin Redirection
- **Vérification :** Tester `dimonoff.com/solutions/mobility-smart-parking/` → doit rediriger vers spatium-iot.com

### 1.2 Ajouter H1 sur la homepage
- **Pourquoi :** Pas de H1 = signal SEO critique manquant
- **Comment :** Ouvrir la homepage dans Elementor > Changer le premier heading widget de H2 à H1
- **Texte recommandé EN :** "Smart City & IoT Solutions — Connected Asset Management"
- **Texte recommandé FR :** "Solutions Villes Intelligentes & IoT — Gestion d'actifs connectés"
- **Faire pour :** EN, FR, ES

### 1.3 Corriger le viewport (accessibilité)
- **Pourquoi :** `user-scalable=0` bloque le zoom → pénalité Google, violation WCAG 2.1 AA
- **Comment :** Dans le theme (The7) > Settings ou via functions.php, retirer `maximum-scale=1, user-scalable=0`
- **Cible :** `<meta name="viewport" content="width=device-width, initial-scale=1">`

### 1.4 Mettre à jour robots.txt
- **Pourquoi :** Pas de référence sitemap, pas de directives IA
- **Comment :** Yoast SEO > Outils > Éditeur de fichiers > robots.txt
- **Contenu :** Ajouter référence sitemap + directives AI bots (GPTBot, ClaudeBot, PerplexityBot, Google-Extended)
- **Voir :** Contenu recommandé dans le rapport d'audit section 1.1

### 1.5 Nettoyer le mega menu (résidus parking)
- **Pourquoi :** Sous-items "Parking Management System" pointent vers des pages qui n'existent plus
- **Comment :** Apparence > Menus > Menu EN > Mega Menu settings sous l'onglet SPATIUM
- **Action :** Supprimer les sous-items ou les rediriger vers spatium-iot.com

---

## Phase 2 — SEO technique et préparation IA (Session 2)

*Durée estimée : 2-3h | Prérequis : Phase 1 complétée*
*Impact : +10 à +12 points*

### 2.1 Créer et déployer `/llms.txt`
- **Pourquoi :** Permet aux agents IA de comprendre rapidement Dimonoff → meilleure citation
- **Comment :** Créer le fichier, l'uploader à la racine du site via FTP ou plugin
- **Contenu :** Déjà rédigé dans le rapport d'audit section 4.1
- **Alternative sans FTP :** Créer via un plugin comme "WP LLMs.txt" ou via functions.php

### 2.2 Optimiser les titles et meta descriptions
- **Homepage EN :** `Dimonoff | Smart City IoT Solutions — Connected Lighting & Asset Management`
- **Homepage FR :** `Dimonoff | Solutions IoT Ville Intelligente — Éclairage & Gestion d'actifs connectés`
- **Page Solutions :** Ajouter mots-clés (SCMS, smart lighting, IoT, connected infrastructure)
- **Comment :** Yoast SEO > Éditer le snippet pour chaque page
- **Faire pour :** Homepage, Solutions, Contact, About (EN/FR/ES = 12 pages)

### 2.3 Nettoyer le sitemap XML
- **Pourquoi :** Contient probablement des URLs 404 (articles parking dépubliés, portfolio)
- **Comment :** Yoast SEO > Réglages > Types de contenu > Désactiver l'indexation des portfolios, tags, auteurs
- **Vérification :** Ouvrir `dimonoff.com/sitemap_index.xml` et vérifier chaque sous-sitemap

### 2.4 Ajouter schema LocalBusiness/Corporation
- **Pourquoi :** Critique pour apparaître dans les réponses locales des agents IA
- **Comment :** Ajouter un bloc JSON-LD dans le header via functions.php ou via un plugin schema
- **Données :** Adresse Québec, téléphone, email, horaires, zone de service

### 2.5 Corriger le bug meta description FR sur articles EN
- **Pourquoi :** Bug Polylang/Yoast détecté — la meta desc FR s'affiche sur les articles EN
- **Comment :** Vérifier les réglages Polylang pour la synchronisation des champs Yoast
- **Vérification :** Tester 3-4 articles EN et confirmer que la meta desc est en anglais

---

## Phase 3 — Performance et images (Session 3)

*Durée estimée : 2-3h | Prérequis : Phase 2 complétée*
*Impact : +8 à +10 points*

### 3.1 Convertir les images en WebP
- **Pourquoi :** 0% WebP actuellement, gain 25-35% sur le poids
- **Comment :** Plugin ShortPixel, Imagify ou EWWW Image Optimizer
- **Note :** ShortPixel est déjà installé sur spatium-iot.com (quota épuisé) — vérifier si actif sur dimonoff.com
- **Scope :** Toutes les images du site (commencer par homepage et pages produits)

### 3.2 Ajouter alt text aux images critiques
- **Pourquoi :** ~70% des images sans alt → mauvais pour SEO image et accessibilité
- **Comment :** Médiathèque WordPress > Filtrer les images sans alt > Ajouter des descriptions pertinentes
- **Priorité :** Homepage (115 images), pages produits, page contact
- **Conseil :** Décrire le contenu de l'image + inclure un mot-clé pertinent quand naturel

### 3.3 Optimiser le chargement CSS/JS
- **Pourquoi :** 35 JS + 10 CSS render-blocking
- **Comment :** Plugin Autoptimize (déjà sur spatium-iot.com) ou WP Rocket
- **Actions :** Concatener CSS, différer JS non critiques, preload des polices Google Fonts (Nunito, Poppins, Roboto)

### 3.4 Preload des polices critiques
- **Pourquoi :** Les Google Fonts sont chargées sans preload → retarde le rendu
- **Comment :** Ajouter dans `<head>` via functions.php :
  ```html
  <link rel="preload" href="[font-url].woff2" as="font" type="font/woff2" crossorigin>
  ```

---

## Phase 4 — Contenu et enrichissement (Sessions 4-5)

*Durée estimée : 6-10h | Prérequis : Phases 1-3 complétées*
*Impact : +8 à +12 points*

### 4.1 Enrichir la page Solutions
- **Pourquoi :** Seulement 327 mots, trop mince pour un bon classement
- **Cible :** 800+ mots avec contenu descriptif structuré (H2/H3)
- **Contenu à ajouter :** Description détaillée SCMS, DOO Express, cas d'usage, bénéfices chiffrés

### 4.2 Ajouter des sections FAQ structurées
- **Pourquoi :** Les agents IA adorent les FAQ → réponses directes aux questions utilisateurs
- **Où :** Pages Solutions, Contact, pages produits principales
- **Comment :** Ajouter des sections avec schema FAQPage (widget Elementor FAQ + JSON-LD)

### 4.3 Créer une page About/Company
- **Pourquoi :** Absence de page "À propos" riche → signal E-E-A-T faible
- **Contenu :** Histoire, mission, chiffres clés, équipe, partenaires, certifications
- **Faire en :** EN + FR + ES

### 4.4 Ajouter Product schema sur les pages produits
- **Pourquoi :** Permet aux agents IA de comprendre les produits Dimonoff
- **Comment :** JSON-LD avec name, description, brand, manufacturer, category
- **Pages :** SCMS, DOO Express, Gateway G3+, RME/RTM/LNLV, Mobile App

### 4.5 Créer un glossaire technique
- **Pourquoi :** Aide les LLMs à comprendre les termes propriétaires (SCMS, LNLV, RME, etc.)
- **Format :** Page `/glossary/` avec termes et définitions structurés
- **Schema :** DefinedTermSet pour un bonus SEO

### 4.6 Ajouter des liens croisés inter-sites du Groupe Vectanor
- **Pourquoi :** Renforce l'autorité de domaine et la compréhension du groupe par les moteurs/agents IA
- **Liens Dimonoff ↔ Spatium :**
  - Page About Dimonoff → lien vers spatium-iot.com (division parking)
  - Page Solutions Dimonoff → mention/lien vers Spatium pour la mobilité
  - Page About Spatium → lien retour vers dimonoff.com (société mère technologique)
- **Liens Dimonoff ↔ Amotus :**
  - Page About Dimonoff → lien vers amotus.com (division ingénierie IoT/électronique)
  - Page Solutions/Produits Dimonoff → mention Amotus comme partenaire de design électronique
  - Page About Amotus → lien retour vers dimonoff.com
- **Comment :** Ajouter dans le footer et/ou pages About une section "Groupe Vectanor" avec liens vers toutes les divisions
- **Faire pour :** EN/FR/ES sur chaque site concerné

---

## Phase 5 — Vérification et monitoring (Post-exécution)

*Durée estimée : 1-2h*

### 5.1 Tests de validation
- Google Search Console : Soumettre le sitemap mis à jour, vérifier les erreurs
- Rich Results Test : Valider tous les schemas JSON-LD
- PageSpeed Insights : Tester mobile et desktop (viser 90+)
- Schema.org Validator : Vérifier la syntaxe

### 5.2 Tests agents IA
- ChatGPT : "What is Dimonoff?" / "smart city IoT solutions Quebec"
- Perplexity : Mêmes requêtes
- Claude : Mêmes requêtes
- Vérifier que llms.txt est accessible et bien formaté

### 5.3 Suivi
- Screaming Frog crawl complet (404, redirections, alt text)
- Comparer positions SEO avant/après (Ahrefs ou SEMrush)
- Refaire un audit dans 30 jours pour mesurer les progrès

---

## Résumé par phase

| Phase | Durée | Impact estimé | Prérequis |
|-------|-------|---------------|-----------|
| **Phase 1** — Quick wins critiques | 1-2h | +10 à +15 pts | Accès wp-admin |
| **Phase 2** — SEO technique + IA | 2-3h | +10 à +12 pts | Phase 1 |
| **Phase 3** — Performance + images | 2-3h | +8 à +10 pts | Phase 2 |
| **Phase 4** — Contenu + enrichissement | 6-10h | +8 à +12 pts | Phases 1-3 |
| **Phase 5** — Vérification | 1-2h | Consolidation | Phases 1-4 |
| **TOTAL** | ~15-20h | **55 → 80+/100** | |

---

## Ce que Claude peut faire vs ce qui nécessite Daniel

| Tâche | Claude peut faire | Daniel doit faire |
|-------|-------------------|-------------------|
| Rédiger contenu llms.txt, robots.txt, schemas | Oui | Valider et déployer |
| Modifier via wp-admin (Elementor, Yoast, menus) | Oui (via Chrome) | Garder la session active |
| Écrire du code PHP (functions.php) | Oui (via Theme Editor) | Valider les changements |
| Créer du contenu texte (FAQ, glossaire, etc.) | Oui | Réviser et valider |
| Accès FTP / fichiers serveur | Non | Uploader si nécessaire |
| Configuration Cloudflare | Non | Purger le cache si nécessaire |
| Google Search Console | Non | Soumettre le sitemap |

---

*Plan prêt pour exécution. Commencer par Phase 1 dès que l'accès wp-admin dimonoff.com est confirmé.*
