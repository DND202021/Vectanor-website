# Domain Pitfalls

**Domain:** WordPress multilingual corporate website (Polylang + Elementor Pro + WPForms + REST API)
**Project:** Groupe Vectanor website -- finishing multilingual support, contact form, and language switcher
**Researched:** 2026-02-18

---

## Critical Pitfalls

Mistakes that cause broken pages, lost work, or require significant rework.

---

### Pitfall 1: Polylang Free Does NOT Support REST API Language Assignment

**What goes wrong:** Developer writes a Python script that creates pages via REST API with `?lang=en&translations[fr]=19`, expecting Polylang to assign language and link translations automatically. The `lang` and `translations` parameters are silently ignored. Pages are created as additional French (default language) pages with no translation links.

**Why it happens:** The Polylang REST API documentation explicitly states: **"The feature is available only in Polylang Pro."** The `lang` and `translations` query parameters on `/wp/v2/posts` and `/wp/v2/pages` endpoints are a Pro-only feature, added in Polylang Pro 2.2. Multiple blog posts and community examples show these parameters without mentioning the Pro requirement. Polylang 3.7 added Languages (`/pll/v1/languages`) and Settings (`/pll/v1/settings`) REST endpoints to the free version, creating further confusion about scope.

**Consequences:**
- Pages exist but are all assigned to the default language (French)
- Language switcher shows no EN/ES options because no translation links exist
- Hreflang tags are missing for EN/ES versions
- All "translation" pages appear as duplicate French content in WP Admin
- Must manually reassign languages and re-link translations in WP Admin, or purchase Polylang Pro

**Prevention:**
1. Do NOT attempt `?lang=en&translations[fr]=19` with Polylang Free -- it will not work
2. Use the **hybrid approach**: create page shells via WP Admin using Polylang's "+" button (which properly assigns language and creates translation links), then push `_elementor_data` content via REST API
3. The `_elementor_data` meta field push does NOT require Polylang Pro -- it is standard WordPress post meta
4. Creating 16 page shells manually (8 EN + 8 ES) takes approximately 10 minutes in WP Admin

**Detection:** In WP Admin > Pages, check the Polylang language columns. If new pages show FR flag instead of EN/ES, language was not assigned. Also: `GET /wp/v2/pages/{id}` -- if the response does not contain a `lang` field at all, the Polylang REST API integration is not active for the free version.

**Confidence:** HIGH -- verified directly against:
- [Polylang REST API docs](https://polylang.pro/doc/rest-api/) which states "The feature is available only in Polylang Pro."
- [GitHub Issue #160](https://github.com/polylang/polylang/issues/160) confirms REST API was added in Pro 2.2
- [Polylang changelog](https://github.com/polylang/polylang/blob/master/changelog.txt) consistently labels REST API as "Pro" feature

**Phase:** Translation page creation (must decide approach BEFORE writing any build scripts)

---

### Pitfall 2: Elementor CSS Not Regenerated After REST API Content Push

**What goes wrong:** After pushing `_elementor_data` via REST API, pages render with broken or missing styles on the frontend. The layout structure appears but colors, spacing, fonts, and custom CSS are absent or stale.

**Why it happens:** Elementor generates per-page CSS files stored in `wp-content/uploads/elementor/css/`. When content is updated via REST API, Elementor does not automatically regenerate these CSS files -- it only does so when a page is saved through the Elementor editor UI. The existing CSS files become stale or nonexistent for new pages.

**Consequences:**
- Translation pages display raw unstyled HTML structure
- Inconsistent appearance between FR (styled via editor) and EN/ES (pushed via API)
- Users see broken layout on translated pages
- With Cloudflare caching, even after regeneration the old CSS may persist

**Warning signs:**
- Translated pages look "bare" compared to French originals
- Browser DevTools shows 404 for CSS files like `post-{id}.css` in `/wp-content/uploads/elementor/css/`
- Styles only appear after visiting WP Admin > Elementor > Tools > Regenerate CSS

**Prevention:**
1. After pushing all translation pages via REST API, go to WP Admin > Elementor > Tools > Regenerate CSS & Data
2. After regenerating, purge Cloudflare cache
3. Open each translated page in Elementor editor at least once and click "Update" to force CSS generation (fallback if regeneration does not work)

**Detection:** After pushing content, visit each translated page in an incognito browser window and check for missing styles.

**Confidence:** HIGH -- well-documented Elementor behavior confirmed by [multiple GitHub issues](https://github.com/elementor/elementor/issues/21246).

**Phase:** After every REST API content push

---

### Pitfall 3: Elementor Theme Builder Templates Show Same Language Across All Pages

**What goes wrong:** The Elementor Pro header/footer template (containing navigation menu and language switcher) displays the same language content regardless of which translation the visitor is viewing. French header appears on English pages.

**Why it happens:** Elementor Theme Builder templates are custom post types. Without language awareness, Elementor applies the same header/footer template globally. Elementor's display conditions do not natively support Polylang language filtering -- this was [officially declined in 2018](https://github.com/elementor/elementor/issues/4839). The "Connect Polylang for Elementor" plugin bridges this gap, but requires specific configuration.

**Consequences:**
- Navigation menu shows French labels on English pages
- Language switcher in header does not reflect current language state
- If header template is not set as translatable in Polylang settings, translations cannot be created for it

**Prevention:**
1. Ensure "Connect Polylang for Elementor" plugin is active (it is already installed)
2. Create the header template in French first, set display conditions to "Entire Site"
3. Use the "+" icon in Polylang's translation column next to the template to create EN/ES translations
4. Connect Polylang for Elementor auto-generates display conditions for translated templates -- no need to set conditions on EN/ES templates
5. Each translated header template should have its own Nav Menu widget pointing to the correct language menu

**Detection:** Visit the site in each language and verify the header/footer text matches the current language.

**Confidence:** HIGH -- most commonly reported issue in the Polylang+Elementor ecosystem. [Connect Polylang for Elementor](https://wordpress.org/plugins/connect-polylang-elementor/) specifically addresses this.

**Phase:** Theme Builder / language switcher setup (must be done before translation pages are visible)

---

### Pitfall 4: WPForms Email Delivery Fails Silently

**What goes wrong:** Contact form submissions appear to succeed (user sees success message), but no email arrives at info@vectanor.com. No error is logged, no bounce notification -- emails simply vanish.

**Why it happens:** WordPress's default `wp_mail()` function sends unauthenticated email through the web server's local mail function. Without proper SMTP configuration:
1. The hosting server may not have a mail transfer agent configured
2. Without SPF/DKIM/DMARC records, even if sent, emails land in spam
3. The From address may not match the SMTP server's authorized domain
4. Behind Cloudflare, if DNS mail records are proxied (orange cloud), SMTP breaks

**Consequences:**
- Potential clients contact the company but get no response
- No notification that emails are failing (silent failure)
- Damage to business reputation and lost leads

**Prevention:**
1. Configure WP Mail SMTP BEFORE activating the contact form
2. Use "Other SMTP" with the same email provider that hosts info@vectanor.com
3. The From Email in WP Mail SMTP must match (or be authorized by) the SMTP server's domain
4. Send a test email via WP Mail SMTP > Tools > Email Test immediately after configuration
5. Check both inbox AND spam folder of info@vectanor.com
6. In Cloudflare DNS, ensure mail-related records use grey cloud (DNS only), never proxied
7. If using Microsoft 365: note that Microsoft is retiring Basic SMTP auth -- use OAuth2 mailer option

**Detection:** WP Mail SMTP has an "Email Test" tool in WP Admin. Use it. After sending a test form submission, verify the email arrives within 5 minutes.

**Confidence:** HIGH -- extensively documented by [WP Mail SMTP](https://wpmailsmtp.com/wpforms-not-sending-email/).

**Phase:** Contact form configuration (should be done and verified before the site goes "complete")

---

### Pitfall 5: Polylang Static Front Page Misconfiguration Causes Redirect Loops

**What goes wrong:** After creating translation homepages (EN/ES), the language switcher on the homepage redirects to the default French homepage instead of the English/Spanish version. Or worse, an infinite redirect loop occurs.

**Why it happens:** Polylang treats the static front page specially. WordPress Reading Settings must point to the French homepage (page 19), and Polylang internally maps the translated page IDs. If the static front page is set before translations are linked, or if translation linking is incomplete, Polylang cannot resolve the homepage for other languages.

**Consequences:**
- Visitors clicking EN/ES in language switcher loop back to French homepage
- Potential infinite redirect (browser shows "too many redirects" error)
- SEO crawlers index incorrect homepage for each language

**Prevention:**
1. Create all translation homepage pages first (EN page 30, ES page 31 already exist)
2. Assign languages and link all three as translations of each other via WP Admin
3. THEN verify the static front page in Settings > Reading (should be page 19, the FR version)
4. Verify each URL resolves: `vectanor.com/` (FR), `vectanor.com/en/` (EN), `vectanor.com/es/` (ES)
5. Do NOT use the Customizer to set the front page -- use Settings > Reading

**Detection:** After setup, visit `vectanor.com/en/` directly -- it should show the English homepage content, not redirect to `vectanor.com/`.

**Confidence:** HIGH -- documented in [Polylang's official guide](https://polylang.pro/documentation/support/getting-started/define-your-home-page-as-a-static-front-page/).

**Phase:** Homepage translation setup

---

## Moderate Pitfalls

### Pitfall 6: Internal Links in Elementor Data Not Updated for Translation Pages

**What goes wrong:** French pages have internal links like `/divisions/`, `/contact/`, `/notre-vision/`. When the same Elementor JSON is pushed to EN/ES translation pages, these links still point to French URLs. English visitors clicking "Learn more" on the English homepage go to the French divisions page.

**Why it happens:** The Python build scripts generate Elementor JSON with hardcoded French URLs. Polylang does NOT automatically rewrite internal links in Elementor data.

**Prevention:**
1. Build a URL mapping table for each language:
   ```python
   LANG_PREFIX = {"fr": "", "en": "/en", "es": "/es"}
   def internal_link(path, lang):
       return f"{LANG_PREFIX[lang]}{path}"
   ```
2. Before pushing translation content, update ALL `"url"` values in the Elementor JSON
3. For CTA buttons, "back to group" links, and division page links, ensure each language version points to the correct translated URL

**Detection:** After pushing translated pages, click every internal link on each translated page to verify it goes to the correct language version.

**Confidence:** HIGH -- inherent to the project's architecture. The `rebuild-wow.py` script hardcodes French URLs throughout.

---

### Pitfall 7: Two-Step Meta Push Sequence Must Be Maintained for All Pages

**What goes wrong:** Pushing `_elementor_data` in a single API call along with `_elementor_edit_mode` and `_elementor_template_type` causes the Elementor data to be silently dropped or corrupted. Page shows blank content.

**Why it happens:** The `_elementor_edit_mode: "builder"` and `_elementor_template_type: "wp-page"` meta must be set BEFORE `_elementor_data` is written. When sent together, race conditions in meta processing can cause `_elementor_data` to be rejected.

**Prevention:** Maintain the two-step push pattern already used in `push_page()`:
- Step 1: `POST /wp/v2/pages/{id}` with `meta: {_elementor_edit_mode: "builder", _elementor_template_type: "wp-page"}`
- Step 2: `POST /wp/v2/pages/{id}` with `meta: {_elementor_data: "[json]"}`

**Confidence:** HIGH -- already documented in the project and implemented in the current build script.

---

### Pitfall 8: One Navigation Menu for All Languages

**What goes wrong:** A single WordPress menu with French labels is used for all language versions of the header template. EN/ES pages show "Accueil", "Notre vision", "Nos divisions" in the navigation.

**Prevention:** Create one WordPress menu per language:
- "Main Menu (FR)": Accueil, Notre vision, Nos divisions, Contact
- "Main Menu (EN)": Home, Our Vision, Our Divisions, Contact
- "Main Menu (ES)": Inicio, Nuestra vision, Nuestras divisiones, Contacto

In each translated header template, select the corresponding language menu in the Nav Menu widget.

**Confidence:** HIGH -- standard Polylang requirement.

---

### Pitfall 9: DeepL Machine Translation Corrupts Elementor JSON

**What goes wrong:** Attempting to use Polylang's DeepL integration or any machine translation plugin to auto-translate Elementor pages. DeepL translates the serialized JSON/HTML instead of just the visible text strings, corrupting the Elementor page structure.

**Prevention:** The [Polylang docs explicitly warn](https://polylang.pro/how-to-translate-elementor-with-polylang/): "Machine Translation DeepL doesn't work with Elementor." Use AI translation of the text strings WITHIN the Python build script, not WordPress-level machine translation.

**Confidence:** HIGH -- explicitly stated in official Polylang documentation.

---

### Pitfall 10: WPForms Contact Form Labels Not Translated

**What goes wrong:** The contact form on EN/ES pages shows French field labels ("Nom", "Courriel", "Message") instead of translated labels.

**Why it happens:** WPForms Lite does not have built-in multilingual support. The form is a single entity with one set of labels.

**Prevention:** Two approaches:
- **Option A (recommended for simplicity):** Create 3 separate WPForms (one per language) with translated labels. Embed the correct form shortcode `[wpforms id="XX"]` on each language's contact page.
- **Option B (simpler but less polished):** Use one form with language-neutral labels and embed the same shortcode on all pages.

**Confidence:** MEDIUM -- WPForms Lite's exact Polylang behavior is not well-documented. Creating separate forms per language is the universally recommended approach.

---

### Pitfall 11: Cloudflare Cache Serves Stale or Wrong-Language Pages

**What goes wrong:** After deploying translated pages, visitors see old/empty content because Cloudflare serves cached versions.

**Prevention:**
1. Use URL-based language structure (`/en/`, `/es/`) -- NOT cookie or browser detection
2. DISABLE "Detect browser language" in Polylang settings (incompatible with page caching)
3. After any REST API content push, purge Cloudflare cache

**Confidence:** HIGH -- well-documented Cloudflare + multilingual issue.

---

## Minor Pitfalls

### Pitfall 12: Hardcoded French Text in Reusable Components

**What goes wrong:** The `back_to_group_cta()` function and inline footer contain hardcoded French strings like "Une division du Groupe Vectanor", "Retour au groupe", "Tous droits reserves". These appear untranslated on EN/ES pages.

**Prevention:** Create a translation dictionary and parameterize all reusable components:
```python
STRINGS = {
    "fr": {"back_to_group": "Retour au groupe", ...},
    "en": {"back_to_group": "Back to group", ...},
    "es": {"back_to_group": "Volver al grupo", ...},
}
```

---

### Pitfall 13: Language Switcher Only Shows Languages With Published Content

**What goes wrong:** The language switcher widget only shows FR, with EN and ES missing.

**Why it happens:** Polylang only displays a language in the switcher if at least one post or page has been published in that language.

**Prevention:** Ensure at least one page is published in each language before testing the switcher.

---

### Pitfall 14: Slug Conflicts Between French and Translation Pages

**What goes wrong:** WordPress may auto-generate slugs like `contact-2` instead of the intended slug.

**Prevention:** Set the slug explicitly when creating pages. Polylang allows same slugs across languages because they have different URL prefixes.

---

### Pitfall 15: Elementor Data Write-Only Limitation

**What goes wrong:** After pushing `_elementor_data` via REST API, attempting to read it back returns an empty string.

**Why it happens:** Elementor registers `_elementor_data` as write-only via REST API by design.

**Prevention:** Rely on the HTTP response status code and the character count reported by `push_page()`. Do not build verification logic that depends on reading `_elementor_data` back. Keep local copies of all pushed JSON.

---

## Phase-Specific Warnings

| Phase Topic | Likely Pitfall | Mitigation |
|---|---|---|
| Polylang configuration | Pitfall 5 (front page redirect), Pitfall 13 (switcher empty) | Configure front page and publish stubs BEFORE enabling switcher |
| Theme Builder header/footer | Pitfall 3 (same language everywhere) | Create per-language templates via Connect Polylang for Elementor |
| Translation page creation | **Pitfall 1 (REST API is Pro-only)** | Use WP Admin "+" button, NOT REST API, for language assignment |
| Content translation push | Pitfall 6 (internal links), Pitfall 12 (hardcoded French), Pitfall 2 (CSS regen) | URL mapping, translation dict, regenerate CSS |
| Contact form setup | Pitfall 4 (email delivery), Pitfall 10 (form labels) | SMTP first, test before going live, separate forms per language |
| Deployment and QA | Pitfall 11 (Cloudflare cache), Pitfall 15 (write-only meta) | Purge cache, visual verification, check hreflang |

---

## Sources

### Polylang REST API (Critical)
- [Polylang REST API Documentation](https://polylang.pro/doc/rest-api/) -- **HIGH confidence** (explicitly states "The feature is available only in Polylang Pro.")
- [GitHub Issue #160: REST API Compatibility](https://github.com/polylang/polylang/issues/160) -- HIGH confidence (confirms Pro since 2.2)
- [Polylang Changelog](https://github.com/polylang/polylang/blob/master/changelog.txt) -- HIGH confidence (labels REST API as "Pro" feature)

### Polylang + Elementor Integration
- [Connect Polylang for Elementor Plugin](https://wordpress.org/plugins/connect-polylang-elementor/) -- HIGH confidence
- [How To Translate Elementor with Polylang](https://polylang.pro/how-to-translate-elementor-with-polylang/) -- HIGH confidence
- [Elementor Issue #4839: Display Conditions](https://github.com/elementor/elementor/issues/4839) -- HIGH confidence

### Email Delivery
- [WP Mail SMTP: WPForms Not Sending Email](https://wpmailsmtp.com/wpforms-not-sending-email/) -- HIGH confidence
- [WP Mail SMTP: Other SMTP Setup](https://wpmailsmtp.com/docs/how-to-set-up-the-other-smtp-mailer-in-wp-mail-smtp/) -- MEDIUM confidence

### Elementor CSS Regeneration
- [Elementor: Regenerate CSS & Data](https://elementor.com/help/regenerate-css-data/) -- HIGH confidence
- [GitHub Issue #21246: Styles Don't Update](https://github.com/elementor/elementor/issues/21246) -- HIGH confidence

### Polylang Configuration
- [Define Your Home Page as a Static Page](https://polylang.pro/documentation/support/getting-started/define-your-home-page-as-a-static-front-page/) -- HIGH confidence
- [The Language Switcher](https://polylang.pro/documentation/support/guides/the-language-switcher/) -- HIGH confidence
