# Phase 4.5: Technical Glossary Plan

## Overview
A dedicated glossary page at `/glossary/` will define key IoT, smart city, and Dimonoff-specific terms. This serves dual purposes:
1. **User Education**: Help visitors understand Dimonoff's technology and industry terminology
2. **SEO Value**: DefinedTermSet schema markup improves rich snippets and knowledge graph visibility

## Page Structure

### URL & Setup
- **Location**: `/glossary/` (EN), `/glossaire/` (FR), `/glosario/` (ES)
- **Title**: "Smart City & IoT Glossary" (EN) | "Glossaire IoT et Villes Intelligentes" (FR) | "Glosario de IoT y Ciudades Inteligentes" (ES)
- **Meta Description**: "Definitions of key IoT, smart city, and lighting terms. Understand Dimonoff's products and industry standards." (EN)
- **Purpose**: Define 20-30 core terms with DefinedTermSet JSON-LD schema

### WordPress Implementation
- Create as a standard WordPress page (not CPT)
- Use Elementor to design a two-column layout:
  - Left: Accordion or toggle list of terms (searchable)
  - Right: Term definitions and related links
- Install mu-plugin: `dimonoff-glossary-schema.php` to inject DefinedTermSet JSON-LD

---

## Glossary Terms (20-30 Terms)

### Dimonoff Products & Platforms

| Term | Definition | Related Page |
|------|-----------|--------------|
| **SCMS** | Smart City Management System - Dimonoff's unified platform for managing connected city infrastructure including lighting, parking, security, and environmental monitoring. | /solutions/ |
| **RME** | Remote Management Engine - A specialized LED controller module that enables wireless control and monitoring of street lighting fixtures. | /products/led-controllers/ |
| **RTM** | Real-Time Monitor - Advanced LED controller with real-time dimming, color management, and energy tracking capabilities. | /products/led-controllers/ |
| **LNLV** | Low Noise Low Voltage - LED controller designed for noise-sensitive environments (parks, residential areas) with minimal EMI. | /products/led-controllers/ |
| **Gateway G3+** | Next-generation IoT gateway providing secure connectivity, data aggregation, and edge processing for Dimonoff SCMS. Supports multiple protocols including TALQ and DALI. | /products/gateway/ |
| **Spatium** | Intelligent parking management platform integrated with SCMS. Provides real-time parking availability, dynamic pricing, and occupancy optimization. | /solutions/smart-parking/ |
| **CitySafe** | Dimonoff security solution integrating surveillance, access control, and incident management with SCMS for comprehensive urban security. | /solutions/security/ |
| **CitySense** | Environmental monitoring solution tracking air quality, noise levels, temperature, and humidity across smart city infrastructure. | /solutions/environment/ |
| **CitySound** | Acoustic management solution for urban areas, monitoring and controlling noise pollution with real-time alerts. | /solutions/experience/ |
| **DOO Express** | Rapid deployment framework for quick-launch smart city solutions in small municipalities. | /solutions/ |

### IoT & Smart City Concepts

| Term | Definition | Related Page |
|------|-----------|--------------|
| **IoT** | Internet of Things - Network of interconnected physical devices embedded with sensors, software, and communication capabilities. | /about/ |
| **Smart City** | Urban area using IoT sensors, data analytics, and automated systems to optimize infrastructure, services, and citizen experience. | /solutions/ |
| **Edge Computing** | Processing data at network edge (gateway/device level) rather than cloud, reducing latency and bandwidth requirements. | /products/gateway/ |
| **Real-Time Monitoring** | Continuous collection and analysis of device data, providing immediate visibility into system performance and status. | /solutions/ |
| **Data Aggregation** | Collecting and combining sensor data from multiple sources into unified datasets for analysis and decision-making. | /solutions/ |
| **Connectivity** | Ability of IoT devices to communicate using wireless or wired protocols (TALQ, DALI, LoRaWAN, etc.). | /products/ |
| **Occupancy Optimization** | Using sensor data to understand and improve space utilization (parking availability, traffic flow, resource allocation). | /solutions/smart-parking/ |
| **Adaptive Lighting** | Dynamic control of street lighting intensity based on traffic, weather, and time - reducing energy while maintaining safety. | /solutions/smart-lighting/ |

### Standards & Protocols

| Term | Definition | Related Page |
|------|-----------|--------------|
| **TALQ** | Telecommunications and Lighting - Open standard for street lighting device communication and management. Dimonoff Gateway G3+ is TALQ-compatible. | /products/gateway/ |
| **DALI** | Digital Addressable Lighting Interface - Protocol for controlling individual light fixtures with precise dimming and status feedback. | /products/led-controllers/ |
| **Zhaga Book 18** | Standard specifying smart outdoor lighting module interfaces, enabling interoperability between manufacturers. | /products/ |
| **ANSI C136.41** | American National Standard for wireless communication protocols in outdoor lighting and electrical delivery systems. | /products/ |
| **LoRaWAN** | Long Range Wide Area Network - Low-power, wide-range wireless protocol ideal for IoT sensor networks in smart cities. | /solutions/ |
| **MQTT** | Message Queuing Telemetry Transport - Lightweight protocol for device-to-cloud communication with minimal bandwidth. | /products/gateway/ |

### Energy & Infrastructure Terms

| Term | Definition | Related Page |
|------|-----------|--------------|
| **Smart Lighting** | Connected street and facility lighting systems that automatically adjust brightness, color, and timing based on real-time conditions. | /solutions/smart-lighting/ |
| **Energy Efficiency** | Optimizing energy consumption while maintaining or improving service quality, core principle of Dimonoff solutions. | /solutions/ |
| **Dimming Control** | Automatic reduction of light intensity based on traffic sensors, time of day, or weather conditions. | /products/led-controllers/ |
| **Power Management** | Monitoring and optimizing power consumption across networked devices to reduce operating costs. | /solutions/ |
| **Peak Load Reduction** | Minimizing maximum power demand during high-usage periods through intelligent load distribution. | /solutions/ |

---

## Schema Implementation

### DefinedTermSet JSON-LD Structure

The mu-plugin will generate and inject the following schema structure:

```json
{
  "@context": "https://schema.org",
  "@type": "DefinedTermSet",
  "name": "Smart City & IoT Glossary",
  "description": "Definitions of key IoT and smart city terms used by Dimonoff",
  "url": "https://dimonoff.com/glossary/",
  "hasDefinedTerm": [
    {
      "@type": "DefinedTerm",
      "name": "SCMS",
      "description": "Smart City Management System - Dimonoff's unified platform for managing connected city infrastructure",
      "url": "https://dimonoff.com/glossary/#scms",
      "inDefinedTermSet": "https://dimonoff.com/glossary/"
    },
    // ... additional terms ...
  ]
}
```

### Benefits
- **Knowledge Graph**: Helps Google understand Dimonoff's expertise and terminology
- **Rich Snippets**: Terms may appear in search results with definitions
- **Semantic SEO**: Improves topical authority and entity recognition
- **Related Searches**: May increase visibility in "People also ask" sections

---

## Page Design Recommendations

### Layout
1. **Header Section**
   - Title and description
   - Search functionality (searchable accordion)

2. **Terms Section**
   - Accordion/toggle interface (Elementor Accordion widget)
   - Grouped by category (Products, Concepts, Standards, Energy)
   - Each term shows: definition + internal links

3. **Internal Links**
   - Link term to relevant solution/product pages
   - Use descriptive anchor text for SEO

4. **Footer**
   - "Still have questions?" CTA
   - Link to contact page

### Accessibility
- Semantic HTML headings
- Proper ARIA labels for accordion
- Good color contrast
- Mobile-responsive design

---

## Multilingual Implementation

### Polylang Setup
Create translated versions of the glossary page:
- **EN**: `/glossary/` - English terms
- **FR**: `/glossaire/` - French terms (translated)
- **ES**: `/glosario/` - Spanish terms (translated)

### Translation Notes
- Use industry-standard translations for technical terms
- Keep acronyms (SCMS, DALI, TALQ) consistent
- Translate definitions to match audience understanding

---

## SEO & Content Strategy

### On-Page SEO
- **Target Keywords**: "smart city glossary", "IoT definitions", "lighting terminology", "TALQ standard definition"
- **Meta Tags**: Title (60 chars), Description (160 chars)
- **Headers**: H1 (page title), H2 (term categories), H3 (term names)
- **Internal Links**: 20-30 contextual internal links to solution/product pages

### Linking Strategy
- Link glossary from blog posts and product pages
- Use "defined term" anchor text where appropriate
- Create a "Learn More" section linking to related pages

### Content Updates
- Review and update glossary annually
- Add new terms as Dimonoff product suite evolves
- Monitor search queries for missing terminology

---

## Implementation Checklist

- [ ] Create glossary page in WordPress (EN version)
- [ ] Design page layout in Elementor
- [ ] Install mu-plugin `dimonoff-glossary-schema.php`
- [ ] Create glossary page translations (FR, ES)
- [ ] Test DefinedTermSet schema with Google Structured Data Tester
- [ ] Add internal linking from solution/product pages
- [ ] Submit page to search console
- [ ] Monitor search performance for new keywords
- [ ] Create related blog content (glossary definitions in longer formats)

---

## Success Metrics

- Track glossary page views and bounce rate
- Monitor keyword rankings for "glossary", "definitions", "SCMS", etc.
- Measure click-through rate from glossary to solution pages
- Check for rich snippet impressions in GSC
- Monitor knowledge graph visibility in Dimonoff-related searches
