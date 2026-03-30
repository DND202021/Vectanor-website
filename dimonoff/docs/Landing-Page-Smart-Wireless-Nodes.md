# Landing Page — Next-Generation Smart Wireless Lighting Nodes

> **Status:** DRAFT v1 — Ready for review
> **Date:** 2026-03-30
> **Author:** Daniel Noiseux / Dimonoff Marketing
> **Target pages:** dimonoff.com/solutions/smart-lighting-control/wireless-nodes/ (EN), /fr/ equivalent (FR)
> **Audience:** Utility decision-makers, municipal procurement, public works directors
> **Positioning:** Wi-SUN-ready, vendor-lock-in-free, utility-grade

---

## SEO / Schema / Meta Implementation Notes

### Meta Tags (EN page)

```html
<title>Smart Wireless Lighting Nodes | Wi-SUN Ready | Utility Grade | Dimonoff</title>
<meta name="description" content="Next-generation RME, RTM and LNLV smart wireless lighting nodes by Dimonoff. Wi-SUN FAN ready, ANSI C136.41 certified, Zhaga Book 18 compatible. No vendor lock-in. Trusted by 500+ cities.">
<meta name="keywords" content="smart wireless lighting node, RME controller, street lighting controller, Wi-SUN FAN, ANSI C136.41, Zhaga Book 18, utility grade, smart street lighting, IoT controller, LoRaWAN, NB-IoT, LTE-M, vendor lock-in free, municipal lighting">
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
<link rel="canonical" href="https://www.dimonoff.com/solutions/smart-lighting-control/wireless-nodes/">
```

### Meta Tags (FR page)

```html
<title>Noeuds Intelligents Eclairage de Rue | Wi-SUN | Grade Utilite | Dimonoff</title>
<meta name="description" content="Noeuds intelligents RME, RTM et LNLV de nouvelle generation par Dimonoff. Compatible Wi-SUN FAN, certifie ANSI C136.41, Zhaga Book 18. Sans dependance fournisseur. 500+ villes font confiance.">
<link rel="canonical" href="https://www.dimonoff.com/fr/solutions/controle-eclairage-intelligent/noeuds-sans-fil/">
<link rel="alternate" hreflang="en" href="https://www.dimonoff.com/solutions/smart-lighting-control/wireless-nodes/">
<link rel="alternate" hreflang="fr" href="https://www.dimonoff.com/fr/solutions/controle-eclairage-intelligent/noeuds-sans-fil/">
```

### JSON-LD Structured Data (Product schema)

```json
{
  "@context": "https://schema.org",
  "@type": "ProductGroup",
  "name": "Smart Wireless Lighting Nodes",
  "description": "Next-generation smart wireless lighting controllers for municipal street lighting. Wi-SUN FAN ready, ANSI C136.41 certified, multi-protocol connectivity.",
  "brand": {
    "@type": "Brand",
    "name": "Dimonoff"
  },
  "manufacturer": {
    "@type": "Organization",
    "name": "Dimonoff",
    "url": "https://www.dimonoff.com"
  },
  "hasVariant": [
    {
      "@type": "Product",
      "name": "RME Smart Wireless Lighting Node",
      "description": "External smart controller for retrofit street lighting. Plugs into any ANSI C136.41 or Zhaga Book 18 photocell receptacle. Compatible with LED, HPS, MH and MV fixtures.",
      "category": "Smart Lighting Controller",
      "additionalProperty": [
        { "@type": "PropertyValue", "name": "Controller Type", "value": "External (retrofit)" },
        { "@type": "PropertyValue", "name": "Connectivity", "value": "DigiMesh, LTE-M, NB-IoT, LoRaWAN, Wi-SUN FAN (coming)" },
        { "@type": "PropertyValue", "name": "Certification", "value": "ANSI C136.41, Zhaga Book 18" },
        { "@type": "PropertyValue", "name": "Fixture Compatibility", "value": "LED, HPS, MH, MV" }
      ]
    },
    {
      "@type": "Product",
      "name": "RTM Smart Wireless Lighting Node",
      "description": "Internal smart controller for decorative and architectural lighting with RGBW capability and analog/digital I/O.",
      "category": "Smart Lighting Controller",
      "additionalProperty": [
        { "@type": "PropertyValue", "name": "Controller Type", "value": "Internal (embedded)" },
        { "@type": "PropertyValue", "name": "Special Feature", "value": "RGBW architectural lighting" },
        { "@type": "PropertyValue", "name": "I/O", "value": "Analog and digital input/output" }
      ]
    },
    {
      "@type": "Product",
      "name": "LNLV Smart Wireless Lighting Node",
      "description": "Low-voltage smart wireless node for solar-powered and low-voltage lighting applications.",
      "category": "Smart Lighting Controller",
      "additionalProperty": [
        { "@type": "PropertyValue", "name": "Controller Type", "value": "Low-voltage" },
        { "@type": "PropertyValue", "name": "Application", "value": "Solar-powered and low-voltage systems" }
      ]
    }
  ],
  "offers": {
    "@type": "Offer",
    "availability": "https://schema.org/InStock",
    "seller": {
      "@type": "Organization",
      "name": "Dimonoff"
    },
    "hasMerchantReturnPolicy": {
      "@type": "MerchantReturnPolicy",
      "name": "Contact Sales"
    }
  },
  "award": ["2024 Smart City Product of the Year", "2024 IoT Security Excellence Award", "2025 Digi Green Tech Award"],
  "isRelatedTo": {
    "@type": "Product",
    "name": "SCMS - Smart City Management System",
    "url": "https://www.dimonoff.com/solutions/smart-lighting-control/products/iot-platforms/scms/"
  }
}
```

### FAQ Schema (for AEO/GEO)

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is the difference between the RME, RTM and LNLV smart lighting nodes?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The RME is an external retrofit controller that plugs into standard ANSI C136.41 or Zhaga Book 18 photocell receptacles, compatible with LED, HPS, MH and MV fixtures. The RTM is an internal controller designed for decorative and architectural lighting with RGBW capability. The LNLV is a low-voltage node for solar-powered and off-grid lighting applications. All three connect to the SCMS cloud platform for centralized management."
      }
    },
    {
      "@type": "Question",
      "name": "Are Dimonoff smart lighting nodes compatible with Wi-SUN FAN?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. As a Contributing Member of the Wi-SUN Alliance, Dimonoff is integrating Wi-SUN FAN connectivity into its next-generation node series. Wi-SUN FAN provides self-forming, self-healing mesh networking based on open IEEE 802.15.4 and IPv6 standards, with enterprise-grade security including X.509 certificates and AES-CCM encryption."
      }
    },
    {
      "@type": "Question",
      "name": "How do Dimonoff nodes prevent vendor lock-in?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Dimonoff nodes are certified to open industry standards (ANSI C136.41, Zhaga Book 18, Wi-SUN FAN) ensuring interoperability with other certified equipment. Cities are not locked into a single vendor ecosystem. The SCMS platform's open API architecture further enables integration with third-party systems and data platforms."
      }
    },
    {
      "@type": "Question",
      "name": "What is the typical ROI for smart street lighting with Dimonoff nodes?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Municipalities typically achieve ROI within 3 to 5 years, with up to 50% reduction in electricity costs and 40% reduction in maintenance costs. For example, the City of Laval saves CA$2.75 million annually across 37,000 luminaires, and the FQM collective project covering 145,000 streetlights generates $6.8 million in annual savings."
      }
    },
    {
      "@type": "Question",
      "name": "Can I purchase Dimonoff nodes through a government cooperative contract?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Dimonoff solutions are available through the Sourcewell cooperative purchasing contract #041525-DIMN, valid through July 2029. This enables government agencies across North America to procure without lengthy RFP processes."
      }
    },
    {
      "@type": "Question",
      "name": "What communication protocols do Dimonoff wireless nodes support?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Dimonoff nodes support multiple protocols to match your infrastructure requirements: DigiMesh for proven mesh networking, LoRaWAN for long-range LPWAN, LTE-M and NB-IoT for cellular IoT, and Wi-SUN FAN for open-standard interoperable mesh. The Gateway G3+ aggregates up to 1,000 nodes with NEMA 4X (IP66) protection."
      }
    }
  ]
}
```

---

## ENGLISH VERSION

### Next-Generation Smart Wireless Lighting Nodes

**Your street lighting infrastructure deserves controllers built for the next 20 years — not the last 20.**

---

#### The Challenge Facing Utilities Today

Public utilities and municipalities across North America manage millions of streetlights that represent one of their largest energy expenses and most visible public safety assets. Yet most are still controlled by aging photocells or proprietary systems that lock cities into a single vendor's roadmap.

The consequences are real:

- **Wasted energy**: Traditional lighting runs at full power regardless of conditions, consuming 40-60% more electricity than necessary
- **Reactive maintenance**: Crews discover outages through citizen complaints, not real-time alerts
- **Vendor lock-in**: Proprietary protocols mean replacing one component often requires replacing the entire system
- **Stranded investment**: Controllers that cannot adapt to new standards become obsolete within a single budget cycle

---

#### Introducing the Dimonoff Smart Wireless Lighting Node Series

Dimonoff's next-generation wireless nodes are engineered for one purpose: giving utilities complete control over their street lighting infrastructure without sacrificing future flexibility.

Every node in the series connects to **SCMS (Smart City Management System)** — one of the most versatile IoT platforms on the market — providing a single pane of glass across your entire lighting network, from a pilot of 50 fixtures to a metropolitan deployment of 100,000+.

**Three nodes. Every application. One platform.**

---

#### RME — External Smart Controller

**The fastest path to smart lighting for any existing infrastructure.**

The RME plugs directly into standard photocell receptacles — no rewiring, no fixture replacement, no downtime. In minutes, any streetlight becomes a connected, controllable, monitorable asset.

| Specification | Detail |
|---------------|--------|
| Installation | External — plugs into ANSI C136.41 or Zhaga Book 18 receptacle |
| Fixture compatibility | LED, HPS, MH, MV — any existing technology |
| Communication | DigiMesh, LTE-M, NB-IoT, LoRaWAN |
| Next-gen connectivity | Wi-SUN FAN ready (Dimonoff is a Wi-SUN Alliance Contributing Member) |
| Certifications | ANSI C136.41, Zhaga Book 18 |
| Dimming | 0-100% continuous dimming with adaptive scheduling |
| Monitoring | Real-time power metering, voltage, current, power factor |
| Alerts | Outage detection, lamp failure, abnormal consumption |

**Why utilities choose the RME:**
- Zero disruption to existing infrastructure — install during routine maintenance
- Multi-protocol flexibility — choose the connectivity that matches your network today, upgrade later
- Open standards — no proprietary lock-in, certified interoperability
- Field-proven across 575+ projects and 850,000+ deployed devices

---

#### RTM — Internal Smart Controller

**Architectural lighting deserves intelligent control.**

The RTM is designed for decorative, architectural, and feature lighting applications where aesthetics matter as much as efficiency. Built-in RGBW capability enables dynamic color scenes while analog and digital I/O allows integration with sensors, switches, and third-party systems.

| Specification | Detail |
|---------------|--------|
| Installation | Internal — embedded within the luminaire |
| Specialty | RGBW architectural and decorative lighting |
| I/O | Analog and digital input/output for sensor integration |
| Communication | Multi-protocol wireless |
| Platform | Managed via SCMS alongside all other lighting assets |

**Ideal for:** Downtown cores, heritage districts, parks, campuses, public plazas, and any application where lighting is both functional and aesthetic.

---

#### LNLV — Low-Voltage Smart Controller

**Smart control for solar-powered and off-grid lighting.**

The LNLV extends intelligent lighting control to applications where traditional line-voltage infrastructure is unavailable or impractical. Solar-powered streetlights, pathway lighting, and remote installations gain the same monitoring, scheduling, and analytics capabilities as grid-connected fixtures.

| Specification | Detail |
|---------------|--------|
| Installation | Low-voltage wiring |
| Application | Solar-powered, battery-backed, and low-voltage systems |
| Communication | Multi-protocol wireless |
| Platform | Full SCMS integration — same dashboard as all other nodes |

**Ideal for:** Solar streetlights, rural pathways, parks, parking lots, temporary installations, and off-grid communities.

---

#### Why Open Standards Matter for Your Investment

As a **Contributing Member of the Wi-SUN Alliance**, Dimonoff is committed to a future where every component in your street lighting network can be sourced from any certified manufacturer — and managed from a single platform.

This is not a roadmap promise. It is an architectural principle:

| Standard | What it guarantees |
|----------|-------------------|
| **ANSI C136.41** | Any C136.41-certified controller fits any C136.41 receptacle — regardless of manufacturer |
| **Zhaga Book 18** | European equivalent ensuring global interoperability for outdoor luminaire interfaces |
| **Wi-SUN FAN** | Self-forming, self-healing mesh with X.509 certificate security — multi-vendor certified |
| **Open API (SCMS)** | Data flows freely to your existing GIS, SCADA, ERP, and analytics platforms |

**The bottom line for procurement:** When you invest in Dimonoff nodes, your investment is protected by international standards — not by a vendor's willingness to support their legacy products.

---

#### Proven Results at Scale

Dimonoff nodes are not lab prototypes. They are field-proven across the most demanding municipal environments in North America:

| Deployment | Scale | Result |
|------------|-------|--------|
| **Montreal, QC** | 132,500+ fixtures | Largest connected lighting network in Quebec |
| **Laval, QC** | 37,000 luminaires | CA$2.75M annual savings |
| **FQM Collective** | 145,000 streetlights | $6.8M annual savings across participating municipalities |
| **Columbus, OH** | City-wide | Full smart lighting deployment with SCMS |
| **Total deployed** | **850,000+ devices** | **575+ projects across 6 countries** |

**Typical financial impact:**
- Up to **50% reduction** in electricity costs
- Up to **40% reduction** in maintenance costs
- ROI achieved within **3 to 5 years**

---

#### Enterprise-Grade Security — Independently Verified

Municipal infrastructure demands security that goes beyond marketing claims. Dimonoff's next-generation nodes implement enterprise-grade cybersecurity aligned with the Wi-SUN Alliance's independently certified security architecture:

- **X.509 device certificates** with ECDSA-SHA256 — every node has a unique, verifiable identity
- **AES-CCM encryption** — all data in transit is encrypted and authenticated
- **EAP-TLS mutual authentication** — based on IEEE 802.1X, the same standard protecting enterprise networks
- **Automatic key rotation** — configurable lifetimes eliminate static credential risks

These capabilities are not self-declared. They are **verified through third-party certification testing** at Wi-SUN-appointed laboratories.

---

#### The SCMS Platform: Your Single Pane of Glass

Every Dimonoff node connects to **SCMS (Smart City Management System)**, built on the **Fundamentum IoT platform** by sister company Amotus. SCMS transforms individual streetlights into a unified, intelligent network:

- **Real-time monitoring** — power consumption, fixture health, operating status across every node
- **Adaptive dimming** — automatic brightness adjustment based on traffic, weather, and time of day
- **Predictive maintenance** — detect failures before they impact service, schedule repairs efficiently
- **Energy analytics** — track consumption trends, measure savings, generate compliance reports
- **Open API** — integrate with your existing GIS, SCADA, asset management, and BI platforms
- **Scalable to 1M+ nodes** — from pilot projects to metropolitan-scale deployments

---

#### Simplified Procurement for Government Agencies

Dimonoff smart lighting solutions are available through the **Sourcewell cooperative purchasing contract #041525-DIMN** (valid through July 2029).

**What this means for you:**
- No lengthy RFP process required
- Pre-negotiated, competitively solicited pricing
- Available to all government agencies across North America
- Compliant with cooperative purchasing regulations

Alternatively, contact our team directly for custom project scoping and technical evaluation.

---

#### Industry Recognition

- **2024 Smart City Product of the Year**
- **2024 IoT Security Excellence Award**
- **2025 Digi Green Tech Award**

---

#### Ready to Modernize Your Street Lighting?

Whether you are converting 500 fixtures or 500,000, Dimonoff's wireless nodes and SCMS platform scale to meet your requirements — with the open standards and proven track record that utility-grade infrastructure demands.

**[Request a Demo]** | **[Download Technical Specifications]** | **[Contact Sales]**

**Naomih Dalpe**
Director of Business Development
ndalpe@dimonoff.com

---
---

## VERSION FRANCAISE

### Noeuds Intelligents de Nouvelle Generation pour Eclairage de Rue

**Votre infrastructure d'eclairage merite des controleurs concus pour les 20 prochaines annees — pas les 20 dernieres.**

---

#### Le defi auquel font face les services publics aujourd'hui

Les services publics et municipalites a travers l'Amerique du Nord gerent des millions de lampadaires qui representent l'une de leurs plus importantes depenses energetiques et l'un de leurs actifs de securite publique les plus visibles. Pourtant, la plupart sont encore controles par des photocellules vieillissantes ou des systemes proprietaires qui enferment les villes dans la feuille de route d'un seul fournisseur.

Les consequences sont reelles :

- **Gaspillage energetique** : L'eclairage traditionnel fonctionne a pleine puissance sans egard aux conditions, consommant 40-60% plus d'electricite que necessaire
- **Maintenance reactive** : Les equipes decouvrent les pannes par les plaintes citoyennes, pas par des alertes en temps reel
- **Dependance fournisseur** : Les protocoles proprietaires signifient que remplacer un composant exige souvent de remplacer le systeme entier
- **Investissement a risque** : Les controleurs incapables de s'adapter aux nouveaux standards deviennent obsoletes en un seul cycle budgetaire

---

#### Presentation de la Serie de Noeuds Intelligents Dimonoff

Les noeuds sans fil de nouvelle generation de Dimonoff sont concus avec un seul objectif : donner aux services publics un controle complet sur leur infrastructure d'eclairage sans sacrifier la flexibilite future.

Chaque noeud de la serie se connecte a **SCMS (Smart City Management System)** — l'une des plateformes IoT les plus polyvalentes du marche — offrant une vue unifiee de l'ensemble de votre reseau d'eclairage, d'un projet pilote de 50 luminaires a un deploiement metropolitain de 100 000+.

**Trois noeuds. Chaque application. Une seule plateforme.**

---

#### RME — Controleur Intelligent Externe

**Le chemin le plus rapide vers l'eclairage intelligent pour toute infrastructure existante.**

Le RME se branche directement dans les receptacles de photocellules standards — sans recablage, sans remplacement de luminaire, sans interruption de service. En quelques minutes, tout lampadaire devient un actif connecte, controlable et surveillable.

| Specification | Detail |
|---------------|--------|
| Installation | Externe — se branche dans un receptacle ANSI C136.41 ou Zhaga Book 18 |
| Compatibilite luminaires | DEL, HPS, MH, MV — toute technologie existante |
| Communication | DigiMesh, LTE-M, NB-IoT, LoRaWAN |
| Connectivite prochaine generation | Compatible Wi-SUN FAN (Dimonoff est membre contributeur de la Wi-SUN Alliance) |
| Certifications | ANSI C136.41, Zhaga Book 18 |
| Gradation | Gradation continue 0-100% avec programmation adaptive |
| Surveillance | Mesure en temps reel : puissance, tension, courant, facteur de puissance |
| Alertes | Detection de panne, defaillance de lampe, consommation anormale |

**Pourquoi les services publics choisissent le RME :**
- Zero perturbation de l'infrastructure existante — installation lors de la maintenance reguliere
- Flexibilite multi-protocole — choisissez la connectivite adaptee a votre reseau aujourd'hui, mettez a niveau plus tard
- Standards ouverts — aucun verrouillage proprietaire, interoperabilite certifiee
- Eprouve sur le terrain dans 575+ projets et 850 000+ appareils deployes

---

#### RTM — Controleur Intelligent Interne

**L'eclairage architectural merite un controle intelligent.**

Le RTM est concu pour les applications d'eclairage decoratif, architectural et d'ambiance ou l'esthetique compte autant que l'efficacite. La capacite RGBW integree permet des scenes de couleurs dynamiques tandis que les E/S analogiques et numeriques permettent l'integration avec des capteurs, commutateurs et systemes tiers.

| Specification | Detail |
|---------------|--------|
| Installation | Interne — integre au luminaire |
| Specialite | Eclairage architectural et decoratif RGBW |
| E/S | Entrees/sorties analogiques et numeriques pour integration de capteurs |
| Communication | Sans fil multi-protocole |
| Plateforme | Gere via SCMS aux cotes de tous vos autres actifs d'eclairage |

**Ideal pour :** Centres-villes, quartiers patrimoniaux, parcs, campus, places publiques et toute application ou l'eclairage est a la fois fonctionnel et esthetique.

---

#### LNLV — Controleur Intelligent Basse Tension

**Le controle intelligent pour l'eclairage solaire et hors reseau.**

Le LNLV etend le controle intelligent de l'eclairage aux applications ou l'infrastructure de tension de ligne traditionnelle est indisponible ou impraticable. Les lampadaires solaires, l'eclairage de sentiers et les installations isolees beneficient des memes capacites de surveillance, de programmation et d'analyse que les luminaires raccordes au reseau.

| Specification | Detail |
|---------------|--------|
| Installation | Cablage basse tension |
| Application | Systemes solaires, a batterie et basse tension |
| Communication | Sans fil multi-protocole |
| Plateforme | Integration complete a SCMS — meme tableau de bord que tous les autres noeuds |

**Ideal pour :** Lampadaires solaires, sentiers ruraux, parcs, stationnements, installations temporaires et communautes hors reseau.

---

#### Pourquoi les standards ouverts protegent votre investissement

En tant que **membre contributeur de la Wi-SUN Alliance**, Dimonoff s'engage pour un avenir ou chaque composant de votre reseau d'eclairage peut etre approvisionne aupres de n'importe quel fabricant certifie — et gere depuis une seule plateforme.

Ce n'est pas une promesse sur la feuille de route. C'est un principe architectural :

| Standard | Ce qu'il garantit |
|----------|------------------|
| **ANSI C136.41** | Tout controleur certifie C136.41 s'adapte a tout receptacle C136.41 — peu importe le fabricant |
| **Zhaga Book 18** | Equivalent europeen assurant l'interoperabilite mondiale pour les interfaces de luminaires exterieurs |
| **Wi-SUN FAN** | Reseau maille auto-formant et auto-reparateur avec securite par certificats X.509 — certification multi-fournisseur |
| **API ouverte (SCMS)** | Les donnees circulent librement vers vos plateformes GIS, SCADA, ERP et analytiques existantes |

**L'essentiel pour l'approvisionnement :** Lorsque vous investissez dans les noeuds Dimonoff, votre investissement est protege par des standards internationaux — pas par la volonte d'un fournisseur a maintenir ses produits existants.

---

#### Resultats prouves a grande echelle

Les noeuds Dimonoff ne sont pas des prototypes de laboratoire. Ils sont eprouves sur le terrain dans les environnements municipaux les plus exigeants en Amerique du Nord :

| Deploiement | Echelle | Resultat |
|-------------|---------|----------|
| **Montreal, QC** | 132 500+ luminaires | Plus grand reseau d'eclairage connecte au Quebec |
| **Laval, QC** | 37 000 luminaires | 2,75 M$ d'economies annuelles |
| **Projet collectif FQM** | 145 000 lampadaires | 6,8 M$ d'economies annuelles pour les municipalites participantes |
| **Columbus, OH** | A l'echelle de la ville | Deploiement complet d'eclairage intelligent avec SCMS |
| **Total deploye** | **850 000+ appareils** | **575+ projets dans 6 pays** |

**Impact financier typique :**
- Jusqu'a **50% de reduction** des couts d'electricite
- Jusqu'a **40% de reduction** des couts de maintenance
- ROI atteint en **3 a 5 ans**

---

#### Securite de grade entreprise — verifiee independamment

L'infrastructure municipale exige une securite qui va au-dela des affirmations marketing. Les noeuds de nouvelle generation de Dimonoff implementent une cybersecurite de grade entreprise alignee sur l'architecture de securite certifiee independamment par la Wi-SUN Alliance :

- **Certificats X.509 par appareil** avec ECDSA-SHA256 — chaque noeud possede une identite unique et verifiable
- **Chiffrement AES-CCM** — toutes les donnees en transit sont chiffrees et authentifiees
- **Authentification mutuelle EAP-TLS** — basee sur IEEE 802.1X, le meme standard qui protege les reseaux d'entreprise
- **Rotation automatique des cles** — les durees de vie configurables eliminent les risques de credentials statiques

Ces capacites ne sont pas auto-declarees. Elles sont **verifiees par des tests de certification tiers** dans des laboratoires mandates par Wi-SUN.

---

#### La plateforme SCMS : votre vue unifiee

Chaque noeud Dimonoff se connecte a **SCMS (Smart City Management System)**, construit sur la **plateforme IoT Fundamentum** de la societe soeur Amotus. SCMS transforme les lampadaires individuels en un reseau unifie et intelligent :

- **Surveillance en temps reel** — consommation, sante des equipements, statut operationnel pour chaque noeud
- **Gradation adaptive** — ajustement automatique de la luminosite selon le trafic, la meteo et l'heure
- **Maintenance predictive** — detectez les defaillances avant qu'elles n'affectent le service
- **Analytique energetique** — suivez les tendances de consommation, mesurez les economies, generez des rapports de conformite
- **API ouverte** — integrez avec vos plateformes GIS, SCADA, gestion d'actifs et BI existantes
- **Evolutif a 1M+ noeuds** — des projets pilotes aux deploiements metropolitains

---

#### Approvisionnement simplifie pour les agences gouvernementales

Les solutions d'eclairage intelligent Dimonoff sont disponibles via le **contrat d'achat cooperatif Sourcewell #041525-DIMN** (valide jusqu'en juillet 2029).

**Ce que cela signifie pour vous :**
- Aucun processus d'appel d'offres requis
- Prix pre-negocies et sollicites de facon competitive
- Disponible pour toutes les agences gouvernementales en Amerique du Nord
- Conforme aux reglements d'achat cooperatif

Vous pouvez aussi contacter notre equipe directement pour un dimensionnement de projet personnalise et une evaluation technique.

---

#### Reconnaissance de l'industrie

- **2024 Produit de l'Annee Ville Intelligente**
- **2024 Prix d'Excellence en Securite IoT**
- **2025 Prix Digi Green Tech**

---

#### Pret a moderniser votre eclairage de rue?

Que vous convertissiez 500 luminaires ou 500 000, les noeuds sans fil et la plateforme SCMS de Dimonoff s'adaptent a vos besoins — avec les standards ouverts et les resultats prouves que l'infrastructure de grade utilite exige.

**[Demander une demo]** | **[Telecharger les specifications techniques]** | **[Contacter les ventes]**

**Naomih Dalpe**
Directrice du developpement des affaires
ndalpe@dimonoff.com

---

## Notes de deploiement

### Mots-cles cibles (SEO non-branded)

| Keyword (EN) | Intent | Volume estimate |
|--------------|--------|-----------------|
| smart street lighting controller | Commercial | High |
| wireless lighting node | Commercial | Medium |
| ANSI C136.41 smart controller | Commercial | Low (high intent) |
| Zhaga Book 18 controller | Commercial | Low (high intent) |
| Wi-SUN street lighting | Informational/Commercial | Emerging |
| smart lighting vendor lock-in | Informational | Medium |
| utility grade street lighting IoT | Commercial | Medium |
| retrofit smart street lighting | Commercial | Medium |
| smart city lighting management platform | Commercial | Medium |
| solar powered smart street light controller | Commercial | Low |

### Liens internes recommandes

- Vers SCMS platform page
- Vers page Sourcewell badge
- Vers news Wi-SUN Alliance membership (quand publiee)
- Vers glossary (termes: ANSI C136.41, Zhaga, Wi-SUN FAN, SCMS)
- Vers case studies (Montreal, Laval, FQM)

### Images requises

1. **Hero banner**: Photo hero des 3 noeuds (RME, RTM, LNLV) avec eclairage urbain en arriere-plan
   - Alt: "Dimonoff RME RTM LNLV smart wireless lighting nodes for municipal street lighting"
   - Taille: 1200x630px minimum
2. **RME product photo**: RME-H3 installe sur un luminaire
   - Alt: "RME smart wireless lighting node installed on street light photocell receptacle"
3. **RTM product photo**: RTM dans un luminaire architectural
   - Alt: "RTM internal smart controller for architectural and decorative lighting"
4. **LNLV product photo**: LNLV sur installation solaire
   - Alt: "LNLV low-voltage smart node on solar-powered street light"
5. **SCMS dashboard**: Capture ecran du tableau de bord SCMS
   - Alt: "SCMS Smart City Management System dashboard showing real-time street lighting monitoring"
6. **Deployment map**: Carte des deploiements (Montreal, Laval, Columbus, etc.)
   - Alt: "Map of Dimonoff smart lighting deployments across North America and internationally"
