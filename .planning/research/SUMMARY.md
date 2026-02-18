# Research Summary: Vectanor Website Trilingual Completion

**Domain:** Corporate holding company website -- multilingual completion phase
**Researched:** 2026-02-18
**Overall confidence:** HIGH

## Executive Summary

The Vectanor website is a WordPress + Elementor Pro corporate site for Groupe Vectanor, a holding company with four divisions (Dimonoff, Spatium, Amotus, Vigilia). All 8 French pages are built with premium design (glassmorphism, animations, division color system) and deployed via Python scripts pushing Elementor JSON through the WordPress REST API. The remaining work is completing trilingual support (FR/EN/ES), adding a language switcher, configuring the contact form, and visual polish.

The most critical finding from this research is that **Polylang Free's REST API does NOT support the `lang` and `translations` parameters** -- these are Pro-only features ($99/year). This means translated page shells cannot be created and linked programmatically via REST API. The recommended approach is a hybrid workflow: create page shells manually via WP Admin (Polylang "+" button, ~10 minutes), then push translated Elementor JSON content via REST API using the existing Python build script pattern.

The existing plugin stack (Polylang Free 3.7.7, Connect Polylang for Elementor 2.5.5, WPForms Lite, WP Mail SMTP) is complete -- no new plugins or tools are needed. The header/footer must be built via Elementor Pro Theme Builder in WP Admin (not via REST API), as Theme Builder templates require display conditions and post type registration that are not exposed through the REST API. Connect Polylang for Elementor provides a native language switcher widget that works directly in the Elementor editor with full styling controls.

DeepL machine translation does NOT work with Elementor (confirmed by Polylang docs). The correct approach is AI translation of text strings within the Python build script, producing translated Elementor JSON that is structurally identical to the French version with only text content changed.

## Key Findings

**Stack:** No new tools needed. Hybrid WP Admin + REST API workflow because Polylang Free lacks REST API language assignment.

**Architecture:** Header/footer via Theme Builder (WP Admin only), page content via REST API (Python scripts), contact form via WPForms shortcode embedded in Elementor JSON.

**Critical pitfall:** Polylang REST API `lang` parameter is PRO-ONLY. Do not attempt programmatic language assignment with the free version.

## Implications for Roadmap

Based on research, suggested phase structure:

1. **WP Admin Configuration Phase** - Foundation setup that cannot be automated
   - Addresses: Header/footer templates, navigation menus, WPForms creation, WP Mail SMTP configuration, translated page shells via Polylang "+"
   - Avoids: Pitfall 1 (REST API Pro-only), Pitfall 3 (same-language templates), Pitfall 4 (silent email failure)
   - Duration estimate: 2-3 hours of WP Admin work
   - Deliverables: Header template (FR/EN/ES), footer template, 3 navigation menus, 16 translated page shells (IDs collected), 3 WPForms (one per language), WP Mail SMTP configured and tested

2. **Translation Content Generation Phase** - AI translation + build script modification
   - Addresses: EN/ES content for all 8 pages, parameterized build script with language support
   - Avoids: Pitfall 6 (hardcoded French URLs), Pitfall 9 (DeepL corruption), Pitfall 12 (hardcoded French in components)
   - Duration estimate: 3-4 hours (script modification + AI translation + testing)
   - Deliverables: `rebuild-wow.py` refactored with language parameter, translated content dictionaries, all 16 translated pages pushed

3. **Deployment and QA Phase** - CSS regeneration, cache purging, verification
   - Addresses: Visual consistency, email delivery testing, language switcher functionality, link audit
   - Avoids: Pitfall 2 (stale CSS), Pitfall 5 (homepage redirect loop), Pitfall 11 (Cloudflare cache)
   - Duration estimate: 1-2 hours
   - Deliverables: All pages verified in all 3 languages, contact form tested end-to-end, hreflang tags verified

4. **Polish Phase** - SEO, accessibility, responsive fixes
   - Addresses: SEO meta titles/descriptions, alt text, mobile responsiveness, privacy policy
   - Duration estimate: 2-3 hours
   - Deliverables: Rank Math configured per page per language, mobile-tested, privacy policy page

**Phase ordering rationale:**
- Phase 1 must come first because it creates the infrastructure (headers, page shells, forms) that all subsequent phases depend on
- Phase 2 depends on Phase 1's page IDs and form IDs
- Phase 3 depends on Phase 2's content being pushed
- Phase 4 is independent polish that can technically start in parallel with Phase 2 but is logically last

**Research flags for phases:**
- Phase 1: Needs WP Mail SMTP credentials from the email provider (external dependency, may block)
- Phase 2: Standard patterns, unlikely to need research. The `rebuild-wow.py` pattern is proven.
- Phase 3: May need Cloudflare dashboard access for cache purging (verify access)
- Phase 4: SEO and privacy policy are standard; Rank Math + Polylang hreflang interaction should be verified

## Confidence Assessment

| Area | Confidence | Notes |
|------|------------|-------|
| Stack | HIGH | All plugins already installed; no decisions needed. Polylang Pro-only limitation confirmed against 3 sources. |
| Features | HIGH | Table stakes are clear and well-scoped. Feature dependencies mapped against existing codebase. |
| Architecture | HIGH | Hybrid WP Admin + REST API approach validated. Theme Builder header/language switcher workflow verified against official plugin docs. |
| Pitfalls | HIGH | Critical pitfalls verified against official docs and GitHub issues. Polylang REST API Pro-only is the single most important finding. |

## Gaps to Address

- **WP Mail SMTP credentials:** The SMTP host, port, and credentials for `info@vectanor.com` depend on where this email is hosted. This is an external dependency that must be resolved before the contact form works. Ask the domain owner.
- **Cloudflare dashboard access:** Cache purging after deployment may require Cloudflare access. Verify whether a Cloudflare WordPress plugin is installed or whether dashboard access is available.
- **Polylang URL structure verification:** Confirm that Polylang is configured with "directory name in pretty permalinks" (`/en/`, `/es/` prefixes), NOT cookie-based or browser-detection-based language routing. Browser detection is incompatible with Cloudflare caching.
- **Existing EN/ES stubs:** Pages 30 (EN homepage) and 31 (ES homepage) already exist. Need to verify their language assignment in WP Admin before creating additional translated page shells. May need to verify whether other EN/ES stubs exist.
