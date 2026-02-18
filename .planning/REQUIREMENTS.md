# Requirements: Vectanor Website

**Defined:** 2026-02-18
**Core Value:** Visitors immediately understand what Groupe Vectanor is, what each division does, and how to contact the group — in their language.

## v1 Requirements

### Multilingual

- [ ] **LANG-01**: Site displays language switcher in header (FR/EN/ES) accessible from every page
- [ ] **LANG-02**: All 8 pages have English translations with AI-generated content
- [ ] **LANG-03**: All 8 pages have Spanish translations with AI-generated content
- [ ] **LANG-04**: Translated pages use URL prefix structure (/en/, /es/)
- [ ] **LANG-05**: Internal links in translated pages point to correct language versions

### Contact Form

- [ ] **FORM-01**: Contact page has functional form with fields: Name, Email, Subject, Message
- [ ] **FORM-02**: Form submissions deliver to info@vectanor.com via authenticated SMTP
- [ ] **FORM-03**: English contact page has form with English labels
- [ ] **FORM-04**: Spanish contact page has form with Spanish labels

### Site Chrome

- [ ] **CHRM-01**: Custom Elementor header with site navigation and language switcher
- [ ] **CHRM-02**: Custom Elementor footer with copyright, legal links, and Vectanor branding
- [ ] **CHRM-03**: Header and footer are mobile-responsive
- [ ] **CHRM-04**: Header and footer display in correct language per page

### SEO

- [ ] **SEO-01**: Each page has unique meta title and description via Rank Math
- [ ] **SEO-02**: Hreflang tags correctly link FR/EN/ES page equivalents
- [ ] **SEO-03**: Open Graph meta tags with branded image for social sharing
- [ ] **SEO-04**: XML sitemap includes all language versions

### Legal

- [ ] **LEGL-01**: Privacy policy page exists in French (Quebec Law 25 compliance)
- [ ] **LEGL-02**: Privacy policy translated to EN and ES
- [ ] **LEGL-03**: Footer links to privacy policy on all pages

### Visual Polish

- [ ] **PLSH-01**: All pages verified mobile-responsive (iOS Safari, Android Chrome)
- [ ] **PLSH-02**: Consistent typography, spacing, and color usage across all pages
- [ ] **PLSH-03**: All images have descriptive alt text
- [ ] **PLSH-04**: Animations perform smoothly without layout shift

## v2 Requirements

### Enhanced Contact

- **FORM-05**: Division-specific contact routing (dropdown selects division)
- **FORM-06**: Auto-reply confirmation email to sender

### SEO Advanced

- **SEO-05**: Schema.org Organization structured data
- **SEO-06**: Google Search Console configured and verified

### Accessibility

- **A11Y-01**: WCAG 2.1 AA compliance audit
- **A11Y-02**: Keyboard navigation verified for all interactive elements

## Out of Scope

| Feature | Reason |
|---------|--------|
| Blog/news section | Not needed for corporate holding page |
| E-commerce/shop | No products to sell |
| User accounts/login | Purely informational site |
| Live chat widget | Overkill for corporate holding; contact form sufficient |
| Newsletter/email capture | Not a marketing site |
| IP-based language detection | Incompatible with Cloudflare caching |
| Social media feeds | Adds complexity and third-party dependencies |
| Custom WordPress theme | Hello Elementor + Elementor Pro is sufficient |
| Professional human translations | AI translations sufficient for v1, can refine later |

## Traceability

| Requirement | Phase | Status |
|-------------|-------|--------|
| LANG-01 | Phase 1 | Pending |
| LANG-02 | Phase 2 | Pending |
| LANG-03 | Phase 2 | Pending |
| LANG-04 | Phase 2 | Pending |
| LANG-05 | Phase 2 | Pending |
| FORM-01 | Phase 1 | Pending |
| FORM-02 | Phase 1 | Pending |
| FORM-03 | Phase 2 | Pending |
| FORM-04 | Phase 2 | Pending |
| CHRM-01 | Phase 1 | Pending |
| CHRM-02 | Phase 1 | Pending |
| CHRM-03 | Phase 1 | Pending |
| CHRM-04 | Phase 1 | Pending |
| SEO-01 | Phase 3 | Pending |
| SEO-02 | Phase 3 | Pending |
| SEO-03 | Phase 3 | Pending |
| SEO-04 | Phase 3 | Pending |
| LEGL-01 | Phase 3 | Pending |
| LEGL-02 | Phase 3 | Pending |
| LEGL-03 | Phase 3 | Pending |
| PLSH-01 | Phase 4 | Pending |
| PLSH-02 | Phase 4 | Pending |
| PLSH-03 | Phase 4 | Pending |
| PLSH-04 | Phase 4 | Pending |

**Coverage:**
- v1 requirements: 24 total
- Mapped to phases: 24
- Unmapped: 0

---
*Requirements defined: 2026-02-18*
*Last updated: 2026-02-18 after roadmap creation*
