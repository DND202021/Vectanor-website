# Phase 4.6: Cross-Links Strategy

## Overview

Strategic cross-linking between Groupe Vectanor's subsidiary websites (Dimonoff, Spatium, Amotus) improves:
- **SEO Authority**: Distributes domain authority across the group ecosystem
- **User Navigation**: Helps users discover related solutions and services
- **Topical Clustering**: Signals to search engines the relationships between subsidiaries
- **Brand Cohesion**: Reinforces the Groupe Vectanor ecosystem

## Website Ecosystem

| Website | Primary Focus | Key Pages |
|---------|---------------|-----------|
| **dimonoff.com** | Smart lighting, smart city solutions, IoT platforms (Quebec City) | /solutions/, /products/, /about/ |
| **spatium-iot.com** | Parking management solutions (included in Dimonoff SCMS) | /solutions/, /features/, /use-cases/ |
| **amotus.com** | IoT engineering, electronics design, embedded systems | /services/, /expertise/, /portfolio/ |

---

## Phase 1: Footer Cross-Links (Already Partially Implemented)

### Current State
- Amotus logo already appears in Dimonoff footer
- Footer links need to be formalized and expanded

### Strategy

#### Dimonoff Footer Links

**Column 1: Groupe Vectanor**
- EN: "Groupe Vectanor" → vectanor.com
- FR: "Groupe Vectanor" → vectanor.com
- ES: "Grupo Vectanor" → vectanor.com

**Column 2: Related Brands**
```
English (EN):
- Intelligent Parking (Spatium) → spatium-iot.com
- IoT Engineering (Amotus) → amotus.com

French (FR):
- Gestion du Stationnement Intelligent (Spatium) → spatium-iot.com
- Ingénierie IoT (Amotus) → amotus.com

Spanish (ES):
- Gestión Inteligente de Estacionamiento (Spatium) → spatium-iot.com
- Ingeniería IoT (Amotus) → amotus.com
```

#### Spatium Footer Links

**Column 1: Groupe Vectanor**
- EN: "Groupe Vectanor" → vectanor.com
- FR: "Groupe Vectanor" → vectanor.com
- ES: "Grupo Vectanor" → vectanor.com

**Column 2: Related Brands**
```
English (EN):
- Smart City Solutions (Dimonoff) → dimonoff.com
- IoT Engineering (Amotus) → amotus.com

French (FR):
- Solutions de Villes Intelligentes (Dimonoff) → dimonoff.com
- Ingénierie IoT (Amotus) → amotus.com

Spanish (ES):
- Soluciones de Ciudades Inteligentes (Dimonoff) → dimonoff.com
- Ingeniería IoT (Amotus) → amotus.com
```

#### Amotus Footer Links

**Column 1: Groupe Vectanor**
- EN: "Groupe Vectanor" → vectanor.com
- FR: "Groupe Vectanor" → vectanor.com
- ES: "Grupo Vectanor" → vectanor.com

**Column 2: Related Brands**
```
English (EN):
- Smart City Solutions (Dimonoff) → dimonoff.com
- Parking Management (Spatium) → spatium-iot.com

French (FR):
- Solutions de Villes Intelligentes (Dimonoff) → dimonoff.com
- Gestion du Stationnement (Spatium) → spatium-iot.com

Spanish (ES):
- Soluciones de Ciudades Inteligentes (Dimonoff) → dimonoff.com
- Gestión de Estacionamiento (Spatium) → spatium-iot.com
```

### Implementation Notes
- **Location**: Footer widgets (WordPress widget area or Elementor footer template)
- **Design**: Subtle text links (not logo/image links - improves crawlability)
- **No Follow**: Use `rel="nofollow"` for footer links (standard practice - these are navigational, not editorial votes)
- **Spacing**: One link per line, clear visual hierarchy

---

## Phase 2: Solution/Service Page Cross-Links

### Dimonoff → Spatium

#### Smart Parking Page (`/solutions/smart-parking/`)

**Context**: Parking is part of Dimonoff's SCMS but also a standalone Spatium solution.

**Link Placement**: In content or "Related Solutions" section

```
EN: "Spatium offers dedicated intelligent parking management features within and beyond SCMS.
    Learn more about Spatium's advanced occupancy optimization and dynamic pricing."
    Anchor: "Spatium's advanced occupancy optimization" → spatium-iot.com

FR: "Spatium propose des fonctionnalités avancées de gestion du stationnement intelligent.
    En savoir plus sur l'optimisation des occupations et la tarification dynamique de Spatium."
    Anchor: "l'optimisation des occupations de Spatium" → spatium-iot.com

ES: "Spatium ofrece características dedicadas de gestión inteligente de estacionamiento.
    Obtenga más información sobre la optimización de ocupación y los precios dinámicos de Spatium."
    Anchor: "la optimización de ocupación de Spatium" → spatium-iot.com
```

**Anchor Text Variants** (use variety for natural linking):
- EN: "Spatium parking solutions", "intelligent parking platform", "parking management system"
- FR: "solutions de stationnement Spatium", "plateforme de gestion du stationnement", "système de gestion du parking"
- ES: "soluciones de estacionamiento de Spatium", "plataforma de gestión de estacionamiento", "sistema de gestión de aparcamiento"

---

### Dimonoff → Amotus

#### Products Page (`/products/`) or LED Controllers

**Context**: Amotus handles design and engineering of Dimonoff's LED controllers and gateways.

**Link Placement**: In product description or "About These Components" section

```
EN: "Dimonoff LED controllers and Gateway G3+ are engineered by Amotus, our advanced IoT
    electronics and embedded systems partner."
    Anchor: "engineered by Amotus" → amotus.com

FR: "Les contrôleurs LED et la passerelle G3+ de Dimonoff sont conçus par Amotus, notre
    partenaire spécialisé en systèmes embarqués et électronique IoT avancée."
    Anchor: "conçus par Amotus" → amotus.com

ES: "Los controladores LED y la puerta de enlace G3+ de Dimonoff están diseñados por Amotus,
    nuestro socio especializado en sistemas embebidos y electrónica IoT avanzada."
    Anchor: "diseñados por Amotus" → amotus.com
```

**Anchor Text Variants**:
- EN: "Amotus IoT engineering", "engineered by Amotus", "Amotus electronics design"
- FR: "Ingénierie IoT d'Amotus", "conçus par Amotus", "conception électronique d'Amotus"
- ES: "Ingeniería IoT de Amotus", "diseñados por Amotus", "diseño electrónico de Amotus"

---

### Spatium → Dimonoff

#### Solutions Page or Features Page

**Context**: Spatium integrates with Dimonoff's SCMS as part of the broader smart city platform.

**Link Placement**: In overview or "Integrated Solutions" section

```
EN: "Spatium integrates seamlessly with Dimonoff's Smart City Management System (SCMS)
    for unified control of parking, lighting, security, and environmental monitoring."
    Anchor: "Dimonoff's Smart City Management System" → dimonoff.com/solutions/

FR: "Spatium s'intègre parfaitement au Système de Gestion des Villes Intelligentes (SCMS)
    de Dimonoff pour un contrôle unifié du stationnement, de l'éclairage et de la sécurité."
    Anchor: "Système de Gestion des Villes Intelligentes de Dimonoff" → dimonoff.com/solutions/

ES: "Spatium se integra perfectamente con el Sistema de Gestión de Ciudades Inteligentes (SCMS)
    de Dimonoff para el control unificado del estacionamiento, iluminación y seguridad."
    Anchor: "Sistema de Gestión de Ciudades Inteligentes de Dimonoff" → dimonoff.com/solutions/
```

**Anchor Text Variants**:
- EN: "Dimonoff SCMS", "Dimonoff smart city solutions", "Dimonoff platform"
- FR: "SCMS de Dimonoff", "solutions de villes intelligentes de Dimonoff", "plateforme Dimonoff"
- ES: "SCMS de Dimonoff", "soluciones de ciudades inteligentes de Dimonoff", "plataforma Dimonoff"

---

### Amotus → Dimonoff

#### Portfolio or Services Page

**Context**: Amotus has worked on Dimonoff's IoT controllers and gateways as a case study.

**Link Placement**: In portfolio section or case study

```
EN: "We designed and engineered IoT controllers and gateway systems for Dimonoff's smart
    city platform, enabling reliable data aggregation and edge computing."
    Anchor: "Dimonoff's smart city platform" → dimonoff.com

FR: "Nous avons conçu et développé les contrôleurs IoT et les systèmes de passerelle pour
    la plateforme de villes intelligentes de Dimonoff."
    Anchor: "plateforme de villes intelligentes de Dimonoff" → dimonoff.com

ES: "Diseñamos e ingeniería los controladores IoT y sistemas de puerta de enlace para la
    plataforma de ciudades inteligentes de Dimonoff."
    Anchor: "plataforma de ciudades inteligentes de Dimonoff" → dimonoff.com
```

**Anchor Text Variants**:
- EN: "Dimonoff", "Dimonoff smart city solutions", "Dimonoff IoT platform"
- FR: "Dimonoff", "solutions de villes intelligentes de Dimonoff", "plateforme IoT de Dimonoff"
- ES: "Dimonoff", "soluciones de ciudades inteligentes de Dimonoff", "plataforma IoT de Dimonoff"

---

## Phase 3: About/Company Pages

### Dimonoff About Page

**Section**: "Part of Groupe Vectanor"

```
EN: "Dimonoff is part of Groupe Vectanor, a leading IoT and smart infrastructure group.
    Our ecosystem includes:

    - Spatium: Intelligent parking management integrated with SCMS
    - Amotus: Advanced IoT engineering and electronics design
    - Vigilia: Critical infrastructure monitoring

    Together, we deliver comprehensive smart city solutions across North America."

FR: "Dimonoff fait partie du Groupe Vectanor, un groupe leader en IoT et infrastructure intelligente.
    Notre écosystème comprend:

    - Spatium: Gestion du stationnement intelligent intégrée à SCMS
    - Amotus: Ingénierie avancée et conception électronique IoT
    - Vigilia: Surveillance des infrastructures critiques

    Ensemble, nous proposons des solutions complètes de villes intelligentes."

ES: "Dimonoff es parte del Grupo Vectanor, un grupo líder en IoT e infraestructura inteligente.
    Nuestro ecosistema incluye:

    - Spatium: Gestión inteligente de estacionamiento integrada con SCMS
    - Amotus: Ingeniería IoT avanzada y diseño electrónico
    - Vigilia: Monitoreo de infraestructura crítica

    Juntos, ofrecemos soluciones completes de ciudades inteligentes."
```

**Internal Links**:
- "Groupe Vectanor" → vectanor.com
- "Spatium" → spatium-iot.com
- "Amotus" → amotus.com

---

### Spatium About Page

**Section**: "Part of Groupe Vectanor"

```
EN: "Spatium is part of Groupe Vectanor and works closely with Dimonoff to deliver
    integrated smart city solutions. Spatium parking management features are available
    as part of Dimonoff's Smart City Management System (SCMS)."

FR: "Spatium fait partie du Groupe Vectanor et travaille en étroite collaboration avec
    Dimonoff pour fournir des solutions de villes intelligentes intégrées. Les fonctionnalités
    de gestion du stationnement de Spatium sont disponibles dans le SCMS de Dimonoff."

ES: "Spatium es parte del Grupo Vectanor y trabaja estrechamente con Dimonoff para
    proporcionar soluciones integradas de ciudades inteligentes."
```

**Internal Links**:
- "Groupe Vectanor" → vectanor.com
- "Dimonoff" → dimonoff.com
- "SCMS" → dimonoff.com/solutions/

---

### Amotus About Page

**Section**: "Our Partnerships & Clients"

```
EN: "Amotus has engineered advanced IoT solutions for Groupe Vectanor subsidiaries,
    including Dimonoff's LED controllers and gateway systems. Our expertise in embedded
    systems and electronics design powers mission-critical smart city infrastructure."

FR: "Amotus a conçu des solutions IoT avancées pour les filiales du Groupe Vectanor,
    notamment les contrôleurs LED et les systèmes de passerelle de Dimonoff."

ES: "Amotus ha diseñado soluciones IoT avanzadas para las subsidiarias del Grupo Vectanor,
    incluidos los controladores LED y sistemas de puerta de enlace de Dimonoff."
```

**Internal Links**:
- "Groupe Vectanor" → vectanor.com
- "Dimonoff" → dimonoff.com

---

## Phase 4: Cross-Link Implementation Approach

### Option A: Elementor Widget (Recommended for Non-Developers)

**Pros**:
- No code required
- Easy to update
- Visual editing
- Works well with Polylang

**Steps**:
1. Create Elementor templates for cross-link sections
2. Add custom text/link widgets to solution pages
3. Duplicate and translate for each language
4. Test links and anchor text readability

### Option B: WordPress Mu-Plugin (Recommended for Developers)

**Pros**:
- Centralized management
- Consistent formatting
- Easy to add/update links programmatically
- Avoids duplication

**Cons**:
- Requires PHP knowledge
- Needs testing

**Approach**:
```php
Create: mu-plugins/vectanor-cross-links.php

Function: Inject cross-links via hooks
- Hook into page content at specific locations
- Check page/solution type
- Output appropriate language-specific links
- Use wp_kses_post() for security
```

### Option C: Hybrid (Best Practice)

- **Footer**: Elementor widget (easy to maintain)
- **Content links**: Mu-plugin (automated, scalable)
- **About pages**: Manual Elementor links (one-time setup)

---

## SEO Best Practices for Cross-Links

### Anchor Text Guidelines

1. **Use Descriptive Text** (not "click here")
   - Good: "Dimonoff Smart City Management System"
   - Bad: "click here for more info"

2. **Avoid Keyword Stuffing**
   - Natural language is key
   - Vary anchor text across pages (not all identical)
   - Match user intent

3. **Multilingual Consistency**
   - Translate meaningfully, not literally
   - Use industry standard terms in each language
   - Ensure consistency across all pages

### Link Velocity & Frequency

- **Distribute over time**: Add links gradually, not all at once
- **One link per page**: Generally, one to three cross-links per page is natural
- **Contextual**: Links should relate to page content

### Internal Link Hierarchy

```
Primary (IMPORTANT):
- Footer links from every page
- Solution page cross-links
- About page links

Secondary:
- Blog post mentions (if applicable)
- Product detail cross-references
```

### Nofollow vs. Dofollow

```
DOFOLLOW (Pass authority):
- Solution/product page links
- About page links
- Contextual content links

NOFOLLOW (Optional - navigation):
- Footer navigation links
- Related/suggested links
- Non-editorial links
```

**Recommendation**: Use dofollow for Phase 2 & 3 links (editorial content), nofollow for Phase 1 footer links (navigation).

---

## Link Priority Matrix

### HIGH PRIORITY (Immediate)

| From | To | Page | Anchor Text (EN) | Type |
|------|-----|------|------------------|------|
| Dimonoff | Spatium | /solutions/smart-parking/ | Spatium's advanced occupancy optimization | dofollow |
| Spatium | Dimonoff | /solutions/ | Dimonoff's Smart City Management System | dofollow |
| Dimonoff | Amotus | /products/ | engineered by Amotus | dofollow |
| All | All | Footer | Brand name links | nofollow |

### MEDIUM PRIORITY (Weeks 2-3)

| From | To | Page | Anchor Text (EN) | Type |
|------|-----|------|------------------|------|
| Dimonoff | Vectanor | /about/ | Groupe Vectanor | dofollow |
| Spatium | Vectanor | /about/ | Groupe Vectanor | dofollow |
| Amotus | Vectanor | /about/ | Groupe Vectanor | dofollow |

### LOW PRIORITY (Weeks 4+)

| From | To | Page | Anchor Text (EN) | Type |
|------|-----|------|------------------|------|
| Amotus | Dimonoff | /portfolio/ or /services/ | Dimonoff smart city platform | dofollow |
| Amotus | Spatium | /portfolio/ or /services/ | Spatium parking management | dofollow |

---

## Monitoring & Reporting

### Metrics to Track

1. **Link Coverage**: % of pages linking to ecosystem sites
2. **Crawl**: Monitor via GSC - ensure all links crawlable
3. **CTR**: Click-through rate from cross-links
4. **Rankings**: Monitor keyword rankings for cross-linked pages
5. **Authority Flow**: Track domain authority distribution

### Tools
- Google Search Console: Monitor internal links, crawl errors
- Google Analytics: Track referral traffic between sites
- Ahrefs/SEMrush: Monitor backlink changes and authority flow

### Review Schedule
- Month 1: Check link implementation and crawlability
- Month 3: Review traffic and engagement metrics
- Quarter 2: Optimize anchor text and high-priority links based on data

---

## Implementation Checklist

### Phase 1: Footer (Week 1)
- [ ] Design footer link sections in Elementor
- [ ] Add Spatium link to Dimonoff footer
- [ ] Add Dimonoff & Amotus links to Spatium footer
- [ ] Add Dimonoff & Spatium links to Amotus footer
- [ ] Translate footer links (FR, ES)
- [ ] Test links on all devices
- [ ] Verify links are crawlable

### Phase 2: Solution Pages (Weeks 2-3)
- [ ] Add Spatium link to Dimonoff /solutions/smart-parking/
- [ ] Add Dimonoff link to Spatium /solutions/
- [ ] Add Amotus link to Dimonoff /products/
- [ ] Create translated versions (FR, ES)
- [ ] Test link placement and readability
- [ ] Verify anchor text variation

### Phase 3: About Pages (Weeks 3-4)
- [ ] Update Dimonoff /about/ with Groupe Vectanor section
- [ ] Update Spatium /about/ with Groupe Vectanor section
- [ ] Update Amotus /about/ with partnership section
- [ ] Add all links (Vectanor, Dimonoff, Spatium, Amotus)
- [ ] Translate about sections (FR, ES)

### Phase 4: Testing & Monitoring (Week 4+)
- [ ] Submit site maps to GSC
- [ ] Check Google crawl of all links
- [ ] Monitor 404 errors
- [ ] Check CTR in GSC
- [ ] Set up GA goals for cross-site navigation
- [ ] Monthly review of rankings and traffic

---

## Recommendations Summary

1. **Start with footer**: Low effort, high visibility
2. **Focus on solution pages**: Most contextually relevant
3. **Use dofollow**: These are editorial links, pass authority
4. **Vary anchor text**: Natural linking patterns
5. **Monitor closely**: Ensure no negative impact on rankings
6. **Plan for future**: Consider Vigilia & Stratys integration later
