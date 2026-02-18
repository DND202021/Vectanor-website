# Roadmap: Vectanor Website

## Overview

Complete the Vectanor corporate holding website by building the site chrome (header/footer with language switcher), translating all 8 pages to English and Spanish via AI-generated content pushed through the REST API, configuring the contact form with SMTP delivery, adding legal and SEO foundations, and polishing responsiveness and visual consistency. Phase 1 handles all WP Admin-only work (templates, page shells, forms, SMTP) since nothing else can proceed without it. Phase 2 generates and deploys translated content. Phase 3 adds legal compliance and SEO. Phase 4 is the final visual and responsive QA pass.

## Phases

**Phase Numbering:**
- Integer phases (1, 2, 3): Planned milestone work
- Decimal phases (2.1, 2.2): Urgent insertions (marked with INSERTED)

Decimal phases appear between their surrounding integers in numeric order.

- [x] **Phase 1: Site Chrome and WP Admin Foundation** - Header/footer templates, language switcher, navigation menus, page shells, contact form, and SMTP configuration via WP Admin
- [ ] **Phase 2: Translation Content Deployment** - AI-translate all 8 pages to EN/ES and push via REST API with correct URL structure and internal links
- [ ] **Phase 3: Legal and SEO** - Privacy policy pages, SEO meta configuration, hreflang tags, Open Graph, and sitemap
- [ ] **Phase 4: Visual Polish and QA** - Mobile responsiveness, typography consistency, alt text, animation performance across all languages

## Phase Details

### Phase 1: Site Chrome and WP Admin Foundation
**Goal**: Visitors see a professional header with navigation and language switcher, a branded footer, and a working contact form -- the site infrastructure that all translated content will plug into
**Depends on**: Nothing (first phase)
**Requirements**: CHRM-01, CHRM-02, CHRM-03, CHRM-04, LANG-01, FORM-01, FORM-02
**Success Criteria** (what must be TRUE):
  1. Every page displays a custom header with site navigation links (Accueil, Vision, Divisions, Contact)
  2. A FR/EN/ES language switcher is visible in the header and switches between language versions
  3. Every page displays a branded footer with copyright and placeholder legal links
  4. Header and footer render correctly on mobile devices (hamburger menu, stacked layout)
  5. Contact form on the French page accepts Name/Email/Subject/Message and delivers to info@vectanor.com via SMTP
**Plans**: 3 plans

Plans:
- [x] 01-01-PLAN.md -- Navigation menus (FR/EN/ES) and header template with language switcher (done manually in WP Admin; user confirmed "ok for now")
- [x] 01-02-PLAN.md -- Footer template with copyright and legal links (implemented per-page via rebuild-wow.py)
- [x] 01-03-PLAN.md -- Contact form with formsubmit.co backend (bypassed WPForms/SMTP; raw HTML push to avoid Elementor caching)

### Phase 2: Translation Content Deployment
**Goal**: English and Spanish visitors can browse all 8 pages in their language with correct URLs, internal links, and localized contact form labels
**Depends on**: Phase 1 (page shells and form IDs must exist)
**Requirements**: LANG-02, LANG-03, LANG-04, LANG-05, FORM-03, FORM-04
**Success Criteria** (what must be TRUE):
  1. All 8 pages exist in English at /en/ prefixed URLs with AI-translated content
  2. All 8 pages exist in Spanish at /es/ prefixed URLs with AI-translated content
  3. Internal links within translated pages point to the correct language version (no links from /en/ pages to French pages)
  4. English contact page has form with English labels; Spanish contact page has form with Spanish labels
**Plans**: 2 plans

Plans:
- [ ] 02-01-PLAN.md -- Create translate-pages.py with all EN/ES content + WP Admin 14 page stubs + fill IDs
- [ ] 02-02-PLAN.md -- Push all 16 translated pages and human verify correct content and links

### Phase 3: Legal and SEO
**Goal**: The site meets Quebec Law 25 privacy requirements and search engines can correctly index all language versions with proper metadata
**Depends on**: Phase 2 (translated pages must exist for per-page SEO and hreflang linking)
**Requirements**: LEGL-01, LEGL-02, LEGL-03, SEO-01, SEO-02, SEO-03, SEO-04
**Success Criteria** (what must be TRUE):
  1. A privacy policy page exists in French, English, and Spanish
  2. Footer on all pages links to the privacy policy in the matching language
  3. Each page (all languages) has a unique meta title and description visible in Rank Math
  4. Hreflang tags on each page correctly reference FR/EN/ES equivalents
  5. XML sitemap includes all pages in all three languages
**Plans**: TBD

Plans:
- [ ] 03-01: TBD
- [ ] 03-02: TBD

### Phase 4: Visual Polish and QA
**Goal**: The site looks polished and consistent across all pages, languages, and devices with no visual regressions
**Depends on**: Phase 3 (all content and pages must be finalized before final polish)
**Requirements**: PLSH-01, PLSH-02, PLSH-03, PLSH-04
**Success Criteria** (what must be TRUE):
  1. All pages render correctly on iOS Safari and Android Chrome (no overflow, no broken layouts)
  2. Typography, spacing, and colors are consistent across all 24+ pages (8 pages x 3 languages)
  3. Every image has a descriptive alt text attribute
  4. Animations and transitions play smoothly without layout shift on desktop and mobile
**Plans**: TBD

Plans:
- [ ] 04-01: TBD

## Progress

**Execution Order:**
Phases execute in numeric order: 1 -> 2 -> 3 -> 4

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Site Chrome and WP Admin Foundation | 3/3 | Complete (with deviations) | 2026-02-18 |
| 2. Translation Content Deployment | 0/2 | Planned | - |
| 3. Legal and SEO | 0/0 | Not started | - |
| 4. Visual Polish and QA | 0/0 | Not started | - |
