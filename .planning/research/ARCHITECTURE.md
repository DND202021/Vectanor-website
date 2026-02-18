# Architecture Research: Vectanor Website Multilingual + Contact Form

**Domain:** WordPress multilingual corporate website (Elementor Pro + Polylang + WPForms)
**Researched:** 2026-02-18
**Confidence:** MEDIUM (verified against official docs and multiple community sources; some Polylang REST API details uncertain due to free vs Pro version ambiguity)

## System Overview

```
+=========================================================================+
|                         VISITOR BROWSER                                  |
|  [vectanor.com/]  [vectanor.com/en/]  [vectanor.com/es/]              |
+============================|============================================+
                             |
+============================v============================================+
|                     WORDPRESS + CLOUDFLARE                              |
|                                                                         |
|  +---------------------------+  +------------------------------------+  |
|  | Elementor Theme Builder   |  | Polylang 3.7.7                    |  |
|  | Header Template (FR)      |  |                                    |  |
|  | Header Template (EN)      |  |  Language Router:                  |  |
|  | Header Template (ES)      |  |  /           -> FR pages           |  |
|  | (linked via Polylang)     |  |  /en/        -> EN pages           |  |
|  | Contains:                 |  |  /es/        -> ES pages           |  |
|  |   - Site Logo             |  |                                    |  |
|  |   - Nav Menu              |  |  Translation DB:                   |  |
|  |   - Language Switcher     |  |  wp_term_taxonomy                  |  |
|  +---------------------------+  |  (post_translations taxonomy)      |  |
|                                 |  Serialized: {fr:19, en:30, es:31} |  |
|  +---------------------------+  +------------------------------------+  |
|  | Connect Polylang for      |                                         |
|  | Elementor Plugin          |  +------------------------------------+  |
|  | - Template routing        |  | Page Content Layer                 |  |
|  | - Language Switcher widget |  |                                    |  |
|  | - Display conditions sync |  | FR Page (ID:19) <---> EN (ID:30)  |  |
|  +---------------------------+  |                  <---> ES (ID:31)  |  |
|                                 | Each page has:                      |  |
|  +---------------------------+  |   _elementor_data (JSON)            |  |
|  | WPForms Lite              |  |   _elementor_edit_mode              |  |
|  | Form ID: [TBD]            |  |   _elementor_template_type         |  |
|  | Fields: Name, Email, Msg  |  +------------------------------------+  |
|  | -> Notification Email     |                                         |
|  +-------------|-------------+                                         |
|                |                                                        |
|  +-------------v-------------+                                         |
|  | WP Mail SMTP              |                                         |
|  | Overrides wp_mail()       |                                         |
|  | -> SMTP server            |                                         |
|  | -> info@vectanor.com      |                                         |
|  +---------------------------+                                         |
+=========================================================================+
```

## Component Boundaries

| Component | Responsibility | Communicates With | Configuration Surface |
|-----------|---------------|-------------------|----------------------|
| **Polylang 3.7.7** | Language routing, translation linking, URL structure (/en/, /es/) | WordPress core, all content | WP Admin > Languages |
| **Elementor Pro Theme Builder** | Global header/footer templates, page layouts | Polylang (via Connect plugin), WordPress theme | Elementor Editor > Theme Builder |
| **Connect Polylang for Elementor** | Bridges Polylang + Elementor: template routing per language, Language Switcher widget | Polylang, Elementor Pro | Automatic (minimal config) |
| **WPForms Lite** | Contact form rendering, field validation, submission handling | WP Mail SMTP (for delivery), Elementor (for embedding) | WP Admin > WPForms |
| **WP Mail SMTP** | Overrides PHP mail with authenticated SMTP, ensures deliverability | WPForms (notification emails), any wp_mail() caller | WP Admin > WP Mail SMTP |
| **Python Build Scripts** | Push Elementor JSON via REST API, 2-step meta field update | WordPress REST API | Local scripts in repo |
| **Hello Elementor Theme** | Minimal theme shell, defers all layout to Elementor | Elementor Pro | WP Admin > Appearance |

## Data Flow: Three Core Flows

### Flow 1: Language Switcher in Header

```
Visitor clicks language flag/link in header
    |
    v
Connect Polylang for Elementor: Language Switcher Widget
    |  (renders flags/names/codes based on widget settings)
    |
    v
Polylang resolves current page's translation group
    |  Query: wp_term_taxonomy WHERE taxonomy='post_translations'
    |  Returns: serialized array {fr: 19, en: 30, es: 31}
    |
    v
Redirect to translated page URL
    |  FR: /contact/
    |  EN: /en/contact/
    |  ES: /es/contact/
    |
    v
Polylang routes to correct page ID
    |
    v
Connect Polylang for Elementor selects matching header template
    |  If visiting /en/contact/:
    |    -> Load EN header template (linked translation of FR header)
    |    -> Load EN page content (page ID from translation group)
    |
    v
Page renders with correct language header + content
```

**Key architectural detail:** The language switcher does NOT simply change the URL prefix. It looks up the specific translated page ID from Polylang's translation group and generates a link to that specific page. If a translation does not exist, the switcher either hides that language option or falls back to the default language page (configurable).

### Flow 2: Translated Page Creation and Linking

**How Polylang stores translations internally (HIGH confidence):**

Polylang uses WordPress's native taxonomy system, NOT custom post meta fields:

1. **Language assignment:** Each post/page gets a term relationship in the `language` taxonomy
   - Table: `wp_term_relationships` (object_id = page_id, term_taxonomy_id = language_term_id)

2. **Translation groups:** Posts are grouped via the `post_translations` taxonomy
   - Table: `wp_term_taxonomy` (taxonomy = 'post_translations')
   - The `description` column contains a PHP-serialized associative array:
     ```
     a:3:{s:2:"fr";i:19;s:2:"en";i:30;s:2:"es";i:31;}
     ```
   - This maps language codes to page IDs within one translation group

3. **Both pages share the same `post_translations` term** via `wp_term_relationships`

**Two methods to create and link translations:**

#### Method A: WP Admin UI (recommended for this project)

```
1. Edit FR page (e.g., Accueil, ID:19) in WP Admin
    |
    v
2. Polylang "Languages" metabox in sidebar shows:
    |  FR: Accueil (current) [pencil icon = edit]
    |  EN: [+ icon = create new] OR [pencil icon = edit existing]
    |  ES: [+ icon = create new] OR [pencil icon = edit existing]
    |
    v
3a. Click [+] to create NEW translation
    |  -> Opens blank page editor, pre-linked to FR original
    |  -> Language auto-set to target language
    |
3b. To link EXISTING page as translation:
    |  -> Edit the existing EN page (ID:30)
    |  -> In Languages metabox, type FR page title in the FR field
    |  -> Autocomplete suggests matching pages
    |  -> Select to link them
    |
    v
4. Polylang creates/updates the post_translations term
    |  wp_term_taxonomy.description = {fr:19, en:30, es:31}
```

#### Method B: REST API (requires Polylang Pro for lang/translations fields)

```
POST /wp/v2/pages/30?lang=en&translations[fr]=19&translations[es]=31

This sets:
  - Page 30's language to English
  - Links it to FR page 19 and ES page 31 as translations
```

**CRITICAL FINDING:** The REST API `lang` and `translations[]` parameters are a **Polylang Pro feature**. The free Polylang (3.7.7) installed on this site exposes the Languages REST API endpoint (`/pll/v1/languages`) but does NOT expose `lang`/`translations` fields on the `/wp/v2/pages` endpoint.

**Confidence:** MEDIUM -- Multiple sources say Pro-only, but Polylang 3.7 expanded some REST APIs to free. Needs live verification.

**Workaround options for free Polylang:**
1. Link translations via WP Admin UI (manual but works)
2. Install `wp-rest-polylang` third-party plugin (read-only, does not write)
3. Write custom PHP snippet using `pll_set_post_language()` and `pll_save_post_translations()` functions via a mu-plugin
4. Upgrade to Polylang Pro (~99 EUR/year)

**Recommended approach:** Use WP Admin UI to link the existing stub pages (IDs 30, 31) to FR originals, then push Elementor content via REST API (which does NOT need Polylang Pro -- `_elementor_data` is plain post meta, language-agnostic).

### Flow 3: Contact Form Submission to Email Delivery

```
Visitor fills out contact form on /contact/ (or /en/contact/, /es/contact/)
    |
    v
WPForms Lite renders form via:
    - Elementor WPForms widget (drag-and-drop in editor), OR
    - Shortcode [wpforms id="X"] in Elementor Shortcode widget, OR
    - Shortcode in Elementor HTML widget
    |
    v
User submits form (client-side validation by WPForms JS)
    |
    v
WPForms processes submission server-side:
    1. Validates fields (honeypot spam check, required fields)
    2. Stores entry in wp_wpforms_entries table (Lite: limited storage)
    3. Triggers notification email
    |
    v
WPForms calls wp_mail() with notification settings:
    - To: info@vectanor.com (configured in WPForms notification settings)
    - From: configured email (must match SMTP sender)
    - Subject: "New Contact Form Submission" (configurable)
    - Body: form field values (Name, Email, Message)
    - Reply-To: visitor's email address (from form field via Smart Tag)
    |
    v
WP Mail SMTP intercepts wp_mail():
    - Overrides PHPMailer configuration
    - Sets SMTP host, port, authentication
    - Sets verified From address
    - Sends via authenticated SMTP connection
    |
    v
SMTP server delivers email to info@vectanor.com
    |
    v
Optional: WPForms shows confirmation message to visitor
    (configurable: message, redirect to page, or show another page)
```

**Key architectural details for the contact form:**

1. **One form, all languages:** WPForms Lite does NOT support multilingual forms natively. The form labels are in the language they are configured in. Options:
   - **Option A (simple):** Create one form with French labels, embed on all language versions (visitors see French form labels even on EN/ES pages)
   - **Option B (proper):** Create 3 separate WPForms (one per language), embed the correct form ID on each language's contact page
   - **Option C (creative):** Use one form with neutral/bilingual labels

2. **WPForms shortcode format:** `[wpforms id="X"]` where X is the form ID assigned by WPForms upon creation

3. **WPForms Elementor widget:** Available in Elementor's widget panel under "WPForms" -- drag/drop, select form from dropdown. This is the cleanest integration but requires the form to already exist.

4. **Embedding via REST API (our case):** Since we push Elementor JSON via Python scripts, we can embed the form using an `html` widget type with the WPForms shortcode, or use the `wpforms` widgetType if available in Elementor's widget registry.

## Recommended Architecture for This Project

### Header Template Strategy

**Use Elementor Pro Theme Builder with Connect Polylang for Elementor:**

1. Create ONE header template in Elementor Theme Builder (FR language)
2. Add to it: Site Logo widget, Nav Menu widget, Language Switcher widget (from Connect Polylang for Elementor)
3. Set display condition: "Entire Site"
4. Create translated versions of this header template for EN and ES (via Polylang's + icon on the template)
5. Connect Polylang for Elementor automatically routes the correct header template per language

**Why this approach:**
- The Connect Polylang for Elementor plugin is already installed
- It handles template routing automatically -- you only set display conditions on the FR (default language) template
- The Language Switcher widget is native to Elementor, fully customizable (flags, names, dropdown)
- No custom code needed

**Header template structure (Elementor JSON):**

```json
{
  "elType": "container",
  "settings": {
    "content_width": "full",
    "flex_direction": "row",
    "flex_justify_content": "space-between",
    "flex_align_items": "center",
    "padding": {"top": "15", "bottom": "15", "left": "30", "right": "30", "unit": "px"},
    "background_background": "classic",
    "background_color": "#0F172A"
  },
  "elements": [
    {"elType": "widget", "widgetType": "theme-site-logo", "settings": {...}},
    {"elType": "widget", "widgetType": "nav-menu", "settings": {...}},
    {"elType": "widget", "widgetType": "language-switcher", "settings": {...}}
  ]
}
```

**IMPORTANT:** Theme Builder templates are NOT regular pages. They are created as `elementor_library` post type with `_elementor_template_type: header`. They CANNOT be pushed via the `/wp/v2/pages` endpoint. They must be created via:
- WP Admin > Elementor > Theme Builder > Add New Header, OR
- REST API: `POST /wp/v2/elementor_library` with appropriate meta fields (if the post type is registered for REST)

### Page Translation Strategy

**Hybrid approach: WP Admin linking + REST API content push**

```
Step 1: In WP Admin, manually link translation stubs
         FR Accueil (19) <-> EN Accueil (30) <-> ES Accueil (31)
         (repeat for all 8 pages x 2 translations = 16 new pages)

Step 2: Create EN/ES page stubs via REST API
         POST /wp/v2/pages  {title: "Our Vision", slug: "our-vision", status: "draft"}
         -> Returns new page ID

Step 3: Link translations via WP Admin
         Edit each FR page, add EN/ES page IDs in Languages metabox

Step 4: Push translated Elementor content via REST API
         Same 2-step push as existing workflow:
         POST /wp/v2/pages/{id}  {meta: {_elementor_edit_mode: "builder", _elementor_template_type: "wp-page"}}
         POST /wp/v2/pages/{id}  {meta: {_elementor_data: "[...]"}}
```

**Page creation alternatives if we can verify REST API lang support:**

```python
# If Polylang REST API works with free version (VERIFY FIRST):
resp = requests.post(f"{WP_URL}/pages?lang=en&translations[fr]=19", auth=AUTH, json={
    "title": "Home",
    "slug": "home",
    "status": "publish",
    "meta": {"_elementor_edit_mode": "builder", "_elementor_template_type": "wp-page"}
})
# This would create page, set language, and link in one call
```

### Contact Form Strategy

**Create per-language forms in WPForms Lite:**

| Form | Language | Embed On | Form ID |
|------|----------|----------|---------|
| Contact FR | French | /contact/ | TBD |
| Contact EN | English | /en/contact/ | TBD |
| Contact ES | Spanish | /es/contact/ | TBD |

All three forms send notifications to `info@vectanor.com`.

**Embedding in Elementor JSON (via Python build script):**

```python
# Replace the placeholder on the contact page with WPForms shortcode
widget("shortcode", {
    "shortcode": '[wpforms id="X"]',
})
# OR using html widget:
widget("html", {
    "html": '[wpforms id="X"]',
})
```

## Build Order Dependencies

```
Phase dependencies (arrows = "must come before"):

1. WP Mail SMTP Configuration
   |  (no dependencies, can be done first)
   |  Configure SMTP server, verify From address
   |
2. WPForms Creation (depends on: WP Mail SMTP)
   |  Create FR contact form, test email delivery
   |  Create EN/ES contact forms
   |
3. Elementor Theme Builder Header (depends on: nothing)
   |  Create FR header template in WP Admin
   |  Add Logo + Nav Menu + Language Switcher
   |  Set display condition: Entire Site
   |
4. Verify Polylang REST API capabilities (depends on: nothing)
   |  Test: GET /wp/v2/pages/19 -- does response include 'lang' field?
   |  Test: POST /wp/v2/pages/30?lang=en -- does it set language?
   |  Result determines automation approach for step 5
   |
5. Create EN/ES page stubs + link translations (depends on: 4)
   |  Create 16 new pages (8 per language)
   |  Link each to FR original via WP Admin or REST API
   |
6. Translate header templates (depends on: 3, 5)
   |  Create EN header template (translation of FR header)
   |  Create ES header template (translation of FR header)
   |  Each gets translated nav menu labels + language switcher
   |
7. Build + push translated page content (depends on: 2, 5, 6)
   |  Translate all Elementor JSON content (FR->EN, FR->ES)
   |  Embed correct WPForms shortcode per language
   |  Push via Python build scripts
   |
8. Test end-to-end (depends on: all above)
      Test language switcher navigates correctly
      Test contact form submits and delivers email
      Test all pages render in correct language
```

**Critical path:** Steps 1-4 can run in parallel. Step 5 must follow step 4. Steps 6-7 must follow step 5. Step 8 is final validation.

## Anti-Patterns to Avoid

### Anti-Pattern 1: Pushing Header Templates via REST API like Regular Pages

**What people do:** Try to create Elementor Theme Builder header/footer templates using `POST /wp/v2/pages` with special meta fields.
**Why it's wrong:** Theme Builder templates are `elementor_library` post type, not `page` post type. The display conditions system, template type registration, and Elementor's internal template manager expect specific post type and meta configuration that differs from regular pages.
**Do this instead:** Create header/footer templates via WP Admin > Elementor > Theme Builder. Use the visual editor for these. Only push page CONTENT via REST API.

### Anti-Pattern 2: One Header Template for All Languages

**What people do:** Create a single header template and hope Polylang translates it automatically.
**Why it's wrong:** The nav menu labels, language switcher display, and any text in the header will remain in the default language. Polylang needs separate template translations to serve language-specific headers.
**Do this instead:** Create the FR header template, then use Polylang's + icon to create EN and ES translations of that template. Connect Polylang for Elementor automatically routes the correct one.

### Anti-Pattern 3: Assuming Polylang Free Has Full REST API Support

**What people do:** Write automation scripts assuming `?lang=en&translations[fr]=19` works on the pages endpoint.
**Why it's wrong:** This feature was historically Polylang Pro only. Polylang 3.7 expanded some REST APIs to the free version, but the `lang`/`translations` parameters on content endpoints may still require Pro.
**Do this instead:** Test the actual endpoint first (`GET /wp/v2/pages/19` and check for `lang` field in response). If absent, fall back to WP Admin UI for linking translations, and only use REST API for pushing `_elementor_data` content.

### Anti-Pattern 4: Hardcoding Internal Links in Translated Content

**What people do:** Translate content and keep `/contact/` as the link URL in EN/ES pages.
**Why it's wrong:** Polylang adds language prefixes to URLs. The EN contact page will be at `/en/contact/` not `/contact/`. Hardcoded FR paths will redirect EN users back to FR pages.
**Do this instead:** Use relative language-aware URLs. If Polylang is configured with URL prefix format (/en/, /es/), internal links in EN content should use `/en/` prefix. Better yet, use Elementor dynamic tags or let Polylang's URL filtering handle it.

### Anti-Pattern 5: Using Elementor Pro Form Widget Instead of WPForms

**What people do:** Use Elementor Pro's built-in Form widget since it seems simpler than a separate plugin.
**Why it's wrong in this context:** The project already has WPForms Lite installed and the architecture calls for WPForms. Mixing form solutions adds complexity. Also, WPForms has better spam protection, entry storage, and notification options in the free tier.
**Do this instead:** Stick with WPForms Lite as already planned. Embed via Elementor's WPForms widget or shortcode.

## Integration Points

### External Services

| Service | Integration Pattern | Gotchas |
|---------|---------------------|---------|
| SMTP Server (for email) | WP Mail SMTP plugin > Settings | From address must match SMTP account; test with real email first |
| Cloudflare | Transparent CDN proxy | May cache pages aggressively; purge cache after translation deploys |
| WordPress REST API | Python scripts with Application Password auth | `_elementor_data` is write-only via API (reads return empty string) |

### Internal Boundaries

| Boundary | Communication | Notes |
|----------|---------------|-------|
| Python scripts <-> WordPress | REST API (POST /wp/v2/pages) | 2-step meta push required; Polylang language linking may need WP Admin |
| Polylang <-> Elementor | Connect Polylang for Elementor plugin | Plugin auto-routes templates; no manual wiring needed after setup |
| WPForms <-> Elementor | WPForms widget in Elementor OR shortcode | WPForms widget appears in Elementor panel only when WPForms is active |
| WPForms <-> WP Mail SMTP | wp_mail() hook override | WP Mail SMTP intercepts all wp_mail() calls including WPForms notifications |
| Header templates <-> Pages | Elementor Theme Builder display conditions | FR header with "Entire Site" condition + Connect plugin = auto language routing |

## Sources

- [Polylang REST API Documentation](https://polylang.pro/documentation/support/developers/rest-api/) - MEDIUM confidence (JS-rendered, could not fully fetch)
- [How Polylang Stores Translations in Database](https://www.epicwpsolutions.com/how-polylang-stores-translations-in-database/) - HIGH confidence (detailed technical deep dive)
- [Connect Polylang for Elementor - GitHub](https://github.com/creame/connect-polylang-elementor) - HIGH confidence (official plugin source)
- [Connect Polylang for Elementor - WordPress.org](https://wordpress.org/plugins/connect-polylang-elementor/) - HIGH confidence
- [Polylang GitHub Issue #160 - REST API](https://github.com/polylang/polylang/issues/160) - HIGH confidence (maintainer confirmed Pro-only at time of writing)
- [Polylang GitHub Issue #140 - Language in REST API](https://github.com/polylang/polylang/issues/140) - HIGH confidence
- [WPForms Notification Setup](https://wpforms.com/docs/setup-form-notification-wpforms/) - HIGH confidence (official docs)
- [WPForms + Elementor Integration](https://wpforms.com/docs/how-to-add-wpforms-to-an-elementor-page/) - HIGH confidence (official docs)
- [WP Mail SMTP - WordPress.org](https://wordpress.org/plugins/wp-mail-smtp/) - HIGH confidence
- [Elementor Header/Footer Builder](https://elementor.com/blog/header-footer-builder/) - HIGH confidence (official docs)
- [Polylang Function Reference](https://polylang.pro/documentation/support/developers/function-reference/) - MEDIUM confidence (could not fully fetch)
- [Polylang Translating Pages Guide](https://polylang.pro/documentation/support/getting-started/translating-pages-posts-categories-and-tags/) - MEDIUM confidence

---
*Architecture research for: Vectanor Website Multilingual + Contact Form Integration*
*Researched: 2026-02-18*
