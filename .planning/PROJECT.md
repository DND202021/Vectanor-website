# Vectanor Website

## What This Is

A corporate holding company website for Groupe Vectanor — a strategic parent company orchestrating specialized divisions for smart cities and industrial infrastructure. The site presents the group's vision, its four divisions (Dimonoff, Spatium, Amotus, Vigilia), and provides a contact point. Built on WordPress with Elementor Pro, trilingual (FR/EN/ES) via Polylang.

## Core Value

Visitors immediately understand what Groupe Vectanor is, what each division does, and how to contact the group.

## Requirements

### Validated

- ✓ WordPress site with Elementor Pro page builder — existing
- ✓ Hello Elementor theme activated — existing
- ✓ Polylang multilingual plugin configured (FR/EN/ES) — existing
- ✓ 8 pages built with premium design (Homepage, Vision, Divisions index, Dimonoff, Spatium, Amotus, Vigilia, Contact) — existing
- ✓ Division logos integrated from media library — existing
- ✓ External links to division websites (dimonoff.com, amotus.com) — existing
- ✓ Brand identity applied (navy/blue palette, Montserrat/Inter/Space Grotesk fonts, glassmorphism cards, animated bar) — existing

### Active

- [ ] Language switcher visible in site header (FR/EN/ES via Polylang)
- [ ] Contact form configured and functional (submissions to info@vectanor.com)
- [ ] English translations for all 8 pages (AI-generated from French content)
- [ ] Spanish translations for all 8 pages (AI-generated from French content)
- [ ] Visual polish and consistency pass across all pages

### Out of Scope

- Blog/news section — not needed for a corporate holding page
- E-commerce/shop — no products to sell
- User accounts/login — purely informational site
- Custom WordPress theme development — using Elementor Pro for layout
- SEO optimization campaign — basic Rank Math is installed, deep SEO is separate effort
- Professional human translations — AI translations sufficient for v1

## Context

**Technical environment:**
- WordPress hosted externally behind Cloudflare (no cPanel/SSH access)
- WP Admin: https://vectanor.com/wp-admin (user: dnoiseux)
- REST API with Application Password for programmatic page management
- Pages built by pushing Elementor JSON via `_elementor_data` meta field (write-only via API)
- Two-step meta push required: (1) edit_mode + template_type, (2) _elementor_data separately
- Build scripts in Python (`rebuild-wow.py` is the main script)

**Existing pages (Page IDs):**
| Page | ID | Slug |
|------|----|------|
| Accueil (homepage) | 19 | / |
| Notre vision | 20 | /notre-vision/ |
| Nos divisions | 21 | /divisions/ |
| Dimonoff | 22 | /divisions/dimonoff/ |
| Spatium | 23 | /divisions/spatium/ |
| Amotus | 24 | /divisions/amotus/ |
| Contact | 25 | /contact/ |
| Vigilia | 36 | /divisions/vigilia/ |
| Accueil - English | 30 | (EN homepage stub) |
| Accueil - Español | 31 | (ES homepage stub) |

**Division details:**
| Division | Color | Logo Key | External URL |
|----------|-------|----------|-------------|
| Dimonoff | #F59E0B (amber) | dimonoff | dimonoff.com |
| Spatium | #10B981 (green) | spatium | dimonoff.com (subdivision) |
| Amotus | #8B5CF6 (purple) | amotus | amotus.com |
| Vigilia | #EC4899 (pink) | vigilia | none |

**Brand:**
- Primary palette: #1E3A8A (navy), #3B82F6 (royal blue), #0EA5E9 (sky blue)
- Fonts: Montserrat (headings), Inter (body), Space Grotesk (accents)
- Tagline: "Trace la direction. Les divisions avancent. Les systemes suivent."

**Plugins active:** Elementor 3.35.5, Elementor Pro 3.35.1, Polylang 3.7.7, Connect Polylang for Elementor, Rank Math SEO, UAE, ShortPixel, Safe SVG, Wordfence, WPForms Lite, WP Mail SMTP

## Constraints

- **Hosting**: No server-side access (no SSH, no cPanel) — all changes via WP Admin or REST API
- **Upload limit**: 413 error on large files — use WP File Manager for large uploads
- **Elementor API**: `_elementor_data` is write-only via REST API (reads return empty string)
- **Language**: French is default language; EN/ES are translations linked via Polylang
- **Contact form**: WPForms Lite (free) — submissions must go to info@vectanor.com
- **Theme**: Must use Hello Elementor for clean Elementor integration

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Elementor Pro for page building | Industry-standard visual builder, REST API compatible | ✓ Good |
| Polylang over WPML | Free, available in WP store, sufficient for 3 languages | ✓ Good |
| Python build scripts for deployment | Programmatic control over Elementor JSON, reproducible builds | ✓ Good |
| AI translations over professional | Fast, sufficient for corporate content, can be refined later | — Pending |
| Hello Elementor theme | Minimal theme, removes unwanted footer links, optimal for Elementor | ✓ Good |

---
*Last updated: 2026-02-18 after initialization*
