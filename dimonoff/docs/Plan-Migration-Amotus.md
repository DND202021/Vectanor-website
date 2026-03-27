# Plan de migration — Retrait du contenu Amotus de dimonoff.com

**Date:** 2026-03-26
**Objectif:** Recentrer dimonoff.com sur l'éclairage intelligent et les villes intelligentes. Le contenu Amotus détaillé doit vivre sur amotus.com, avec seulement des mentions légères et des cross-links sur dimonoff.com.
**Principe directeur:** Chaque division du Groupe Vectanor a son propre site avec l'information qui lui est rattachée.

---

## 1. Inventaire du contenu Amotus actuel

### 1.1 Menu de navigation principal (Max Mega Menu)

| Élément | Langue | Contenu actuel | Impact |
|---------|--------|----------------|--------|
| Item "AMOTUS" dans mega menu | EN | Lien vers amotus.com + logo + sous-items (Amotus - IoT Design House Services, Fundamentum – IoT PaaS) | **Les liens pointent déjà vers amotus.com** — à évaluer si on garde l'entrée de menu ou on la retire |
| Item "AMOTUS" dans mega menu | FR | Liens vers amotus.com/fr/ + sous-items FR | Idem |

### 1.2 Page Solutions (EN: ID 24 / FR: ID 4950 / ES: ID 74278)

| Widget ID | Type | Contenu | Action proposée |
|-----------|------|---------|-----------------|
| `bb12bf7` | text-editor | Paragraphe descriptif d'Amotus (~2 phrases détaillées) | **Réduire** à 1 phrase + lien vers amotus.com |
| `4dac93c` | image | Logo Amotus avec lien vers amotus.com | **Garder** (cross-link léger) |
| `4e741e1` | menu-anchor | Ancre `#amotus-services` | **Renommer** ou retirer selon la décision sur la section |
| Widget footer Vectanor | html | Barre "Groupe Vectanor" avec logos Dimonoff, Spatium, Amotus, Vigilia | **Garder** (présentation du groupe, pas du contenu détaillé) |

### 1.3 Page About / À propos / Sobre nosotros

#### EN (ID 60677)
| Widget ID | Type | Contenu | Action proposée |
|-----------|------|---------|-----------------|
| `9792c1c` | text-editor | Paragraphe complet sur Amotus + Fundamentum PaaS | **Remplacer** par mention courte + lien |
| `c836e51` | text-editor | Section Groupe Vectanor mentionnant Amotus comme société sœur | **Garder** (mention légitime dans le contexte du groupe) |

#### FR (ID 60677 — même page, widgets différents)
| Widget ID | Type | Contenu | Action proposée |
|-----------|------|---------|-----------------|
| `9a8ae50` | text-editor | Paragraphe complet Amotus + Fundamentum (FR) | **Remplacer** par mention courte + lien |
| `8167085` | text-editor | Section Groupe Vectanor mentionnant Amotus (FR) | **Garder** |

#### ES (ID 74215)
| Widget ID | Type | Contenu | Action proposée |
|-----------|------|---------|-----------------|
| `8e9cc3d` | text-editor | Paragraphe complet Amotus + Fundamentum (ES) | **Remplacer** par mention courte + lien |
| `c719333` | text-editor | Section Groupe Vectanor mentionnant Amotus (ES) | **Garder** |

### 1.4 Page Services (ID 80440) — LE GROS MORCEAU

| Widget ID | Type | Contenu | Action proposée |
|-----------|------|---------|-----------------|
| `7b6aa41` | heading | "AMOTUS: EXTENDING OUR IMPACT" | **Retirer** toute la section |
| `d49f8a8` | image-box | Historique: acquisition 2018, fusion 2021 | **Retirer** |
| `9d4e034` | image-box | Relancement Amotus, expansion industrielle | **Retirer** |
| `0e77e80` | text-editor | Description des services Amotus (design électronique, software) | **Retirer** |
| `6ef4f50` | ? | Contenu additionnel Amotus | **Retirer** |
| `f255dbe` | nav-menu | Menu latéral: Overview, Embedded Systems, Fundamentum, Custom IoT (liens vers amotus.com) | **Retirer** ou remplacer par un lien unique vers amotus.com |

### 1.5 Page d'accueil / Homepage

| Élément | Contenu | Action proposée |
|---------|---------|-----------------|
| Widget `bb12bf7` | Paragraphe descriptif Amotus (partagé avec Solutions) | **Réduire** à 1 phrase + lien |
| Widget footer Vectanor | Barre logos du groupe | **Garder** |

### 1.6 Footer (global)

| Élément | Contenu | Action proposée |
|---------|---------|-----------------|
| Lien Amotus + logo | Lien vers amotus.com dans le footer | **Garder** (cross-link léger, normal pour un groupe d'entreprises) |

### 1.7 Articles de presse / News

| URL | Titre | Action proposée |
|-----|-------|-----------------|
| `/news/dimonoff-and-amotus-announce-their-strategic-merger/` | Annonce de la fusion (2023) | **Garder** — historique corporatif |
| `/news/dimonoff-unveils-expanded-amotus-division.../` | Expansion division Amotus (2024) | **Garder** — historique corporatif |
| `/news/strategic-investment-dimonoff-smart-city-expansion.../` | Investissement $6M via Fundamentum (2025) | **Garder** — historique corporatif |
| `/news/amotus-and-omron-collaboration.../` | Partenariat Amotus-Omron | **Garder** — historique corporatif |

### 1.8 Redirections existantes

| URL | Destination | Statut |
|-----|-------------|--------|
| `/services/fundamentum-iot-platform-paas/` | amotus.com/solutions/fundamentum-iot-platform-paas/ | 301 déjà en place |
| `/es/servicios/fundamentum-iot-plataforma-paas/` | amotus.com/solutions/fundamentum-iot-platform-paas/ | 301 déjà en place |

---

## 2. Audit croisé — Couverture sur amotus.com

### 2.1 Ce qu'amotus.com couvre DÉJÀ bien

| Contenu à retirer de dimonoff.com | Présent sur amotus.com? | Détails |
|-------------------------------------|------------------------|---------|
| Services IoT engineering (design électronique, software) | ✅ OUI | Page d'accueil + Expertise (6 sous-pages: Hardware, Firmware, Embedded OS, Software, Cloud, Connectivity) |
| Fundamentum PaaS | ✅ OUI | Page dédiée complète: `/solutions/fundamentum-iot-platform-paas/` avec détails (Edge, Connect, Core, ML/AI, Insights, DevSecOps) |
| Historique / About Amotus | ✅ OUI | Page About Us: "Since 2013, Amotus has been providing engineering services..." + mention "Amotus is a Dimonoff division" |
| Custom IoT Solutions | ✅ OUI | Section dédiée + lien dans la navigation |
| Industries servies | ✅ OUI | Energy, Healthcare, Transportation, Consumer Electronics, Smart Buildings, Industrial, Smart Cities, AgTech |
| Lien vers Dimonoff | ✅ OUI | "Amotus is a Dimonoff division" sur la page About |
| Version française | ✅ OUI | `/fr/` — contenu FR complet (conception, logiciel, infonuagique) |
| Case studies / Resources | ✅ OUI | Section Resource Center: News, Case Studies, Testimonials, White Papers, Videos |

### 2.2 LACUNES identifiées sur amotus.com

| Contenu | Présent? | Impact | Action requise |
|---------|----------|--------|----------------|
| **Version espagnole** | ❌ NON | **IMPORTANT** — dimonoff.com a du contenu Amotus en ES qu'on retire, mais amotus.com n'a pas de version ES | **À discuter** : faut-il créer une version ES sur amotus.com avant de retirer le contenu ES de dimonoff.com? |
| Mention du Groupe Vectanor | ❌ NON | Faible — le contexte groupe n'est pas le rôle d'amotus.com | Aucune (on garde la mention Vectanor sur dimonoff.com) |
| Historique acquisition 2018 / fusion 2021 | ❌ NON | Faible — c'est de l'historique corporatif, pas du contenu client | Aucune (on garde les articles de presse sur dimonoff.com) |
| Expansion industrielle 2024 | ❌ NON | Faible — couvert indirectement par les industries listées | Aucune |

### 2.3 Conclusion de l'audit croisé

**Bonne nouvelle :** Le contenu détaillé sur les services, Fundamentum, et l'expertise technique est déjà très bien couvert sur amotus.com — il est même plus complet que sur dimonoff.com. La migration peut donc se faire en toute confiance pour les versions EN et FR.

**Point d'attention :** La **version espagnole** est la seule lacune significative. Amotus.com existe en EN et FR mais pas en ES. Deux options :
1. **Option A** — On retire quand même le contenu ES de dimonoff.com et on met un lien vers amotus.com (EN). Les visiteurs hispanophones verront le contenu en anglais.
2. **Option B** — On attend que amotus.com ait une version ES avant de retirer le contenu ES de dimonoff.com.
3. **Option C** — On garde une mention un peu plus substantielle en ES sur dimonoff.com (plus qu'une phrase, moins que le paragraphe actuel), en attendant la version ES d'amotus.com.

---

## 3. Résumé des actions

### Ce qui PART (contenu détaillé → déjà couvert sur amotus.com) (contenu détaillé à retirer)

1. **Page Services** — Section complète Amotus (heading, historique, description des services, menu latéral) → ~6 widgets
2. **Pages About (EN/FR/ES)** — Paragraphes détaillés sur Amotus/Fundamentum → 3 widgets (1 par langue)
3. **Pages Solutions (EN/FR/ES)** — Paragraphes descriptifs détaillés → 3 widgets (réduire, pas supprimer)
4. **Homepage** — Paragraphe descriptif → 1 widget (réduire)

### Ce qui RESTE (mentions légères + cross-links)

1. **Menu de navigation** — Entrée "AMOTUS" avec lien vers amotus.com (à simplifier si souhaité)
2. **Barre Groupe Vectanor** — Logo Amotus dans la barre des divisions (footer/bas de page)
3. **Footer** — Lien vers amotus.com
4. **Pages About** — Mention d'Amotus dans la section "Groupe Vectanor" (contexte légitime)
5. **Articles de presse** — Tous conservés (historique corporatif)
6. **Redirections 301** — Fundamentum déjà redirigé

### Ce qui est REMPLACÉ (contenu actuel → nouveau contenu allégé)

Pour les pages Solutions, About et Homepage, le paragraphe détaillé sur Amotus sera remplacé par une formule courte du type :

- **EN:** "Amotus, our sister company, specializes in IoT engineering and platform services. [Visit amotus.com →]"
- **FR:** "Amotus, notre société sœur, se spécialise en ingénierie IoT et services de plateforme. [Visitez amotus.com →]"
- **ES:** "Amotus, nuestra empresa hermana, se especializa en ingeniería IoT y servicios de plataforma. [Visite amotus.com →]"

---

## 4. Décisions de Daniel (2026-03-26)

| Question | Décision |
|----------|----------|
| Version espagnole (ES) | **Attendre amotus.com/es/** — On ne touche pas au contenu ES tant que amotus.com n'a pas de version espagnole |
| Mega menu | **Simplifier** — Garder un seul lien "Amotus" vers amotus.com, retirer les sous-items (Fundamentum, IoT Design House) |
| Page Services | **Réduire significativement** — Garder la section mais couper l'historique et le menu latéral. Reste: 1 paragraphe + logo + lien |
| Articles de presse | **Tout garder** — Historique corporatif |
| Barre Vectanor + footer | **Tout garder** — Identité de groupe |

---

## 5. Plan d'exécution par phases (révisé selon décisions)

### Phase 1 — Page Services EN/FR (priorité haute, plus gros changement)
- **Risque:** Moyen — réduction importante de contenu
- **Méthode:** Elementor visual editor via Chrome
- **Actions:**
  - Retirer le heading "AMOTUS: EXTENDING OUR IMPACT" (`7b6aa41`)
  - Retirer les image-boxes d'historique (`d49f8a8`, `9d4e034`)
  - Retirer le menu latéral Amotus (`f255dbe`)
  - **Garder** 1 paragraphe de description allégé (`0e77e80`) → réduire à ~2 phrases + lien amotus.com
  - **Garder** le logo Amotus comme cross-link visuel
  - Appliquer sur EN et FR (pas ES — on attend amotus.com/es/)

### Phase 2 — Pages About EN/FR
- **Risque:** Faible — remplacement de texte dans widgets existants
- **Méthode:** Elementor JS API (déjà éprouvée)
- **Actions:**
  - EN widget `9792c1c`: remplacer paragraphe détaillé Amotus/Fundamentum par mention courte + lien
  - FR widget `9a8ae50`: idem en français
  - ES widget `8e9cc3d`: **NE PAS TOUCHER** (on attend amotus.com/es/)
  - Garder les sections Groupe Vectanor intactes (`c836e51`, `8167085`, `c719333`)

### Phase 3 — Pages Solutions + Homepage EN/FR
- **Risque:** Faible — réduction de texte
- **Méthode:** Elementor JS API
- **Actions:**
  - Widget `bb12bf7`: réduire le paragraphe descriptif Amotus à 1 phrase + lien
  - Widget `4dac93c`: garder le logo + lien (cross-reference)
  - Appliquer sur EN et FR (pas ES)

### Phase 4 — Menu de navigation (Mega Menu)
- **Risque:** Moyen — le mega menu est global, affecte toutes les pages
- **Méthode:** Max Mega Menu dans WordPress admin
- **Actions:**
  - Simplifier l'entrée AMOTUS: garder un seul lien vers amotus.com
  - Retirer les sous-items: "IoT Design House Services", "Fundamentum – IoT PaaS"
  - Appliquer pour EN et FR

### Phase 5 — Validation
- Vérifier toutes les pages modifiées en EN et FR
- Confirmer que le contenu ES est intact (non modifié)
- Tester tous les liens vers amotus.com
- Vérifier que le SEO (hreflang, meta, schema) n'est pas impacté
- Vérifier le mega menu sur plusieurs pages

---

## 6. Hors périmètre (à faire plus tard)

- Contenu ES sur dimonoff.com → à migrer quand amotus.com/es/ sera disponible
- Création de amotus.com/es/ → projet séparé, responsabilité équipe Amotus
