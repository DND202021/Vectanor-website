# Feature Landscape

**Domain:** Corporate holding company multilingual website (WordPress/Elementor)
**Researched:** 2026-02-18
**Scope:** Focused on what remains to ship -- multilingual UX, contact forms, SEO basics, accessibility, legal compliance -- for an already-built 8-page informational site.

---

## Table Stakes

Features visitors and search engines expect. Missing any of these makes the site feel unfinished or unprofessional for a corporate holding company.

### TS-1: Visible Language Switcher in Header

| Attribute | Detail |
|-----------|--------|
| Why Expected | The site declares itself trilingual (FR/EN/ES). Without a visible switcher, translated content is unreachable. Visitors landing on the wrong language version have no recourse. |
| Complexity | **Low** |
| Implementation | Use "Connect Polylang for Elementor" plugin (already installed) to add the Language Switcher widget in the Elementor Pro header template. Display language names in their native form: Francais, English, Espanol. Use a horizontal inline list (only 3 languages -- dropdown is overkill). |
| Placement | Top-right of header, persistent on all pages. Text-only, no flags. Flags are an anti-pattern: Spanish is spoken in 20+ countries, French in many African nations -- flags create cultural assumptions. |
| Mobile | Must be touch-friendly (44x44px minimum tap target). Can collapse into a compact row or small dropdown on mobile nav. |
| Confidence | **HIGH** -- Polylang + Connect Polylang for Elementor is a well-documented integration path. |

### TS-2: Functional Contact Form

| Attribute | Detail |
|-----------|--------|
| Why Expected | A corporate holding company without a working contact form signals "we don't want to hear from you." The Contact page exists but the form is not configured. |
| Complexity | **Low** |
| Implementation | WPForms Lite (already installed): create "Simple Contact Form" template, configure notification to info@vectanor.com. WP Mail SMTP (already installed) handles deliverability. |
| Fields | Keep minimal (3-5 fields max for best conversion): **Name** (required), **Email** (required), **Subject** (dropdown: General Inquiry / Partnership / Media / Other), **Message** (textarea, required). No phone number field -- this is a corporate holding, not a sales funnel. |
| Submit Button | Label: "Envoyer le message" / "Send Message" / "Enviar mensaje" (match page language). Not generic "Submit". |
| Confirmation | On-submit success message + auto-reply email confirming receipt. Set expectation: "We will respond within 2 business days." |
| Spam Protection | WPForms Lite includes honeypot anti-spam. No CAPTCHA needed for a low-traffic corporate site -- it degrades UX. |
| Confidence | **HIGH** -- WPForms Lite + WP Mail SMTP is a standard, proven setup. |

### TS-3: Complete EN/ES Page Translations

| Attribute | Detail |
|-----------|--------|
| Why Expected | Having Polylang configured with FR/EN/ES but only French content live is worse than not declaring multilingual support at all. Search engines will index empty translation stubs. Visitors clicking EN/ES get nothing. |
| Complexity | **Medium** -- 8 pages x 2 languages = 16 translation units, each requiring Elementor JSON manipulation via the REST API build scripts. |
| Implementation | Use AI translation of French content. Generate Elementor-compatible JSON for each translated page. Push via the existing Python build script workflow (`rebuild-wow.py` pattern). Link translations in Polylang so the language switcher routes correctly. |
| Quality Bar | AI translations are sufficient for v1 of a corporate holding site. The content is formal/professional -- not creative writing. Have a native speaker spot-check key pages (Homepage, Contact) before launch. |
| Confidence | **HIGH** -- The build script workflow for pushing Elementor JSON is already proven. |

### TS-4: SEO Meta Titles and Descriptions (All Pages, All Languages)

| Attribute | Detail |
|-----------|--------|
| Why Expected | Without meta titles and descriptions, Google displays auto-generated snippets that look unprofessional. Rank Math is installed but not configured per-page. |
| Complexity | **Low** |
| Implementation | For each of the 8 pages x 3 languages (24 total), set via Rank Math: (1) SEO title (under 60 chars), (2) meta description (under 155 chars), (3) focus keyword. |
| Pattern | Title format: "[Page Name] - Groupe Vectanor" (or localized equivalent). Description: one sentence summarizing the page purpose with a call to action. |
| Multilingual SEO | Polylang automatically generates hreflang tags when translations are linked. Verify hreflang output by checking page source after setup. Note: Polylang and Rank Math do not have native compatibility -- may need the compatibility code from Rank Math KB if sitemap or canonical issues arise. |
| Confidence | **MEDIUM** -- Rank Math + Polylang integration has known friction points. Test hreflang and sitemaps after setup. |

### TS-5: XML Sitemap Submitted to Google Search Console

| Attribute | Detail |
|-----------|--------|
| Why Expected | Without a sitemap, Google may not discover all 24+ pages (8 pages x 3 languages). For a new domain, this is critical for indexing. |
| Complexity | **Low** |
| Implementation | Rank Math generates XML sitemaps automatically. Submit `vectanor.com/sitemap_index.xml` to Google Search Console. Verify that Polylang language variants appear correctly in the sitemap. |
| Confidence | **HIGH** -- Standard Rank Math feature. |

### TS-6: Privacy Policy Page

| Attribute | Detail |
|-----------|--------|
| Why Expected | **Legally required** under Quebec Law 25 (effective since September 2023). Any website collecting personal information (the contact form collects name + email) must publish a privacy policy. Penalties: up to CAD 10 million or 2% of worldwide turnover. Also required by Google Search Console and advertising platforms. |
| Complexity | **Low** |
| Implementation | Create a simple Privacy Policy page covering: what data is collected (name, email via contact form), purpose (responding to inquiries), retention period, rights of the individual, contact for privacy officer. Translate into all 3 languages. Link from footer. |
| Content | Can use a template/generator. Must name the privacy officer or state the CEO is responsible (Law 25 requirement). |
| Confidence | **HIGH** -- Legal requirement is well-documented. Content is templatable. |

### TS-7: Proper Footer with Legal Links and Company Info

| Attribute | Detail |
|-----------|--------|
| Why Expected | Corporate sites without a structured footer look unfinished. The footer is where visitors expect to find legal links, contact info, and secondary navigation. |
| Complexity | **Low** |
| Implementation | Footer should include: (1) Company name + copyright year, (2) Links: Privacy Policy, Contact, (3) Language switcher (secondary placement), (4) Brief tagline or company description. |
| What NOT to include | Social media icons (unless Vectanor has active social accounts -- dormant profiles look worse than no links). No excessive navigation duplication. |
| Confidence | **HIGH** -- Standard web practice. |

### TS-8: Alt Text on All Images

| Attribute | Detail |
|-----------|--------|
| Why Expected | Missing alt text is the single most common accessibility failure on the web. Screen readers cannot describe images without it. Also impacts SEO (image search, Google image indexing). |
| Complexity | **Low** |
| Implementation | Audit all images across 8 pages. Add descriptive alt text to meaningful images (logos, team photos, illustrations). Mark purely decorative images (background gradients, spacers) with empty alt="" so screen readers skip them. |
| Division logos | Alt text should be: "Logo [Division Name]" (e.g., "Logo Dimonoff"). |
| Confidence | **HIGH** -- Elementor image widgets have an alt text field. |

### TS-9: Mobile Responsiveness Verification

| Attribute | Detail |
|-----------|--------|
| Why Expected | 60%+ of web traffic is mobile. Elementor provides responsive modes but custom CSS (glassmorphism, animations) can break on small screens. A corporate site that looks broken on mobile is worse than no site. |
| Complexity | **Medium** -- Requires testing across breakpoints and fixing any layout issues. |
| Implementation | Test all 8 pages on Elementor's mobile preview, actual devices (iOS Safari, Android Chrome), and Google's Mobile-Friendly Test tool. Fix padding, font sizes, and overflow issues. |
| Confidence | **HIGH** -- Standard QA process. |

---

## Differentiators

Features that elevate the site above typical corporate holding company websites. Not expected, but signal professionalism and attention to detail.

### D-1: Smooth Page Transition Animations

| Attribute | Detail |
|-----------|--------|
| Value Proposition | Most holding company sites (including Berkshire Hathaway's famously plain site) are static and utilitarian. Vectanor already has glassmorphism and animations -- consistent, polished transitions between sections and pages would reinforce the "innovative technology holding" positioning. |
| Complexity | **Low** -- Already partially implemented. Polish pass needed. |
| Notes | Ensure animations respect `prefers-reduced-motion` media query for accessibility. |

### D-2: Division Color-Coded Visual Identity

| Attribute | Detail |
|-----------|--------|
| Value Proposition | Each division has a distinct accent color (amber/green/purple/pink). Consistently using these as visual markers (card borders, section accents, hover states) across the site creates an intuitive wayfinding system. Visitors learn to associate colors with divisions. |
| Complexity | **Low** -- Color system already defined in brand guide. |
| Notes | Verify color contrast ratios meet WCAG 2.1 AA (4.5:1 for text, 3:1 for large text and UI components). |

### D-3: Open Graph / Social Sharing Cards

| Attribute | Detail |
|-----------|--------|
| Value Proposition | When someone shares vectanor.com on LinkedIn (the primary sharing channel for a B2B corporate holding), a well-designed preview card with the Vectanor logo, page title, and description looks professional. Without OG tags, LinkedIn/Twitter show a generic or broken preview. |
| Complexity | **Low** |
| Implementation | Rank Math handles OG tags. Set per-page: OG title, OG description, OG image (use a branded social card image -- 1200x630px with Vectanor logo on navy background). Ensure each language version has its own localized OG tags. |
| Confidence | **HIGH** -- Rank Math generates OG tags natively. |

### D-4: Cookie Consent Banner (Law 25 Compliance)

| Attribute | Detail |
|-----------|--------|
| Value Proposition | Quebec Law 25 requires explicit opt-in consent for non-essential cookies (analytics, tracking). Even if Vectanor currently has no analytics, adding a lightweight consent banner signals legal sophistication and future-proofs the site for when analytics are added. |
| Complexity | **Medium** -- Needs a multilingual-compatible consent plugin. |
| Implementation | Use CookieYes or Complianz (both have free WordPress plugins with multilingual support). Configure for 3 languages. If no analytics/tracking cookies exist yet, the banner can be minimal: "This site uses essential cookies only." |
| When to Build | Can defer if no analytics are active. Becomes table stakes the moment Google Analytics or any tracking is added. |
| Confidence | **MEDIUM** -- Plugin ecosystem is mature but multilingual configuration needs testing. |

### D-5: Structured Data / Schema Markup

| Attribute | Detail |
|-----------|--------|
| Value Proposition | Adding Organization schema markup helps Google display rich results (company name, logo, contact info in Knowledge Panel). For a holding company with subsidiaries, this is particularly valuable for brand disambiguation. |
| Complexity | **Low** |
| Implementation | Rank Math supports Organization schema out of the box. Configure: organization name, logo URL, contact email, same-as links (division websites). |
| Confidence | **HIGH** -- Rank Math feature. |

### D-6: Custom 404 Error Page

| Attribute | Detail |
|-----------|--------|
| Value Proposition | A branded 404 page prevents visitors who hit a broken link from seeing a generic WordPress error. Shows attention to detail. |
| Complexity | **Low** |
| Implementation | Create a simple Elementor template for 404 with: Vectanor branding, "Page not found" message in current language, link back to homepage. |
| Confidence | **HIGH** -- Elementor Pro Theme Builder supports 404 templates. |

### D-7: Breadcrumb Navigation

| Attribute | Detail |
|-----------|--------|
| Value Proposition | With a hierarchical page structure (Divisions > Dimonoff/Spatium/Amotus/Vigilia), breadcrumbs help visitors understand where they are and navigate up. Also generates breadcrumb rich snippets in Google search results. |
| Complexity | **Low** |
| Implementation | Rank Math includes Google-compliant breadcrumbs. Add to page templates via Elementor or Rank Math settings. |
| Confidence | **HIGH** |

---

## Anti-Features

Features to explicitly NOT build. These are common requests that would waste effort or actively harm this specific type of site.

### AF-1: Blog / News Section

| Why Avoid | A holding company blog requires ongoing content creation. An empty or stale blog (last post: 6 months ago) signals abandonment and is worse than no blog. Vectanor's divisions have their own websites for content marketing. The holding company site should be a stable, evergreen presence. |
| What to Do Instead | If corporate news is ever needed, link to LinkedIn posts or a simple "Latest News" section on the homepage with 2-3 manually updated items. |

### AF-2: Live Chat Widget

| Why Avoid | Live chat creates an expectation of immediate response. A holding company does not have customer support staff monitoring chat. An offline chat widget ("Leave a message!") is inferior to a simple contact form. |
| What to Do Instead | The contact form with a clear response time expectation ("We respond within 2 business days") is the correct pattern. |

### AF-3: Newsletter Signup / Email Collection

| Why Avoid | A corporate holding company has no newsletter content to send. Collecting emails without a plan to use them violates PIPEDA/Law 25 principles (purpose limitation). An unused mailing list is a liability, not an asset. |
| What to Do Instead | Nothing. The contact form serves the communication need. |

### AF-4: User Accounts / Login System

| Why Avoid | Purely informational site. No gated content, no customer portal, no investor dashboard. Authentication adds complexity, security surface area, and maintenance burden for zero value. |
| What to Do Instead | Nothing. Keep it static. |

### AF-5: Automated IP-Based Language Detection

| Why Avoid | Automatically redirecting users based on IP geolocation is a notorious UX anti-pattern. It fails for: expats, VPN users, travelers, bilingual users who prefer a specific language. It also causes SEO problems (Googlebot sees different content from different locations). |
| What to Do Instead | Default to French (primary market). Show the language switcher prominently. Let users choose. Respect `Accept-Language` browser header only as a subtle suggestion, never a forced redirect. |

### AF-6: Social Media Feed Integration

| Why Avoid | Embedding live social feeds adds third-party dependencies, slows page load, and looks empty if accounts are inactive. Corporate holding companies rarely post frequently on social media. |
| What to Do Instead | If social links are desired, use simple icon links in the footer pointing to profiles. No embedded feeds. |

### AF-7: Complex Multi-Step Contact Form

| Why Avoid | Adding fields like company size, revenue range, industry, "how did you hear about us" etc. is appropriate for a SaaS product's sales pipeline. For a corporate holding company, it creates friction. The goal is to make contact easy, not to qualify leads. |
| What to Do Instead | 4 fields maximum: Name, Email, Subject (dropdown), Message. |

### AF-8: Parallax Scrolling / Heavy Scroll Animations

| Why Avoid | The site already uses glassmorphism and subtle animations. Adding parallax scrolling would push it from "premium" to "distracting." Parallax also causes performance issues on mobile, triggers motion sickness for some users, and is increasingly seen as a dated design trend. |
| What to Do Instead | Keep existing subtle entrance animations. Add `prefers-reduced-motion` support. |

### AF-9: Full E-commerce or Pricing Pages

| Why Avoid | Vectanor is a holding company, not a vendor. Divisions have their own commercial operations. |
| What to Do Instead | Link to division websites for any commercial inquiries. |

---

## Feature Dependencies

```
TS-3 (Translations) --> TS-1 (Language Switcher)
    Translations must exist before the switcher is useful.
    However, switcher can be built first and show stubs.

TS-4 (SEO Meta) --> TS-3 (Translations)
    Meta titles/descriptions in EN/ES require translated content to write against.

TS-5 (Sitemap) --> TS-3 (Translations) + TS-4 (SEO Meta)
    Sitemap should be submitted after all pages and translations are live.

TS-6 (Privacy Policy) --> TS-2 (Contact Form)
    Privacy policy must reference what data the contact form collects.
    Should go live before or simultaneously with the contact form.

TS-7 (Footer) --> TS-6 (Privacy Policy)
    Footer links to privacy policy page -- page must exist first.

TS-1 (Language Switcher) --> TS-7 (Footer)
    Secondary switcher placement in footer depends on footer being built.

D-3 (OG Cards) --> TS-4 (SEO Meta)
    OG tags use same title/description data. Configure together.

D-4 (Cookie Consent) --> TS-6 (Privacy Policy)
    Consent banner should link to privacy policy.

D-5 (Schema) --> TS-4 (SEO Meta)
    Configure Rank Math schema alongside SEO meta setup.
```

**Suggested execution order based on dependencies:**

1. **TS-2** Contact Form + **TS-6** Privacy Policy (no dependencies, enable each other)
2. **TS-3** EN/ES Translations (largest effort, unblocks everything else)
3. **TS-1** Language Switcher + **TS-7** Footer (need translations + privacy page)
4. **TS-4** SEO Meta + **TS-5** Sitemap + **D-3** OG + **D-5** Schema (SEO batch)
5. **TS-8** Alt Text + **TS-9** Mobile QA + **D-1** Animation Polish (final QA batch)
6. **D-2** Color consistency, **D-6** 404 page, **D-7** Breadcrumbs (nice-to-have polish)

---

## MVP Recommendation

**Prioritize (must ship before site is "launched"):**

1. **TS-2: Contact Form** -- Easiest win, 30 minutes of configuration. A contact page without a working form is embarrassing.
2. **TS-6: Privacy Policy** -- Legal requirement under Quebec Law 25. Create from template, translate to 3 languages.
3. **TS-3: EN/ES Translations** -- The largest single effort. Without translations, the site is functionally monolingual despite Polylang being installed.
4. **TS-1: Language Switcher** -- Once translations exist, the switcher makes them accessible. This is the most visible missing feature.
5. **TS-7: Footer** -- Ties everything together with legal links and secondary navigation.
6. **TS-4: SEO Meta** -- Quick pass through Rank Math for all pages. Do after translations are live.

**Defer to post-launch polish:**

- **D-4: Cookie Consent** -- Only urgent if analytics tracking is added. No analytics = no non-essential cookies = low risk.
- **D-6: Custom 404** -- Nice but not blocking launch.
- **D-7: Breadcrumbs** -- Helpful for SEO but the site has only 8 pages with shallow hierarchy.

**Skip entirely:**

- All anti-features (AF-1 through AF-9). These should be documented in project decisions so future stakeholders don't re-request them.

---

## Sources

### Language Switcher UX
- [Linguise: Language Selector Design Best Practices](https://www.linguise.com/blog/guide/best-practices-designing-language-selector/) -- HIGH confidence
- [Robert Jelenic: Language Switching UI/UX](https://www.robertjelenic.com/language-switching-ui-ux-on-multilingual-sites/) -- MEDIUM confidence
- [Smartling: Website Language Selectors](https://www.smartling.com/blog/language-selector-best-practices) -- MEDIUM confidence
- [Weglot: Multilingual Website Design](https://www.weglot.com/guides/multi-language-website) -- MEDIUM confidence

### Polylang + Elementor Integration
- [Connect Polylang for Elementor Plugin](https://wordpress.org/plugins/connect-polylang-elementor/) -- HIGH confidence (official plugin page)
- [Polylang: How to Add Language Switcher](https://polylang.pro/how-to-add-a-language-switcher-to-your-wordpress-website/) -- HIGH confidence (official docs)
- [Polylang: Translate Elementor](https://polylang.pro/how-to-translate-elementor-with-polylang/) -- HIGH confidence (official docs)

### Contact Form Best Practices
- [Prosper Marketing: Contact Form Best Practices 2025](https://www.prospermarketingsolutions.com/blogs-contact-form-best-practices-for-2025/) -- MEDIUM confidence
- [WPForms: How to Create a Simple Contact Form](https://wpforms.com/how-to-create-a-simple-contact-form-in-wordpress/) -- HIGH confidence (official docs)
- [Jetpack: Contact Form Best Practices](https://jetpack.com/resources/contact-form-best-practices/) -- MEDIUM confidence

### SEO / Rank Math
- [Rank Math: WordPress SEO Checklist](https://rankmath.com/blog/wordpress-seo-checklist/) -- HIGH confidence (official)
- [Rank Math: Polylang Compatibility](https://rankmath.com/kb/polylang-compatibility/) -- HIGH confidence (official KB)
- [Rank Math: How to Setup](https://rankmath.com/kb/how-to-setup/) -- HIGH confidence (official)
- [Rank Math: Hreflang Tags Guide](https://rankmath.com/blog/hreflang-tags/) -- HIGH confidence (official)

### Corporate Website Design
- [Webstacks: Corporate Website Design Examples](https://www.webstacks.com/blog/corporate-website-design) -- MEDIUM confidence
- [Webflow: Holding Company Templates](https://webflow.com/list/holding-company) -- MEDIUM confidence
- [UXPin: Corporate Website Design](https://www.uxpin.com/studio/blog/corporate-website-design-examples/) -- MEDIUM confidence

### Accessibility
- [W3C: WCAG 2.1](https://www.w3.org/TR/WCAG21/) -- HIGH confidence (authoritative standard)
- [Elementor: Fix Accessibility Issues](https://elementor.com/help/fix-accessibility-issues/) -- HIGH confidence (official docs)
- [Elementor: WordPress Accessibility](https://elementor.com/blog/wordpress-accessibility-elementor/) -- HIGH confidence (official)

### Legal / Privacy (Quebec Law 25)
- [OneTrust: Quebec Law 25 Overview](https://www.onetrust.com/blog/quebecs-law-25-what-is-it-and-what-do-you-need-to-know/) -- MEDIUM confidence
- [BigID: Quebec Law 25 Requirements](https://bigid.com/blog/quebec-law-25-canada-new-privacy-law-requirements/) -- MEDIUM confidence
- [PIPEDA Requirements (Privacy Commissioner)](https://www.priv.gc.ca/en/privacy-topics/privacy-laws-in-canada/the-personal-information-protection-and-electronic-documents-act-pipeda/pipeda_brief/) -- HIGH confidence (official government)

### Footer Best Practices
- [Orbit Media: Website Footer Best Practices](https://www.orbitmedia.com/blog/website-footer-design-best-practices/) -- MEDIUM confidence
- [HubSpot: Footer Design Examples](https://blog.hubspot.com/website/website-footer) -- MEDIUM confidence
