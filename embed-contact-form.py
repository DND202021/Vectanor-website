#!/usr/bin/env python3
"""
Vectanor Website -- Embed WPForms Contact Form in Contact Page (page 25)

Usage:
    python3 embed-contact-form.py --form-id XX

Where XX is the WPForms form ID found in:
    WP Admin > WPForms > All Forms (shown in the ID column or at the top of the editor)

What this does:
    Rebuilds the French Contact page (page 25) with the WPForms shortcode
    [wpforms id="XX"] embedded in the right-hand panel where the placeholder text is.

Pattern:
    Follows the two-step meta push from rebuild-wow.py:
    Step 1: POST to set edit_mode and template_type meta
    Step 2: POST to set _elementor_data with the contact page + form shortcode
"""

import argparse
import json
import random
import string
import sys

import requests

# ═══════════════════════════════════════
# CREDENTIALS (same as rebuild-wow.py)
# ═══════════════════════════════════════
WP_URL = "https://vectanor.com/wp-json/wp/v2"
AUTH = ("dnoiseux", "RcF2 FMi0 wjwu QlJV bNEo pPs5")

# Page ID for the French Contact page
CONTACT_PAGE_ID = 25

# Brand colours (keep consistent with rebuild-wow.py)
NAVY = "#1E3A8A"
ROYAL_BLUE = "#3B82F6"
NEAR_BLACK = "#0F172A"
DARK_NAVY = "#0F1E4A"
SLATE = "#94A3B8"
LIGHT_GREY = "#F1F5F9"
WHITE = "#FFFFFF"

LOGOS = {
    "vectanor": "https://vectanor.com/wp-content/uploads/2026/02/vectanor_logo_concept_3.svg",
}
LOGO_IDS = {"vectanor": 9}

FADE_DOWN_CSS = """
selector {
    animation: fadeDown 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94) 0.1s both;
}
@keyframes fadeDown {
    from { opacity: 0; transform: translateY(-10px); }
    to   { opacity: 1; transform: translateY(0); }
}
"""

TAGLINE_REVEAL_CSS = """
selector {
    max-width: 650px;
    margin-left: auto;
    margin-right: auto;
    animation: tagReveal 1s cubic-bezier(0.25, 0.46, 0.45, 0.94) 0.7s both;
}
@keyframes tagReveal {
    from { opacity: 0; transform: translateY(15px); filter: blur(3px); }
    to   { opacity: 1; transform: translateY(0); filter: blur(0); }
}
"""

HERO_TITLE_CSS = """
selector .elementor-heading-title {
    background: linear-gradient(135deg, #FFFFFF 0%, #CBD5E1 40%, #93C5FD 70%, #3B82F6 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    display: inline-block;
    animation: fadeUp 1s cubic-bezier(0.25, 0.46, 0.45, 0.94) 0.2s both;
}
@keyframes fadeUp {
    from { opacity: 0; transform: translateY(30px); filter: blur(8px); }
    to   { opacity: 1; transform: translateY(0); filter: blur(0); }
}
"""


# ═══════════════════════════════════════
# ELEMENT BUILDERS (mirrors rebuild-wow.py)
# ═══════════════════════════════════════

def eid():
    """Generate a random 7-character Elementor element ID."""
    return ''.join(random.choices(string.hexdigits[:16], k=7))


def container(settings=None, elements=None):
    return {
        "id": eid(),
        "elType": "container",
        "settings": settings or {},
        "elements": elements or [],
        "isInner": False,
    }


def inner_container(settings=None, elements=None):
    return {
        "id": eid(),
        "elType": "container",
        "settings": settings or {},
        "elements": elements or [],
        "isInner": True,
    }


def widget(widget_type, settings=None):
    return {
        "id": eid(),
        "elType": "widget",
        "widgetType": widget_type,
        "settings": settings or {},
    }


def push_page(page_id, elementor_data, title_hint="Contact"):
    """
    Two-step meta push (same pattern as rebuild-wow.py):
    Step 1: Set edit_mode and template_type
    Step 2: Push _elementor_data JSON
    """
    json_str = json.dumps(elementor_data)

    print(f"  Step 1: Setting Elementor edit mode for page {page_id}...")
    r1 = requests.post(
        f"{WP_URL}/pages/{page_id}",
        auth=AUTH,
        json={
            "status": "publish",
            "meta": {
                "_elementor_edit_mode": "builder",
                "_elementor_template_type": "wp-page",
            },
        },
    )
    if r1.status_code not in (200, 201):
        print(f"  ERROR step 1: HTTP {r1.status_code} -- {r1.text[:300]}")
        return False

    print(f"  Step 2: Pushing _elementor_data ({len(json_str):,} chars)...")
    r2 = requests.post(
        f"{WP_URL}/pages/{page_id}",
        auth=AUTH,
        json={"meta": {"_elementor_data": json_str}},
    )
    if r2.status_code not in (200, 201):
        print(f"  ERROR step 2: HTTP {r2.status_code} -- {r2.text[:300]}")
        return False

    d = r2.json()
    saved = d.get("meta", {}).get("_elementor_data", "")
    title = d.get("title", {}).get("rendered", title_hint)
    status = d.get("status", "?")
    print(f"  OK -> {title}: {len(saved):,} chars saved [{status}]")
    return True


# ═══════════════════════════════════════
# CONTACT PAGE BUILDER (with embedded form)
# ═══════════════════════════════════════

def build_contact_page_with_form(form_id: int):
    """
    Rebuilds the full French Contact page with the WPForms shortcode embedded
    in the right-hand panel. Mirrors the layout from rebuild-wow.py's
    build_contact_page() but replaces the placeholder text with the live form.
    """
    elements = []

    # --- HERO ---
    elements.append(container(
        settings={
            "content_width": "full",
            "min_height": {"size": 50, "unit": "vh"},
            "background_background": "gradient",
            "background_color": NEAR_BLACK,
            "background_color_b": DARK_NAVY,
            "background_gradient_angle": {"size": 145, "unit": "deg"},
            "background_overlay_background": "gradient",
            "background_overlay_color": "rgba(59,130,246,0.12)",
            "background_overlay_color_b": "rgba(14,165,233,0)",
            "background_overlay_gradient_type": "radial",
            "background_overlay_gradient_position": "top center",
            "flex_direction": "column",
            "flex_justify_content": "center",
            "flex_align_items": "center",
            "padding": {"top": "100", "bottom": "100", "left": "40", "right": "40", "unit": "px"},
        },
        elements=[
            widget("heading", {
                "title": "Contactez-nous",
                "header_size": "h1",
                "align": "center",
                "title_color": WHITE,
                "typography_typography": "custom",
                "typography_font_family": "Montserrat",
                "typography_font_size": {"size": 56, "unit": "px"},
                "typography_font_weight": "700",
                "typography_letter_spacing": {"size": 2, "unit": "px"},
                "_margin": {"top": "0", "bottom": "24", "left": "0", "right": "0", "unit": "px"},
                "custom_css": HERO_TITLE_CSS,
            }),
            widget("heading", {
                "title": "Parlons de vos projets d'infrastructure",
                "header_size": "h3",
                "align": "center",
                "title_color": "#94A3B8",
                "typography_typography": "custom",
                "typography_font_family": "Space Grotesk",
                "typography_font_size": {"size": 21, "unit": "px"},
                "typography_font_weight": "400",
                "typography_line_height": {"size": 1.7, "unit": "em"},
                "_margin": {"top": "0", "bottom": "0", "left": "0", "right": "0", "unit": "px"},
                "custom_css": TAGLINE_REVEAL_CSS,
            }),
        ],
    ))

    # --- MAIN CONTENT: left info + right form ---
    elements.append(container(
        settings={
            "content_width": "boxed",
            "background_background": "classic",
            "background_color": WHITE,
            "flex_direction": "column",
            "flex_align_items": "center",
            "padding": {"top": "80", "bottom": "80", "left": "40", "right": "40", "unit": "px"},
        },
        elements=[
            inner_container(
                settings={
                    "flex_direction": "row",
                    "flex_wrap": "wrap",
                    "flex_gap": {"size": 60, "unit": "px"},
                    "flex_justify_content": "center",
                    "width": {"size": 100, "unit": "%"},
                    "max_width": {"size": 900, "unit": "px"},
                },
                elements=[
                    # Left column: logo + contact info
                    inner_container(
                        settings={
                            "flex_direction": "column",
                            "flex_gap": {"size": 25, "unit": "px"},
                            "width": {"size": 350, "unit": "px"},
                            "_animation": "fadeInLeft",
                        },
                        elements=[
                            widget("image", {
                                "image": {
                                    "url": LOGOS["vectanor"],
                                    "id": LOGO_IDS["vectanor"],
                                },
                                "image_size": "full",
                                "width": {"size": 180, "unit": "px"},
                                "_margin": {"top": "0", "bottom": "10", "left": "0", "right": "0", "unit": "px"},
                            }),
                            widget("icon-list", {
                                "icon_list": [
                                    {
                                        "_id": eid(),
                                        "text": "Quebec, Canada",
                                        "selected_icon": {"value": "fas fa-map-marker-alt", "library": "fa-solid"},
                                        "link": {"url": ""},
                                    },
                                    {
                                        "_id": eid(),
                                        "text": "info@vectanor.com",
                                        "selected_icon": {"value": "fas fa-envelope", "library": "fa-solid"},
                                        "link": {"url": "mailto:info@vectanor.com"},
                                    },
                                ],
                                "icon_color": ROYAL_BLUE,
                                "text_color": "#475569",
                                "typography_typography": "custom",
                                "typography_font_family": "Inter",
                                "typography_font_size": {"size": 16, "unit": "px"},
                            }),
                            widget("text-editor", {
                                "editor": (
                                    '<p style="font-size:16px; line-height:1.8; color:#475569;">'
                                    'Pour les demandes li\u00e9es \u00e0 une division sp\u00e9cifique, '
                                    "n\u2019h\u00e9sitez pas \u00e0 nous contacter. Nous vous dirigerons "
                                    'vers l\u2019\u00e9quipe appropri\u00e9e.</p>'
                                ),
                            }),
                        ],
                    ),
                    # Right column: WPForms contact form
                    inner_container(
                        settings={
                            "flex_direction": "column",
                            "width": {"size": 450, "unit": "px"},
                            "background_background": "classic",
                            "background_color": LIGHT_GREY,
                            "border_radius": {
                                "top": "12", "bottom": "12",
                                "left": "12", "right": "12", "unit": "px",
                            },
                            "padding": {
                                "top": "35", "bottom": "35",
                                "left": "35", "right": "35", "unit": "px",
                            },
                            "_animation": "fadeInRight",
                        },
                        elements=[
                            widget("heading", {
                                "title": "Envoyez-nous un message",
                                "header_size": "h4",
                                "title_color": NEAR_BLACK,
                                "typography_typography": "custom",
                                "typography_font_family": "Montserrat",
                                "typography_font_size": {"size": 20, "unit": "px"},
                                "typography_font_weight": "600",
                                "_margin": {
                                    "top": "0", "bottom": "20",
                                    "left": "0", "right": "0", "unit": "px",
                                },
                            }),
                            # WPForms shortcode widget
                            widget("shortcode", {
                                "shortcode": f'[wpforms id="{form_id}"]',
                            }),
                        ],
                    ),
                ],
            ),
        ],
    ))

    return elements


# ═══════════════════════════════════════
# MAIN
# ═══════════════════════════════════════

def parse_args():
    parser = argparse.ArgumentParser(
        description="Embed WPForms contact form into the Vectanor French Contact page (page 25)."
    )
    parser.add_argument(
        "--form-id",
        type=int,
        required=False,
        metavar="ID",
        help="WPForms form ID (shown in WP Admin > WPForms > All Forms).",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    # Prompt for form ID if not supplied via CLI
    form_id = args.form_id
    if form_id is None:
        try:
            raw = input("Enter WPForms form ID: ").strip()
            form_id = int(raw)
        except (ValueError, EOFError):
            print("ERROR: Form ID must be an integer.")
            sys.exit(1)

    if form_id <= 0:
        print(f"ERROR: Form ID must be a positive integer, got {form_id}.")
        sys.exit(1)

    print("=" * 60)
    print("VECTANOR -- Embed WPForms Contact Form")
    print("=" * 60)
    print(f"  Form ID : {form_id}")
    print(f"  Page ID : {CONTACT_PAGE_ID} (Contact / /contact/)")
    print(f"  WP URL  : {WP_URL}")
    print()

    elements = build_contact_page_with_form(form_id)
    success = push_page(CONTACT_PAGE_ID, elements, title_hint="Contact")

    print()
    if success:
        print("=" * 60)
        print("SUCCESS! Contact form embedded.")
        print(f"  Shortcode used : [wpforms id=\"{form_id}\"]")
        print("  Verify at      : https://vectanor.com/contact/")
        print("=" * 60)
    else:
        print("=" * 60)
        print("FAILED. Check errors above.")
        print("  Common causes:")
        print("  - Invalid WP Application Password (AUTH in script)")
        print("  - Network / firewall issue reaching vectanor.com")
        print("  - Page ID 25 does not exist (check WP Admin > Pages)")
        print("=" * 60)
        sys.exit(1)


if __name__ == "__main__":
    main()
