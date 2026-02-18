# Phase 1: Site Chrome and WP Admin Foundation - Research

**Researched:** 2026-02-18
**Domain:** WordPress Elementor Pro Theme Builder (header/footer), Polylang multilingual menus, WPForms Lite contact form, WP Mail SMTP
**Confidence:** HIGH

## Summary

Phase 1 builds the site infrastructure that all future phases depend on: a custom Elementor Pro header with navigation and language switcher, a branded footer, and a working contact form with SMTP delivery. All of this work happens in WP Admin -- none of it can be done via the REST API. The key architectural insight is that Elementor Theme Builder templates (header/footer) are `elementor_library` post types with proprietary display conditions, not regular pages, and MUST be created through the Elementor editor UI.

The standard pattern for multilingual headers with Polylang + Elementor Pro is: (1) create one WordPress navigation menu per language in Appearance > Menus, (2) build the FR header template in Elementor Theme Builder, (3) use Connect Polylang for Elementor's "+" button to create EN/ES translations of that header template, (4) in each translated header, select the corresponding language's menu in the Nav Menu widget. The Connect Polylang for Elementor plugin (already installed, v2.5.5) handles automatic display condition routing -- you only set conditions on the FR (default language) template.

For the contact form, WPForms Lite (already installed) provides a drag-and-drop form builder with dropdown fields available in the free tier. WP Mail SMTP (already installed) must be configured FIRST with valid SMTP credentials for info@vectanor.com before the form can deliver emails. This is an external dependency -- the SMTP host/port/credentials depend on the email provider.

**Primary recommendation:** Complete all Phase 1 work in WP Admin UI. Do NOT attempt to create header/footer templates or forms via REST API or Python scripts. The only scripting possible in this phase is embedding a WPForms shortcode in the Contact page's Elementor JSON.

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|-----------------|
| CHRM-01 | Custom Elementor header with site navigation and language switcher | Elementor Pro Theme Builder header template + Nav Menu widget + Connect Polylang for Elementor Language Switcher widget. All verified as standard workflow. |
| CHRM-02 | Custom Elementor footer with copyright, legal links, and Vectanor branding | Elementor Pro Theme Builder footer template. Same creation workflow as header. Replaces current in-page footer sections. |
| CHRM-03 | Header and footer are mobile-responsive | Nav Menu widget has built-in hamburger menu with configurable breakpoint (Mobile/Tablet). Footer uses flexbox stacking. |
| CHRM-04 | Header and footer display in correct language per page | Connect Polylang for Elementor auto-routes translated templates. Create FR template first, then EN/ES translations via "+" button. Each gets its own Nav Menu pointing to the correct language menu. |
| LANG-01 | Site displays language switcher in header (FR/EN/ES) accessible from every page | Connect Polylang for Elementor provides native "Language Switcher" Elementor widget. Horizontal layout, flags + language code, available in "General Elements" category. |
| FORM-01 | Contact page has functional form with fields: Name, Email, Subject, Message | WPForms Lite supports all these fields including dropdown (Subject) in the free tier. Create via WP Admin > WPForms > Add New. |
| FORM-02 | Form submissions deliver to info@vectanor.com via authenticated SMTP | WP Mail SMTP "Other SMTP" mailer configuration. SMTP credentials are an external dependency. Must be configured and tested BEFORE enabling form. |
</phase_requirements>

## Standard Stack

### Core (Already Installed -- No New Plugins Needed)

| Plugin | Version | Purpose | Why Standard |
|--------|---------|---------|--------------|
| Elementor Pro | 3.35.1 | Theme Builder for header/footer templates, Nav Menu widget | Industry-standard visual builder with Theme Builder for site-wide templates |
| Hello Elementor | Latest | Minimal theme shell, defers all layout to Elementor | Official Elementor companion theme, zero conflicts |
| Polylang | 3.7.7 (Free) | Language routing, menu locations per language, URL structure | Already configured with FR/EN/ES. Creates per-language menu locations automatically |
| Connect Polylang for Elementor | 2.5.5 | Language Switcher widget, template translation routing, display condition sync | The standard glue plugin for Polylang + Elementor Pro. 2M+ downloads, 4.8/5 rating |
| WPForms Lite | Latest | Contact form builder with drag-and-drop fields | Already installed. Free tier includes dropdown fields, honeypot spam protection |
| WP Mail SMTP | Latest | Overrides wp_mail() with authenticated SMTP delivery | Already installed. Required for reliable email delivery from WordPress |

### Supporting (No Installation Needed)

| Tool | Purpose | When to Use |
|------|---------|-------------|
| WordPress Menus (Appearance > Menus) | Create one navigation menu per language | During header template setup. Polylang automatically creates per-language menu locations |
| Elementor Theme Builder (Templates > Theme Builder) | Create/manage header and footer templates | Primary workspace for CHRM-01, CHRM-02, CHRM-04 |
| WP Mail SMTP Email Test (WP Mail SMTP > Tools) | Verify SMTP configuration works | After SMTP setup, before form goes live |

### Alternatives Considered

| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| WPForms Lite | Elementor Pro Form widget | WPForms already installed, better spam protection, dedicated notification settings. Elementor Pro Forms would work but mixing form solutions adds complexity |
| WPForms Lite | Contact Form 7 | WPForms has visual builder, native Elementor widget. CF7 requires HTML knowledge for customization |
| Connect Polylang for Elementor | "Language Switcher for Elementor & Polylang" (separate plugin) | Connect Polylang already installed and is the maintained solution. The other plugin duplicates functionality |
| Per-language header templates | Single header with dynamic content | Polylang + Elementor requires separate templates for correct Nav Menu and Language Switcher behavior. Dynamic approach does not work reliably |

## Architecture Patterns

### Recommended Workflow (Build Order)

```
Step 1: Create WordPress Navigation Menus (Appearance > Menus)
        -> "Menu Principal (FR)": Accueil, Notre vision, Nos divisions, Contact
        -> "Main Menu (EN)": Home, Our Vision, Our Divisions, Contact
        -> "Menu Principal (ES)": Inicio, Nuestra vision, Nuestras divisiones, Contacto
        -> Assign each to its Polylang language-specific menu location

Step 2: Build FR Header Template (Templates > Theme Builder > Add New Header)
        -> Add Site Logo widget (link to homepage, max-width ~150px)
        -> Add Nav Menu widget (select "Menu Principal (FR)")
        -> Add Language Switcher widget (from Connect Polylang for Elementor)
        -> Style with brand colors: background #0F172A, text white
        -> Set Display Condition: "Entire Site"
        -> Publish

Step 3: Create EN Header Translation (Polylang "+" on FR header template)
        -> Replace Nav Menu widget's selected menu with "Main Menu (EN)"
        -> Language Switcher widget auto-adapts (no changes needed)
        -> DO NOT set display conditions (Connect plugin handles routing)
        -> Publish

Step 4: Create ES Header Translation (Polylang "+" on FR header template)
        -> Replace Nav Menu widget's selected menu with "Menu Principal (ES)"
        -> Publish

Step 5: Build FR Footer Template (Templates > Theme Builder > Add New Footer)
        -> Vectanor logo (white/inverted, ~120px)
        -> Copyright text: "(c) 2026 Groupe Vectanor. Tous droits reserves."
        -> Placeholder links: Politique de confidentialite, Contact
        -> Set Display Condition: "Entire Site"
        -> Publish

Step 6: Create EN/ES Footer Translations (same pattern as header)

Step 7: Configure WP Mail SMTP (WP Mail SMTP > Settings)
        -> REQUIRES: SMTP host, port, username, password for info@vectanor.com
        -> Test email delivery via WP Mail SMTP > Tools > Email Test

Step 8: Create WPForms Contact Form (WPForms > Add New)
        -> Start from "Simple Contact Form" template
        -> Add Subject dropdown field (General Inquiry, Partnership, Media, Other)
        -> Configure notification: Send To = info@vectanor.com
        -> Note the form ID for embedding

Step 9: Embed Contact Form in French Contact Page
        -> Either via WP Admin Elementor editor (drag WPForms widget)
        -> Or via Python script: push shortcode widget [wpforms id="XX"] to page 25
```

### Header Template Structure

```
+================================================================+
| [Logo]       [Nav Menu]        [Language Switcher] [Hamburger] |
|                                                    (mobile)    |
+================================================================+

Desktop (>1024px):
  [Logo left] --- [Nav links horizontal center/right] --- [FR|EN|ES right]

Mobile (<1024px):
  [Logo left] --- [Hamburger icon right]
  (tap hamburger -> dropdown with nav links + language switcher)
```

### Footer Template Structure

```
+================================================================+
|                                                                |
|              [Vectanor Logo - white, small]                    |
|     (c) 2026 Groupe Vectanor. Tous droits reserves.            |
|     Politique de confidentialite  |  Contact                   |
|                                                                |
+================================================================+
```

### Key Architectural Rule: Theme Builder Templates vs. Pages

| Aspect | Theme Builder Templates | Regular Pages |
|--------|------------------------|---------------|
| Post type | `elementor_library` | `page` |
| Creation method | WP Admin > Elementor > Theme Builder | WP Admin or REST API |
| Display conditions | Proprietary Elementor format | N/A (accessed via URL) |
| Polylang translation | Via Connect Polylang for Elementor "+" button | Via Polylang "+" in Pages list |
| REST API access | NOT reliably supported | Full support via /wp/v2/pages |
| CSS generation | Automatic on publish in editor | Requires regeneration after API push |

### Anti-Patterns to Avoid

- **Creating header/footer templates via REST API:** Theme Builder templates are `elementor_library` post type with specific meta (`_elementor_template_type: header`) and display conditions stored in proprietary format. The REST API does not expose these properly. Always use WP Admin.

- **One header template for all languages:** The Nav Menu widget selects a specific WordPress menu. Without per-language header templates, all visitors see French navigation labels regardless of their language.

- **Skipping SMTP configuration:** WordPress default `wp_mail()` uses PHP mail which is unreliable on most hosts. Forms will appear to submit successfully but emails silently vanish.

- **Setting display conditions on translated templates:** Only set display conditions on the FR (default language) template. Connect Polylang for Elementor automatically generates matching conditions for translated templates.

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| Language switcher | Custom HTML/CSS/JS switcher with flag images | Connect Polylang for Elementor Language Switcher widget | Widget is native Elementor with full styling controls (typography, hover states, flags), handles translation URL resolution automatically, respects Polylang's translation groups |
| Mobile hamburger menu | Custom responsive nav with media queries | Elementor Nav Menu widget built-in breakpoint setting | Widget automatically converts to hamburger at configurable breakpoint (Mobile/Tablet), handles toggle animation, full-width dropdown option |
| Contact form | Custom HTML form with PHP handler | WPForms Lite (already installed) | Handles validation, honeypot spam protection, notification emails, confirmation messages, entry storage. Drag-and-drop builder |
| SMTP email delivery | Custom PHPMailer configuration | WP Mail SMTP plugin (already installed) | Intercepts all wp_mail() calls, provides test tool, handles authentication, supports OAuth2 for Microsoft 365/Google |
| Per-language template routing | Custom PHP with conditional template loading | Connect Polylang for Elementor | Plugin automatically detects current language and serves correct header/footer template. Zero custom code |

**Key insight:** Every piece of Phase 1 functionality is handled by already-installed plugins. The work is configuration, not development.

## Common Pitfalls

### Pitfall 1: SMTP Credentials Are an External Dependency
**What goes wrong:** Team reaches the contact form step and discovers they don't know the SMTP host, port, or credentials for info@vectanor.com. Work stalls.
**Why it happens:** The SMTP configuration depends on wherever info@vectanor.com is hosted (Microsoft 365, Google Workspace, Zoho, hosting provider, etc.). This is not something WordPress or any plugin can auto-discover.
**How to avoid:** Determine the email provider BEFORE starting Phase 1. Check the MX records for vectanor.com (`dig MX vectanor.com` or use MXToolbox). Common providers: Microsoft 365 (outlook.office365.com:587), Google Workspace (smtp.gmail.com:587), Zoho (smtp.zoho.com:587).
**Warning signs:** If nobody knows the email hosting credentials, this blocks FORM-02 entirely.

### Pitfall 2: Header Template Shows French on All Pages
**What goes wrong:** After creating the FR header template and setting "Entire Site" display condition, all pages (including EN/ES) show French navigation.
**Why it happens:** Did not create EN/ES translations of the header template via Connect Polylang for Elementor.
**How to avoid:** After publishing the FR header, go to Templates > Saved Templates. Find the FR header. Click the "+" icon in the EN column (Polylang's translation interface) to create the EN translation. Repeat for ES. In each translated header, change the Nav Menu widget to select the correct language's WordPress menu.
**Warning signs:** Language switcher changes the page content language but the header stays in French.

### Pitfall 3: Language Switcher Shows Only French
**What goes wrong:** The Language Switcher widget in the header only displays "FR" with no EN/ES options.
**Why it happens:** Polylang only shows a language in the switcher if content exists in that language. If no pages are published in EN/ES, the switcher hides those options.
**How to avoid:** Ensure at least one page is published in each language before testing the switcher. The existing stubs (page 30 = EN homepage, page 31 = ES homepage) should be sufficient IF they have their language properly assigned in Polylang.
**Warning signs:** Visiting the site shows a language switcher with only one language option.

### Pitfall 4: WPForms Email Delivery Fails Silently
**What goes wrong:** Contact form submissions appear successful (user sees confirmation message) but no email arrives at info@vectanor.com.
**Why it happens:** WP Mail SMTP not configured, SMTP credentials wrong, or From Email doesn't match SMTP account domain.
**How to avoid:** Configure WP Mail SMTP FIRST. Use WP Mail SMTP > Tools > Email Test immediately after configuration. Check both inbox AND spam folder. If using Microsoft 365, note Basic SMTP auth retirement -- use OAuth2 mailer option.
**Warning signs:** WP Mail SMTP test email fails, or test email lands in spam.

### Pitfall 5: Polylang Static Front Page Redirect Loop
**What goes wrong:** After creating translation homepages, visiting vectanor.com/en/ redirects back to vectanor.com/ (French), or causes infinite redirect loop.
**Why it happens:** WordPress Reading Settings static front page set incorrectly, or homepage translations not properly linked in Polylang.
**How to avoid:** Verify WordPress Settings > Reading > Static Front Page is set to page 19 (FR Accueil). Verify EN (page 30) and ES (page 31) homepage stubs are properly assigned their languages in Polylang and linked as translations of page 19. Test each URL directly.
**Warning signs:** Browser shows "too many redirects" error on /en/ or /es/ URLs.

### Pitfall 6: Nav Menu Widget Points to Wrong Menu After Template Translation
**What goes wrong:** Creating a translated header template copies the entire FR header -- including the Nav Menu widget pointing to the FR menu. The EN header still shows French navigation labels.
**Why it happens:** Template translation copies all widget settings from the source template. The Nav Menu widget's menu selection is a setting, so it copies too.
**How to avoid:** After creating each translated header template, ALWAYS edit it and change the Nav Menu widget's selected menu to the correct language's menu (e.g., "Main Menu (EN)" for the EN header).
**Warning signs:** English header shows "Accueil, Notre vision, Nos divisions" instead of "Home, Our Vision, Our Divisions".

## Code Examples

### Embedding WPForms in Contact Page via REST API (Python)

```python
# Source: Existing rebuild-wow.py pattern + WPForms shortcode
# After creating the WPForms form in WP Admin and noting the form ID:

WPFORMS_ID = "XX"  # Replace with actual form ID from WPForms

# In the contact page builder, replace the placeholder with:
widget("shortcode", {
    "shortcode": f'[wpforms id="{WPFORMS_ID}"]',
})

# Alternative: use text-editor widget
widget("text-editor", {
    "editor": f'[wpforms id="{WPFORMS_ID}"]',
})
```

### Navigation Menu Items Per Language

```
FR Menu ("Menu Principal"):
  Accueil        -> /
  Notre vision   -> /notre-vision/
  Nos divisions  -> /divisions/
  Contact        -> /contact/

EN Menu ("Main Menu"):
  Home           -> /en/
  Our Vision     -> /en/notre-vision/  (or /en/our-vision/ if slug changed)
  Our Divisions  -> /en/divisions/
  Contact        -> /en/contact/

ES Menu ("Menu Principal ES"):
  Inicio              -> /es/
  Nuestra vision      -> /es/notre-vision/  (or /es/nuestra-vision/ if slug changed)
  Nuestras divisiones -> /es/divisions/
  Contacto            -> /es/contact/
```

**Note on slugs:** Polylang allows translating slugs. If the EN/ES page shells are created with translated slugs (e.g., "our-vision" instead of "notre-vision"), the menu URLs should match. If slugs are kept as-is (French slugs with language prefix), that also works but looks less polished.

### Header Template Elementor Settings (Reference for Styling)

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
    "background_color": "#0F172A",
    "position": "fixed",
    "z_index": 100
  },
  "elements": [
    {
      "elType": "widget",
      "widgetType": "theme-site-logo",
      "settings": {
        "width": {"size": 150, "unit": "px"},
        "custom_css": "selector img { filter: brightness(0) invert(1); }"
      }
    },
    {
      "elType": "widget",
      "widgetType": "nav-menu",
      "settings": {
        "menu": "menu-principal-fr",
        "layout": "horizontal",
        "submenu_icon": {"value": "fas fa-chevron-down"},
        "breakpoint": "tablet",
        "toggle": "burger",
        "text_color": "#FFFFFF",
        "text_color_hover": "#3B82F6",
        "typography_typography": "custom",
        "typography_font_family": "Montserrat",
        "typography_font_size": {"size": 14, "unit": "px"},
        "typography_font_weight": "600"
      }
    },
    {
      "elType": "widget",
      "widgetType": "language-switcher",
      "settings": {
        "layout": "horizontal",
        "show_flags": true,
        "show_name": false,
        "show_code": true
      }
    }
  ]
}
```

**IMPORTANT:** This JSON is for REFERENCE ONLY. Do NOT push this via REST API. Build the header in Elementor's visual editor using these values as a styling guide.

### Footer Template Styling Reference

```
Background: #0F172A (Near Black)
Logo: Vectanor logo, white/inverted, width ~120px
Copyright: "(c) 2026 Groupe Vectanor. Tous droits reserves."
  Font: Inter, 13px, color #475569
Links: "Politique de confidentialite" | "Contact"
  Font: Inter, 13px, color #94A3B8, hover color #3B82F6
Layout: Centered column, padding 40px top/bottom
```

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| Elementor "Header, Footer & Blocks" free plugin for header/footer | Elementor Pro Theme Builder (native) | Elementor Pro 2.0+ (2019) | No need for third-party header/footer plugin; native support is more reliable |
| PHP mail() for WordPress emails | SMTP authentication via WP Mail SMTP | Industry shift 2020-2024 | Gmail, Yahoo, and Outlook now require authenticated sending. PHP mail() emails go to spam or get rejected |
| Microsoft 365 Basic SMTP Auth | OAuth2 for Microsoft 365 | Microsoft retiring Basic Auth (2025) | If info@vectanor.com is on M365, must use OAuth2 option in WP Mail SMTP, not username/password |
| Cookie-based language detection | URL prefix-based language routing (/en/, /es/) | Best practice since 2020+ | Cookie-based breaks CDN caching (Cloudflare). URL prefix is CDN-compatible and SEO-friendly |
| Manual display conditions per translated template | Connect Polylang for Elementor auto-routing | Plugin v2.0+ | Set display conditions once on default language template; plugin automatically routes translated templates |

**Deprecated/outdated:**
- "Elementor Header & Footer Builder" free plugin by Brainstorm Force: still works but unnecessary with Elementor Pro Theme Builder
- Microsoft Basic SMTP auth: being retired. Use OAuth2 mailer if M365

## Open Questions

1. **SMTP Credentials for info@vectanor.com**
   - What we know: WP Mail SMTP is installed and needs SMTP host/port/username/password
   - What's unclear: Which email provider hosts info@vectanor.com (M365, Google Workspace, Zoho, other?)
   - Recommendation: Check MX records (`dig MX vectanor.com` or MXToolbox). Obtain credentials from domain owner. If M365, use OAuth2 mailer. This should be resolved BEFORE Phase 1 planning starts to avoid blocking FORM-02.

2. **Existing EN/ES Homepage Stubs (pages 30 and 31)**
   - What we know: Pages exist with IDs 30 and 31
   - What's unclear: Are they properly assigned to EN/ES languages in Polylang? Are they linked as translations of page 19?
   - Recommendation: Verify in WP Admin > Pages. Check the Polylang language columns. If not properly linked, fix during Phase 1 setup. This affects whether the language switcher works on the homepage.

3. **Polylang URL Structure Verification**
   - What we know: Polylang is installed and configured with FR/EN/ES
   - What's unclear: Is it configured for "Directory name in pretty permalinks" format (/en/, /es/) vs. other formats?
   - Recommendation: Verify in WP Admin > Languages > Settings > URL modifications. Must be "The language is set from the directory name in pretty permalinks" for Cloudflare compatibility.

4. **Cloudflare Cache Purge Access**
   - What we know: Site is behind Cloudflare
   - What's unclear: Whether the Cloudflare WordPress plugin is installed, or whether dashboard access is available for cache purging
   - Recommendation: After making header/footer changes, Cloudflare may serve stale versions. Verify purge method before deployment.

## Sources

### Primary (HIGH confidence)
- [Connect Polylang for Elementor - WordPress.org](https://wordpress.org/plugins/connect-polylang-elementor/) -- Full feature list, v2.5.5 compatibility (WordPress 6.9, Elementor 3.34, Polylang 3.7.5)
- [Elementor Nav Menu Widget (Pro)](https://elementor.com/help/nav-menu-widget-pro/) -- Menu selection, breakpoint settings, mobile hamburger configuration
- [Elementor Header & Footer Builder](https://elementor.com/blog/header-footer-builder/) -- Theme Builder template creation workflow
- [Polylang: Create Menus](https://polylang.pro/doc/create-menus/) -- One menu per language, per-language menu locations
- [Polylang: How to Translate Elementor with Polylang](https://polylang.pro/how-to-translate-elementor-with-polylang/) -- Template translation workflow, DeepL warning
- [Elementor Issue #4839](https://github.com/elementor/elementor/issues/4839) -- Confirms Elementor natively declined Polylang support in display conditions (2018), validating need for Connect plugin

### Secondary (MEDIUM confidence)
- [WPForms: How to Set Up SMTP](https://wpforms.com/docs/how-to-set-up-smtp-using-the-wp-mail-smtp-plugin/) -- WPForms + WP Mail SMTP integration guide
- [WPForms: How to Customize Dropdown Field](https://wpforms.com/docs/how-to-customize-the-dropdown-field-in-wpforms/) -- Subject dropdown available in Lite
- [WP Mail SMTP: WPForms Not Sending Email](https://wpmailsmtp.com/wpforms-not-sending-email/) -- Troubleshooting guide, confirms silent failure pattern
- [Polylang: The Language Switcher](https://polylang.pro/documentation/support/guides/the-language-switcher/) -- Switcher behavior when translations don't exist

### Tertiary (LOW confidence)
- Elementor JSON structure for header template: Based on training data knowledge of Elementor container/widget JSON format. Widget type names (`nav-menu`, `language-switcher`, `theme-site-logo`) should be verified in the actual Elementor editor.

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH -- All plugins already installed with known versions. No decisions to make.
- Architecture: HIGH -- Elementor Pro Theme Builder + Connect Polylang for Elementor is the documented, standard workflow for multilingual headers. Verified against official plugin docs and WordPress.org listings.
- Pitfalls: HIGH -- Pitfalls verified against official documentation, GitHub issues, and the existing project research. The SMTP credential dependency is the only genuine blocker.
- Code examples: MEDIUM -- Elementor JSON widget types are based on training data. The WPForms shortcode pattern is well-documented. Menu slug names are illustrative.

**Research date:** 2026-02-18
**Valid until:** 2026-03-18 (stable domain -- plugin versions unlikely to change significantly in 30 days)
