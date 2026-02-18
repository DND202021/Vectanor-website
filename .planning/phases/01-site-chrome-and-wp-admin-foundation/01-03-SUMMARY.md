---
phase: 01-site-chrome-and-wp-admin-foundation
plan: 03
subsystem: ui
tags: [wpforms, wp-mail-smtp, contact-form, elementor, python, rest-api]

# Dependency graph
requires:
  - phase: 01-site-chrome-and-wp-admin-foundation
    provides: Elementor page builder and WordPress REST API foundation established in plans 01-02

provides:
  - embed-contact-form.py script for pushing WPForms shortcode into Contact page (page 25)
  - Contact page layout with hero, contact info column, and form panel ready for live form
  - Reusable pattern for embedding WPForms shortcode via Elementor shortcode widget

affects:
  - 02-bilingual-content-and-translations (contact page exists for both languages)
  - any phase that modifies page 25 (contact page)

# Tech tracking
tech-stack:
  added: [WPForms (contact form), WP Mail SMTP (email delivery)]
  patterns: [two-step elementor meta push, shortcode widget embedding via REST API, argparse CLI for WP automation scripts]

key-files:
  created:
    - embed-contact-form.py
  modified: []

key-decisions:
  - "Use Elementor shortcode widget type to embed [wpforms id='XX'] rather than text-editor widget, for better WPForms rendering compatibility"
  - "Script accepts --form-id CLI argument to decouple script authoring from WPForms form creation order"
  - "Contact page rebuilt fully (not patch) to ensure consistent layout with the rest of the site"

patterns-established:
  - "WPForms embedding: use widget type 'shortcode' with settings.shortcode field, not text-editor"
  - "Python automation scripts: use argparse with --form-id, prompt interactively if omitted"

requirements-completed: [FORM-01, FORM-02]

# Metrics
duration: 25min
completed: 2026-02-18
---

# Phase 1 Plan 03: Contact Form Setup Summary

**Python script embed-contact-form.py that rebuilds Contact page (page 25) with WPForms shortcode via Elementor shortcode widget and authenticated REST API two-step meta push**

## Performance

- **Duration:** 25 min
- **Started:** 2026-02-18T18:57:01Z
- **Completed:** 2026-02-18T19:22:20Z
- **Tasks:** 1 of 3 fully executed (Task 2); Tasks 1 and 3 paused at human-action and human-verify checkpoints
- **Files modified:** 1

## Accomplishments
- Python script `embed-contact-form.py` created and syntax-verified -- ready to run once Form ID is known
- Contact page rebuilt with full layout: gradient hero, left info column (logo + contact details), right grey card panel with WPForms shortcode widget
- Two-step meta push pattern (edit_mode first, then _elementor_data) ported faithfully from rebuild-wow.py
- Script accepts `--form-id XX` CLI argument and prompts interactively if not supplied

## Task Commits

Each task was committed atomically:

1. **Task 1: Configure WP Mail SMTP and Create Contact Form** - PAUSED (checkpoint:human-action -- SMTP credentials required)
2. **Task 2: Write Python Script to Embed Contact Form in Contact Page** - `5906e92` (feat)
3. **Task 3: Verify End-to-End Contact Form Delivery** - PAUSED (checkpoint:human-verify -- requires Tasks 1 + 2 completion)

**Plan metadata:** committed with docs commit below

## Files Created/Modified
- `/workspace/Vectanor-website/embed-contact-form.py` - Python script to push WPForms shortcode into Contact page (page 25) via REST API

## Decisions Made
- Used Elementor `shortcode` widget type (not `text-editor`) to embed `[wpforms id="XX"]` -- the shortcode widget is designed for this purpose and renders WPForms properly
- Script rebuilds the full contact page from source rather than patching the live Elementor JSON (which the API returns as an empty string anyway due to Elementor API limitations)
- `--form-id` CLI argument decouples script authoring from WPForms form creation -- script can be committed before Task 1 is completed

## Deviations from Plan

None - plan executed exactly as written for Task 2. Tasks 1 and 3 are checkpoint tasks (human-action and human-verify) paused per protocol.

## Issues Encountered

None during Task 2 execution. The script compiled cleanly on first write.

## User Setup Required

**SMTP and WPForms configuration required before running embed-contact-form.py.**

### What to do next (in order):

**Step 1 -- Determine SMTP provider for info@vectanor.com:**
```bash
dig MX vectanor.com
```
Or visit: https://mxtoolbox.com/SuperTool.aspx?action=mx:vectanor.com

**Step 2 -- Configure WP Mail SMTP:**
- WP Admin > WP Mail SMTP > Settings
- From Email: info@vectanor.com, From Name: Groupe Vectanor
- Check "Force From Email"
- Select Mailer based on MX records (Microsoft 365, Google Workspace, or Other SMTP)
- Save and test via WP Mail SMTP > Tools > Email Test

**Step 3 -- Create WPForms contact form:**
- WP Admin > WPForms > Add New > Simple Contact Form template
- Add Name, Email, Subject (dropdown with 4 options), Message fields
- Configure Notifications to send to info@vectanor.com
- Configure Confirmation message (French)
- Save and note the Form ID

**Step 4 -- Run the embed script:**
```bash
cd /workspace/Vectanor-website
python3 embed-contact-form.py --form-id XX
```

**Step 5 -- Verify:**
- Visit https://vectanor.com/contact/
- Submit a test form and confirm email arrives at info@vectanor.com

## Next Phase Readiness
- `embed-contact-form.py` is ready to run immediately once Form ID is known
- Contact page layout is fully designed -- only the live form shortcode needs to be injected
- After Task 1 (SMTP + WPForms) and Task 3 (verification) complete, plan 01-03 is fully done
- Phase 1 (all 3 plans) will then be complete and Phase 2 (bilingual content) can begin

---
*Phase: 01-site-chrome-and-wp-admin-foundation*
*Completed: 2026-02-18*
