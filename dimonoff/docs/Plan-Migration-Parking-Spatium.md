# Plan de migration du contenu Parking/Spatium
## De dimonoff.com vers spatium-iot.com

**Date :** 24 mars 2026
**Responsable :** Daniel Noiseux
**Groupe :** Vectanor (Dimonoff + Spatium)

---

## Contexte

Le groupe Vectanor possede deux verticales de marche :
- **Dimonoff** (dimonoff.com) : Eclairage intelligent, villes intelligentes, IoT
- **Spatium** (spatium-iot.com) : Gestion de stationnement intelligent

Le site dimonoff.com contient actuellement du contenu sur les deux verticales. Ce plan detaille le retrait progressif du contenu stationnement de dimonoff.com et sa migration vers spatium-iot.com, tout en maintenant le SEO et l'experience utilisateur.

---

## Phase 0 : Preparation (AVANT toute modification)

### 0.1 Backup complet
- [ ] Backup de la base de donnees WordPress (phpMyAdmin ou plugin)
- [ ] Backup des fichiers du site (wp-content, themes, plugins)
- [ ] Verifier que le backup est restaurable
- [ ] Installer les 9 mises a jour WordPress en attente (securite)

### 0.2 Audit du site spatium-iot.com
- [ ] Verifier la structure du site Spatium
- [ ] Identifier les pages equivalentes qui existent deja
- [ ] Planifier les URLs de destination pour les redirections

---

## Phase 1 : Corrections techniques immediates (non liees au parking)

### 1.1 Banniere de cookies
- **Probleme :** Variables de template non resolues ({vendor_count}, {title})
- **Action :** Corriger la configuration du plugin de consentement (probablement Complianz ou CookieYes)
- **Priorite :** Haute (visible par tous les visiteurs)

### 1.2 Image incorrecte article Naomih Dalpe
- **Probleme :** L'article "Naomih Dalpe Joins Dimonoff" affiche la photo de Brigitte Baril
- **Action :** Remplacer l'image dans WordPress Media Library
- **URL :** /news/naomih-dalpe-director-business-development-2/
- **Priorite :** Haute

### 1.3 Copyright footer
- **Probleme :** "Dimonoff inc. (c) 2025" (verifier si dynamique ou code en dur)
- **Action :** Mettre a jour pour 2026 si necessaire
- **Priorite :** Moyenne

### 1.4 Lien Twitter/X
- **Probleme :** Pointe vers twitter.com/dimonoffinc
- **Action :** Verifier si le compte est migre vers X, mettre a jour le lien
- **Priorite :** Basse

---

## Phase 2 : Modifications de la page d'accueil

### 2.1 Retirer la section "Parking Management System"
- **Localisation :** Section complete sur la page d'accueil (~1/3 de la page)
- **Contenu a retirer :**
  - Titre "Parking Management System"
  - 6 icones de fonctionnalites (IoT Platform, Sensors, Analytics, Payment, Barriers, Displays)
  - 3 boutons CTA (Smart Parking Solution, Private Indoor/Outdoor, Cities Street Curbside)
  - Image de fond associee
- **Remplacement suggere :** Ajouter un encart "Powered by Vectanor" avec lien vers spatium-iot.com
  Exemple : "Pour nos solutions de stationnement intelligent, visitez spatium-iot.com - une entreprise du groupe Vectanor"

### 2.2 Carrousel de nouvelles
- **Articles parking a retirer du carrousel :**
  - "Canadian Parking Association Conference in Vancouver"
- **Action :** Retirer de la selection du carrousel (pas de l'article lui-meme)

### 2.3 Carrousel d'etudes de cas
- **Etudes parking a retirer :**
  - "On-Street Parking Management System in Montreal"
  - "Mixed-Use Parking Operations"
  - "Smart Parking Innovation for Royalmount Shopping Mall"
- **Action :** Retirer de la selection du carrousel

### 2.4 Footer
- **Texte actuel :** "Dimonoff provides innovative IoT-based solutions for smart cities and smart parking..."
- **Action :** Retirer "and smart parking" et ajouter une mention Vectanor/Spatium

---

## Phase 3 : Navigation principale

### 3.1 Retirer l'item "PARKING" du menu principal (EN)
- **Localisation :** Menu principal, 2eme item de premier niveau
- **Sous-items a retirer :**
  - Tous les liens vers /solutions/mobility-smart-parking/...

### 3.2 Retirer l'item "STATIONNEMENT" du menu mobile (FR)
- **Meme structure a retirer en francais**

### 3.3 Retirer l'item "PARKING/ESTACIONAMIENTO" (ES)
- **Meme structure en espagnol**

### 3.4 Ajouter un lien vers Spatium
- **Suggestion :** Remplacer l'item de menu PARKING par un lien simple :
  "SPATIUM" -> https://www.spatium-iot.com (avec ouverture dans un nouvel onglet)
  Similaire a ce qui est deja fait pour "AMOTUS" -> https://amotus.com/

### 3.5 Nettoyer le menu Ressources
- **Retirer :** Le filtre "systeme-gestion-stationnement" (/fr/ressources/?term=systeme-gestion-stationnement)
- **Retirer :** L'etude de cas parking mise en vedette dans le mega-menu

### 3.6 Nettoyer le menu Nouvelles
- **Retirer :** Le filtre "mobilite" (/fr/nouvelles/?term=mobilite)

---

## Phase 4 : Pages statiques a depublier

### Pages parking EN (7 pages) :
| # | URL | Action |
|---|-----|--------|
| 1 | /solutions/mobility-smart-parking/ | Depublier + redirect 301 |
| 2 | /solutions/mobility-smart-parking/benefits-managers-users/ | Depublier + redirect 301 |
| 3 | /solutions/mobility-smart-parking/key-differentiators/ | Depublier + redirect 301 |
| 4 | /solutions/mobility-smart-parking/private/ | Depublier + redirect 301 |
| 5 | /solutions/mobility-smart-parking/curbside/ | Depublier + redirect 301 |
| 6 | /solutions/mobility-smart-parking/products/ | Depublier + redirect 301 |
| 7 | /solutions/smart-parking-management-system/faq/ | Depublier + redirect 301 |

### Pages parking FR (7 pages) :
| # | URL | Action |
|---|-----|--------|
| 1 | /fr/solutions/mobilite-stationnement-intelligent/ | Depublier + redirect 301 |
| 2 | /fr/solutions/mobilite-stationnement-intelligent/avantages-gestionnaires-utilisateurs/ | Depublier + redirect 301 |
| 3 | /fr/solutions/mobilite-stationnement-intelligent/differenciateurs-cles/ | Depublier + redirect 301 |
| 4 | /fr/solutions/mobilite-stationnement-intelligent/prive/ | Depublier + redirect 301 |
| 5 | /fr/solutions/mobilite-stationnement-intelligent/bordure-de-rue/ | Depublier + redirect 301 |
| 6 | /fr/solutions/mobilite-stationnement-intelligent/produits/ | Depublier + redirect 301 |
| 7 | /fr/solutions/mobilite-stationnement-intelligent/faq/ | Depublier + redirect 301 |

### Pages parking ES (7 pages) :
| # | URL | Action |
|---|-----|--------|
| 1 | /es/soluciones/movilidad-aparcamientos-inteligente/ | Depublier + redirect 301 |
| 2 | /es/soluciones/movilidad-aparcamientos-inteligente/beneficios-gestores-usuarios/ | Depublier + redirect 301 |
| 3 | /es/soluciones/movilidad-aparcamientos-inteligente/diferenciadores-clave/ | Depublier + redirect 301 |
| 4 | /es/soluciones/movilidad-aparcamientos-inteligente/privado/ | Depublier + redirect 301 |
| 5 | /es/soluciones/movilidad-aparcamientos-inteligente/en-acera-de-calle/ | Depublier + redirect 301 |
| 6 | /es/soluciones/movilidad-aparcamientos-inteligente/productos/ | Depublier + redirect 301 |
| 7 | /es/soluciones/movilidad-aparcamientos-inteligente/preguntas-frecuentes/ | Depublier + redirect 301 |

---

## Phase 5 : Etudes de cas parking a migrer

### EN (3 etudes) :
| Etude | URL Dimonoff | Destination Spatium |
|-------|-------------|-------------------|
| Quebec City Curbside | /resources/case-studies/quebec-city-smart-parking-management-system-street-curbside/ | A definir |
| Montreal On-Street | /resources/case-studies/on-street-parking-management-system-montreal/ | A definir |
| Royalmount Mall | /resources/case-studies/smart-parking-shopping-mall-operations-centralized-management-platform/ | A definir |

### FR (3 etudes) :
| Etude | URL Dimonoff |
|-------|-------------|
| Quebec ville stationnement | /fr/ressources/etudes-de-cas/quebec-ville-systeme-intelligent-stationnement-bordure-rue/ |
| Montreal stationnement | /fr/ressources/etudes-de-cas/systeme-gestion-stationnements-bordure-rue-montreal/ |
| Royalmount centre commercial | /fr/ressources/etudes-de-cas/stationnement-intelligent-centre-commercial-operations-plateforme-gestion-centralisee/ |

### ES (3 etudes) :
| Etude | URL Dimonoff |
|-------|-------------|
| Quebec aparcamiento | /es/recursos/estudios-de-caso/quebec-ciudad-sistema-inteligente-gestion-aparcamientos-de-calle/ |
| Montreal estacionamiento | /es/recursos/estudios-de-caso/sistema-gestion-estacionamientos-publicos-acera-de-calle-montreal/ |
| Royalmount centro comercial | /es/recursos/estudios-de-caso/aparcamiento-inteligente-centro-comercial-operaciones-plataforma-gestion-centralizada/ |

---

## Phase 6 : Articles de blog parking a migrer (~21 articles x 3 langues)

### Articles a traiter (EN - avec equivalents FR et ES) :

1. ROI Smart Parking System (/news/what-is-the-roi-for-a-smart-parking-system/)
2. Creating Tomorrow Smart Parking Experience (/news/creating-tomorrow-smart-parking-experience/)
3. Future of Parking (/news/comment-on-the-future-of-parking/)
4. Curbside Parking Scarcity (/news/solving-curbside-parking-scarcity-through-availability-information/)
5. ParkSmart Certification (/news/parksmart-certification-parking/)
6. Connected Parking LED Signs (/news/dimonoff-scms-integrated-orange-traffic-connected-parking-led-signs/)
7. Smart LED Signs Snow Removal (/news/smart-led-signs-snow-removal-st-augustin-de-desmaures/)
8. APDS Parking Data Standards (/news/apds-supporter-alliance-parking-data-standards/)
9. Canadian Parking Association 2021 (/news/canadian-parking-association-2021-conference-trade-show/)
10. Canadian Parking Association 2022 (/news/canadian-parking-association-conference-quebec-2022/)
11. Canadian Parking Association 2023 (/news/canadian-parking-association-conference-calgary-2023/)
12. Canadian Parking Association Vancouver 2025 (/news/canadian-parking-association-conference-vancouver-2025-2/)
13. IPMI Parking Mobility Fort Worth 2023 (/news/ipmi-parking-mobility-conference-fort-worth-2023/)
14. IPMI Parking Mobility Columbus 2024 (/news/ipmi-parking-mobility-columbus-ohio-2024/)
15. Comment rentabiliser investissement stationnement (FR seulement)

---

## Phase 7 : Ajouts et liens inter-sites

### 7.1 Page "A propos" / About Us
- [ ] Ajouter une mention du groupe Vectanor
- [ ] Mentionner que Spatium (spatium-iot.com) gere la verticale stationnement

### 7.2 Footer
- [ ] Ajouter un lien vers spatium-iot.com
- [ ] Mettre a jour la description pour mentionner le groupe Vectanor

### 7.3 Sitemap XML
- [ ] Regenerer le sitemap apres les depublications
- [ ] Verifier qu'aucune URL parking ne reste dans le sitemap

---

## Recommandation pour les redirections

**Methode recommandee : Plugin "Redirection" pour WordPress**

Raisons :
- Yoast SEO Premium est deja installe (on voit la barre admin SEO) et gere les redirections automatiques quand on change un slug
- Un plugin dedie comme Redirection permet de gerer facilement 60+ redirections
- Plus facile a maintenir que le .htaccess pour une equipe non technique
- Monitoring des 404 integre pour detecter les liens casses

**Structure des redirections 301 :**
- Toutes les pages /solutions/mobility-smart-parking/* -> https://www.spatium-iot.com/ (ou page equivalente)
- Tous les articles parking -> https://www.spatium-iot.com/blog/ (ou article equivalent si migre)
- Toutes les etudes de cas parking -> https://www.spatium-iot.com/case-studies/ (ou equivalent)

---

## Ordre d'execution recommande

1. **Backup complet** (Phase 0)
2. **Corrections techniques** (Phase 1) - independantes du parking
3. **Navigation** (Phase 3) - retirer les menus parking
4. **Page d'accueil** (Phase 2) - retirer la section parking
5. **Pages statiques** (Phase 4) - depublier + redirections
6. **Etudes de cas** (Phase 5) - migrer puis depublier
7. **Articles** (Phase 6) - migrer puis depublier
8. **Liens inter-sites** (Phase 7) - ajouter les ponts Vectanor
9. **Verification finale** - tester toutes les redirections et le sitemap
