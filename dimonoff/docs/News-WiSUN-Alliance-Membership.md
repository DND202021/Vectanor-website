# News Article — Wi-SUN Alliance Membership

> **Status:** DRAFT v3 — Ready for review
> **Date:** 2026-03-27
> **Author:** Daniel Noiseux / Dimonoff Marketing
> **Target pages:** dimonoff.com/news/ (EN), dimonoff.com/fr/nouvelles/ (FR)
> **Target date of publication:** TBD

---

## SEO / Schema / Meta Implementation Notes

### Meta Tags (EN page)

```html
<title>Dimonoff Joins the Wi-SUN Alliance as Contributing Member | Dimonoff</title>
<meta name="description" content="Vectanor Group inc., parent company of smart street lighting leader Dimonoff, joins the Wi-SUN Alliance as Contributing Member. This reinforces Dimonoff's commitment to open, interoperable IoT standards for smart cities and utilities worldwide.">
<meta name="keywords" content="Wi-SUN Alliance, Dimonoff, Vectanor Group, smart street lighting, IoT, smart city, Contributing Member, interoperability, SCMS, open standards, Wi-SUN FAN, smart lighting control">
<meta name="author" content="Dimonoff">
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
<link rel="canonical" href="https://www.dimonoff.com/news/dimonoff-joins-wi-sun-alliance-contributing-member/">
```

### Meta Tags (FR page)

```html
<title>Dimonoff rejoint la Wi-SUN Alliance comme membre contributeur | Dimonoff</title>
<meta name="description" content="Vectanor Group inc., societe mere du chef de file en eclairage intelligent Dimonoff, rejoint la Wi-SUN Alliance en tant que membre contributeur. Un engagement renforce envers les standards ouverts IoT pour les villes intelligentes et les services publics.">
<meta name="keywords" content="Wi-SUN Alliance, Dimonoff, Vectanor Group, eclairage intelligent, IoT, ville intelligente, membre contributeur, interoperabilite, SCMS, standards ouverts, Wi-SUN FAN, controle eclairage">
<meta name="author" content="Dimonoff">
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
<link rel="canonical" href="https://www.dimonoff.com/fr/nouvelles/dimonoff-rejoint-wi-sun-alliance-membre-contributeur/">
<link rel="alternate" hreflang="en" href="https://www.dimonoff.com/news/dimonoff-joins-wi-sun-alliance-contributing-member/">
<link rel="alternate" hreflang="fr" href="https://www.dimonoff.com/fr/nouvelles/dimonoff-rejoint-wi-sun-alliance-membre-contributeur/">
```

### Open Graph / Social Media Tags (EN)

```html
<meta property="og:type" content="article">
<meta property="og:title" content="Dimonoff Joins the Wi-SUN Alliance as Contributing Member">
<meta property="og:description" content="Vectanor Group inc., parent company of smart street lighting leader Dimonoff, joins the Wi-SUN Alliance — reinforcing its commitment to open, interoperable IoT standards for smart cities and utilities.">
<meta property="og:url" content="https://www.dimonoff.com/news/dimonoff-joins-wi-sun-alliance-contributing-member/">
<meta property="og:site_name" content="Dimonoff">
<meta property="og:image" content="https://www.dimonoff.com/wp-content/uploads/2026/03/dimonoff-wi-sun-alliance-membership.jpg">
<meta property="og:image:alt" content="Dimonoff and Wi-SUN Alliance logos side by side">
<meta property="article:published_time" content="2026-04-XX T09:00:00-04:00">
<meta property="article:author" content="Dimonoff">
<meta property="article:section" content="News">
<meta property="article:tag" content="Wi-SUN Alliance">
<meta property="article:tag" content="Smart Street Lighting">
<meta property="article:tag" content="IoT">
<meta property="article:tag" content="Smart City">
<meta property="article:tag" content="Interoperability">
```

### Twitter Card Tags

```html
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Dimonoff Joins the Wi-SUN Alliance as Contributing Member">
<meta name="twitter:description" content="Vectanor Group, parent of smart lighting leader Dimonoff, joins the Wi-SUN Alliance. 575+ projects, 850K+ devices deployed, now committed to open Wi-SUN standards.">
<meta name="twitter:image" content="https://www.dimonoff.com/wp-content/uploads/2026/03/dimonoff-wi-sun-alliance-membership.jpg">
```

### JSON-LD Structured Data (NewsArticle schema)

```json
{
  "@context": "https://schema.org",
  "@type": "NewsArticle",
  "headline": "Dimonoff Joins the Wi-SUN Alliance as Contributing Member, Reinforcing Its Commitment to Open Standards for Smart Cities",
  "alternativeHeadline": "Smart Street Lighting Leader Dimonoff Joins Wi-SUN Alliance to Advance Open IoT Standards",
  "description": "Vectanor Group inc., parent company of Dimonoff, joins the Wi-SUN Alliance as a Contributing Member, reinforcing its commitment to open, interoperable IoT standards for smart cities and utilities worldwide.",
  "datePublished": "2026-04-XX",
  "dateModified": "2026-04-XX",
  "author": {
    "@type": "Organization",
    "name": "Dimonoff",
    "url": "https://www.dimonoff.com"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Dimonoff",
    "url": "https://www.dimonoff.com",
    "logo": {
      "@type": "ImageObject",
      "url": "https://www.dimonoff.com/wp-content/uploads/dimonoff-logo.png"
    }
  },
  "image": "https://www.dimonoff.com/wp-content/uploads/2026/03/dimonoff-wi-sun-alliance-membership.jpg",
  "url": "https://www.dimonoff.com/news/dimonoff-joins-wi-sun-alliance-contributing-member/",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://www.dimonoff.com/news/dimonoff-joins-wi-sun-alliance-contributing-member/"
  },
  "articleSection": "News",
  "keywords": ["Wi-SUN Alliance", "smart street lighting", "IoT", "smart city", "interoperability", "SCMS", "Dimonoff", "Vectanor Group", "Contributing Member", "Wi-SUN FAN", "open standards"],
  "inLanguage": "en",
  "about": [
    {
      "@type": "Organization",
      "name": "Wi-SUN Alliance",
      "url": "https://wi-sun.org/",
      "description": "Global industry association promoting interoperable wireless solutions for smart utilities, smart cities, and IoT"
    },
    {
      "@type": "Organization",
      "name": "Dimonoff",
      "url": "https://www.dimonoff.com",
      "description": "Global leader in smart street lighting control, member of Groupe Vectanor"
    }
  ],
  "mentions": [
    {
      "@type": "Product",
      "name": "SCMS - Smart City Management System",
      "manufacturer": { "@type": "Organization", "name": "Dimonoff" },
      "description": "IoT management platform for smart street lighting and smart city applications"
    },
    {
      "@type": "Product",
      "name": "RME Smart Wireless Lighting Node",
      "manufacturer": { "@type": "Organization", "name": "Dimonoff" }
    },
    {
      "@type": "Organization",
      "name": "Vectanor Group inc.",
      "url": "https://www.vectanor.com"
    },
    {
      "@type": "Organization",
      "name": "Amotus",
      "url": "https://www.amotus.com",
      "description": "IoT engineering and electronics design company, developer of the Fundamentum IoT platform"
    }
  ]
}
```

### Image Requirements

Prepare a hero image (recommended 1200x630px minimum) showing:
- Dimonoff logo + Wi-SUN Alliance logo side by side
- Alt text: "Dimonoff joins the Wi-SUN Alliance as Contributing Member — logos of Dimonoff and Wi-SUN Alliance"
- File name: `dimonoff-wi-sun-alliance-membership.jpg`
- Note: Wi-SUN logo usage must follow Alliance brand guidelines (see Section 16 of the membership agreement)

---

## ENGLISH VERSION

### Dimonoff Joins the Wi-SUN Alliance as Contributing Member, Reinforcing Its Commitment to Open Standards for Smart Cities

**Quebec City, QC — April 2026** — Dimonoff, a globally recognized leader in smart street lighting control, is proud to announce that its parent company, **Vectanor Group inc.**, has joined the [Wi-SUN Alliance](https://wi-sun.org/) as a Contributing Member. This milestone reinforces Dimonoff's long-standing commitment to delivering interoperable, standards-based IoT solutions for utilities and municipalities worldwide.

#### What is the Wi-SUN Alliance?

The Wi-SUN (Wireless Smart Ubiquitous Network) Alliance is a global industry association of over 300 member organizations across 46 countries. It promotes and certifies interoperable wireless solutions based on open standards, particularly for smart utilities, smart cities, and industrial IoT.

With more than 100 million Wi-SUN-enabled devices deployed globally — including large-scale smart lighting networks in cities such as Miami, Paris, and London — Wi-SUN has established itself as the leading open standard for outdoor IoT mesh networking. The Wi-SUN FAN (Field Area Network) specification, built on IEEE 802.15.4 and IPv6, provides self-forming, self-healing mesh connectivity that can scale to millions of devices across large geographic areas.

#### Why This Matters for Utilities and Municipalities

For public utilities and municipalities evaluating smart infrastructure investments, vendor lock-in remains one of the greatest risks. Wi-SUN directly addresses this concern by certifying that products from different manufacturers can operate on a single, unified network. Cities can select best-in-class components — controllers, gateways, sensors — with the confidence that they will interoperate seamlessly, today and for decades to come.

Wi-SUN's enterprise-grade security architecture meets the stringent cybersecurity requirements that critical municipal infrastructure demands:

- **X.509 device certificates** with ECDSA-SHA256 for unique device identity
- **AES-CCM encryption** for data confidentiality and authenticity
- **EAP-TLS mutual authentication** based on IEEE 802.1X access control
- **Automatic key rotation** with configurable lifetimes

These capabilities are not proprietary claims — they are independently verified through third-party certification testing at Wi-SUN-appointed laboratories.

#### What Dimonoff Brings to the Wi-SUN Ecosystem

With over 575 projects across 6 countries and more than 850,000 products deployed on its existing platform, Dimonoff brings deep, field-tested expertise in smart street lighting to the Wi-SUN ecosystem. Joining the Alliance as a Contributing Member signals the company's commitment to bringing that depth of experience to the Wi-SUN standard.

Dimonoff's documented results across municipal deployments include:

- **Up to 50% reduction in electricity costs** and **40% reduction in maintenance costs**, with ROI typically achieved within 3 to 5 years
- Deployments serving cities of all sizes — from large metropolitan areas such as Montreal (132,500+ fixtures) and Laval (37,000 luminaires saving CA$2.75M annually) to small municipalities through cooperative programs like the FQM collective project (145,000 streetlights, $6.8M in annual savings)
- Award-winning technology recognized by the industry: **2024 Smart City Product of the Year**, **2024 IoT Security Excellence Award**, and **2025 Digi Green Tech Award**

#### SCMS: The Most Versatile Smart City Platform

At the heart of Dimonoff's solution is **SCMS (Smart City Management System)**, one of the most versatile IoT management platforms on the market. Built on the **Fundamentum IoT platform** developed by sister company [Amotus](https://www.amotus.com) — also part of Groupe Vectanor — SCMS transforms every connected streetlight into a launchpad for broader smart city services, including air quality monitoring, noise sensing, public safety, and parking management.

SCMS's open API architecture aligns naturally with the Wi-SUN Alliance's philosophy of open, interoperable standards. As Dimonoff integrates Wi-SUN FAN capabilities, SCMS will serve as the unified command center for managing Wi-SUN-certified field devices alongside existing infrastructure — giving utilities a single pane of glass across their entire connected network.

#### A Natural Fit: Shared Values, Shared Vision

Dimonoff's product line already reflects the standards-first philosophy that defines the Wi-SUN Alliance:

- **RME** — Smart Wireless Lighting Node (external controller), certified ANSI C136.41 and Zhaga Book 18
- **RTM** — Smart Wireless Lighting Node (internal controller) with RGBW architectural lighting capability
- **LNLV** — Smart Wireless Lighting Node for low-voltage and solar-powered applications
- **G3+** — IoT Gateway supporting up to 1,000 nodes with autonomous operation and NEMA 4X (IP66) enclosure
- **DOO Express** — Cost-effective IoT management platform for smaller deployments

As a Contributing Member, Vectanor Group will actively participate in shaping future Wi-SUN specifications, with full access to technical working groups and draft standards — ensuring that the needs of smart lighting deployments are well represented in the evolution of the Wi-SUN FAN standard.

For existing Wi-SUN Alliance members, the addition of Dimonoff strengthens the ecosystem with a proven smart city platform provider possessing deep vertical expertise in outdoor lighting — consistently the number one entry point for Wi-SUN smart city deployments worldwide.

#### Availability

Dimonoff's smart lighting solutions, including SCMS, are available through direct engagement or via the **Sourcewell cooperative purchasing contract #041525-DIMN** (valid through July 2029), enabling streamlined procurement for government agencies across North America without lengthy RFP processes.

#### About Dimonoff

Dimonoff, a member of Groupe Vectanor, is a global leader in smart street lighting control, headquartered in Quebec City, Canada. Founded in 2006, Dimonoff provides end-to-end IoT solutions — from wireless controllers and gateways to its flagship SCMS cloud platform powered by the Fundamentum IoT platform — enabling cities and utilities to reduce energy consumption, optimize maintenance, and build the foundation for smarter, more sustainable communities. Learn more at [dimonoff.com](https://www.dimonoff.com).

#### About the Wi-SUN Alliance

The Wi-SUN Alliance is a global non-profit industry association with over 300 member companies across 46 countries, driving the adoption of interoperable wireless solutions for smart utilities, smart cities, and IoT. Based on open IEEE and IETF standards, Wi-SUN FAN certification ensures multi-vendor interoperability, enterprise-grade security, and scalability to millions of devices. Over 100 million Wi-SUN-enabled devices are deployed worldwide. Learn more at [wi-sun.org](https://wi-sun.org).

#### Media Contact

**Naomih Dalpe**
Director of Business Development, Dimonoff
ndalpe@dimonoff.com

---

## VERSION FRANCAISE

### Dimonoff rejoint la Wi-SUN Alliance en tant que membre contributeur, renforçant son engagement envers les standards ouverts pour les villes intelligentes

**Quebec, QC — Avril 2026** — Dimonoff, chef de file mondialement reconnu en controle intelligent de l'eclairage public, est fier d'annoncer que sa societe mere, **Vectanor Group inc.**, a rejoint la [Wi-SUN Alliance](https://wi-sun.org/) en tant que membre contributeur. Cette etape marque un renforcement de l'engagement de longue date de Dimonoff a offrir des solutions IoT interoperables, fondees sur des standards ouverts, aux services publics et municipalites a travers le monde.

#### Qu'est-ce que la Wi-SUN Alliance?

La Wi-SUN Alliance (Wireless Smart Ubiquitous Network) est une association industrielle mondiale regroupant plus de 300 organisations membres reparties dans 46 pays. Elle promeut et certifie des solutions sans fil interoperables basees sur des standards ouverts, particulierement pour les services publics intelligents, les villes intelligentes et l'IoT industriel.

Avec plus de 100 millions d'appareils Wi-SUN deployes mondialement — incluant des reseaux d'eclairage intelligent a grande echelle dans des villes telles que Miami, Paris et Londres — Wi-SUN s'est impose comme le principal standard ouvert pour les reseaux mailles IoT exterieurs. La specification Wi-SUN FAN (Field Area Network), construite sur IEEE 802.15.4 et IPv6, fournit une connectivite maillée auto-formante et auto-reparatrice pouvant supporter des millions d'appareils sur de vastes zones geographiques.

#### Pourquoi c'est important pour les services publics et les municipalites

Pour les services publics et les municipalites qui evaluent des investissements en infrastructure intelligente, la dependance envers un seul fournisseur demeure l'un des plus grands risques. Wi-SUN repond directement a cette preoccupation en certifiant que des produits de differents fabricants peuvent fonctionner sur un reseau unique et unifie. Les villes peuvent selectionner les meilleurs composants — controleurs, passerelles, capteurs — avec l'assurance qu'ils interopereront parfaitement, aujourd'hui et pour les decennies a venir.

L'architecture de securite de niveau entreprise de Wi-SUN repond aux exigences rigoureuses de cybersecurite que les infrastructures municipales critiques exigent :

- **Certificats X.509 par appareil** avec ECDSA-SHA256 pour une identite unique
- **Chiffrement AES-CCM** pour la confidentialite et l'authenticite des donnees
- **Authentification mutuelle EAP-TLS** basee sur le controle d'acces IEEE 802.1X
- **Rotation automatique des cles** avec durees de vie configurables

Il ne s'agit pas de promesses proprietaires — ces capacites sont verifiees independamment par des tests de certification effectues par des laboratoires tiers mandates par Wi-SUN.

#### Ce que Dimonoff apporte a l'ecosysteme Wi-SUN

Avec plus de 575 projets dans 6 pays et plus de 850 000 produits deployes sur sa plateforme existante, Dimonoff apporte une expertise approfondie et eprouvee sur le terrain en eclairage public intelligent a l'ecosysteme Wi-SUN. En rejoignant l'Alliance en tant que membre contributeur, l'entreprise signale son engagement a apporter cette profondeur d'experience au standard Wi-SUN.

Les resultats documentes de Dimonoff a travers ses deploiements municipaux incluent :

- **Jusqu'a 50 % de reduction des couts d'electricite** et **40 % de reduction des couts de maintenance**, avec un retour sur investissement typiquement atteint en 3 a 5 ans
- Des deploiements desservant des villes de toutes tailles — des grandes metropoles comme Montreal (132 500+ luminaires) et Laval (37 000 luminaires, economies de 2,75 M$ CA par an) aux petites municipalites via des programmes cooperatifs comme le projet collectif de la FQM (145 000 lampadaires, 6,8 M$ d'economies annuelles)
- Une technologie primee et reconnue par l'industrie : **Produit de l'annee 2024 pour les villes intelligentes**, **Prix d'excellence 2024 en securite IoT** et **Prix Digi Green Tech 2025**

#### SCMS : La plateforme de ville intelligente la plus polyvalente

Au coeur de la solution Dimonoff se trouve **SCMS (Smart City Management System)**, l'une des plateformes de gestion IoT les plus polyvalentes sur le marche. Construite sur la **plateforme IoT Fundamentum** developpee par la societe soeur [Amotus](https://www.amotus.com) — egalement membre du Groupe Vectanor — SCMS transforme chaque lampadaire connecte en point de lancement pour des services de ville intelligente elargis, incluant la surveillance de la qualite de l'air, la mesure du bruit, la securite publique et la gestion du stationnement.

L'architecture API ouverte de SCMS s'aligne naturellement avec la philosophie de standards ouverts et interoperables de la Wi-SUN Alliance. Alors que Dimonoff integre les capacites Wi-SUN FAN, SCMS servira de centre de commande unifie pour gerer les appareils certifies Wi-SUN aux cotes de l'infrastructure existante — offrant aux services publics une vue consolidee de l'ensemble de leur reseau connecte.

#### Une synergie naturelle : des valeurs et une vision partagees

La gamme de produits Dimonoff reflete deja la philosophie axee sur les standards qui definit la Wi-SUN Alliance :

- **RME** — Noeud d'eclairage intelligent sans fil (controleur externe), certifie ANSI C136.41 et Zhaga Book 18
- **RTM** — Noeud d'eclairage intelligent sans fil (controleur interne) avec capacite d'eclairage architectural RGBW
- **LNLV** — Noeud d'eclairage intelligent sans fil pour applications basse tension et solaires
- **G3+** — Passerelle IoT supportant jusqu'a 1 000 noeuds avec operation autonome et boitier NEMA 4X (IP66)
- **DOO Express** — Plateforme de gestion IoT economique pour les deploiements de plus petite envergure

En tant que membre contributeur, Vectanor Group participera activement a l'elaboration des futures specifications Wi-SUN, avec un acces complet aux groupes de travail techniques et aux standards en developpement — s'assurant que les besoins des deploiements d'eclairage intelligent sont bien representes dans l'evolution du standard Wi-SUN FAN.

Pour les membres actuels de la Wi-SUN Alliance, l'ajout de Dimonoff renforce l'ecosysteme avec un fournisseur de plateforme de ville intelligente eprouve possedant une expertise verticale approfondie en eclairage exterieur — systematiquement le point d'entree numero un pour les deploiements Wi-SUN en ville intelligente a travers le monde.

#### Disponibilite

Les solutions d'eclairage intelligent de Dimonoff, incluant SCMS, sont disponibles en engagement direct ou via le **contrat d'achat cooperatif Sourcewell #041525-DIMN** (valide jusqu'en juillet 2029), permettant un approvisionnement simplifie pour les agences gouvernementales a travers l'Amerique du Nord sans processus d'appel d'offres.

#### A propos de Dimonoff

Dimonoff, membre du Groupe Vectanor, est un chef de file mondial en controle intelligent de l'eclairage public, dont le siege social est situe a Quebec, Canada. Fondee en 2006, Dimonoff fournit des solutions IoT de bout en bout — des controleurs sans fil et passerelles a sa plateforme infonuagique phare SCMS, propulsee par la plateforme IoT Fundamentum — permettant aux villes et services publics de reduire leur consommation energetique, optimiser la maintenance et batir les fondations de communautes plus intelligentes et durables. En savoir plus sur [dimonoff.com](https://www.dimonoff.com).

#### A propos de la Wi-SUN Alliance

La Wi-SUN Alliance est une association industrielle mondiale a but non lucratif regroupant plus de 300 entreprises membres dans 46 pays, promouvant l'adoption de solutions sans fil interoperables pour les services publics intelligents, les villes intelligentes et l'IoT. Basee sur les standards ouverts IEEE et IETF, la certification Wi-SUN FAN assure l'interoperabilite multi-fournisseurs, une securite de niveau entreprise et une mise a l'echelle vers des millions d'appareils. Plus de 100 millions d'appareils Wi-SUN sont deployes dans le monde. En savoir plus sur [wi-sun.org](https://wi-sun.org).

#### Contact media

**Naomih Dalpe**
Directrice du developpement des affaires, Dimonoff
ndalpe@dimonoff.com

---

## PRESS DISTRIBUTION CHECKLIST

### Newswire / PR Distribution
- [ ] Submit EN version to GlobeNewswire, PR Newswire, or BusinessWire
- [ ] Select categories: IoT, Smart Cities, Smart Lighting, Utilities, Technology
- [ ] Target geographies: North America, Europe
- [ ] Include hero image with both logos

### Direct Outreach
- [ ] Send to Wi-SUN Alliance PR/communications team for cross-promotion
- [ ] Send to trade publications: LEDs Magazine, Smart Cities World, IoT World Today, Smart Energy International, Municipal World (Canada)
- [ ] Send to Canadian tech media: BetaKit, IT World Canada, Direction Informatique

### Social Media Posts
- [ ] LinkedIn company page (Dimonoff + Vectanor Group)
- [ ] Tag @WiSUNAlliance in posts
- [ ] Share with key employees for amplification

### Website Publishing
- [ ] Publish on dimonoff.com/news/ with all meta tags and schema above
- [ ] Create FR version on dimonoff.com/fr/nouvelles/
- [ ] Add internal links from Solutions and Smart Lighting Control pages
- [ ] Update llms.txt if present to include Wi-SUN membership fact
- [ ] Consider adding Wi-SUN logo/badge to homepage or product pages (per Alliance brand guidelines)

### Syndication Signals
- [ ] Submit URL to Google Search Console after publishing
- [ ] Ping Google News sitemap
- [ ] Ensure page is included in XML sitemap with `<news:news>` tags if site has Google News approval
