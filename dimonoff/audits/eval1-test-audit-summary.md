# SEO/AEO/GEO Audit Summary
**Page**: Smart Lighting Control  
**URL**: https://dimonoff.com/smart-lighting-control/  
**Audit Date**: 2026-03-26  
**Language**: English  

---

## Current Scores

| Dimension | Score | Status |
|-----------|-------|--------|
| **SEO** | 60/100 | ⚠️ Below Average |
| **AEO** | 18/100 | 🔴 Critical |
| **GEO** | 35/100 | 🔴 Poor |
| **Total** | 113/300 | 🔴 Needs Work |

---

## Executive Summary

The Smart Lighting Control page has **strong technical foundations** (good canonical, hreflangs, HTTPS, internal links) but suffers from **critical gaps in content optimization for AI and search results**. The page scores particularly poorly on AEO (Answer Engine Optimization) and GEO (Generative Engine Optimization), which are essential for visibility in featured snippets, voice search, and AI-powered search results (ChatGPT, Perplexity, Claude, etc.).

**Key Issues:**
1. **Performance bottleneck**: TTFB of 4.2 seconds (threshold: <800ms)
2. **Content structure problems**: 12 of 15 H2 headings are duplicates
3. **Missing structured data**: No FAQ, Product, or HowTo schemas
4. **Image accessibility**: Only 27% of images have alt text (38 missing)
5. **AI optimization gaps**: No entity-first paragraph, no article dates, missing llms.txt entry
6. **Excessive resources**: 129 scripts, 11 stylesheets, 0 lazy-loaded images

---

## Detailed Findings by Dimension

### SEO Scoring (60/100)

**Passing Signals:**
- ✅ Meta description (10/10) — Well-written, 155 chars, contains keywords and value prop
- ✅ H1 tag (8/8) — Single, optimized H1 with primary keyword
- ✅ Internal links (6/6) — 23 relevant links with descriptive anchors
- ✅ External links (4/4) — 4 authoritative external links with proper rel attributes
- ✅ Canonical URL (5/5) — Correct self-referencing
- ✅ Hreflang tags (5/5) — All three language versions (EN/FR/ES) properly linked
- ✅ DOM complexity (5/5) — 2,458 elements (within 1500-3000 range)
- ✅ Mobile viewport (5/5) — Present and responsive
- ✅ HTTPS (5/5) — Full HTTPS, no mixed content

**Warning Signals:**
- ⚠️ Meta title (5/10) — 33 chars, too short (ideal: 50-60), lacks keyword depth

**Critical Failures:**
- 🔴 Heading hierarchy (2/8) — 12 of 15 H2s are **duplicates**, breaking logical structure
- 🔴 Image alt text (0/10) — Only 14 of 52 images (27%) have alt text; 38 missing
- 🔴 TTFB (0/10) — **4,200ms response time** (threshold: <800ms, fail point: >2000ms)
- 🔴 Resource loading (0/5) — 129 scripts (threshold: <50), 11 stylesheets, 0 lazy-loaded images
- 🔴 Sitemap in robots.txt (0/4) — Sitemap exists but not declared in robots.txt (68 bytes only)

**SEO Impact**: Strong foundations but crippled by performance issues and accessibility gaps.

---

### AEO Scoring (18/100)

**Passing Signals:**
- ✅ Breadcrumb Schema (5/5) — BreadcrumbList schema present via Yoast
- ✅ Structured lists (7/7) — 3 ordered/unordered lists with clear labels

**Warning Signals:**
- ⚠️ Question-format headings (3/10) — Only 1 of 15 headings phrased as questions
- ⚠️ Voice search readiness (3/10) — Formal, technical tone (not conversational)

**Critical Failures:**
- 🔴 FAQ Schema (0/15) — **No FAQPage schema**; expected for high-value product page
- 🔴 HowTo Schema (0/10) — Not applicable to page type
- 🔴 Definition paragraphs (0/10) — **No "X is a..." entity-first definitions**
- 🔴 Comparison tables (0/8) — **No feature/product comparison tables**
- 🔴 Product Schema (0/15) — **Missing Product schema** for SCMS service offering
- 🔴 Direct answer paragraphs (0/10) — No concise (40-60 word) answers following questions

**AEO Impact**: Page is entirely missing featured snippet and voice search optimization. This is the weakest dimension.

---

### GEO Scoring (35/100)

**Passing Signals:**
- ✅ Structured data richness (7/10) — 2 schema types (BreadcrumbList, Organization)

**Warning Signals:**
- ⚠️ llms.txt (6/12) — File exists (2,621 bytes, 16 pages listed) but **Smart Lighting Control is NOT included**
- ⚠️ AI crawler access (2/10) — robots.txt is basic, **lacks explicit AI crawler directives** (GPTBot, ClaudeBot, PerplexityBot, Google-Extended)
- ⚠️ sameAs links (4/8) — Partial sameAs links (LinkedIn, Twitter) but incomplete coverage
- ⚠️ Citable statistics (3/10) — Only 1 statistic found; threshold is ≥3 sourced data points
- ⚠️ Author/source authority (4/7) — Organization name (Dimonoff) present but no named author or credentials
- ⚠️ Unique value proposition (5/8) — SCMS platform is unique, but some commodity information
- ⚠️ Cross-language consistency (4/7) — Moderate gaps between FR and EN versions

**Critical Failures:**
- 🔴 Entity-first paragraph (0/12) — **No opening paragraph clearly defining entity in first 2 sentences**
- 🔴 Article dates (0/8) — **No article:published_time or article:modified_time meta tags**, no visible "last updated"
- 🔴 Freshness signals (0/8) — **No update date visible**; AI systems can't determine content freshness

**GEO Impact**: Missing critical AI citability signals. Pages without entity introductions, dates, and AI crawler directives perform poorly in LLM-powered search results.

---

## Prioritized Recommendations

### Priority 1 (High Impact + Quick Win) — Potential Gain: +40 SEO, +23 AEO, +17 GEO

1. **Fix Server TTFB (4200ms → <800ms)** — SEO +10
   - TTFB of 4.2 seconds is a critical performance issue
   - Contact hosting provider or implement caching layer
   - Expected: +10 SEO points

2. **Add alt text to 38 missing images (27% → 100% coverage)** — SEO +10
   - Requires descriptive, keyword-relevant alt attributes
   - Can be done via WordPress media editor
   - Expected: +10 SEO points

3. **Add FAQ Schema with 3+ Q&A pairs** — AEO +15, GEO +5
   - Target common customer questions about smart lighting control
   - Use Yoast SEO FAQ block or manual JSON-LD
   - Expected: +15 AEO, +5 GEO points

4. **Add entity-first opening paragraph** — AEO +3, GEO +12
   - Rewrite: "Smart Lighting Control is a [definition]..."
   - Should clearly state what the product is in first 2 sentences
   - Expected: +12 GEO, +3 AEO points

5. **Fix duplicate H2 headings (12 duplicates → unique structure)** — SEO +6, AEO +5
   - Audit all 15 H2s and remove/rename duplicates
   - Restructure for logical content hierarchy
   - Expected: +6 SEO, +5 AEO points

### Priority 2 (High Impact, Moderate Effort) — Potential Gain: +5 SEO, +15 AEO, +14 GEO

6. **Reduce scripts from 129 → <50 (defer non-critical JS)** — SEO +5
   - Audit JavaScript dependencies; defer non-critical scripts
   - Implement image lazy loading for all 52 images
   - Expected: +5 SEO points

7. **Add sitemap directive to robots.txt** — SEO +4
   - Add line: `Sitemap: https://dimonoff.com/sitemap.xml`
   - Expected: +4 SEO points

8. **Add Product Schema for SCMS service** — AEO +15, GEO +8
   - Include name, description, brand, pricing, availability
   - Use Yoast or manual JSON-LD
   - Expected: +15 AEO, +8 GEO points

9. **Add AI crawler directives to robots.txt** — GEO +8
   - Add: Allow directives for GPTBot, ClaudeBot, PerplexityBot, Google-Extended
   - Expected: +8 GEO points

10. **Add Smart Lighting Control to llms.txt** — GEO +6
    - Include in site's llms.txt with accurate description
    - Expected: +6 GEO points

### Priority 3 (Nice to Have, Lower Effort) — Potential Gain: +5 SEO, +12 AEO, +18 GEO

11. **Convert 2-3 headings to question format** — AEO +7, GEO +3
    - Example: "How does Smart Lighting Control work?"
    - Helps with voice search and People Also Ask boxes
    - Expected: +7 AEO, +3 GEO points

12. **Add article:published_time and modified_time meta tags** — GEO +8
    - Add date signals for freshness; include visible "Last updated" date
    - Expected: +8 GEO points

13. **Add 2-3 citable statistics** — AEO +5, GEO +7
    - Research market data, energy savings, adoption rates
    - Include with sources
    - Expected: +5 AEO, +7 GEO points

14. **Expand meta title to 50-60 characters** — SEO +5
    - Rewrite: "Smart Lighting Control Systems | Dimonoff SCMS" (55 chars)
    - Expected: +5 SEO points

---

## Projected Impact

**After P1 fixes:**
- SEO: 60 → 76 (+16 points)
- AEO: 18 → 46 (+28 points)
- GEO: 35 → 57 (+22 points)
- **Total: 113 → 179/300 (+66 points, 59% improvement)**

**After P1+P2 fixes:**
- SEO: 76 → 85 (+9 points)
- AEO: 46 → 70 (+24 points)
- GEO: 57 → 79 (+22 points)
- **Total: 179 → 234/300 (+55 points, 78% overall)**

**After P1+P2+P3 fixes:**
- SEO: 85 → 95 (+10 points)
- AEO: 70 → 87 (+17 points)
- GEO: 79 → 113 (+34 points)
- **Total: 234 → 295/300 (+61 points, 98% overall)**

---

## Data Collection Notes

**Raw data used:**
- Meta title: "Smart Lighting Control | Dimonoff" (33 chars)
- Meta description: 155 chars (good quality)
- H1: 1x "Smart Lighting Control" ✅
- H2s: 15 total, 12 duplicates 🔴
- Images: 52 total, 14 with alt, 38 without (27% coverage)
- Internal links: 23 ✅
- External links: 4 with rel attributes ✅
- Canonical: self-referencing ✅
- Hreflangs: EN/FR/ES ✅
- TTFB: 4200ms 🔴
- DOM elements: 2458 ✅
- Scripts: 129 🔴
- Stylesheets: 11
- Lazy loading: 0 images
- HTTPS: Yes, no mixed content ✅
- Viewport: Present ✅
- Sitemap in robots.txt: NO 🔴
- FAQ Schema: No
- HowTo Schema: N/A
- Product Schema: No
- BreadcrumbList Schema: Yes ✅
- Organization Schema: Yes ✅
- Question headings: 1/15
- Definition paragraphs: 0
- Comparison tables: 0
- Structured lists: 3
- Voice search tone: Formal (not conversational)
- llms.txt: Present but missing Smart Lighting Control page
- robots.txt: Basic (68 bytes), no AI directives, no sitemap
- Entity-first paragraph: No
- Article dates: No meta tags
- sameAs links: Partial (LinkedIn, Twitter)
- Citable statistics: 1
- Freshness: Unknown (no visible update date)
- Author: Organization (Dimonoff) only
- Unique value: SCMS platform ✅
- Cross-language consistency: Partial

---

## Interactive Report

A detailed interactive HTML dashboard has been generated with:
- Score cards showing SEO (60), AEO (18), GEO (35)
- Audit items table with pass/warn/fail indicators
- Prioritized recommendations with impact estimates
- Implementation status tracking

**Report location**: `/sessions/kind-eager-bardeen/seo-audit-workspace/iteration-1/eval-1-audit-dimonoff/with_skill/outputs/audit-report.html`

---

## Next Steps

1. **Review & Approve**: Confirm which priority levels to implement (P1 / P1+P2 / P1+P2+P3)
2. **Implement**: Deploy fixes in order, testing 1-2 changes at a time
3. **Revalidate**: Re-run audit after 1 week to measure actual impact vs. projections
4. **Iterate**: Repeat audit cycle if score improvements plateau or new issues appear

**Recommendation**: Start with P1 fixes (performance, images, FAQ schema) for maximum impact with reasonable effort.

