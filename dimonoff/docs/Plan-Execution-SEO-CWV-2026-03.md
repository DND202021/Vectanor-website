# Plan d'Execution SEO & CWV — dimonoff.com
**Date**: 2026-03-29
**Objectif**: Corriger tous les problemes techniques et on-page identifies dans l'audit GSC
**Approche**: Prudente, par phases, avec validation apres chaque etape
**Prerequis**: Acces WP admin dimonoff.com (login requis par l'utilisateur)

---

## Vue d'ensemble des phases

| Phase | Objectif | Risque | Impact | Effort |
|-------|----------|--------|--------|--------|
| 0 | Connexion et reconnaissance | Nul | - | 15 min |
| 1 | Fix CWV Desktop (CLS + LCP) | Faible | TRES ELEVE | 2h |
| 2 | Title tags et meta descriptions | Nul | TRES ELEVE | 2h |
| 3 | Fix erreurs 404 et redirections | Faible | ELEVE | 2-3h |
| 4 | Fix canonicals et duplicates | Faible | ELEVE | 1-2h |
| 5 | Contraste et accessibilite | Nul | MOYEN | 1h |
| 6 | Backlinks cross-Vectanor | Nul | MOYEN | 30 min |
| 7 | Validation finale | Nul | - | 30 min |

**Temps total estime**: 8-10 heures
**Risque global**: FAIBLE (aucune modification de structure, uniquement ajouts CSS/JS/meta)

---

## Phase 0 — Connexion et Reconnaissance

### 0.1 Login WP Admin
- [ ] L'utilisateur se connecte a https://www.dimonoff.com/wp-admin/
- [ ] Verifier qu'on a acces au Theme Editor (Appearance > Theme File Editor)
- [ ] Verifier qu'on a acces a Yoast SEO (Posts, Pages)
- [ ] Verifier le acces au File Manager (pour mu-plugins)

### 0.2 Reconnaissance technique
- [ ] Identifier le fichier functions.php actif (theme The7)
- [ ] Lister les mu-plugins deja deployes (16 connus, voir STATUS.md)
- [ ] Verifier la config Autoptimize actuelle
- [ ] Verifier la config Hummingbird actuelle
- [ ] Tester que le site charge correctement avant modifications

### 0.3 Backup
- [ ] S'assurer que Snapshot Pro a un backup recent
- [ ] Noter l'heure de debut des modifications

---

## Phase 1 — Fix Core Web Vitals Desktop (CLS + LCP)

**Probleme**: 237/237 URLs desktop sont "Poor" (CLS > 0.25 + LCP > 4s)
**Cause**: Elementor rendering pipeline + images lourdes + TTFB 4200ms
**Approche**: Meme technique que Spatium (prouvee) + optimisations supplementaires

### 1.1 Fix CLS Desktop via CSS (mu-plugin)
**Fichier**: `dimonoff-cls-stabilize.php` (nouveau mu-plugin)
**Methode**: Upload via File Manager (elFinder) dans /wp-content/mu-plugins/

```php
<?php
/*
Plugin Name: Dimonoff CLS Stabilization
Description: Reduce CLS on desktop by stabilizing Elementor sections
Version: 1.0
*/

// CLS stabilization CSS
add_action('wp_head', function() {
    echo '<style id="dimonoff-cls-stabilize">
.elementor-section-wrap>.elementor-section,.elementor>.e-con{contain:layout style}
.elementor-section-wrap>.elementor-section:first-child,.elementor>.e-con:first-child{min-height:600px}
.elementor-widget{contain:layout style}
.elementor-widget-image img{content-visibility:auto}
@media(min-width:1025px){
.elementor-section-wrap>.elementor-section~.elementor-section~.elementor-section~.elementor-section,
.elementor>.e-con~.e-con~.e-con~.e-con{content-visibility:auto;contain-intrinsic-size:auto 500px}
}
</style>' . "\n";
}, 1);
```

**IMPORTANT**: Pas de backslashes dans le code (contrainte elFinder stripslashes)

### 1.2 Fix LCP via preload + lazy loading
**Fichier**: `dimonoff-lcp-fix.php` (nouveau mu-plugin)

```php
<?php
/*
Plugin Name: Dimonoff LCP Fix
Description: Preload hero image, defer non-critical CSS
Version: 1.0
*/

// Preload hero image LCP
add_action('wp_head', function() {
    if (is_front_page()) {
        // Preload the hero background image (identifier l'URL exacte apres reconnaissance)
        // echo '<link rel="preload" as="image" href="URL_HERO_IMAGE">' . "\n";
    }
}, 1);

// Optimize Google Fonts: display=swap to display=optional
add_filter('style_loader_src', function($src) {
    if (strpos($src, 'fonts.googleapis.com') !== false) {
        $src = str_replace('display=swap', 'display=optional', $src);
    }
    return $src;
}, 100);

// Add fetchpriority=high to hero images
add_action('wp_footer', function() {
    if (is_admin()) return;
    echo '<script id="dimonoff-lcp-priority">!function(){var h=document.querySelector(".elementor-section:first-child img");if(h)h.setAttribute("fetchpriority","high")}()</script>';
});
```

### 1.3 Autoptimize — activer CSS aggregation
- [ ] Naviguer a Settings > Autoptimize
- [ ] Verifier que "Optimize CSS Code" est coche
- [ ] Activer "Aggregate CSS-files" si pas deja fait
- [ ] Verifier que "Do not aggregate but defer" est coche pour JS
- [ ] Sauvegarder et vider le cache
- [ ] **VERIFIER** que le site fonctionne apres

### 1.4 Hummingbird — verifier config
- [ ] Verifier que le cache de page est actif
- [ ] Verifier que GZIP compression est active
- [ ] Verifier la config de minification (pas de conflit avec Autoptimize)

### 1.5 Validation Phase 1
- [ ] Charger la homepage et verifier visuellement
- [ ] Charger /solutions/smart-lighting-control/ et verifier
- [ ] Verifier que les compteurs Elementor fonctionnent encore (conflit Hummingbird connu)
- [ ] Scanner le console du navigateur pour erreurs JS

---

## Phase 2 — Title Tags et Meta Descriptions

**Probleme**: Title tags faibles, meta descriptions identiques partout, CTR 0.1% sur la page cle
**Methode**: Via Yoast SEO dans l'editeur WordPress de chaque page

### 2.1 Title Tags a reecrire

| Page ID | Page | Title actuel | Title optimise |
|---------|------|-------------|----------------|
| 48318 | Homepage EN | Home \| Dimonoff | Smart City IoT Solutions for Lighting & Infrastructure \| Dimonoff |
| — | Homepage FR | Accueil \| Dimonoff | Solutions IoT Ville Intelligente pour Eclairage et Infrastructure \| Dimonoff |
| — | Homepage ES | Inicio \| Dimonoff | Soluciones IoT Ciudad Inteligente para Iluminacion e Infraestructura \| Dimonoff |
| 79360 | Smart Lighting EN | Smart Street Lighting \| Dimonoff | Smart Street Lighting Control System \| IoT Platform \| Dimonoff |
| 79365 | Smart Lighting FR | Eclairage intelligent \| Dimonoff | Systeme de Controle d'Eclairage de Rue Intelligent \| Plateforme IoT \| Dimonoff |
| 79372 | Smart Lighting ES | Alumbrado inteligente \| Dimonoff | Sistema de Control de Alumbrado Publico Inteligente \| IoT \| Dimonoff |
| — | SCMS EN | Dimonoff \| SCMS Platform \| Dimonoff | SCMS Smart City Management System \| IoT Lighting Platform \| Dimonoff |
| 3958 | About EN | About Us \| Dimonoff | About Dimonoff \| Smart City IoT Pioneer Since 2008 \| Quebec |
| 24 | Solutions EN | Solutions \| Dimonoff | Smart City Solutions \| Lighting Control, Parking & Infrastructure \| Dimonoff |
| — | RME EN | RME \| Dimonoff | RME Smart Wireless Lighting Node \| External Controller \| Dimonoff |
| — | Wireless Nodes EN | Wireless Nodes \| Dimonoff | Smart Wireless Lighting Nodes \| RME, RTM, LNLV Controllers \| Dimonoff |

### 2.2 Meta Descriptions a ecrire

| Page | Meta Description (max 155 chars) |
|------|--------------------------------|
| Homepage EN | Dimonoff designs smart city IoT solutions for connected street lighting, parking management and urban infrastructure. Trusted by 500+ cities since 2008. |
| Homepage FR | Dimonoff concoit des solutions IoT ville intelligente pour l'eclairage de rue connecte et la gestion d'infrastructure urbaine. 500+ villes depuis 2008. |
| Smart Lighting EN | Complete IoT platform for smart street lighting control. Monitor, dim and manage 850,000+ luminaires remotely. SCMS platform by Dimonoff. Free demo. |
| Smart Lighting FR | Plateforme IoT complete pour le controle d'eclairage de rue intelligent. Gerez 850 000+ luminaires a distance. Plateforme SCMS par Dimonoff. Demo gratuite. |
| SCMS EN | SCMS is Dimonoff's smart city management system. Real-time monitoring, adaptive dimming, energy analytics for street lighting. Open API, scalable to 1M+ nodes. |
| About EN | Dimonoff is a Quebec-based IoT company specializing in smart city solutions since 2008. 50-100 employees, 575+ projects in 6 countries. Part of Groupe Vectanor. |
| RME EN | The RME is Dimonoff's external smart wireless lighting node for retrofit street lighting projects. NEMA/Zhaga compatible, LoRaWAN/Wi-Fi/cellular connectivity. |
| Solutions EN | Explore Dimonoff smart city solutions: connected street lighting control, IoT parking management with Spatium, and urban infrastructure monitoring. |

### 2.3 Methode d'execution
- [ ] Pour chaque page: Edit Page > Yoast SEO meta box > SEO Title + Meta Description
- [ ] Utiliser le snippet preview Yoast pour valider la longueur
- [ ] Sauvegarder chaque page (Update)
- [ ] **NE PAS** modifier le contenu Elementor de la page

### 2.4 Validation Phase 2
- [ ] Verifier le title tag dans le source HTML de chaque page modifiee
- [ ] Verifier avec Yoast que tous les indicateurs sont verts
- [ ] Les changements prendront effet dans Google en 1-4 semaines

---

## Phase 3 — Fix Erreurs 404 et Redirections

**Probleme**: 77 pages 404, 22 soft 404, 713 redirects
**Methode**: Redirections 301 via mu-plugin (pas de .htaccess pour eviter conflits WAF)

### 3.1 Identifier les 404
- [ ] Dans GSC > Pages > Not found (404) > cliquer pour voir la liste des URLs
- [ ] Exporter la liste (bouton EXPORT)
- [ ] Categoriser: ancien contenu supprime vs liens casses vs typos d'URL

### 3.2 Identifier les Soft 404
- [ ] Dans GSC > Pages > Soft 404 > cliquer pour voir la liste
- [ ] Ce sont des pages qui existent mais retournent un contenu quasi-vide
- [ ] Solution: soit ajouter du contenu, soit mettre noindex

### 3.3 Creer mu-plugin de redirections 301
**Fichier**: `dimonoff-301-redirects.php`

```php
<?php
/*
Plugin Name: Dimonoff 301 Redirects
Description: Clean 301 redirects for old/broken URLs
Version: 1.0
*/

add_action('template_redirect', function() {
    $redirects = [
        // A REMPLIR apres export GSC des 404
        // '/old-url/' => '/new-url/',
    ];
    $uri = rtrim(parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH), '/') . '/';
    if (isset($redirects[$uri])) {
        wp_redirect(home_url($redirects[$uri]), 301);
        exit;
    }
});
```

**NOTE**: Sur dimonoff.com, `$_SERVER['REQUEST_URI']` est bloque par le WAF dans les requetes PUT mais fonctionne en lecture (GET). Le mu-plugin ci-dessus est safe car il lit uniquement.

### 3.4 Analyser les 713 redirects
- [ ] Dans GSC > Pages > Page with redirect > exporter
- [ ] Identifier les chaines de redirects (A -> B -> C)
- [ ] Pour chaque chaine: creer une redirection directe A -> C
- [ ] Verifier si certaines redirects pointent vers des pages 404 (redirect loops)

### 3.5 Validation Phase 3
- [ ] Tester chaque redirection 301 manuellement
- [ ] Verifier qu'aucune redirection ne boucle (302 -> 301 -> 302...)
- [ ] Soumettre les URLs corrigees a Google via "Request indexing" dans GSC

---

## Phase 4 — Fix Canonical et Duplicates

**Probleme**: 81 pages "Duplicate without user-selected canonical"

### 4.1 Identifier les duplicates
- [ ] Dans GSC > Pages > "Duplicate without user-selected canonical" > exporter
- [ ] Categoriser: versions www vs non-www, HTTP vs HTTPS, parametres UTM, pagination

### 4.2 Solutions possibles
1. **www vs non-www**: Verifier que Cloudflare redirige correctement
2. **HTTP vs HTTPS**: Verifier la redirection forcee HTTPS
3. **Parametres UTM**: Ajouter canonical sans parametres
4. **Pagination**: Ajouter rel="next"/"prev" ou noindex sur les pages de pagination
5. **Duplicates Polylang**: Verifier que chaque traduction a la bonne langue assignee

### 4.3 Fix via Yoast
- [ ] Pour chaque page dupliquee: Edit Page > Yoast > Advanced > Canonical URL
- [ ] Entrer l'URL canonique preferee
- [ ] Sauvegarder

### 4.4 Fix via mu-plugin (si necessaire)
**Fichier**: `dimonoff-canonical-fix.php` (nouveau)

```php
<?php
/*
Plugin Name: Dimonoff Canonical Fix
Description: Force canonical URLs to remove query parameters
Version: 1.0
*/

add_filter('wpseo_canonical', function($canonical) {
    // Remove UTM and tracking parameters from canonical
    if ($canonical) {
        $parsed = parse_url($canonical);
        if (isset($parsed['query'])) {
            $canonical = $parsed['scheme'] . '://' . $parsed['host'] . $parsed['path'];
            if (substr($canonical, -1) !== '/') $canonical .= '/';
        }
    }
    return $canonical;
});
```

### 4.5 Verifier les 244 pages noindex
- [ ] Dans GSC > Pages > "Excluded by noindex tag" > exporter
- [ ] Verifier si c'est intentionnel (archive pages, author pages, tag pages)
- [ ] Si des pages utiles sont en noindex par erreur: retirer le noindex via Yoast

---

## Phase 5 — Contraste et Accessibilite

**Methode**: Meme approche que Spatium (script JS + CSS)

### 5.1 Audit des couleurs
- [ ] Scanner la homepage pour les problemes de contraste WCAG AA
- [ ] Identifier les couleurs de marque The7 qui posent probleme
- [ ] Creer un mu-plugin de fix

### 5.2 Fix contraste (mu-plugin)
**Fichier**: `dimonoff-a11y-contrast.php` (nouveau)

```php
<?php
/*
Plugin Name: Dimonoff Accessibility Contrast
Description: Fix color contrast issues for WCAG AA compliance
Version: 1.0
*/

// Skip link CSS
add_action('wp_head', function() {
    echo '<style id="dimonoff-a11y">
.skip-link:focus,a.screen-reader-text:focus{clip:auto!important;display:block!important;
height:auto;width:auto;position:fixed!important;top:7px;left:7px;z-index:100000;
background:#0a1628;color:#fff;padding:15px 23px;font-size:14px;text-decoration:none;
box-shadow:0 0 2px 2px rgba(0,0,0,.3)}
</style>' . "\n";
}, 2);

// Aria labels for unlabeled inputs
add_action('wp_footer', function() {
    if (is_admin()) return;
    echo '<script id="dimonoff-a11y-fix">!function(){document.querySelectorAll("input:not([aria-label]):not([id]),textarea:not([aria-label]):not([id])").forEach(function(e){var p=e.getAttribute("placeholder");if(p)e.setAttribute("aria-label",p)})}()</script>';
});
```

### 5.3 Fix alt text images
- [ ] Aller dans Media > Library
- [ ] Filtrer les images sans alt text
- [ ] Ajouter des alt texts descriptifs pour chaque image

---

## Phase 6 — Backlinks Cross-Vectanor

### 6.1 Verifier les crosslinks existants
- [ ] Le mu-plugin `dimonoff-crosslinks.php` est deja deploye
- [ ] Verifier qu'il fonctionne correctement en frontend
- [ ] Verifier que spatium-iot.com linke vers dimonoff.com (deja fait via footer Vectanor)

### 6.2 Ajouter backlink depuis spatium-iot.com
- [ ] Deja fait dans la session precedente (footer Groupe Vectanor)
- [ ] Verifier que le lien est crawlable (pas nofollow)

### 6.3 Ajouter backlink depuis amotus.com
- [ ] Necessite login amotus.com (a faire par l'utilisateur)
- [ ] Meme approche: footer Groupe Vectanor ou page Solutions

---

## Phase 7 — Validation Finale

### 7.1 Tests fonctionnels
- [ ] Charger homepage EN, FR, ES — verifier OK
- [ ] Charger /solutions/smart-lighting-control/ — verifier OK
- [ ] Charger page SCMS — verifier OK
- [ ] Charger page About — verifier OK
- [ ] Verifier les compteurs Elementor (bug connu avec Hummingbird)
- [ ] Tester sur mobile (responsive)

### 7.2 Tests techniques
- [ ] Verifier les title tags dans le source HTML
- [ ] Verifier les meta descriptions dans le source HTML
- [ ] Verifier les canonical tags
- [ ] Verifier que le sitemap XML est a jour
- [ ] Lancer un test PageSpeed Insights desktop/mobile

### 7.3 Documentation
- [ ] Mettre a jour dimonoff/STATUS.md avec les changements effectues
- [ ] Ajouter les mu-plugins crees dans le repo Git
- [ ] Commit + push sur GitHub

### 7.4 Suivi post-deploiement
- [ ] Soumettre les URLs modifiees a Google via GSC "Request indexing"
- [ ] Verifier les CWV dans 28 jours (CrUX data met 28 jours a se mettre a jour)
- [ ] Monitorer le CTR de /solutions/smart-lighting-control/ (objectif: passer de 0.1% a 2%+)
- [ ] Monitorer les 404 dans GSC (objectif: 0)

---

## Contraintes et Precautions

### Contraintes techniques connues (voir STATUS.md)
1. **elFinder stripslashes()**: ZERO backslash dans les fichiers PHP deployes via File Manager
2. **WAF HostGator**: Bloque `$_SERVER['REQUEST_URI']` dans les requetes PUT (pas en GET)
3. **Elementor cache**: Utiliser `files_manager->clear_cache()` pour purger
4. **Hummingbird**: Casse les compteurs Elementor — mu-plugin `dimonoff-counter-fix.php` deja en place
5. **The7 theme**: Ne PAS modifier le theme directement — utiliser mu-plugins uniquement

### Precautions de deploiement
- Deployer les mu-plugins UN PAR UN
- Verifier le site apres chaque mu-plugin
- Si erreur: supprimer immediatement le mu-plugin via File Manager
- Ne JAMAIS modifier Elementor page content (seulement Yoast meta)
- Toujours utiliser File Manager (pas Theme Editor) pour les mu-plugins

### Rollback plan
- Si un mu-plugin casse le site: le supprimer via File Manager
- Si les title tags causent un probleme: revenir aux titres precedents via Yoast
- Snapshot Pro backup disponible pour restauration complete

---

## Estimation des resultats attendus

| Metrique | Avant | Objectif 30j | Objectif 90j |
|----------|-------|-------------|-------------|
| CWV Desktop Poor | 237 | <100 | <20 |
| CWV Desktop Good | 0 | >50 | >200 |
| CTR moyen | 0.8% | 1.5% | 3%+ |
| CTR /smart-lighting-control/ | 0.1% | 1% | 3%+ |
| Pages 404 | 77 | 0 | 0 |
| Canonical duplicates | 81 | <20 | 0 |
| Position moyenne | 10.1 | 8 | 6 |
| Non-branded clicks | ~50/mois | 100/mois | 300/mois |
