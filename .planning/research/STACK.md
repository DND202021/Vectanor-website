# Technology Stack

**Project:** Vectanor Website -- Trilingual Completion
**Researched:** 2026-02-18

## Current Stack (Already Deployed)

| Technology | Version | Purpose | Status |
|------------|---------|---------|--------|
| WordPress | Latest | CMS platform | Active |
| Elementor Pro | 3.35.1 | Page builder (visual + JSON API) | Active |
| Hello Elementor | Latest | Minimal theme for Elementor | Active |
| Polylang (Free) | 3.7.7 | Multilingual (FR/EN/ES) | Configured, pages pending |
| Connect Polylang for Elementor | 2.5.5 | Glue plugin: language switcher widget, template translation | Active |
| WPForms Lite | Latest | Contact form builder (free) | Installed, not configured |
| WP Mail SMTP | Latest | Email delivery for form submissions | Installed, not configured |
| Rank Math SEO | Latest | Basic SEO | Active |
| UAE (Ultimate Addons for Elementor) | Latest | Extended Elementor widgets | Active |
| Python (build scripts) | 3.x | Programmatic page deployment via REST API | Active |

## Recommended Approaches for Completion

### 1. Language Switcher in Header

**Approach:** Build header via Elementor Pro Theme Builder (WP Admin UI), add language switcher widget from Connect Polylang for Elementor.

**Confidence:** HIGH -- verified against official plugin docs and WordPress.org listing.

| Step | Action | Tool |
|------|--------|------|
| 1 | Go to Templates > Theme Builder > Header > Add New | WP Admin |
| 2 | Design header with Site Logo, Nav Menu, and Language Switcher widget | Elementor Pro Editor |
| 3 | Configure Language Switcher: horizontal layout, show flags + language codes, hide current language | Elementor Pro Editor |
| 4 | Set display condition: "Entire Site" | Elementor Pro Editor |
| 5 | Create FR header first, then click "+" to create EN and ES translations via Connect Polylang | WP Admin |

**Why this approach:**
- Connect Polylang for Elementor (v2.5.5, updated Dec 2025) provides a native Elementor widget called "Language switcher" in the "General Elements" and "Site" categories.
- The widget supports: show/hide flags, language names, language codes; vertical list, horizontal list, or styled dropdown layouts; SVG scalable flags; full typography controls with normal/hover/active states.
- Template translation is automatic: set display conditions on the FR (default) header only; EN/ES headers inherit conditions via the plugin.
- **This CANNOT be done via REST API** -- Elementor Theme Builder templates (post type `elementor_library`) require specific meta fields (`_elementor_template_type: header`) and display conditions that are not properly exposed via REST API. The header must be built in the WP Admin Elementor editor.

**What NOT to attempt:**
- Do NOT try to create header templates via REST API / Python scripts. The `elementor_library` custom post type's meta fields are not reliably registered for REST API write access, and display conditions are stored in a separate proprietary format.
- Do NOT use a separate "Language Switcher for Elementor & Polylang" plugin -- Connect Polylang for Elementor already includes this functionality and is the maintained, recommended solution.

**Sources:**
- [Connect Polylang for Elementor - WordPress.org](https://wordpress.org/plugins/connect-polylang-elementor/) -- MEDIUM confidence (official plugin listing)
- [How To Translate Elementor with Polylang](https://polylang.pro/how-to-translate-elementor-with-polylang/) -- MEDIUM confidence (official Polylang docs)

---

### 2. Contact Form (WPForms + WP Mail SMTP)

**Approach:** Create a simple contact form in WPForms Lite via WP Admin, configure WP Mail SMTP with "Other SMTP" mailer, embed form via shortcode widget in Elementor.

**Confidence:** HIGH -- well-documented standard WordPress workflow.

#### WPForms Lite Configuration

| Step | Action | Details |
|------|--------|---------|
| 1 | WPForms > Add New > Simple Contact Form template | Creates Name, Email, Message fields |
| 2 | Settings > Notifications > Send To Email | Set to `info@vectanor.com` |
| 3 | Settings > Notifications > From Email | Must match authenticated SMTP domain |
| 4 | Settings > Confirmations | Set thank-you message (in French for default) |
| 5 | Note the form ID (e.g., `[wpforms id="XX"]`) | Needed for embedding |

#### WP Mail SMTP Configuration

| Setting | Value | Notes |
|---------|-------|-------|
| Mailer | Other SMTP | Generic SMTP for custom domain |
| From Email | info@vectanor.com | Must be a real mailbox |
| Force From Email | Checked | Prevents WordPress from overriding |
| From Name | Groupe Vectanor | Display name in emails |
| SMTP Host | Depends on email provider | e.g., smtp.office365.com, smtp.zoho.com |
| Encryption | TLS | Recommended |
| SMTP Port | 587 | Standard TLS port |
| Authentication | On | Required for most providers |
| SMTP Username | info@vectanor.com | The sending email account |
| SMTP Password | App-specific password | NOT the regular account password |

**IMPORTANT:** The SMTP host/port/credentials depend on where `info@vectanor.com` is hosted (Microsoft 365, Google Workspace, Zoho, hosting provider, etc.). This must be determined from the email provider. If using Microsoft 365/Outlook: note that Microsoft is retiring Basic SMTP auth by September 2025 -- use OAuth2 mailer option instead if available.

#### Embedding in Elementor Contact Page

**Two methods available:**

1. **WPForms native widget** (preferred): In Elementor editor, search for "WPForms" in the widget panel, drag it to the page, select the form from the dropdown.

2. **Shortcode widget** (fallback, also works via REST API): Use Elementor's Shortcode widget with `[wpforms id="XX"]`. This can also be pushed via the Python build script as an HTML or shortcode widget in the `_elementor_data` JSON.

**For programmatic deployment via REST API:**
```python
widget("shortcode", {
    "shortcode": '[wpforms id="XX"]',
})
```
Or using the text-editor widget:
```python
widget("text-editor", {
    "editor": '[wpforms id="XX"]',
})
```

**Sources:**
- [WPForms SMTP Setup Guide](https://wpforms.com/docs/how-to-set-up-smtp-using-the-wp-mail-smtp-plugin/) -- MEDIUM confidence
- [WP Mail SMTP Other SMTP Setup](https://wpmailsmtp.com/docs/how-to-set-up-the-other-smtp-mailer-in-wp-mail-smtp/) -- MEDIUM confidence
- [How to Add WPForms to Elementor](https://wpforms.com/docs/how-to-add-wpforms-to-an-elementor-page/) -- MEDIUM confidence

---

### 3. Translated Page Creation (EN/ES)

**Approach:** Create translated pages via WP Admin (Polylang "+" button), then push Elementor content via REST API using existing Python build script pattern.

**Confidence:** HIGH for the hybrid approach; the pure REST API approach has significant caveats.

#### CRITICAL FINDING: Polylang REST API `lang` Parameter is PRO-ONLY

The Polylang REST API documentation explicitly states: **"The feature is available only in Polylang Pro."** This means:

- **CANNOT** set `?lang=en` on REST API page creation with Polylang Free
- **CANNOT** link translations via `?translations[fr]=19` with Polylang Free
- **CAN** use the Languages REST API (`/wp-json/pll/v1/languages`) to list languages (added in free 3.7)
- **CAN** use the Settings REST API (`/wp-json/pll/v1/settings`) to read settings (added in free 3.7)

**Verified against:** [Polylang REST API docs](https://polylang.pro/doc/rest-api/) (states "Pro only"), [GitHub issue #160](https://github.com/polylang/polylang/issues/160) (confirms Pro since 2.2), [Polylang changelog](https://github.com/polylang/polylang/blob/master/changelog.txt).

#### Recommended Workflow (Hybrid: WP Admin + REST API)

**Phase A: Create page shells in WP Admin (manual, one-time)**

| Step | Action | Result |
|------|--------|--------|
| 1 | Go to Pages in WP Admin | See all FR pages with Polylang language columns |
| 2 | For each FR page, click "+" in the EN column | Creates blank EN page linked to FR as translation |
| 3 | For each FR page, click "+" in the ES column | Creates blank ES page linked to FR as translation |
| 4 | Note the new page IDs for EN and ES pages | Needed for Python script |

This gives you ~16 new pages (8 EN + 8 ES), each properly linked to their FR counterpart via Polylang.

**Phase B: Push translated Elementor content via REST API (automated)**

Use the existing `rebuild-wow.py` pattern to push translated `_elementor_data` JSON to each new page:

```python
# Example: push English homepage
EN_PAGES = {
    "accueil": XX,      # EN homepage ID from step 4
    "vision": XX,       # EN vision page ID
    "divisions": XX,    # etc.
    ...
}

def push_page(page_id, elementor_data, status="publish"):
    # Same two-step meta push as existing script
    requests.post(f"{WP_URL}/pages/{page_id}", auth=AUTH, json={
        "status": status,
        "meta": {"_elementor_edit_mode": "builder", "_elementor_template_type": "wp-page"},
    })
    json_str = json.dumps(elementor_data)
    requests.post(f"{WP_URL}/pages/{page_id}", auth=AUTH, json={
        "meta": {"_elementor_data": json_str}
    })
```

The translated content (EN/ES text strings) would be generated via AI translation of the French content objects, then rebuilt into the same Elementor JSON structure with translated strings.

#### Alternative: PHP Snippet Workaround for REST API Language Assignment

A community workaround exists to add `lang` parameter support to Polylang Free's REST API:

```php
// In functions.php or a custom plugin
add_filter('rest_page_query', function($args, $request) {
    $lang = $request->get_param('lang');
    if ($lang) {
        $args['lang'] = $lang;
    }
    return $args;
}, 10, 2);
```

**However, this only enables READING/FILTERING pages by language -- it does NOT enable SETTING language or LINKING translations via REST API.** Language assignment and translation linking require `pll_set_post_language()` and `pll_save_post_translations()` PHP functions that are not triggered by REST API calls in the free version.

**Verdict:** The WP Admin hybrid approach is the correct path. Creating 16 page shells manually takes ~10 minutes and avoids purchasing Polylang Pro ($99/year).

**Sources:**
- [Polylang REST API - Pro Only](https://polylang.pro/doc/rest-api/) -- HIGH confidence (official docs, explicit statement)
- [GitHub Polylang Issue #160](https://github.com/polylang/polylang/issues/160) -- HIGH confidence
- [Community workaround gist](https://gist.github.com/them-es/3ab1aa674fdb1829a3079f09559c8614) -- MEDIUM confidence (community, not official)

---

### 4. Elementor Pro Header/Footer with Theme Builder

**Approach:** Create header/footer templates manually in Elementor Pro Theme Builder (WP Admin), not via REST API.

**Confidence:** HIGH -- this is the standard Elementor Pro workflow.

#### Header Template Structure

```
[Site Logo] ---- [Nav Menu] ---- [Language Switcher]
```

| Component | Elementor Widget | Configuration |
|-----------|-----------------|---------------|
| Logo | Site Logo | Link to homepage, max width ~150px |
| Navigation | Nav Menu | WordPress menu (Appearance > Menus), one per language |
| Language Switcher | Language Switcher (from Connect Polylang) | Horizontal, flags + 2-letter code, hide current |

#### Footer Template Structure

```
[Vectanor Logo (white)]
[Copyright text]
```

Keep the footer simple -- the existing in-page footer sections can be replaced by a proper Theme Builder footer for consistency.

#### Template Translation Workflow

1. Build FR header/footer in Elementor Theme Builder
2. Set display conditions on FR template: "Entire Site"
3. In Templates > Saved Templates, click "+" next to the FR header to create EN translation
4. Translate menu text, keep same layout
5. Repeat for ES
6. Connect Polylang for Elementor automatically serves correct header/footer per language

**Navigation Menus (one per language):**
- Appearance > Menus > Create "Main Menu (FR)", assign to Primary location
- Create "Main Menu (EN)" with translated menu items, assign FR translations
- Create "Main Menu (ES)" with translated menu items, assign FR translations
- Polylang handles menu switching automatically based on current language

**Sources:**
- [Elementor Header/Footer Builder](https://elementor.com/blog/header-footer-builder/) -- MEDIUM confidence
- [Connect Polylang for Elementor - Template Translation](https://wordpress.org/plugins/connect-polylang-elementor/) -- HIGH confidence

---

### 5. Translation Content Strategy

**Approach:** Use AI (Claude or similar) to translate French content, then inject into Elementor JSON structure via Python build script.

**Confidence:** HIGH -- the existing `rebuild-wow.py` already demonstrates this JSON structure.

#### Translation Workflow

1. Extract all French text strings from `rebuild-wow.py` (titles, descriptions, button labels, etc.)
2. Translate to EN and ES using AI
3. Create `rebuild-wow-en.py` and `rebuild-wow-es.py` (or a parameterized version)
4. Push translated content to the EN/ES page IDs

#### What Needs Translation

| Category | Count | Example |
|----------|-------|---------|
| Hero titles | 8 | "Notre vision" -> "Our Vision" |
| Hero subtitles | 8 | "Donner une trajectoire..." -> "Giving direction..." |
| Section headings | ~15 | "Orchestrer la complexite" -> "Orchestrating Complexity" |
| Body paragraphs | ~12 | Division descriptions, philosophy text |
| Button labels | ~20 | "Decouvrir nos divisions" -> "Discover Our Divisions" |
| Card titles/descriptions | ~16 | Feature cards on division pages |
| Contact info text | 3 | Form labels, CTA text |
| Footer text | 2 | Copyright, "Une division du Groupe Vectanor" |

**Keep in French (do not translate):**
- Company name: "Groupe Vectanor"
- Division names: "Dimonoff", "Spatium", "Amotus", "Vigilia"
- Tagline: Keep in original French or provide localized version per language
- Email address: info@vectanor.com

---

## Alternatives Considered

| Category | Recommended | Alternative | Why Not |
|----------|-------------|-------------|---------|
| Multilingual | Polylang Free + WP Admin page creation | Polylang Pro ($99/yr) | Not worth the cost for a one-time page creation of 16 pages; manual WP Admin takes 10 min |
| Multilingual | Polylang Free | WPML ($39+/yr) | Already invested in Polylang setup; WPML is heavier and more expensive |
| Language Switcher | Connect Polylang for Elementor widget | Custom HTML/CSS switcher | Plugin provides native Elementor widget with full styling controls; no custom code needed |
| Contact Form | WPForms Lite + WP Mail SMTP | Elementor Pro Form widget | WPForms Lite is already installed; Elementor Pro forms require Elementor Pro (already have it) but WPForms is simpler to configure for SMTP |
| Contact Form | WPForms Lite + WP Mail SMTP | Contact Form 7 | WPForms is more user-friendly, already installed, has native Elementor widget |
| Email Delivery | WP Mail SMTP (Other SMTP) | PHP mail() | PHP mail() is unreliable on most hosts; SMTP ensures delivery |
| Header/Footer | Elementor Pro Theme Builder | In-page header sections | Theme Builder provides consistent header/footer across ALL pages including translated versions |
| Content Translation | AI + Python script push | Manual Elementor editor editing | 8 pages x 2 languages = 16 pages; manual editing would take hours; script takes minutes |
| Content Translation | AI translation | DeepL/Google Translate | DeepL does NOT work with Elementor (confirmed by Polylang docs); AI translation via script sidesteps this limitation entirely |

## Stack Summary for Roadmap

**No new plugins or tools needed.** Everything required is already installed. The completion work involves:

1. **WP Admin manual work:** Header/footer template creation (Theme Builder), translated page shell creation (Polylang "+"), WPForms configuration, WP Mail SMTP configuration, navigation menus per language
2. **Python script work:** Translating content and pushing to EN/ES page IDs via REST API (same pattern as existing `rebuild-wow.py`)
3. **Configuration only:** WP Mail SMTP settings depend on email provider credentials

## Sources

- [Polylang REST API Documentation](https://polylang.pro/doc/rest-api/) -- HIGH confidence (official, confirms Pro-only)
- [Connect Polylang for Elementor - WordPress.org](https://wordpress.org/plugins/connect-polylang-elementor/) -- HIGH confidence (official plugin listing, v2.5.5, Dec 2025)
- [Polylang GitHub Issue #160 - REST API](https://github.com/polylang/polylang/issues/160) -- HIGH confidence
- [WP Mail SMTP Other SMTP Setup](https://wpmailsmtp.com/docs/how-to-set-up-the-other-smtp-mailer-in-wp-mail-smtp/) -- MEDIUM confidence
- [WPForms Embedding in Elementor](https://wpforms.com/docs/how-to-add-wpforms-to-an-elementor-page/) -- MEDIUM confidence
- [Elementor Theme Builder](https://elementor.com/help/the-elementor-theme-builder/) -- MEDIUM confidence
- [How to Programmatically Create Elementor Posts](https://www.soliddigital.com/blog/how-to-programmatically-create-elementor-posts) -- MEDIUM confidence
- [Polylang 3.7 Features](https://polylang.pro/polylang-pro-3-7-beta1-is-now-available-for-download/) -- MEDIUM confidence
- [Community Polylang REST API workaround](https://gist.github.com/them-es/3ab1aa674fdb1829a3079f09559c8614) -- LOW confidence (community, may break on updates)
