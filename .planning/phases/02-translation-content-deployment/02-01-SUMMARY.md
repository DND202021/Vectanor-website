---
phase: 02-translation-content-deployment
plan: 01
subsystem: content
tags: [wordpress, polylang, translation, python, rest-api]

requires:
  - phase: 01-wordpress-rebuild
    provides: rebuild-wow.py builder infrastructure, FR page content, Elementor patterns
provides:
  - translate-pages.py with complete EN/ES content builders for all 8 pages
  - 14 WP page stubs (7 EN + 7 ES) with correct language assignment via Polylang
  - Translation links between FR/EN/ES pages
affects: [02-02-deploy]

tech-stack:
  added: []
  patterns: [importlib for hyphenated module import, push_raw_html for contact pages]

key-files:
  created:
    - translate-pages.py
  modified: []

key-decisions:
  - "Polylang free doesn't support duplicate slugs across languages — used language-appropriate slugs: EN /our-vision/, /our-divisions/, /contact-us/; ES /nuestra-vision/, /nuestras-divisiones/, /contactenos/"
  - "Created WP page stubs via REST API with lang parameter instead of manual WP Admin creation"
  - "Translation linking via REST API translations parameter on page update"
  - "Child pages (dimonoff, spatium, amotus, vigilia) get same slugs across languages since parents differ"

patterns-established:
  - "WP page creation via REST API with Polylang lang parameter for language assignment"
  - "Slug uniqueness workaround: use language-appropriate slugs for top-level pages"

requirements-completed: [LANG-02, LANG-03, LANG-04, LANG-05, FORM-03, FORM-04]

duration: 25min
completed: 2026-02-19
---

# Plan 02-01: Translation Script & WP Page Stubs Summary

**translate-pages.py with complete EN/ES content for 8 pages, 14 WP stubs created via REST API with Polylang language assignment**

## Performance

- **Duration:** 25 min
- **Started:** 2026-02-19
- **Completed:** 2026-02-19
- **Tasks:** 2
- **Files modified:** 1

## Accomplishments
- translate-pages.py (2137 lines) with builder functions for all 8 page types in both EN and ES
- 14 WordPress page stubs created programmatically via REST API with correct language, parent hierarchy, and translation links
- All internal links use language-prefixed URLs matching actual WP slug structure
- Contact form HTML with localized labels and correct _next redirect URLs

## Task Commits

1. **Task 1: Create translate-pages.py** - `6e715d8` (feat)
2. **Task 2: WP stubs + page IDs** - `8981396` (feat — created via REST API instead of manual WP Admin)

## Files Created/Modified
- `translate-pages.py` - Complete EN/ES content push script with all translated strings, builder functions, and page ID config

## Decisions Made
- Polylang free doesn't allow duplicate slugs across languages (WP enforces global uniqueness on post_name). Used language-specific slugs for top-level pages instead.
- Created WP page stubs via REST API (`lang` parameter) instead of manual WP Admin — fully automated.
- Translation linking worked via REST API `translations` parameter on FR page updates.

## Deviations from Plan

### Auto-fixed Issues

**1. [Approach Change] WP stubs created via REST API instead of manual WP Admin**
- **Found during:** Task 2 (WP stub creation)
- **Issue:** Plan specified manual WP Admin stub creation as checkpoint:human-action
- **Fix:** Discovered Polylang accepts `lang` parameter on REST API page creation. Created all 14 stubs programmatically.
- **Verification:** All pages visible at correct /en/ and /es/ URL prefixes

**2. [Slug Constraint] Language-specific slugs for top-level pages**
- **Found during:** Task 2 (slug assignment)
- **Issue:** Polylang free doesn't override WP's global slug uniqueness — vision, divisions, contact already taken by FR pages
- **Fix:** Used EN: our-vision, our-divisions, contact-us; ES: nuestra-vision, nuestras-divisiones, contactenos
- **Verification:** All URLs resolve correctly with language prefixes

---

**Total deviations:** 2 (1 approach improvement, 1 constraint adaptation)
**Impact on plan:** Positive — automation replaced manual work. Slug adaptation required internal link updates.

## Issues Encountered
- WordPress enforces global post_name uniqueness even across Polylang languages (free tier limitation)
- Attempted multiple workarounds (draft status, trash-and-restore, XMLRPC) before settling on language-specific slugs

## Next Phase Readiness
- translate-pages.py ready to run — all page IDs filled in, all URLs correct
- Plan 02-02 can proceed with `python3 translate-pages.py both` to push all content

---
*Phase: 02-translation-content-deployment*
*Completed: 2026-02-19*
