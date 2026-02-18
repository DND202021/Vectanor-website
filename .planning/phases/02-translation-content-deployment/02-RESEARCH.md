# Phase 2: Translation Content Deployment - Research

**Researched:** 2026-02-18
**Domain:** Polylang REST API, WordPress page creation, AI content translation, formsubmit.co localization, Elementor raw HTML push
**Confidence:** HIGH

## Summary

Phase 2 deploys English and Spanish content to 8 pages each using a hybrid workflow: page shells are created manually in WP Admin (Polylang language assignment is REST API-opaque on the free tier), and content is pushed via Python REST API scripts following the patterns established in Phase 1.

The core constraint is that Polylang's `lang` parameter in the WP REST API is PRO-only — verified by direct API testing showing that `?lang=fr`, `?lang=en`, and `?lang=es` all return the same 10 pages regardless. This means creating pages in the correct language and linking them as Polylang translations of their French originals MUST be done in WP Admin. This is not new information; it was already known from Phase 1 research. What Phase 2 adds is the full scope: only 2 page stubs (homepage) exist for EN and ES — 14 more stubs must be created manually before content can be pushed.

Content deployment follows two patterns established in Phase 1: (1) Elementor JSON push via `push_page()` for Elementor-rendered pages, and (2) raw HTML push (clear `_elementor_edit_mode`) for the contact page. Translated pages will use AI-generated content (Claude or similar LLM) to translate French text into English and Spanish. Internal links within translated pages must point to `/en/` or `/es/` prefixed URLs. Contact pages require localized form labels (different text for each language in the CONTACT_FORM_HTML constant).

**Primary recommendation:** Create a new script `translate-pages.py` that reuses rebuild-wow.py's builder functions but with translated text constants, then push to translated page IDs. Use Claude/AI to generate the translated content strings before coding. The manual WP Admin work (14 page stubs) is the critical blocking dependency.

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|-----------------|
| LANG-02 | All 8 pages have English translations with AI-generated content | Create EN page shells in WP Admin, push Elementor JSON with English content via REST API using rebuild-wow.py pattern. Contact page uses raw HTML bypass. |
| LANG-03 | All 8 pages have Spanish translations with AI-generated content | Same workflow as LANG-02 but with ES text and `/es/` URLs. Spanish contact form uses formsubmit.co with `_next` pointing to `/es/contact/?sent=1`. |
| LANG-04 | Translated pages use URL prefix structure (/en/, /es/) | Confirmed working: Polylang `force_lang=1` (directory mode), `hide_default=true`. `/en/` and `/es/` already serve EN and ES content. Page slug determines the URL path after the language prefix. |
| LANG-05 | Internal links in translated pages point to correct language versions | All CTA buttons and navigation links in the builder functions must use language-prefixed URLs (e.g., `/en/divisions/` not `/divisions/`). The `back_to_group_cta()` function's `/` link must become `/en/` or `/es/` in translated versions. |
| FORM-03 | English contact page has form with English labels | `CONTACT_FORM_HTML` constant must be replicated with English text: "Name", "Email", "Subject", "Message", "Send", dropdown options in English, `_next` redirect to `/en/contact/?sent=1`. |
| FORM-04 | Spanish contact page has form with Spanish labels | Same as FORM-03 but Spanish: "Nombre", "Correo electrónico", "Asunto", "Mensaje", "Enviar", dropdown options in Spanish, `_next` redirect to `/es/contact/?sent=1`. |
</phase_requirements>

## Standard Stack

### Core (No New Dependencies)

| Tool | Version | Purpose | Why Standard |
|------|---------|---------|--------------|
| WordPress REST API | wp/v2 | Create and push page content | Already in use, all patterns established |
| Python 3 + requests | existing | REST API scripting | Already used in rebuild-wow.py |
| formsubmit.co | N/A (hosted) | Contact form backend | Already configured in Phase 1 |
| Claude / AI LLM | N/A | Generate English and Spanish translations | Agreed approach per project requirements |
| rebuild-wow.py | existing | Builder function library | All Elementor patterns already implemented here |

### Supporting

| Tool | Purpose | When to Use |
|------|---------|-------------|
| WP Admin > Pages | Create EN/ES page stubs, assign language, link as translations | Before any REST API content push — this is the blocking dependency |
| Polylang WP Admin UI | Link translated pages to their French originals | Part of page stub creation in WP Admin |
| `pll/v1/languages` endpoint | Verify language configuration (already confirmed: FR/EN/ES active) | Diagnostic only — already verified |

### Alternatives Considered

| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| Manual page stubs + REST content | Polylang REST API lang parameter | PRO-only. Verified: free tier `lang` parameter does not filter and does not assign language on creation. Manual WP Admin approach is the only option. |
| New translate-pages.py script | Modify rebuild-wow.py | Keeping them separate avoids breaking working FR pages. Either works; separate script is cleaner. |
| AI translation per-string | Manual translation | Project decision: AI translations sufficient for v1 per out-of-scope list. Professional translations are explicitly excluded. |
| Separate Elementor data per language | Shared structure, language-swapped text | Separate data per language is simpler and matches the existing push_page() pattern. No risk of accidentally overwriting FR pages. |

## Architecture Patterns

### Confirmed URL Structure (Verified Live)

```
Default language (FR): no prefix
  https://vectanor.com/             -> page 19 (accueil)
  https://vectanor.com/vision/      -> page 20
  https://vectanor.com/divisions/   -> page 21
  https://vectanor.com/contact/     -> page 25
  https://vectanor.com/divisions/dimonoff/ -> page 22
  (etc.)

English: /en/ prefix
  https://vectanor.com/en/          -> routes to page_on_front for EN (page 30)
  https://vectanor.com/en/[slug]/   -> depends on slug assigned when page is created

Spanish: /es/ prefix
  https://vectanor.com/es/          -> routes to page_on_front for ES (page 31)
  https://vectanor.com/es/[slug]/   -> depends on slug assigned when page is created
```

**Slug strategy for EN/ES pages:** When creating stubs in WP Admin, use English/Spanish slugs (e.g., `vision` for the EN vision page, since "vision" works in both English and French). Division pages under `/divisions/` parent: child page slugs stay the same (`dimonoff`, `spatium`, `amotus`, `vigilia`) — these names don't need translation.

**Important:** The EN homepage stub (page 30) currently has slug `accueil-english` which produces URL `/en/accueil-english/`. The `/en/` root redirects there (Polylang's `page_on_front` routing). The slug is ugly but functional. During Phase 2 stub creation, fix the homepage slug to something cleaner, or create the contact/vision/etc. stubs with clean slugs from the start.

### Current Page Inventory (Verified via REST API)

| FR Page | FR ID | FR URL | EN Stub | ES Stub |
|---------|-------|--------|---------|---------|
| Accueil (homepage) | 19 | / | ID=30 at /en/accueil-english/ | ID=31 at /es/accueil-espanol/ |
| Notre vision | 20 | /vision/ | MISSING | MISSING |
| Nos divisions | 21 | /divisions/ | MISSING | MISSING |
| Dimonoff | 22 | /divisions/dimonoff/ | MISSING | MISSING |
| Spatium | 23 | /divisions/spatium/ | MISSING | MISSING |
| Amotus | 24 | /divisions/amotus/ | MISSING | MISSING |
| Contact | 25 | /contact/ | MISSING | MISSING |
| Vigilia | 36 | /divisions/vigilia/ | MISSING | MISSING |

**Total WP Admin work before scripting can begin:** Create 14 page stubs (7 EN + 7 ES), assign language, link as translations of French originals. The homepage stubs (30, 31) already exist but need their slugs cleaned up.

### Pattern 1: Elementor JSON Push (For Pages 1-7, excluding contact)

Reuse `push_page()` from rebuild-wow.py unchanged. Create translated builder functions:

```python
# New file: translate-pages.py
# Imports rebuild_wow or duplicates builder utilities

EN_PAGES = {
    "homepage": 30,  # existing stub, will be content-updated
    "vision": None,  # ID assigned after WP Admin stub creation
    "divisions": None,
    "dimonoff": None,
    "spatium": None,
    "amotus": None,
    "vigilia": None,
}

ES_PAGES = {
    "homepage": 31,
    "vision": None,
    # ...
}

# After WP Admin creates stubs, fill in page IDs and push content:
push_page(EN_PAGES["homepage"], build_homepage_en())
push_page(EN_PAGES["vision"], build_vision_page_en())
# etc.
```

### Pattern 2: Raw HTML Push for Contact Page (LANG-05, FORM-03, FORM-04)

Contact pages use the bypass established in Phase 1: push raw HTML to `content` field, clear `_elementor_edit_mode`. This is the only approach that works reliably for contact (Elementor caching prevents updating via `_elementor_data`).

```python
# Source: Phase 1 discovery (01-03-SUMMARY.md)
def push_raw_html(page_id, html):
    resp = requests.post(f"{WP_URL}/pages/{page_id}", auth=AUTH, json={
        "content": html,
        "status": "publish",
        "meta": {"_elementor_edit_mode": "", "_elementor_data": ""}
    })
    return resp

# English contact form HTML: replace all French strings
EN_CONTACT_FORM_HTML = """
<form action="https://formsubmit.co/info@vectanor.com" method="POST" ...>
  <input type="hidden" name="_subject" value="New message via vectanor.com">
  <input type="hidden" name="_next" value="https://vectanor.com/en/contact/?sent=1">
  <label>Name</label>
  <label>Email</label>
  <label>Subject</label>
  <option>General Inquiry</option>
  <option>Partnership</option>
  <option>Media</option>
  <option>Other</option>
  <label>Message</label>
  <button>Send</button>
  <!-- Success: "Thank you for your message! We will get back to you shortly." -->
</form>
"""

ES_CONTACT_FORM_HTML = """
<form action="https://formsubmit.co/info@vectanor.com" method="POST" ...>
  <input type="hidden" name="_subject" value="Nuevo mensaje via vectanor.com">
  <input type="hidden" name="_next" value="https://vectanor.com/es/contact/?sent=1">
  <label>Nombre</label>
  <label>Correo electrónico</label>
  <label>Asunto</label>
  <option>Consulta general</option>
  <option>Asociación</option>
  <option>Medios</option>
  <option>Otro</option>
  <label>Mensaje</label>
  <button>Enviar</button>
  <!-- Success: "¡Gracias por su mensaje! Le responderemos a la brevedad." -->
</form>
"""
```

**Note on formsubmit.co multi-language:** formsubmit.co activation is per-email address, not per-URL. Since the French form is already activated for `info@vectanor.com`, EN and ES forms will work immediately without re-activation. Only the visible text and `_next` redirect URL differ.

### Pattern 3: Internal Link Translation

All `link` fields in Elementor widget settings must be language-prefixed. Key changes per page type:

```
In EN builder functions:
  /            -> /en/
  /contact/    -> /en/contact/
  /divisions/  -> /en/divisions/
  /divisions/dimonoff/ -> /en/divisions/dimonoff/
  (external links like dimonoff.com, amotus.com: unchanged)

In ES builder functions:
  /            -> /es/
  /contact/    -> /es/contact/
  /divisions/  -> /es/divisions/
  /divisions/dimonoff/ -> /es/divisions/dimonoff/
```

The `back_to_group_cta()` function in division pages has `"link": {"url": "/", ...}` — this must become `/en/` or `/es/` in translated versions.

### Recommended Build Workflow

```
Step 1 (WP Admin - human action):
  Create 14 page stubs in WP Admin:
    For each of: vision, divisions, dimonoff, spatium, amotus, contact, vigilia
      - Create new page with correct slug
      - Set parent page (divisions/* pages need parent = EN divisions page ID)
      - Assign language = English, link as translation of FR page
      - Publish (empty/stub)
    Repeat for Spanish
  Note all 14 new page IDs

Step 2 (Script - update IDs):
  Fill in page IDs in translate-pages.py

Step 3 (Content generation - AI):
  Generate English and Spanish translations of all French content strings
  Translate: headings, body text, button labels, dropdown options, placeholders
  Do NOT translate: brand names (Dimonoff, Spatium, Amotus, Vigilia, Vectanor),
                    technical terms, email addresses, external URLs

Step 4 (Script run):
  python3 translate-pages.py en    # push all 8 EN pages
  python3 translate-pages.py es    # push all 8 ES pages

Step 5 (Verify):
  Visit each EN and ES page URL
  Check internal links point to correct language version
  Submit EN and ES contact forms, verify redirect to correct language success page
```

### Anti-Patterns to Avoid

- **Modifying rebuild-wow.py to also push EN/ES pages:** Risk of accidentally overwriting French pages. Create a separate script.
- **Using Elementor push for the contact pages:** Phase 1 proved this doesn't re-render post_content. Contact pages require raw HTML bypass.
- **Hardcoding French slugs in EN/ES links:** Carefully audit every `link.url` in each builder function. Miss one and a translated page links to French content.
- **Forgetting the parent page for division pages:** In WP Admin, EN divisions/dimonoff page needs parent = EN divisions page (not French). If parent is wrong, URL will be incorrect.
- **Re-activating formsubmit.co for EN/ES:** Not needed. One activation per email address, not per form URL.
- **Using the `lang` REST API parameter to create pages:** Verified to not work on free Polylang tier.

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| Content translation | Custom ML translation | Claude or other LLM via conversation | AI translation is the project decision; quality sufficient for v1 |
| Language assignment on page creation | REST API hack via meta | WP Admin manual page creation | Polylang free tier: REST lang parameter verified non-functional |
| Contact form email delivery | Custom PHP mailer | formsubmit.co (already configured) | Zero-config, already activated for info@vectanor.com, handles EN/ES without changes |
| Language-aware internal links | Dynamic PHP template logic | Static URL prefixes in Python builder | Simpler, reproducible, no server-side dependencies |

**Key insight:** Phase 2 is content work, not architecture work. All the hard infrastructure (Polylang, URL routing, REST API patterns, formsubmit.co) is already in place. The work is: translate text, update links, push content.

## Common Pitfalls

### Pitfall 1: Wrong Parent Page for Division Page Stubs
**What goes wrong:** EN Dimonoff page is created with parent = French Divisions page (ID=21) instead of English Divisions page. The URL becomes `/en/divisions/` correctly at the parent level, but the child's hierarchy is incorrect in Polylang's translation graph.
**Why it happens:** WP Admin page editor "Parent" dropdown shows all pages. Easy to accidentally select the French parent.
**How to avoid:** In WP Admin, create EN divisions page first. Then create EN dimonoff/spatium/amotus/vigilia with EN divisions as parent. Same order for ES.
**Warning signs:** Visiting `/en/divisions/dimonoff/` returns 404 after content push.

### Pitfall 2: Homepage Slug Issue
**What goes wrong:** EN homepage (page 30) has slug `accueil-english` giving URL `/en/accueil-english/`. Internal links in EN pages point to `/en/` (root), which redirects correctly, but the actual URL in the address bar stays `/en/accueil-english/` which looks unprofessional.
**Why it happens:** Phase 1 created the stub with a default slug before this was considered.
**How to avoid:** During Phase 2 WP Admin work, edit page 30 and change its slug to something clean (e.g., `home` or just keep it as is since Polylang's `home_url` for EN is already `https://vectanor.com/en/accueil-english/`). The `/en/` URL redirects correctly for search purposes.
**Warning signs:** CTA buttons say "Go to /en/" but browser shows `/en/accueil-english/` after redirect.
**Recommendation:** Accept the current slug as-is. The redirect from `/en/` to `/en/accueil-english/` is transparent to users. Fixing it risks disrupting Polylang's page_on_front configuration.

### Pitfall 3: Elementor Push for Contact Page Doesn't Re-Render
**What goes wrong:** Developer pushes EN/ES contact page via `push_page()` (Elementor JSON), the API returns success (200), but visiting the page shows the French contact page or blank content.
**Why it happens:** Elementor's rendered `post_content` is not regenerated when `_elementor_data` is updated via REST API. The stored HTML is stale.
**How to avoid:** Use the raw HTML bypass pattern established in Phase 1. Push to `content` field, clear `_elementor_edit_mode` and `_elementor_data`. This is the only reliable approach for updating contact pages.
**Warning signs:** API returns 200, saved char count is large, but browser shows old/blank content.

### Pitfall 4: Internal Links Not Translated
**What goes wrong:** EN visitors on the EN homepage click "Discover our divisions" and land on `/divisions/` (French page) instead of `/en/divisions/`.
**Why it happens:** The builder function's `cta_link="/divisions/"` was not updated to `/en/divisions/` in the English version.
**How to avoid:** Systematically audit every `link.url` and `href` in the translated builder functions. Create a checklist: homepage CTA, division card links, division page "back to group" button, contact CTA button, nav menu links (in header — separate concern).
**Warning signs:** Browser switches to French URL when clicking any CTA on an EN/ES page.

### Pitfall 5: formsubmit.co `_next` Redirect Goes to Wrong Language
**What goes wrong:** After submitting the EN contact form, user sees a French "Merci pour votre message" or gets redirected to `/contact/?sent=1` (French URL) instead of `/en/contact/?sent=1`.
**Why it happens:** The `_next` hidden field in the contact form HTML points to the French success URL.
**How to avoid:** In EN_CONTACT_FORM_HTML, set `_next` to `https://vectanor.com/en/contact/?sent=1`. In ES_CONTACT_FORM_HTML, set to `https://vectanor.com/es/contact/?sent=1`. Also update the JavaScript success detection script that checks `window.location.search` for `sent=1` — this part is language-agnostic.
**Warning signs:** After form submission on EN page, browser redirects to French success URL.

### Pitfall 6: Division Page "Back to Group" Links to French Homepage
**What goes wrong:** EN Dimonoff page footer has a "← Back to group" button linking to `/` (French homepage) instead of `/en/`.
**Why it happens:** The `back_to_group_cta()` function in rebuild-wow.py has `"url": "/"` hardcoded.
**How to avoid:** In the EN builder functions, pass the language prefix to `back_to_group_cta()` or create `back_to_group_cta_en()` and `back_to_group_cta_es()` variants.
**Warning signs:** Clicking "← Back to group" on an EN division page lands on French homepage.

## Code Examples

### Verified: push_page() Works for Regular Pages

```python
# Source: rebuild-wow.py push_page() — verified working for all 8 FR pages
def push_page(page_id, elementor_data, status="publish"):
    json_str = json.dumps(elementor_data)
    requests.post(f"{WP_URL}/pages/{page_id}", auth=AUTH, json={
        "status": status,
        "meta": {"_elementor_edit_mode": "builder", "_elementor_template_type": "wp-page"},
    })
    resp = requests.post(f"{WP_URL}/pages/{page_id}", auth=AUTH, json={"meta": {"_elementor_data": json_str}})
    d = resp.json()
    saved = d.get("meta", {}).get("_elementor_data", "")
    print(f"  -> {d['title']['rendered']}: {len(saved)} chars [{d['status']}]")
```

### Verified: Raw HTML Bypass for Contact Page

```python
# Source: Phase 1 discovery (01-03-SUMMARY.md) — verified working for FR contact page
def push_raw_html(page_id, html):
    resp = requests.post(f"{WP_URL}/pages/{page_id}", auth=AUTH, json={
        "content": html,
        "status": "publish",
        "meta": {"_elementor_edit_mode": "", "_elementor_data": ""}
    })
    d = resp.json()
    print(f"  -> {d.get('title',{}).get('rendered','?')}: raw HTML [{d.get('status','?')}]")
    return resp
```

### Verified: Polylang URL Configuration

```python
# Source: Live API response from pll/v1/settings (verified 2026-02-18)
# force_lang=1 means directory-prefix mode (/en/, /es/)
# hide_default=true means French has no prefix (vectanor.com/, not vectanor.com/fr/)
# default_lang="fr" — French is the canonical/default language

# URL patterns confirmed live:
#   /en/ -> redirects to /en/accueil-english/ (page 30)
#   /es/ -> redirects to /es/accueil-espanol/ (page 31)
#   /en/[slug]/ -> serves EN page with that slug
#   /es/[slug]/ -> serves ES page with that slug
```

### Translation String Approach

```python
# Translate-pages.py structure (recommended pattern)
# French source strings from rebuild-wow.py -> English and Spanish equivalents

# Homepage tagline
FR_TAGLINE = "Trace la direction. Les divisions avancent. Les systèmes suivent."
EN_TAGLINE = "Sets the direction. Divisions advance. Systems follow."  # AI-translated
ES_TAGLINE = "Marca la dirección. Las divisiones avanzan. Los sistemas siguen."  # AI-translated

# Homepage CTA
FR_CTA = "Découvrir nos divisions"
EN_CTA = "Discover our divisions"
ES_CTA = "Descubrir nuestras divisiones"

# Section headings
FR_ORCHESTRER = "Orchestrer la complexité"
EN_ORCHESTRER = "Orchestrating complexity"
ES_ORCHESTRER = "Orquestando la complejidad"

# Division description (abbreviated)
FR_DIMONOFF_DESC = "Éclairage intelligent et infrastructures urbaines connectées."
EN_DIMONOFF_DESC = "Smart lighting and connected urban infrastructure."
ES_DIMONOFF_DESC = "Iluminación inteligente e infraestructura urbana conectada."
```

### EN Contact Form HTML Structure

```python
# Localized contact form for English contact page
# Key differences from FR version in CONTACT_FORM_HTML:
# 1. _subject hidden field: "New message via vectanor.com"
# 2. _next hidden field: "https://vectanor.com/en/contact/?sent=1"
# 3. label text: Name, Email, Subject, Message
# 4. placeholder text: "Your full name", "your@email.com"
# 5. dropdown options: "General Inquiry", "Partnership", "Media", "Other"
# 6. button text: "Send"
# 7. JS success message: "Thank you for your message! We will get back to you shortly."
```

### formsubmit.co - No Re-Activation Needed

```
# Source: formsubmit.co documentation behavior (verified understanding)
# formsubmit.co activation is per EMAIL ADDRESS, not per page or domain
# info@vectanor.com was already activated when the French contact form was submitted
# EN and ES forms pointing to formsubmit.co/info@vectanor.com work immediately
# The _next redirect URL just controls where the user lands after submission
```

## State of the Art

| Old Approach | Current Approach | Impact |
|--------------|------------------|--------|
| Manual copy-paste page translation | AI-generated translation via LLM | Fast, sufficient quality for v1 corporate site |
| Polylang REST API (free) for language assignment | WP Admin manual page creation | Polylang free tier REST API limitations are stable and unlikely to change |
| Elementor push for all page types | Elementor push for content pages + raw HTML bypass for contact | Phase 1 discovery: Elementor REST API does not trigger post_content re-render |

**Current project state (verified 2026-02-18):**
- FR: 8 pages live, all with Elementor content
- EN: 1 page stub (ID=30, homepage, empty content)
- ES: 1 page stub (ID=31, homepage, empty content)
- Polylang: FR/EN/ES active, URL prefix mode, hide_default=true
- formsubmit.co: pending first-form-submission activation for info@vectanor.com

## Open Questions

1. **Exact EN/ES Page IDs After WP Admin Stub Creation**
   - What we know: 14 stubs must be created in WP Admin before scripting
   - What's unclear: The IDs assigned by WordPress (auto-incremented)
   - Recommendation: Plan tasks so IDs are filled in as a variable after WP Admin work. Script should accept IDs as configuration at the top of the file, not hardcoded.

2. **Homepage Slug Cleanup (Page 30: accueil-english)**
   - What we know: `/en/` redirects correctly to `/en/accueil-english/`. The slug is ugly.
   - What's unclear: Whether changing the slug mid-phase breaks Polylang's page_on_front config.
   - Recommendation: Leave as-is during Phase 2. Document as a Phase 4 polish item if needed. Risk of disrupting Polylang routing outweighs cosmetic benefit.

3. **Division Page URL Hierarchy for EN/ES**
   - What we know: FR division pages use `/divisions/[name]/` with parent=21. EN/ES need equivalent.
   - What's unclear: Whether Polylang automatically creates the nested URL or if parent page assignment matters.
   - Recommendation: In WP Admin, create EN/ES divisions stub first, then create child division pages with EN/ES divisions page as parent. This ensures `/en/divisions/dimonoff/` URL structure.

4. **Header Language Switching After Phase 2**
   - What we know: Phase 1 created a single French header. EN/ES header translations were deferred.
   - What's unclear: Whether the language switcher in the header will correctly link to EN/ES pages once they're created, or if EN/ES header templates need to be created first.
   - Recommendation: Creating EN/ES page shells and linking them as Polylang translations should make the language switcher work automatically. Test the switcher after first EN/ES page stubs are created and linked. If switcher shows no options, EN/ES header templates need to be created in WP Admin (Theme Builder > create EN/ES translations of the FR header).

## Sources

### Primary (HIGH confidence)

- Live API: `GET /wp-json/pll/v1/languages` (2026-02-18) — Confirmed FR/EN/ES active, force_lang=1, hide_default=true, default_lang=fr, EN page_on_front=30, ES page_on_front=31
- Live API: `GET /wp-json/pll/v1/settings` (2026-02-18) — Confirmed URL mode, all settings
- Live API: `GET /wp-json/wp/v2/pages?lang=fr` (2026-02-18) — Confirmed returns ALL 10 pages regardless of lang param (PRO-only limitation)
- Live API: `GET /wp-json/wp/v2/pages?per_page=50` (2026-02-18) — Confirmed only 2 EN/ES stubs exist (IDs 30, 31)
- Phase 1 01-03-SUMMARY.md — Raw HTML bypass pattern for contact page, confirmed working
- /workspace/Vectanor-website/rebuild-wow.py — push_page() pattern, CONTACT_FORM_HTML structure, all builder functions

### Secondary (MEDIUM confidence)

- formsubmit.co behavior: activation per email address, not per URL — based on formsubmit.co documentation behavior and Phase 1 implementation. The `_next` redirect is configurable per form.

### Tertiary (LOW confidence)

- Polylang parent page requirement for division URL hierarchy: based on WordPress page hierarchy behavior. If EN dimonoff page has EN divisions as parent, URL should be `/en/divisions/dimonoff/`. Should be verified in WP Admin after stub creation.

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH — All tools already in use, no new dependencies needed
- Architecture: HIGH — URL structure verified live, REST API patterns proven in Phase 1, page inventory confirmed
- Pitfalls: HIGH — Most pitfalls derived from Phase 1 discoveries + direct API testing
- Content generation: MEDIUM — AI translation quality is sufficient per project decision but content strings must be generated before coding

**Research date:** 2026-02-18
**Valid until:** 2026-03-18 (stable domain — Polylang free tier REST API limitations, formsubmit.co behavior, WordPress REST API patterns are all stable)
