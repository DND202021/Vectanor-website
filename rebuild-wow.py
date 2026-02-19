#!/usr/bin/env python3
"""
Vectanor Website — Complete WOW Redesign
Rebuilds ALL pages with premium 2026 design:
- Glassmorphism cards, gradient text, animated bars
- Entrance animations, hover glow effects
- Logo integration, external division links
- Vigilia division page
"""

import json
import random
import string
import requests

WP_URL = "https://vectanor.com/wp-json/wp/v2"
AUTH = ("dnoiseux", "RcF2 FMi0 wjwu QlJV bNEo pPs5")

# ═══════════════════════════════════════
# BRAND SYSTEM
# ═══════════════════════════════════════
NAVY = "#1E3A8A"
ROYAL_BLUE = "#3B82F6"
SKY_BLUE = "#0EA5E9"
NEAR_BLACK = "#0F172A"
DARK_NAVY = "#0F1E4A"
SLATE = "#94A3B8"
LIGHT_GREY = "#F1F5F9"
WHITE = "#FFFFFF"
AMBER = "#F59E0B"
GREEN = "#10B981"
PURPLE = "#8B5CF6"
PINK = "#EC4899"

# Logo URLs from media library
LOGOS = {
    "vectanor": "https://vectanor.com/wp-content/uploads/2026/02/vectanor_logo_concept_3.svg",
    "dimonoff": "https://vectanor.com/wp-content/uploads/2026/02/Logo-Dimonoff-horizontal-charcoal_original-1.svg",
    "spatium": "https://vectanor.com/wp-content/uploads/2026/02/logo-Dimonoff-Mobility.Spatium-color.png",
    "amotus": "https://vectanor.com/wp-content/uploads/2026/02/AMOTUS-Logo_H-RGB-2.svg",
    "vigilia": "https://vectanor.com/wp-content/uploads/2026/02/Vigilia_Logo_vector.svg",
}

LOGO_IDS = {"vectanor": 9, "dimonoff": 12, "spatium": 14, "amotus": 13, "vigilia": 15}

# External links
DIVISION_URLS = {
    "dimonoff": "https://dimonoff.com",
    "spatium": "https://dimonoff.com",  # Spatium is part of Dimonoff
    "amotus": "https://amotus.com",
    "vigilia": None,  # No website yet
}

# Page IDs
PAGES = {
    "accueil": 19,
    "vision": 20,
    "divisions": 21,
    "dimonoff": 22,
    "spatium": 23,
    "amotus": 24,
    "contact": 25,
    "vigilia": 36,
}

# ═══════════════════════════════════════
# LANGUAGE URL MAPS
# ═══════════════════════════════════════
LANG_URLS = {
    "fr": {
        "homepage": "/", "vision": "/vision/", "divisions": "/divisions/",
        "dimonoff": "/divisions/dimonoff/", "spatium": "/divisions/spatium/",
        "amotus": "/divisions/amotus/", "vigilia": "/divisions/vigilia/",
        "contact": "/contact/",
    },
    "en": {
        "homepage": "/en/", "vision": "/en/our-vision/", "divisions": "/en/our-divisions/",
        "dimonoff": "/en/our-divisions/dimonoff/", "spatium": "/en/our-divisions/spatium/",
        "amotus": "/en/our-divisions/amotus/", "vigilia": "/en/our-divisions/vigilia/",
        "contact": "/en/contact-us/",
    },
    "es": {
        "homepage": "/es/", "vision": "/es/nuestra-vision/", "divisions": "/es/nuestras-divisiones/",
        "dimonoff": "/es/nuestras-divisiones/dimonoff/", "spatium": "/es/nuestras-divisiones/spatium/",
        "amotus": "/es/nuestras-divisiones/amotus/", "vigilia": "/es/nuestras-divisiones/vigilia/",
        "contact": "/es/contactenos/",
    },
}

LANG_LABELS = {"fr": "FR", "en": "EN", "es": "ES"}


# Navigation labels per language
NAV_LABELS = {
    "fr": {"vision": "Vision", "divisions": "Divisions", "contact": "Contact"},
    "en": {"vision": "Our Vision", "divisions": "Our Divisions", "contact": "Contact Us"},
    "es": {"vision": "Nuestra Visión", "divisions": "Nuestras Divisiones", "contact": "Contáctenos"},
}

# Footer translations
FOOTER_TEXT = {
    "fr": {
        "description": "Holding technologique canadienne. Éclairage, mobilité, électronique, monitoring.",
        "divisions_label": "DIVISIONS",
        "links_label": "LIENS RAPIDES",
        "contact_label": "CONTACT",
        "location": "Québec, Canada",
        "copyright": "© 2026 Groupe Vectanor. Tous droits réservés.",
    },
    "en": {
        "description": "Canadian technology holding. Lighting, mobility, electronics, monitoring.",
        "divisions_label": "DIVISIONS",
        "links_label": "QUICK LINKS",
        "contact_label": "CONTACT",
        "location": "Québec, Canada",
        "copyright": "© 2026 Groupe Vectanor. All rights reserved.",
    },
    "es": {
        "description": "Holding tecnológica canadiense. Iluminación, movilidad, electrónica, monitoreo.",
        "divisions_label": "DIVISIONES",
        "links_label": "ENLACES RÁPIDOS",
        "contact_label": "CONTACTO",
        "location": "Québec, Canadá",
        "copyright": "© 2026 Groupe Vectanor. Todos los derechos reservados.",
    },
}


def site_header(current_lang, page_key):
    """Elementor container: sticky glassmorphic header with logo, nav, and language switcher."""
    urls = LANG_URLS[current_lang]
    nav = NAV_LABELS[current_lang]

    # Build nav links HTML
    nav_items = []
    for key, label in nav.items():
        url = urls.get(key, "/")
        is_current = (key == page_key)
        if is_current:
            nav_items.append(
                f'<a href="{url}" style="color:#FFFFFF;font-family:Montserrat,sans-serif;font-size:14px;'
                f'font-weight:600;text-decoration:none;letter-spacing:0.5px;border-bottom:2px solid {ROYAL_BLUE};'
                f'padding-bottom:4px;">{label}</a>'
            )
        else:
            nav_items.append(
                f'<a href="{url}" style="color:{SLATE};font-family:Montserrat,sans-serif;font-size:14px;'
                f'font-weight:600;text-decoration:none;letter-spacing:0.5px;padding-bottom:4px;'
                f'border-bottom:2px solid transparent;transition:all 0.25s ease;"'
                f' onmouseover="this.style.color=\'#FFFFFF\';this.style.borderBottomColor=\'{ROYAL_BLUE}\'"'
                f' onmouseout="this.style.color=\'{SLATE}\';this.style.borderBottomColor=\'transparent\'">{label}</a>'
            )
    nav_html = '  '.join(nav_items)

    # Build language switcher HTML
    lang_links = []
    for lang in ("fr", "en", "es"):
        url = LANG_URLS[lang].get(page_key, "/")
        label = LANG_LABELS[lang]
        if lang == current_lang:
            lang_links.append(f'<span style="color:#FFFFFF;font-weight:700;font-size:12px;">{label}</span>')
        else:
            lang_links.append(
                f'<a href="{url}" style="color:{SLATE};font-size:12px;text-decoration:none;font-weight:500;'
                f'transition:color 0.2s;" onmouseover="this.style.color=\'#FFFFFF\'"'
                f' onmouseout="this.style.color=\'{SLATE}\'">{label}</a>'
            )
    lang_html = ' <span style="color:#334155;font-size:12px;">|</span> '.join(lang_links)

    # 4-color accent bar (bottom of header)
    bar_html = (
        '<div style="position:absolute;bottom:0;left:0;right:0;height:2px;display:flex;">'
        f'<div style="flex:1;background:{AMBER};"></div>'
        f'<div style="flex:1;background:{GREEN};"></div>'
        f'<div style="flex:1;background:{PURPLE};"></div>'
        f'<div style="flex:1;background:{PINK};"></div>'
        '</div>'
    )

    header_html = (
        f'<div style="position:sticky;top:0;z-index:999;background:rgba(15,23,42,0.92);'
        f'backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);padding:0 30px;">'
        f'<div style="max-width:1200px;margin:0 auto;display:flex;align-items:center;'
        f'justify-content:space-between;height:60px;">'
        # Logo
        f'<a href="{urls.get("homepage", "/")}" style="display:flex;align-items:center;text-decoration:none;">'
        f'<img src="{LOGOS["vectanor"]}" alt="Vectanor" style="height:30px;filter:brightness(0) invert(1);"></a>'
        # Nav
        f'<nav style="display:flex;gap:32px;align-items:center;">{nav_html}</nav>'
        # Language
        f'<div style="display:flex;gap:10px;align-items:center;font-family:Montserrat,sans-serif;'
        f'letter-spacing:1px;">{lang_html}</div>'
        f'</div>'
        f'{bar_html}'
        f'</div>'
    )

    return container(
        settings={
            "content_width": "full",
            "padding": {"top": "0", "bottom": "0", "left": "0", "right": "0", "unit": "px"},
            "margin": {"top": "0", "bottom": "0", "left": "0", "right": "0", "unit": "px"},
        },
        elements=[widget("html", {"html": header_html})],
    )


def site_footer(current_lang):
    """Elementor container: 4-column footer with divisions, links, contact."""
    urls = LANG_URLS[current_lang]
    txt = FOOTER_TEXT[current_lang]
    nav = NAV_LABELS[current_lang]

    # 4-color top bar
    bar = (
        f'<div style="height:3px;display:flex;margin-bottom:50px;">'
        f'<div style="flex:1;background:{AMBER};"></div>'
        f'<div style="flex:1;background:{GREEN};"></div>'
        f'<div style="flex:1;background:{PURPLE};"></div>'
        f'<div style="flex:1;background:{PINK};"></div>'
        f'</div>'
    )

    label_style = "font-family:Montserrat,sans-serif;font-size:11px;font-weight:700;letter-spacing:2px;color:#64748B;margin-bottom:18px;text-transform:uppercase;"
    link_style = f"display:block;font-family:Outfit,sans-serif;font-size:14px;color:{SLATE};text-decoration:none;margin-bottom:10px;transition:color 0.2s;"

    # Column 1: Logo + desc
    col1 = (
        f'<div style="flex:1.2;min-width:200px;">'
        f'<img src="{LOGOS["vectanor"]}" alt="Vectanor" style="height:28px;filter:brightness(0) invert(1) opacity(0.7);margin-bottom:14px;">'
        f'<p style="font-family:Outfit,sans-serif;font-size:14px;line-height:1.7;color:#64748B;margin:0;">{txt["description"]}</p>'
        f'</div>'
    )

    # Column 2: Divisions
    div_links = ''.join(
        f'<a href="{urls.get(k, "/")}" style="{link_style}" '
        f'onmouseover="this.style.color=\'#FFFFFF\'" onmouseout="this.style.color=\'{SLATE}\'">{n}</a>'
        for k, n in [("dimonoff", "Dimonoff"), ("spatium", "Spatium"), ("amotus", "Amotus"), ("vigilia", "Vigilia")]
    )
    col2 = f'<div style="flex:0.8;min-width:140px;"><p style="{label_style}">{txt["divisions_label"]}</p>{div_links}</div>'

    # Column 3: Quick Links
    quick_links = ''.join(
        f'<a href="{urls.get(k, "/")}" style="{link_style}" '
        f'onmouseover="this.style.color=\'#FFFFFF\'" onmouseout="this.style.color=\'{SLATE}\'">{nav[k]}</a>'
        for k in ("vision", "divisions", "contact")
    )
    col3 = f'<div style="flex:0.8;min-width:140px;"><p style="{label_style}">{txt["links_label"]}</p>{quick_links}</div>'

    # Column 4: Contact
    col4 = (
        f'<div style="flex:0.8;min-width:140px;">'
        f'<p style="{label_style}">{txt["contact_label"]}</p>'
        f'<p style="font-family:Outfit,sans-serif;font-size:14px;color:{SLATE};margin:0 0 10px 0;">{txt["location"]}</p>'
        f'<a href="mailto:info@vectanor.com" style="{link_style}" '
        f'onmouseover="this.style.color=\'#FFFFFF\'" onmouseout="this.style.color=\'{SLATE}\'">info@vectanor.com</a>'
        f'</div>'
    )

    # Language switcher for bottom row
    lang_links = []
    for lang in ("fr", "en", "es"):
        lbl = LANG_LABELS[lang]
        url = LANG_URLS[lang].get("homepage", "/")
        if lang == current_lang:
            lang_links.append(f'<span style="color:#FFFFFF;font-weight:700;font-size:12px;">{lbl}</span>')
        else:
            lang_links.append(
                f'<a href="{url}" style="color:#64748B;font-size:12px;text-decoration:none;transition:color 0.2s;"'
                f' onmouseover="this.style.color=\'#FFFFFF\'" onmouseout="this.style.color=\'#64748B\'">{lbl}</a>'
            )
    lang_sw = ' <span style="color:#334155;font-size:12px;">|</span> '.join(lang_links)

    bottom = (
        f'<div style="display:flex;justify-content:space-between;align-items:center;'
        f'border-top:1px solid rgba(255,255,255,0.06);margin-top:40px;padding-top:24px;flex-wrap:wrap;gap:12px;">'
        f'<p style="font-family:Outfit,sans-serif;font-size:13px;color:#475569;margin:0;">{txt["copyright"]}</p>'
        f'<div style="font-family:Montserrat,sans-serif;letter-spacing:1px;">{lang_sw}</div>'
        f'</div>'
    )

    footer_html = (
        f'{bar}'
        f'<div style="max-width:1100px;margin:0 auto;display:flex;flex-wrap:wrap;gap:40px;">'
        f'{col1}{col2}{col3}{col4}'
        f'</div>'
        f'{bottom}'
    )

    return container(
        settings={
            "content_width": "full",
            "background_background": "gradient",
            "background_color": NEAR_BLACK,
            "background_color_b": DARK_NAVY,
            "background_gradient_angle": {"size": 180, "unit": "deg"},
            "padding": {"top": "60", "bottom": "40", "left": "40", "right": "40", "unit": "px"},
        },
        elements=[widget("html", {"html": footer_html})],
    )


def site_header_html(current_lang, page_key):
    """Raw HTML header for non-Elementor pages (contact pages)."""
    urls = LANG_URLS[current_lang]
    nav = NAV_LABELS[current_lang]

    nav_items = []
    for key, label in nav.items():
        url = urls.get(key, "/")
        is_current = (key == page_key)
        if is_current:
            nav_items.append(
                f'<a href="{url}" style="color:#FFFFFF;font-family:Montserrat,sans-serif;font-size:14px;'
                f'font-weight:600;text-decoration:none;letter-spacing:0.5px;border-bottom:2px solid {ROYAL_BLUE};'
                f'padding-bottom:4px;">{label}</a>'
            )
        else:
            nav_items.append(
                f'<a href="{url}" style="color:{SLATE};font-family:Montserrat,sans-serif;font-size:14px;'
                f'font-weight:600;text-decoration:none;letter-spacing:0.5px;padding-bottom:4px;'
                f'border-bottom:2px solid transparent;transition:all 0.25s ease;"'
                f' onmouseover="this.style.color=\'#FFFFFF\';this.style.borderBottomColor=\'{ROYAL_BLUE}\'"'
                f' onmouseout="this.style.color=\'{SLATE}\';this.style.borderBottomColor=\'transparent\'">{label}</a>'
            )
    nav_html = '  '.join(nav_items)

    lang_links = []
    for lang in ("fr", "en", "es"):
        url = LANG_URLS[lang].get(page_key, "/")
        label = LANG_LABELS[lang]
        if lang == current_lang:
            lang_links.append(f'<span style="color:#FFFFFF;font-weight:700;font-size:12px;">{label}</span>')
        else:
            lang_links.append(
                f'<a href="{url}" style="color:{SLATE};font-size:12px;text-decoration:none;font-weight:500;'
                f'transition:color 0.2s;" onmouseover="this.style.color=\'#FFFFFF\'"'
                f' onmouseout="this.style.color=\'{SLATE}\'">{label}</a>'
            )
    lang_html = ' <span style="color:#334155;font-size:12px;">|</span> '.join(lang_links)

    bar_html = (
        '<div style="position:absolute;bottom:0;left:0;right:0;height:2px;display:flex;">'
        f'<div style="flex:1;background:{AMBER};"></div>'
        f'<div style="flex:1;background:{GREEN};"></div>'
        f'<div style="flex:1;background:{PURPLE};"></div>'
        f'<div style="flex:1;background:{PINK};"></div>'
        '</div>'
    )

    return (
        f'<div style="position:sticky;top:0;z-index:999;background:rgba(15,23,42,0.92);'
        f'backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);padding:0 30px;">'
        f'<div style="max-width:1200px;margin:0 auto;display:flex;align-items:center;'
        f'justify-content:space-between;height:60px;">'
        f'<a href="{urls.get("homepage", "/")}" style="display:flex;align-items:center;text-decoration:none;">'
        f'<img src="{LOGOS["vectanor"]}" alt="Vectanor" style="height:30px;filter:brightness(0) invert(1);"></a>'
        f'<nav style="display:flex;gap:32px;align-items:center;">{nav_html}</nav>'
        f'<div style="display:flex;gap:10px;align-items:center;font-family:Montserrat,sans-serif;'
        f'letter-spacing:1px;">{lang_html}</div>'
        f'</div>'
        f'{bar_html}'
        f'</div>'
    )


def site_footer_html(current_lang):
    """Raw HTML footer for non-Elementor pages (contact pages)."""
    urls = LANG_URLS[current_lang]
    txt = FOOTER_TEXT[current_lang]
    nav = NAV_LABELS[current_lang]

    label_style = "font-family:Montserrat,sans-serif;font-size:11px;font-weight:700;letter-spacing:2px;color:#64748B;margin-bottom:18px;text-transform:uppercase;"
    link_style = f"display:block;font-family:Outfit,sans-serif;font-size:14px;color:{SLATE};text-decoration:none;margin-bottom:10px;transition:color 0.2s;"

    bar = (
        f'<div style="height:3px;display:flex;margin-bottom:50px;">'
        f'<div style="flex:1;background:{AMBER};"></div>'
        f'<div style="flex:1;background:{GREEN};"></div>'
        f'<div style="flex:1;background:{PURPLE};"></div>'
        f'<div style="flex:1;background:{PINK};"></div>'
        f'</div>'
    )

    col1 = (
        f'<div style="flex:1.2;min-width:200px;">'
        f'<img src="{LOGOS["vectanor"]}" alt="Vectanor" style="height:28px;filter:brightness(0) invert(1) opacity(0.7);margin-bottom:14px;">'
        f'<p style="font-family:Outfit,sans-serif;font-size:14px;line-height:1.7;color:#64748B;margin:0;">{txt["description"]}</p>'
        f'</div>'
    )

    div_links = ''.join(
        f'<a href="{urls.get(k, "/")}" style="{link_style}"'
        f' onmouseover="this.style.color=\'#FFFFFF\'" onmouseout="this.style.color=\'{SLATE}\'">{n}</a>'
        for k, n in [("dimonoff", "Dimonoff"), ("spatium", "Spatium"), ("amotus", "Amotus"), ("vigilia", "Vigilia")]
    )
    col2 = f'<div style="flex:0.8;min-width:140px;"><p style="{label_style}">{txt["divisions_label"]}</p>{div_links}</div>'

    quick_links = ''.join(
        f'<a href="{urls.get(k, "/")}" style="{link_style}"'
        f' onmouseover="this.style.color=\'#FFFFFF\'" onmouseout="this.style.color=\'{SLATE}\'">{nav[k]}</a>'
        for k in ("vision", "divisions", "contact")
    )
    col3 = f'<div style="flex:0.8;min-width:140px;"><p style="{label_style}">{txt["links_label"]}</p>{quick_links}</div>'

    col4 = (
        f'<div style="flex:0.8;min-width:140px;">'
        f'<p style="{label_style}">{txt["contact_label"]}</p>'
        f'<p style="font-family:Outfit,sans-serif;font-size:14px;color:{SLATE};margin:0 0 10px 0;">{txt["location"]}</p>'
        f'<a href="mailto:info@vectanor.com" style="{link_style}"'
        f' onmouseover="this.style.color=\'#FFFFFF\'" onmouseout="this.style.color=\'{SLATE}\'">info@vectanor.com</a>'
        f'</div>'
    )

    lang_links = []
    for lang in ("fr", "en", "es"):
        lbl = LANG_LABELS[lang]
        url = LANG_URLS[lang].get("homepage", "/")
        if lang == current_lang:
            lang_links.append(f'<span style="color:#FFFFFF;font-weight:700;font-size:12px;">{lbl}</span>')
        else:
            lang_links.append(
                f'<a href="{url}" style="color:#64748B;font-size:12px;text-decoration:none;transition:color 0.2s;"'
                f' onmouseover="this.style.color=\'#FFFFFF\'" onmouseout="this.style.color=\'#64748B\'">{lbl}</a>'
            )
    lang_sw = ' <span style="color:#334155;font-size:12px;">|</span> '.join(lang_links)

    return (
        f'<div style="background:linear-gradient(180deg,{NEAR_BLACK},{DARK_NAVY});padding:60px 40px 40px;">'
        f'{bar}'
        f'<div style="max-width:1100px;margin:0 auto;display:flex;flex-wrap:wrap;gap:40px;">'
        f'{col1}{col2}{col3}{col4}'
        f'</div>'
        f'<div style="max-width:1100px;margin:0 auto;display:flex;justify-content:space-between;align-items:center;'
        f'border-top:1px solid rgba(255,255,255,0.06);margin-top:40px;padding-top:24px;flex-wrap:wrap;gap:12px;">'
        f'<p style="font-family:Outfit,sans-serif;font-size:13px;color:#475569;margin:0;">{txt["copyright"]}</p>'
        f'<div style="font-family:Montserrat,sans-serif;letter-spacing:1px;">{lang_sw}</div>'
        f'</div>'
        f'</div>'
    )


# ═══════════════════════════════════════
# FONT LOADER
# ═══════════════════════════════════════

def font_loader():
    """Elementor HTML widget that loads Google Fonts. Inject as first element of every page."""
    return widget("html", {
        "html": (
            '<link rel="preconnect" href="https://fonts.googleapis.com">'
            '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
            '<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700;800&family=Outfit:wght@300;400;500&family=Sora:wght@400;500;600&display=swap" rel="stylesheet">'
        ),
    })


# ═══════════════════════════════════════
# CSS LIBRARY
# ═══════════════════════════════════════

# --- Background texture constants ---

GRAIN_OVERLAY_CSS = """
selector::before {
    content: '';
    position: absolute;
    inset: 0;
    opacity: 0.035;
    pointer-events: none;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
    background-repeat: repeat;
    background-size: 256px 256px;
    z-index: 1;
    mix-blend-mode: overlay;
}
selector { position: relative; }
selector > * { position: relative; z-index: 2; }
"""

GRID_PATTERN_CSS = """
selector::before {
    content: '';
    position: absolute;
    inset: 0;
    opacity: 0.04;
    pointer-events: none;
    background-image: radial-gradient(circle, #94A3B8 1px, transparent 1px);
    background-size: 28px 28px;
    z-index: 1;
}
selector { position: relative; }
selector > * { position: relative; z-index: 2; }
"""

HERO_GLOW_CSS = """
selector::after {
    content: '';
    position: absolute;
    top: -20%;
    left: 50%;
    transform: translateX(-50%);
    width: 600px;
    height: 600px;
    background: radial-gradient(circle, rgba(59,130,246,0.12) 0%, rgba(139,92,246,0.06) 40%, transparent 70%);
    pointer-events: none;
    z-index: 1;
}
selector { position: relative; overflow: hidden; }
selector > * { position: relative; z-index: 2; }
"""

DIAGONAL_ACCENT_CSS = """
selector::after {
    content: '';
    position: absolute;
    bottom: -2px;
    left: 0;
    right: 0;
    height: 80px;
    background: linear-gradient(175deg, transparent 49.5%, #F1F5F9 49.5%);
    pointer-events: none;
    z-index: 1;
}
selector { position: relative; overflow: hidden; }
"""

ORBITAL_RINGS_HTML = """
<div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:100%;height:100%;pointer-events:none;z-index:0;overflow:hidden;">
  <div style="position:absolute;top:50%;left:50%;width:500px;height:500px;margin:-250px 0 0 -250px;border:1px solid rgba(59,130,246,0.08);border-radius:50%;animation:orbitSpin 40s linear infinite;"></div>
  <div style="position:absolute;top:50%;left:50%;width:750px;height:750px;margin:-375px 0 0 -375px;border:1px solid rgba(139,92,246,0.05);border-radius:50%;animation:orbitSpin 60s linear infinite reverse;"></div>
</div>
<style>@keyframes orbitSpin{from{transform:rotate(0deg)}to{transform:rotate(360deg)}}</style>
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

CTA_BUTTON_CSS = """
selector .elementor-button {
    background: linear-gradient(135deg, #3B82F6, #0EA5E9) !important;
    border: none !important;
    position: relative;
    overflow: hidden;
    transition: all 0.35s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    animation: fadeUp 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94) 1s both;
}
selector .elementor-button:hover {
    transform: translateY(-3px);
    box-shadow: 0 12px 40px rgba(59,130,246,0.45);
}
"""

FOUR_COLOR_BAR_HTML = """
<div style="display:flex;width:240px;height:4px;margin:0 auto;overflow:hidden;border-radius:2px;gap:3px;">
  <div style="flex:1;background:#F59E0B;animation:barIn 0.6s ease 0.5s both;transform-origin:left;"></div>
  <div style="flex:1;background:#10B981;animation:barIn 0.6s ease 0.65s both;transform-origin:left;"></div>
  <div style="flex:1;background:#8B5CF6;animation:barIn 0.6s ease 0.8s both;transform-origin:left;"></div>
  <div style="flex:1;background:#EC4899;animation:barIn 0.6s ease 0.95s both;transform-origin:left;"></div>
</div>
<style>@keyframes barIn{from{transform:scaleX(0);opacity:0}to{transform:scaleX(1);opacity:1}}</style>
"""


CONTACT_FORM_HTML = """
<form action="https://formsubmit.co/info@vectanor.com" method="POST" style="display:flex;flex-direction:column;gap:14px;">
  <input type="hidden" name="_subject" value="Nouveau message via vectanor.com">
  <input type="hidden" name="_captcha" value="false">
  <input type="hidden" name="_next" value="https://vectanor.com/contact/?sent=1">
  <input type="hidden" name="_template" value="table">
  <input type="text" name="_honey" style="display:none">
  <div>
    <label style="display:block;font-family:Outfit,sans-serif;font-size:14px;color:#475569;margin-bottom:5px;font-weight:500;">Nom <span style="color:#EF4444;">*</span></label>
    <input type="text" name="name" placeholder="Votre nom complet" required
      style="width:100%;padding:10px 14px;border:1px solid #CBD5E1;border-radius:6px;font-family:Outfit,sans-serif;font-size:14px;color:#0F172A;background:#FFFFFF;outline:none;transition:border-color 0.2s;"
      onfocus="this.style.borderColor='#3B82F6'" onblur="this.style.borderColor='#CBD5E1'">
  </div>
  <div>
    <label style="display:block;font-family:Outfit,sans-serif;font-size:14px;color:#475569;margin-bottom:5px;font-weight:500;">Courriel <span style="color:#EF4444;">*</span></label>
    <input type="email" name="email" placeholder="votre@courriel.com" required
      style="width:100%;padding:10px 14px;border:1px solid #CBD5E1;border-radius:6px;font-family:Outfit,sans-serif;font-size:14px;color:#0F172A;background:#FFFFFF;outline:none;transition:border-color 0.2s;"
      onfocus="this.style.borderColor='#3B82F6'" onblur="this.style.borderColor='#CBD5E1'">
  </div>
  <div>
    <label style="display:block;font-family:Outfit,sans-serif;font-size:14px;color:#475569;margin-bottom:5px;font-weight:500;">Sujet</label>
    <select name="subject"
      style="width:100%;padding:10px 14px;border:1px solid #CBD5E1;border-radius:6px;font-family:Outfit,sans-serif;font-size:14px;color:#0F172A;background:#FFFFFF;outline:none;transition:border-color 0.2s;cursor:pointer;"
      onfocus="this.style.borderColor='#3B82F6'" onblur="this.style.borderColor='#CBD5E1'">
      <option value="Demande générale">Demande générale</option>
      <option value="Partenariat">Partenariat</option>
      <option value="Média">Média</option>
      <option value="Autre">Autre</option>
    </select>
  </div>
  <div>
    <label style="display:block;font-family:Outfit,sans-serif;font-size:14px;color:#475569;margin-bottom:5px;font-weight:500;">Message <span style="color:#EF4444;">*</span></label>
    <textarea name="message" placeholder="Votre message..." required rows="4"
      style="width:100%;padding:10px 14px;border:1px solid #CBD5E1;border-radius:6px;font-family:Outfit,sans-serif;font-size:14px;color:#0F172A;background:#FFFFFF;outline:none;resize:vertical;transition:border-color 0.2s;"
      onfocus="this.style.borderColor='#3B82F6'" onblur="this.style.borderColor='#CBD5E1'"></textarea>
  </div>
  <button type="submit"
    style="width:100%;padding:14px;background:linear-gradient(135deg,#3B82F6,#0EA5E9);color:#FFFFFF;border:none;border-radius:6px;font-family:Montserrat,sans-serif;font-size:14px;font-weight:600;cursor:pointer;transition:all 0.3s;letter-spacing:0.5px;"
    onmouseover="this.style.transform='translateY(-2px)';this.style.boxShadow='0 8px 25px rgba(59,130,246,0.4)'"
    onmouseout="this.style.transform='translateY(0)';this.style.boxShadow='none'">
    Envoyer
  </button>
</form>
<script>
if(new URLSearchParams(window.location.search).get('sent')==='1'){
  document.querySelector('form[action*="formsubmit"]').innerHTML='<div style="text-align:center;padding:40px 20px;"><div style="font-size:28px;margin-bottom:12px;">✓</div><p style="font-family:Outfit,sans-serif;font-size:16px;color:#0F172A;font-weight:500;">Merci pour votre message!</p><p style="font-family:Outfit,sans-serif;font-size:14px;color:#64748B;margin-top:8px;">Nous vous répondrons dans les plus brefs délais.</p></div>';
}
</script>
"""


def card_glow_css(color):
    return f"""
selector {{
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border-top: 3px solid {color} !important;
    transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}}
selector:hover {{
    background: rgba(255,255,255,0.07) !important;
    transform: translateY(-8px);
    box-shadow:
        0 20px 60px rgba(0,0,0,0.4),
        0 0 0 1px rgba(255,255,255,0.1),
        0 0 40px {color}20;
}}
"""


def card_light_glow_css(color):
    return f"""
selector {{
    transition: all 0.35s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    border-top: 3px solid {color} !important;
}}
selector:hover {{
    transform: translateY(-6px);
    box-shadow:
        0 20px 60px -15px {color}40,
        0 8px 25px rgba(0,0,0,0.12);
}}
"""


def button_hover_css(color):
    return f"""
selector .elementor-button {{
    transition: all 0.25s ease;
}}
selector .elementor-button:hover {{
    background: {color} !important;
    box-shadow: 0 4px 20px {color}60;
    transform: translateX(4px);
}}
"""


# ═══════════════════════════════════════
# ELEMENT BUILDERS
# ═══════════════════════════════════════

def eid():
    return ''.join(random.choices(string.hexdigits[:16], k=7))


def container(settings=None, elements=None):
    return {"id": eid(), "elType": "container", "settings": settings or {}, "elements": elements or [], "isInner": False}


def inner_container(settings=None, elements=None):
    return {"id": eid(), "elType": "container", "settings": settings or {}, "elements": elements or [], "isInner": True}


def widget(widget_type, settings=None):
    return {"id": eid(), "elType": "widget", "widgetType": widget_type, "settings": settings or {}}


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


def flush_elementor_cache():
    """Clear Elementor's rendering cache so updated _elementor_data takes effect."""
    r = requests.delete(f"{WP_URL.replace('/wp/v2', '/elementor/v1')}/cache", auth=AUTH)
    if r.status_code == 200:
        print("  -> Elementor cache cleared")
    else:
        print(f"  -> WARNING: Elementor cache clear failed ({r.status_code})")


# ═══════════════════════════════════════
# REUSABLE COMPONENTS
# ═══════════════════════════════════════

def hero_section(title, subtitle, full_height=True, show_logo=False, show_bar=True, show_cta=False, cta_text="", cta_link="/"):
    """Premium hero with gradient overlay, grain texture, orbital rings, animations."""
    elems = []

    # Add orbital rings and grain overlay for full-height heroes (homepage)
    if full_height:
        elems.append(widget("html", {
            "html": ORBITAL_RINGS_HTML,
        }))

    if show_logo:
        elems.append(widget("image", {
            "image": {"url": LOGOS["vectanor"], "id": LOGO_IDS["vectanor"]},
            "image_size": "full",
            "width": {"size": 200, "unit": "px"},
            "align": "center",
            "_margin": {"top": "0", "bottom": "30", "left": "0", "right": "0", "unit": "px"},
            "custom_css": FADE_DOWN_CSS,
        }))
    elif title == "VECTANOR":
        # GROUPE eyebrow
        elems.append(widget("heading", {
            "title": "GROUPE",
            "header_size": "h6",
            "align": "center",
            "title_color": SLATE,
            "typography_typography": "custom",
            "typography_font_family": "Montserrat",
            "typography_font_size": {"size": 13, "unit": "px"},
            "typography_font_weight": "600",
            "typography_letter_spacing": {"size": 6, "unit": "px"},
            "_margin": {"top": "0", "bottom": "16", "left": "0", "right": "0", "unit": "px"},
            "custom_css": FADE_DOWN_CSS,
        }))

    # Main title
    title_settings = {
        "title": title,
        "header_size": "h1",
        "align": "center",
        "title_color": WHITE,
        "typography_typography": "custom",
        "typography_font_family": "Montserrat",
        "typography_font_size": {"size": 80 if title == "VECTANOR" else 56, "unit": "px"},
        "typography_font_weight": "800" if title == "VECTANOR" else "700",
        "typography_letter_spacing": {"size": 6 if title == "VECTANOR" else 2, "unit": "px"},
        "_margin": {"top": "0", "bottom": "24", "left": "0", "right": "0", "unit": "px"},
    }
    if title == "VECTANOR":
        title_settings["custom_css"] = HERO_TITLE_CSS
    else:
        title_settings["_animation"] = "fadeInUp"
        title_settings["_animation_duration"] = "slow"
    elems.append(widget("heading", title_settings))

    if show_bar:
        elems.append(widget("html", {
            "html": FOUR_COLOR_BAR_HTML,
            "_margin": {"top": "0", "bottom": "32", "left": "0", "right": "0", "unit": "px"},
        }))

    # Subtitle
    elems.append(widget("heading", {
        "title": subtitle,
        "header_size": "h3",
        "align": "center",
        "title_color": "#94A3B8",
        "typography_typography": "custom",
        "typography_font_family": "Sora",
        "typography_font_size": {"size": 21, "unit": "px"},
        "typography_font_weight": "400",
        "typography_line_height": {"size": 1.7, "unit": "em"},
        "_margin": {"top": "0", "bottom": "48" if show_cta else "0", "left": "0", "right": "0", "unit": "px"},
        "custom_css": TAGLINE_REVEAL_CSS,
    }))

    if show_cta:
        elems.append(widget("button", {
            "text": cta_text,
            "link": {"url": cta_link, "is_external": False},
            "align": "center",
            "button_type": "default",
            "background_color": ROYAL_BLUE,
            "button_text_color": WHITE,
            "border_radius": {"top": "6", "bottom": "6", "left": "6", "right": "6", "unit": "px"},
            "typography_typography": "custom",
            "typography_font_family": "Montserrat",
            "typography_font_size": {"size": 14, "unit": "px"},
            "typography_font_weight": "600",
            "typography_letter_spacing": {"size": 1, "unit": "px"},
            "button_padding": {"top": "18", "bottom": "18", "left": "44", "right": "44", "unit": "px"},
            "custom_css": CTA_BUTTON_CSS,
        }))

    hero_css = GRAIN_OVERLAY_CSS + HERO_GLOW_CSS if full_height else GRAIN_OVERLAY_CSS

    return container(
        settings={
            "content_width": "full",
            "min_height": {"size": 100 if full_height else 50, "unit": "vh"},
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
            "custom_css": hero_css,
            "padding": {"top": "120", "bottom": "120", "left": "40", "right": "40", "unit": "px"},
        },
        elements=elems,
    )


def section_heading(title, subtitle=None, dark=False):
    """Section heading with divider."""
    elems = [
        widget("heading", {
            "title": title,
            "header_size": "h2",
            "align": "center",
            "title_color": WHITE if dark else NEAR_BLACK,
            "typography_typography": "custom",
            "typography_font_family": "Montserrat",
            "typography_font_size": {"size": 42, "unit": "px"},
            "typography_font_weight": "700",
            "_margin": {"top": "0", "bottom": "15", "left": "0", "right": "0", "unit": "px"},
            "_animation": "fadeInUp",
            "_animation_duration": "slow",
        }),
        widget("divider", {
            "style": "custom",
            "color": ROYAL_BLUE,
            "weight": {"size": 3, "unit": "px"},
            "width": {"size": 80, "unit": "px"},
            "align": "center",
            "_margin": {"top": "0", "bottom": "30" if not subtitle else "15", "left": "0", "right": "0", "unit": "px"},
        }),
    ]
    if subtitle:
        elems.append(widget("text-editor", {
            "editor": f'<p style="text-align:center; font-size:18px; color:{"#94A3B8" if dark else "#64748B"}; max-width:600px; margin:0 auto;">{subtitle}</p>',
            "_margin": {"top": "0", "bottom": "50", "left": "0", "right": "0", "unit": "px"},
        }))
    return elems


def back_to_group_cta():
    """Footer CTA for division pages."""
    return container(
        settings={
            "content_width": "full",
            "background_background": "gradient",
            "background_color": NEAR_BLACK,
            "background_color_b": DARK_NAVY,
            "background_gradient_angle": {"size": 135, "unit": "deg"},
            "flex_direction": "column",
            "flex_justify_content": "center",
            "flex_align_items": "center",
            "padding": {"top": "60", "bottom": "60", "left": "40", "right": "40", "unit": "px"},
        },
        elements=[
            widget("image", {
                "image": {"url": LOGOS["vectanor"], "id": LOGO_IDS["vectanor"]},
                "image_size": "full",
                "width": {"size": 140, "unit": "px"},
                "align": "center",
                "_margin": {"top": "0", "bottom": "20", "left": "0", "right": "0", "unit": "px"},
                "custom_css": "selector img { filter: brightness(0) invert(1) opacity(0.6); }",
            }),
            widget("heading", {
                "title": "Une division du Groupe Vectanor",
                "header_size": "h5",
                "align": "center",
                "title_color": SLATE,
                "typography_typography": "custom",
                "typography_font_family": "Montserrat",
                "typography_font_size": {"size": 14, "unit": "px"},
                "typography_font_weight": "500",
                "typography_letter_spacing": {"size": 3, "unit": "px"},
                "_margin": {"top": "0", "bottom": "20", "left": "0", "right": "0", "unit": "px"},
            }),
            widget("button", {
                "text": "\u2190 Retour au groupe",
                "link": {"url": "/", "is_external": False},
                "align": "center",
                "background_color": "transparent",
                "button_text_color": WHITE,
                "border_border": "solid",
                "border_width": {"top": "1", "bottom": "1", "left": "1", "right": "1", "unit": "px"},
                "border_color": "#475569",
                "border_radius": {"top": "4", "bottom": "4", "left": "4", "right": "4", "unit": "px"},
                "typography_typography": "custom",
                "typography_font_family": "Montserrat",
                "typography_font_size": {"size": 13, "unit": "px"},
                "typography_font_weight": "500",
                "button_padding": {"top": "12", "bottom": "12", "left": "30", "right": "30", "unit": "px"},
            }),
        ],
    )


# ═══════════════════════════════════════
# HOMEPAGE
# ═══════════════════════════════════════

def build_homepage():
    elements = []

    # HERO
    elements.append(hero_section(
        "VECTANOR",
        "Trace la direction. Les divisions avancent. Les syst\u00e8mes suivent.",
        full_height=True, show_bar=True, show_cta=True,
        cta_text="D\u00e9couvrir nos divisions", cta_link="/divisions/",
    ))

    # VISION BRIEF — with grid pattern texture
    elements.append(container(
        settings={
            "content_width": "boxed",
            "background_background": "classic",
            "background_color": WHITE,
            "flex_direction": "column",
            "flex_align_items": "center",
            "padding": {"top": "90", "bottom": "90", "left": "40", "right": "40", "unit": "px"},
            "custom_css": GRID_PATTERN_CSS,
        },
        elements=[
            *section_heading("Orchestrer la complexit\u00e9"),
            widget("text-editor", {
                "editor": (
                    '<div style="text-align:center; max-width:800px; margin:0 auto; border-left:3px solid ' + ROYAL_BLUE + '; padding-left:24px;">'
                    '<p style="font-size:18px; line-height:1.9; color:#475569; font-family:Outfit,sans-serif; margin-bottom:20px;">'
                    'Les villes, les infrastructures et les environnements industriels sont devenus des '
                    'syst\u00e8mes complexes, souvent g\u00e9r\u00e9s en silos. <strong>Groupe Vectanor</strong> '
                    'agit comme une structure de pilotage capable d\u2019aligner des expertises sp\u00e9cialis\u00e9es '
                    'vers un objectif commun\u00a0: rendre les syst\u00e8mes urbains et industriels plus fiables, '
                    'plus efficients et plus durables.'
                    '</p>'
                    '<p style="font-size:17px; line-height:1.9; color:#64748B; font-family:Outfit,sans-serif;">'
                    'De l\u2019\u00e9clairage intelligent \u00e0 la mobilit\u00e9 urbaine, de la conception '
                    '\u00e9lectronique au monitoring d\u2019infrastructures critiques \u2014 nos divisions couvrent '
                    'l\u2019ensemble de la cha\u00eene de valeur technologique des villes et industries de demain.'
                    '</p>'
                    '</div>'
                ),
                "_animation": "fadeInUp",
                "_animation_delay": 200,
            }),
        ],
    ))

    # KEY FIGURES — glass stat cards
    def stat_block(number, label, delay=0):
        return inner_container(
            settings={
                "flex_direction": "column",
                "flex_align_items": "center",
                "background_background": "classic",
                "background_color": "rgba(255,255,255,0.03)",
                "border_border": "solid",
                "border_width": {"top": "1", "bottom": "1", "left": "1", "right": "1", "unit": "px"},
                "border_color": "rgba(255,255,255,0.06)",
                "border_radius": {"top": "12", "bottom": "12", "left": "12", "right": "12", "unit": "px"},
                "padding": {"top": "24", "bottom": "24", "left": "28", "right": "28", "unit": "px"},
                "_animation": "fadeInUp",
                "_animation_delay": delay,
            },
            elements=[
                widget("heading", {
                    "title": number,
                    "header_size": "h2",
                    "align": "center",
                    "title_color": WHITE,
                    "typography_typography": "custom",
                    "typography_font_family": "Montserrat",
                    "typography_font_size": {"size": 46, "unit": "px"},
                    "typography_font_weight": "800",
                    "_margin": {"top": "0", "bottom": "8", "left": "0", "right": "0", "unit": "px"},
                    "custom_css": f"""
selector .elementor-heading-title {{
    background: linear-gradient(135deg, {WHITE} 0%, {ROYAL_BLUE} 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}}
""",
                }),
                widget("text-editor", {
                    "editor": (
                        f'<p style="text-align:center;font-size:12px;color:#94A3B8;'
                        f'text-transform:uppercase;letter-spacing:2.5px;font-family:Montserrat,sans-serif;'
                        f'font-weight:600;">{label}</p>'
                    ),
                }),
            ],
        )

    stats = container(
        settings={
            "content_width": "boxed",
            "background_background": "gradient",
            "background_color": NEAR_BLACK,
            "background_color_b": DARK_NAVY,
            "background_gradient_angle": {"size": 90, "unit": "deg"},
            "flex_direction": "column",
            "flex_align_items": "center",
            "padding": {"top": "60", "bottom": "60", "left": "40", "right": "40", "unit": "px"},
        },
        elements=[
            inner_container(
                settings={
                    "flex_direction": "row",
                    "flex_wrap": "wrap",
                    "flex_justify_content": "center",
                    "flex_gap": {"size": 50, "unit": "px"},
                    "width": {"size": 100, "unit": "%"},
                    "max_width": {"size": 900, "unit": "px"},
                },
                elements=[
                    stat_block("4", "Divisions sp\u00e9cialis\u00e9es", 0),
                    stat_block("10+", "Ann\u00e9es d\u2019expertise", 100),
                    stat_block("IoT", "Grande \u00e9chelle", 200),
                    stat_block("360\u00b0", "Couverture technologique", 300),
                ],
            ),
            widget("html", {
                "html": FOUR_COLOR_BAR_HTML,
                "_margin": {"top": "25", "bottom": "0", "left": "0", "right": "0", "unit": "px"},
            }),
        ],
    )
    elements.append(stats)

    # DIVISIONS — Dark glassmorphism section
    def division_card(name, desc, color, link, logo_key, delay, external_url=None, highlights=None):
        card_elems = [
            widget("image", {
                "image": {"url": LOGOS[logo_key], "id": LOGO_IDS[logo_key]},
                "image_size": "full",
                "width": {"size": 140, "unit": "px"},
                "_margin": {"top": "0", "bottom": "15", "left": "0", "right": "0", "unit": "px"},
                "custom_css": "selector img { filter: brightness(0) invert(1); transition: filter 0.3s; }",
            }),
            widget("heading", {
                "title": name,
                "header_size": "h3",
                "title_color": WHITE,
                "typography_typography": "custom",
                "typography_font_family": "Montserrat",
                "typography_font_size": {"size": 24, "unit": "px"},
                "typography_font_weight": "700",
            }),
            widget("text-editor", {
                "editor": f'<p style="font-size:15px; line-height:1.75; color:#94A3B8;">{desc}</p>',
            }),
        ]
        if highlights:
            bullets_html = ''.join(
                f'<li style="font-size:13px;line-height:1.6;color:#CBD5E1;padding:4px 0;">'
                f'<span style="color:{color};margin-right:8px;">&#9656;</span>{h}</li>'
                for h in highlights
            )
            card_elems.append(widget("html", {
                "html": f'<ul style="list-style:none;padding:0;margin:8px 0 4px;">{bullets_html}</ul>',
            }))
        # Buttons row
        btn_elems = [
            widget("button", {
                "text": "En savoir plus",
                "link": {"url": link, "is_external": False},
                "button_type": "default",
                "background_color": "transparent",
                "button_text_color": color,
                "border_border": "solid",
                "border_width": {"top": "1", "bottom": "1", "left": "1", "right": "1", "unit": "px"},
                "border_color": color,
                "border_radius": {"top": "4", "bottom": "4", "left": "4", "right": "4", "unit": "px"},
                "typography_typography": "custom",
                "typography_font_family": "Montserrat",
                "typography_font_size": {"size": 12, "unit": "px"},
                "typography_font_weight": "600",
                "button_padding": {"top": "8", "bottom": "8", "left": "20", "right": "20", "unit": "px"},
                "custom_css": button_hover_css(color),
            }),
        ]
        if external_url:
            btn_elems.append(widget("button", {
                "text": f"Visiter {name.lower()}.com \u2197",
                "link": {"url": external_url, "is_external": True},
                "button_type": "default",
                "background_color": "transparent",
                "button_text_color": "#64748B",
                "border_border": "none",
                "typography_typography": "custom",
                "typography_font_family": "Outfit",
                "typography_font_size": {"size": 12, "unit": "px"},
                "typography_font_weight": "500",
                "button_padding": {"top": "8", "bottom": "8", "left": "10", "right": "10", "unit": "px"},
            }))

        card_elems.append(inner_container(
            settings={"flex_direction": "row", "flex_gap": {"size": 10, "unit": "px"}, "flex_wrap": "wrap"},
            elements=btn_elems,
        ))

        return inner_container(
            settings={
                "background_background": "classic",
                "background_color": "rgba(255,255,255,0.06)",
                "border_border": "solid",
                "border_width": {"top": "1", "bottom": "1", "left": "1", "right": "1", "unit": "px", "isLinked": True},
                "border_color": "rgba(255,255,255,0.10)",
                "border_radius": {"top": "16", "bottom": "16", "left": "16", "right": "16", "unit": "px"},
                "padding": {"top": "45", "bottom": "45", "left": "35", "right": "35", "unit": "px"},
                "flex_direction": "column",
                "flex_align_items": "flex-start",
                "flex_gap": {"size": 14, "unit": "px"},
                "_animation": "fadeInUp",
                "_animation_delay": delay,
                "_animation_duration": "slow",
                "custom_css": card_glow_css(color),
            },
            elements=card_elems,
        )

    divisions_section = container(
        settings={
            "content_width": "boxed",
            "background_background": "gradient",
            "background_color": NEAR_BLACK,
            "background_color_b": DARK_NAVY,
            "background_gradient_angle": {"size": 145, "unit": "deg"},
            "flex_direction": "column",
            "flex_align_items": "center",
            "padding": {"top": "100", "bottom": "100", "left": "40", "right": "40", "unit": "px"},
            "custom_css": GRAIN_OVERLAY_CSS,
        },
        elements=[
            *section_heading(
                "Nos divisions",
                "Chaque entit\u00e9 du groupe est autonome dans son march\u00e9, mais int\u00e9gr\u00e9e dans une architecture globale.",
                dark=True,
            ),
            inner_container(
                settings={
                    "flex_direction": "row",
                    "flex_wrap": "wrap",
                    "flex_gap": {"size": 25, "unit": "px"},
                    "flex_justify_content": "center",
                    "width": {"size": 100, "unit": "%"},
                },
                elements=[
                    division_card(
                        "Dimonoff",
                        "\u00c9clairage intelligent et infrastructures urbaines connect\u00e9es.",
                        AMBER, "/divisions/dimonoff/", "dimonoff", 0,
                        external_url="https://dimonoff.com",
                        highlights=[
                            "T\u00e9l\u00e9gestion municipale \u00e0 grande \u00e9chelle",
                            "R\u00e9duction \u00e9nerg\u00e9tique mesurable",
                            "Plateforme SaaS multi-sites",
                        ],
                    ),
                    division_card(
                        "Spatium",
                        "Mobilit\u00e9 et stationnement intelligent.",
                        GREEN, "/divisions/spatium/", "spatium", 100,
                        external_url="https://dimonoff.com",
                        highlights=[
                            "D\u00e9tection et guidage en temps r\u00e9el",
                            "Capteurs IoT basse consommation",
                            "Analytique de flux de mobilit\u00e9",
                        ],
                    ),
                    division_card(
                        "Amotus",
                        "Design House et catalyseur d\u2019innovation industrielle.",
                        PURPLE, "/divisions/amotus/", "amotus", 200,
                        external_url="https://amotus.com",
                        highlights=[
                            "Conception \u00e9lectronique sur mesure",
                            "Du prototype \u00e0 la certification",
                            "Syst\u00e8mes embarqu\u00e9s industriels",
                        ],
                    ),
                    division_card(
                        "Vigilia",
                        "Surveillance et monitoring d\u2019infrastructures critiques.",
                        PINK, "/divisions/vigilia/", "vigilia", 300,
                        highlights=[
                            "Monitoring 24/7 d\u2019infrastructures",
                            "Alertes pr\u00e9dictives par IA",
                            "Communication MQTT s\u00e9curis\u00e9e",
                        ],
                    ),
                ],
            ),
        ],
    )
    elements.append(divisions_section)

    # APPROACH — Premium cards with left accent + top accent
    def value_card(icon, title, desc, accent_color, delay=0):
        return inner_container(
            settings={
                "background_background": "classic",
                "background_color": WHITE,
                "border_border": "solid",
                "border_width": {"top": "3", "bottom": "0", "left": "3", "right": "0", "unit": "px", "isLinked": False},
                "border_color": accent_color,
                "border_radius": {"top": "12", "bottom": "12", "left": "12", "right": "12", "unit": "px"},
                "box_shadow_box_shadow_type": "yes",
                "box_shadow_box_shadow": {"horizontal": 0, "vertical": 4, "blur": 30, "spread": 0, "color": "rgba(0,0,0,0.06)"},
                "padding": {"top": "40", "bottom": "40", "left": "30", "right": "30", "unit": "px"},
                "flex_direction": "column",
                "flex_align_items": "center",
                "flex_gap": {"size": 8, "unit": "px"},
                "_animation": "fadeInUp",
                "_animation_delay": delay,
                "_animation_duration": "slow",
                "custom_css": f"""
selector {{
    transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}}
selector:hover {{
    transform: translateY(-8px);
    box-shadow: 0 20px 60px -15px {accent_color}30, 0 8px 25px rgba(0,0,0,0.08);
}}
""",
            },
            elements=[
                widget("html", {
                    "html": (
                        f'<div style="width:68px;height:68px;border-radius:50%;'
                        f'background:linear-gradient(135deg,{accent_color}18,{accent_color}08);'
                        f'display:flex;align-items:center;justify-content:center;margin:0 auto;">'
                        f'<i class="{icon}" style="font-size:26px;color:{accent_color};"></i></div>'
                    ),
                }),
                widget("heading", {
                    "title": title,
                    "header_size": "h4",
                    "align": "center",
                    "title_color": NEAR_BLACK,
                    "typography_typography": "custom",
                    "typography_font_family": "Montserrat",
                    "typography_font_size": {"size": 22, "unit": "px"},
                    "typography_font_weight": "700",
                    "_margin": {"top": "8", "bottom": "5", "left": "0", "right": "0", "unit": "px"},
                }),
                widget("divider", {
                    "style": "custom",
                    "color": accent_color,
                    "weight": {"size": 2, "unit": "px"},
                    "width": {"size": 40, "unit": "px"},
                    "align": "center",
                    "_margin": {"top": "0", "bottom": "5", "left": "0", "right": "0", "unit": "px"},
                }),
                widget("text-editor", {
                    "editor": f'<p style="text-align:center; font-size:15px; line-height:1.8; color:#64748B;">{desc}</p>',
                }),
            ],
        )

    approach = container(
        settings={
            "content_width": "boxed",
            "background_background": "classic",
            "background_color": LIGHT_GREY,
            "flex_direction": "column",
            "flex_align_items": "center",
            "padding": {"top": "90", "bottom": "90", "left": "40", "right": "40", "unit": "px"},
            "custom_css": GRID_PATTERN_CSS,
        },
        elements=[
            *section_heading("Notre approche"),
            widget("text-editor", {
                "editor": (
                    '<p style="text-align:center; max-width:700px; margin:0 auto 50px; font-size:17px; '
                    'line-height:1.8; color:#64748B;">'
                    'Nous croyons que la technologie doit servir une vision claire. Chaque solution d\u00e9ploy\u00e9e '
                    'par le groupe repose sur trois piliers fondamentaux qui guident nos d\u00e9cisions techniques '
                    'et strat\u00e9giques.'
                    '</p>'
                ),
                "_animation": "fadeInUp",
            }),
            inner_container(
                settings={
                    "flex_direction": "row",
                    "flex_wrap": "wrap",
                    "flex_gap": {"size": 30, "unit": "px"},
                    "flex_justify_content": "center",
                    "width": {"size": 100, "unit": "%"},
                    "max_width": {"size": 1100, "unit": "px"},
                },
                elements=[
                    value_card(
                        "fas fa-project-diagram",
                        "Interop\u00e9rabilit\u00e9",
                        "Des syst\u00e8mes con\u00e7us pour communiquer entre eux, sans d\u00e9pendance \u00e0 un "
                        "fournisseur unique. Nous privil\u00e9gions les standards ouverts et les protocoles "
                        "reconnus pour garantir la p\u00e9rennit\u00e9 des investissements et la libert\u00e9 "
                        "de choix de nos clients.",
                        ROYAL_BLUE,
                        0,
                    ),
                    value_card(
                        "fas fa-shield-alt",
                        "Confiance",
                        "Des infrastructures fiables, s\u00e9curis\u00e9es et construites pour durer. Chaque composant "
                        "est test\u00e9, certifi\u00e9 et d\u00e9ploy\u00e9 selon des processus rigoureux. "
                        "La robustesse n\u2019est pas une option\u00a0: c\u2019est notre standard de r\u00e9f\u00e9rence.",
                        "#10B981",
                        100,
                    ),
                    value_card(
                        "fas fa-expand-arrows-alt",
                        "\u00c9volutivit\u00e9",
                        "Une architecture modulaire capable d\u2019\u00e9voluer sans rupture et de s\u2019adapter "
                        "aux besoins futurs. Nos solutions sont pens\u00e9es pour grandir avec les projets de "
                        "nos clients, de quelques points connect\u00e9s \u00e0 des d\u00e9ploiements \u00e0 "
                        "l\u2019\u00e9chelle d\u2019une ville.",
                        PURPLE,
                        200,
                    ),
                ],
            ),
        ],
    )
    elements.append(approach)

    # CTA SECTION — grain overlay
    cta = container(
        settings={
            "content_width": "full",
            "min_height": {"size": 380, "unit": "px"},
            "background_background": "gradient",
            "background_color": NEAR_BLACK,
            "background_color_b": NAVY,
            "background_gradient_angle": {"size": 135, "unit": "deg"},
            "background_overlay_background": "gradient",
            "background_overlay_color": "rgba(59,130,246,0.10)",
            "background_overlay_color_b": "rgba(139,92,246,0.06)",
            "background_overlay_gradient_type": "radial",
            "background_overlay_gradient_position": "center center",
            "flex_direction": "column",
            "flex_justify_content": "center",
            "flex_align_items": "center",
            "padding": {"top": "90", "bottom": "90", "left": "40", "right": "40", "unit": "px"},
            "custom_css": GRAIN_OVERLAY_CSS,
        },
        elements=[
            widget("heading", {
                "title": "GROUPE",
                "header_size": "h6",
                "align": "center",
                "title_color": SLATE,
                "typography_typography": "custom",
                "typography_font_family": "Montserrat",
                "typography_font_size": {"size": 12, "unit": "px"},
                "typography_font_weight": "600",
                "typography_letter_spacing": {"size": 5, "unit": "px"},
                "_margin": {"top": "0", "bottom": "12", "left": "0", "right": "0", "unit": "px"},
                "_animation": "fadeInUp",
            }),
            widget("heading", {
                "title": "Pr\u00eat \u00e0 structurer l\u2019avenir\u00a0?",
                "header_size": "h2",
                "align": "center",
                "title_color": WHITE,
                "typography_typography": "custom",
                "typography_font_family": "Montserrat",
                "typography_font_size": {"size": 40, "unit": "px"},
                "typography_font_weight": "700",
                "_margin": {"top": "0", "bottom": "20", "left": "0", "right": "0", "unit": "px"},
                "_animation": "fadeInUp",
            }),
            widget("text-editor", {
                "editor": (
                    '<p style="text-align:center; font-size:18px; color:#94A3B8; max-width:600px; margin:0 auto; font-family:Outfit,sans-serif;">'
                    'Contactez-nous pour d\u00e9couvrir comment Groupe Vectanor peut accompagner vos projets '
                    'd\u2019infrastructure et de transformation technologique.'
                    '</p>'
                ),
                "_animation": "fadeInUp",
                "_animation_delay": 100,
            }),
            widget("html", {
                "html": FOUR_COLOR_BAR_HTML,
                "_margin": {"top": "30", "bottom": "30", "left": "0", "right": "0", "unit": "px"},
            }),
            widget("button", {
                "text": "Nous contacter",
                "link": {"url": "/contact/", "is_external": False},
                "align": "center",
                "background_color": ROYAL_BLUE,
                "button_text_color": WHITE,
                "border_radius": {"top": "6", "bottom": "6", "left": "6", "right": "6", "unit": "px"},
                "typography_typography": "custom",
                "typography_font_family": "Montserrat",
                "typography_font_size": {"size": 14, "unit": "px"},
                "typography_font_weight": "600",
                "button_padding": {"top": "18", "bottom": "18", "left": "44", "right": "44", "unit": "px"},
                "custom_css": CTA_BUTTON_CSS,
            }),
        ],
    )
    elements.append(cta)

    return elements


# ═══════════════════════════════════════
# DIVISION PAGE BUILDER
# ═══════════════════════════════════════

def build_division_page(name, accent, tagline, description, features, logo_key, external_url=None):
    elements = []

    # HERO with division logo
    hero_elems = [
        widget("image", {
            "image": {"url": LOGOS[logo_key], "id": LOGO_IDS[logo_key]},
            "image_size": "full",
            "width": {"size": 180, "unit": "px"},
            "align": "center",
            "_margin": {"top": "0", "bottom": "25", "left": "0", "right": "0", "unit": "px"},
            "custom_css": "selector img { filter: brightness(0) invert(1); }",
            "_animation": "fadeInDown",
            "_animation_duration": "slow",
        }),
        widget("divider", {
            "style": "custom", "color": accent,
            "weight": {"size": 4, "unit": "px"}, "width": {"size": 60, "unit": "px"},
            "align": "center",
            "_margin": {"top": "0", "bottom": "20", "left": "0", "right": "0", "unit": "px"},
        }),
        widget("heading", {
            "title": tagline,
            "header_size": "h2",
            "align": "center",
            "title_color": "#CBD5E1",
            "typography_typography": "custom",
            "typography_font_family": "Sora",
            "typography_font_size": {"size": 22, "unit": "px"},
            "typography_font_weight": "400",
            "typography_line_height": {"size": 1.6, "unit": "em"},
            "_animation": "fadeInUp",
            "_animation_duration": "slow",
        }),
    ]
    if external_url:
        hero_elems.append(widget("button", {
            "text": f"Visiter {external_url.replace('https://','')} \u2197",
            "link": {"url": external_url, "is_external": True},
            "align": "center",
            "background_color": "transparent",
            "button_text_color": accent,
            "border_border": "solid",
            "border_width": {"top": "1", "bottom": "1", "left": "1", "right": "1", "unit": "px"},
            "border_color": accent,
            "border_radius": {"top": "4", "bottom": "4", "left": "4", "right": "4", "unit": "px"},
            "typography_typography": "custom",
            "typography_font_family": "Montserrat",
            "typography_font_size": {"size": 13, "unit": "px"},
            "typography_font_weight": "600",
            "button_padding": {"top": "10", "bottom": "10", "left": "24", "right": "24", "unit": "px"},
            "_margin": {"top": "25", "bottom": "0", "left": "0", "right": "0", "unit": "px"},
            "custom_css": button_hover_css(accent),
        }))

    elements.append(container(
        settings={
            "content_width": "full",
            "min_height": {"size": 55, "unit": "vh"},
            "background_background": "gradient",
            "background_color": NEAR_BLACK,
            "background_color_b": DARK_NAVY,
            "background_gradient_angle": {"size": 145, "unit": "deg"},
            "background_overlay_background": "gradient",
            "background_overlay_color": f"{accent}12",
            "background_overlay_color_b": "rgba(0,0,0,0)",
            "background_overlay_gradient_type": "radial",
            "background_overlay_gradient_position": "top center",
            "flex_direction": "column",
            "flex_justify_content": "center",
            "flex_align_items": "center",
            "padding": {"top": "80", "bottom": "80", "left": "40", "right": "40", "unit": "px"},
        },
        elements=hero_elems,
    ))

    # ABOUT — grid pattern
    elements.append(container(
        settings={
            "content_width": "boxed",
            "background_background": "classic",
            "background_color": WHITE,
            "flex_direction": "column",
            "flex_align_items": "center",
            "padding": {"top": "80", "bottom": "80", "left": "40", "right": "40", "unit": "px"},
            "custom_css": GRID_PATTERN_CSS,
        },
        elements=[
            *section_heading(f"\u00c0 propos de {name}"),
            widget("text-editor", {
                "editor": f'<p style="text-align:center; max-width:800px; margin:0 auto; font-size:18px; line-height:1.9; color:#475569; font-family:Outfit,sans-serif;">{description}</p>',
                "_animation": "fadeInUp",
            }),
        ],
    ))

    # FEATURES — glassmorphism on dark
    feat_cards = []
    for i, feat in enumerate(features):
        feat_cards.append(inner_container(
            settings={
                "background_background": "classic",
                "background_color": "rgba(255,255,255,0.04)",
                "border_border": "solid",
                "border_width": {"top": "1", "bottom": "1", "left": "1", "right": "1", "unit": "px"},
                "border_color": "rgba(255,255,255,0.08)",
                "border_radius": {"top": "12", "bottom": "12", "left": "12", "right": "12", "unit": "px"},
                "padding": {"top": "30", "bottom": "30", "left": "25", "right": "25", "unit": "px"},
                "flex_direction": "column",
                "flex_align_items": "flex-start",
                "flex_gap": {"size": 10, "unit": "px"},
                "_animation": "fadeInUp",
                "_animation_delay": i * 100,
                "_animation_duration": "slow",
                "custom_css": card_glow_css(accent),
            },
            elements=[
                widget("icon", {
                    "selected_icon": {"value": feat["icon"], "library": "fa-solid"},
                    "primary_color": accent,
                    "icon_size": {"size": 28, "unit": "px"},
                }),
                widget("heading", {
                    "title": feat["title"],
                    "header_size": "h4",
                    "title_color": WHITE,
                    "typography_typography": "custom",
                    "typography_font_family": "Montserrat",
                    "typography_font_size": {"size": 18, "unit": "px"},
                    "typography_font_weight": "600",
                }),
                widget("text-editor", {
                    "editor": f'<p style="font-size:15px; line-height:1.7; color:#94A3B8;">{feat["desc"]}</p>',
                }),
            ],
        ))

    elements.append(container(
        settings={
            "content_width": "boxed",
            "background_background": "gradient",
            "background_color": NEAR_BLACK,
            "background_color_b": DARK_NAVY,
            "background_gradient_angle": {"size": 145, "unit": "deg"},
            "flex_direction": "column",
            "flex_align_items": "center",
            "padding": {"top": "80", "bottom": "80", "left": "40", "right": "40", "unit": "px"},
            "custom_css": GRAIN_OVERLAY_CSS,
        },
        elements=[
            *section_heading("Domaines d\u2019expertise", dark=True),
            inner_container(
                settings={
                    "flex_direction": "row",
                    "flex_wrap": "wrap",
                    "flex_gap": {"size": 25, "unit": "px"},
                    "flex_justify_content": "center",
                    "width": {"size": 100, "unit": "%"},
                },
                elements=feat_cards,
            ),
        ],
    ))

    # Back to group
    elements.append(back_to_group_cta())
    return elements


# ═══════════════════════════════════════
# DIVISION DATA
# ═══════════════════════════════════════

DIVISIONS = {
    "dimonoff": {
        "name": "Dimonoff",
        "accent": AMBER,
        "tagline": "\u00c9clairage intelligent et infrastructures urbaines connect\u00e9es",
        "description": (
            "Dimonoff est la r\u00e9f\u00e9rence en gestion d\u2019\u00e9clairage intelligent et d\u2019infrastructures "
            "urbaines connect\u00e9es. Depuis plus d\u2019une d\u00e9cennie, Dimonoff d\u00e9ploie des solutions de "
            "t\u00e9l\u00e9gestion \u00e0 grande \u00e9chelle pour les municipalit\u00e9s et les exploitants "
            "d\u2019infrastructures, permettant un contr\u00f4le pr\u00e9cis, une r\u00e9duction de la consommation "
            "\u00e9nerg\u00e9tique et une maintenance pr\u00e9dictive de milliers de points lumineux."
        ),
        "features": [
            {"icon": "fas fa-lightbulb", "title": "T\u00e9l\u00e9gestion d\u2019\u00e9clairage", "desc": "Contr\u00f4le intelligent de r\u00e9seaux d\u2019\u00e9clairage municipal \u00e0 grande \u00e9chelle avec surveillance en temps r\u00e9el."},
            {"icon": "fas fa-city", "title": "Ville intelligente", "desc": "Plateformes int\u00e9gr\u00e9es pour la gestion d\u2019actifs urbains connect\u00e9s et l\u2019optimisation des op\u00e9rations municipales."},
            {"icon": "fas fa-bolt", "title": "Efficacit\u00e9 \u00e9nerg\u00e9tique", "desc": "R\u00e9duction mesurable de la consommation \u00e9nerg\u00e9tique gr\u00e2ce \u00e0 des algorithmes de gradation adapt\u00e9s au contexte."},
            {"icon": "fas fa-tools", "title": "Maintenance pr\u00e9dictive", "desc": "D\u00e9tection proactive des pannes et planification optimis\u00e9e des interventions terrain."},
        ],
        "logo_key": "dimonoff",
        "external_url": "https://dimonoff.com",
    },
    "spatium": {
        "name": "Spatium",
        "accent": GREEN,
        "tagline": "Mobilit\u00e9 et stationnement intelligent",
        "description": (
            "Spatium adresse les d\u00e9fis de mobilit\u00e9 urbaine avec des solutions int\u00e9gr\u00e9es de "
            "stationnement intelligent et de gestion dynamique des flux. En combinant capteurs IoT, analytique "
            "avanc\u00e9e et int\u00e9gration multi-plateformes, Spatium permet aux villes et aux op\u00e9rateurs "
            "de transformer le stationnement d\u2019un irritant urbain en un levier de mobilit\u00e9 durable."
        ),
        "features": [
            {"icon": "fas fa-parking", "title": "Stationnement intelligent", "desc": "D\u00e9tection en temps r\u00e9el de la disponibilit\u00e9, guidage dynamique et optimisation du taux d\u2019occupation."},
            {"icon": "fas fa-route", "title": "Gestion de la mobilit\u00e9", "desc": "Analyse des flux de circulation et outils d\u2019aide \u00e0 la d\u00e9cision pour les planificateurs urbains."},
            {"icon": "fas fa-wifi", "title": "IoT & Capteurs", "desc": "R\u00e9seaux de capteurs connect\u00e9s pour une vision compl\u00e8te et en temps r\u00e9el de l\u2019espace urbain."},
            {"icon": "fas fa-chart-line", "title": "Analytique & Donn\u00e9es", "desc": "Tableaux de bord et rapports pour mesurer la performance et guider les investissements en mobilit\u00e9."},
        ],
        "logo_key": "spatium",
        "external_url": "https://dimonoff.com",
    },
    "amotus": {
        "name": "Amotus",
        "accent": PURPLE,
        "tagline": "Design House et catalyseur d\u2019innovation industrielle",
        "description": (
            "Amotus agit comme Design House au sein du Groupe Vectanor, con\u00e7evant des solutions technologiques "
            "sur mesure pour des environnements industriels exigeants. De la conception \u00e9lectronique \u00e0 "
            "l\u2019int\u00e9gration de syst\u00e8mes, Amotus transforme les d\u00e9fis techniques complexes en "
            "produits fiables, certifi\u00e9s et pr\u00eats pour la production."
        ),
        "features": [
            {"icon": "fas fa-microchip", "title": "Conception \u00e9lectronique", "desc": "Design de cartes \u00e9lectroniques, firmware et syst\u00e8mes embarqu\u00e9s pour applications industrielles critiques."},
            {"icon": "fas fa-cogs", "title": "Int\u00e9gration de syst\u00e8mes", "desc": "Assemblage et int\u00e9gration de sous-syst\u00e8mes complexes en solutions industrielles cl\u00e9s en main."},
            {"icon": "fas fa-flask", "title": "R&D et prototypage", "desc": "Du concept au prototype fonctionnel, acc\u00e9l\u00e9ration du cycle d\u2019innovation avec une approche pragmatique."},
            {"icon": "fas fa-certificate", "title": "Certification & Qualit\u00e9", "desc": "Accompagnement vers les certifications industrielles (CE, UL, CSA) et gestion de la qualit\u00e9 de production."},
        ],
        "logo_key": "amotus",
        "external_url": "https://amotus.com",
    },
    "vigilia": {
        "name": "Vigilia",
        "accent": PINK,
        "tagline": "Surveillance et monitoring d\u2019infrastructures critiques",
        "description": (
            "Vigilia est la division du Groupe Vectanor d\u00e9di\u00e9e \u00e0 la surveillance et au monitoring "
            "d\u2019infrastructures critiques. Gr\u00e2ce \u00e0 des capteurs intelligents, des syst\u00e8mes de "
            "communication MQTT et une plateforme d\u2019analyse en temps r\u00e9el, Vigilia permet aux op\u00e9rateurs "
            "de d\u00e9tecter les anomalies, d\u2019anticiper les d\u00e9faillances et d\u2019assurer la continuit\u00e9 "
            "op\u00e9rationnelle de leurs installations les plus sensibles."
        ),
        "features": [
            {"icon": "fas fa-eye", "title": "Monitoring temps r\u00e9el", "desc": "Surveillance continue des param\u00e8tres critiques avec alertes instantan\u00e9es et tableaux de bord op\u00e9rationnels."},
            {"icon": "fas fa-broadcast-tower", "title": "IoT & Communication", "desc": "R\u00e9seaux de capteurs connect\u00e9s via MQTT pour une collecte de donn\u00e9es fiable et \u00e0 faible latence."},
            {"icon": "fas fa-brain", "title": "Analyse pr\u00e9dictive", "desc": "Algorithmes d\u2019intelligence artificielle pour anticiper les d\u00e9faillances avant qu\u2019elles ne surviennent."},
            {"icon": "fas fa-database", "title": "Historisation & Rapports", "desc": "Stockage longue dur\u00e9e des donn\u00e9es de performance et g\u00e9n\u00e9ration de rapports de conformit\u00e9 automatis\u00e9s."},
        ],
        "logo_key": "vigilia",
        "external_url": None,
    },
}


# ═══════════════════════════════════════
# VISION PAGE
# ═══════════════════════════════════════

def build_vision_page():
    elements = []

    elements.append(hero_section(
        "Notre vision",
        "Donner une trajectoire aux syst\u00e8mes complexes",
        full_height=False, show_bar=False,
    ))

    # Story + Philosophy combined for tighter layout
    elements.append(container(
        settings={
            "content_width": "boxed",
            "background_background": "classic",
            "background_color": WHITE,
            "flex_direction": "column",
            "flex_align_items": "center",
            "padding": {"top": "60", "bottom": "40", "left": "40", "right": "40", "unit": "px"},
            "custom_css": GRID_PATTERN_CSS,
        },
        elements=[
            *section_heading("L\u2019histoire de Groupe Vectanor"),
            widget("text-editor", {
                "editor": (
                    '<div style="max-width:800px; margin:0 auto; font-size:17px; line-height:1.9; color:#475569; font-family:Outfit,sans-serif;">'
                    '<p>Groupe Vectanor est n\u00e9 d\u2019un constat simple\u00a0: les villes, les infrastructures et les '
                    'environnements industriels sont devenus des syst\u00e8mes complexes, fragment\u00e9s, souvent g\u00e9r\u00e9s '
                    'en silos. Pourtant, leur performance repose sur une chose fondamentale\u00a0: la capacit\u00e9 \u00e0 '
                    'orchestrer des flux \u2014 \u00e9nergie, donn\u00e9es, mobilit\u00e9, s\u00e9curit\u00e9, '
                    'op\u00e9rations \u2014 de mani\u00e8re coh\u00e9rente et intelligente.</p>'
                    '<p>Le nom <strong>Vectanor</strong> provient de la notion de <em>vecteur</em>\u00a0: une direction, '
                    'une force, un mouvement ma\u00eetris\u00e9. Il incarne l\u2019id\u00e9e qu\u2019un groupe '
                    'technologique ne doit pas seulement fournir des outils, mais donner une trajectoire.</p>'
                    '</div>'
                ),
                "_animation": "fadeInUp",
            }),
        ],
    ))

    # Philosophy on dark — grain overlay
    elements.append(container(
        settings={
            "content_width": "boxed",
            "background_background": "gradient",
            "background_color": NEAR_BLACK,
            "background_color_b": DARK_NAVY,
            "background_gradient_angle": {"size": 145, "unit": "deg"},
            "flex_direction": "column",
            "flex_align_items": "center",
            "padding": {"top": "50", "bottom": "50", "left": "40", "right": "40", "unit": "px"},
            "custom_css": GRAIN_OVERLAY_CSS,
        },
        elements=[
            *section_heading("Notre philosophie", dark=True),
            widget("text-editor", {
                "editor": (
                    '<div style="max-width:800px; margin:0 auto; font-size:17px; line-height:1.9; color:#94A3B8; font-family:Outfit,sans-serif;">'
                    '<p>Groupe Vectanor agit comme une maison-m\u00e8re strat\u00e9gique, con\u00e7ue pour permettre \u00e0 '
                    'chaque division de se concentrer sur son domaine d\u2019excellence tout en b\u00e9n\u00e9ficiant '
                    'd\u2019une vision partag\u00e9e, d\u2019une gouvernance technologique solide et d\u2019une capacit\u00e9 '
                    'd\u2019ex\u00e9cution commune.</p>'
                    '<p>Le groupe privil\u00e9gie une approche pragmatique\u00a0: des technologies \u00e9prouv\u00e9es, '
                    'une int\u00e9gration ma\u00eetris\u00e9e, et une compr\u00e9hension fine des contraintes '
                    'op\u00e9rationnelles sur le terrain.</p>'
                    '</div>'
                ),
                "_animation": "fadeInUp",
            }),
        ],
    ))

    # Quote — compact, no tagline repeat (it's already in the hero)
    elements.append(container(
        settings={
            "content_width": "boxed",
            "background_background": "classic",
            "background_color": WHITE,
            "flex_direction": "column",
            "flex_align_items": "center",
            "padding": {"top": "50", "bottom": "50", "left": "40", "right": "40", "unit": "px"},
        },
        elements=[
            widget("text-editor", {
                "editor": (
                    '<blockquote style="max-width:700px; margin:0 auto; text-align:center; border:none; '
                    f'font-size:22px; line-height:1.8; color:{NEAR_BLACK}; font-style:italic;">'
                    '<p>\u00ab\u00a0Les syst\u00e8mes qui structurent nos villes et nos industries doivent \u00eatre '
                    'con\u00e7us comme des infrastructures de confiance, capables d\u2019\u00e9voluer sans rupture '
                    'et sans d\u00e9pendance inutile.\u00a0\u00bb</p>'
                    '</blockquote>'
                ),
                "_animation": "fadeIn",
                "_animation_duration": "slow",
            }),
            widget("html", {
                "html": FOUR_COLOR_BAR_HTML,
                "_margin": {"top": "20", "bottom": "0", "left": "0", "right": "0", "unit": "px"},
            }),
        ],
    ))

    return elements


# ═══════════════════════════════════════
# DIVISIONS INDEX PAGE
# ═══════════════════════════════════════

def build_divisions_index():
    elements = []

    elements.append(hero_section(
        "Nos divisions",
        "Un \u00e9cosyst\u00e8me d\u2019expertises align\u00e9es",
        full_height=False, show_bar=True,
    ))

    # Large cards
    def large_card(div_key, delay=0):
        d = DIVISIONS[div_key]
        card_elems = [
            widget("image", {
                "image": {"url": LOGOS[d["logo_key"]], "id": LOGO_IDS[d["logo_key"]]},
                "image_size": "full",
                "width": {"size": 160, "unit": "px"},
                "_margin": {"top": "0", "bottom": "15", "left": "0", "right": "0", "unit": "px"},
            }),
            widget("heading", {
                "title": d["tagline"].upper(),
                "header_size": "h5",
                "title_color": d["accent"],
                "typography_typography": "custom",
                "typography_font_family": "Montserrat",
                "typography_font_size": {"size": 12, "unit": "px"},
                "typography_font_weight": "600",
                "typography_letter_spacing": {"size": 2, "unit": "px"},
                "_margin": {"top": "0", "bottom": "15", "left": "0", "right": "0", "unit": "px"},
            }),
            widget("text-editor", {
                "editor": f'<p style="font-size:16px; line-height:1.8; color:#475569;">{d["description"][:200]}...</p>',
            }),
        ]
        # Buttons
        btn_elems = [
            widget("button", {
                "text": f"D\u00e9couvrir {d['name']} \u2192",
                "link": {"url": f"/divisions/{div_key}/", "is_external": False},
                "button_type": "default",
                "background_color": d["accent"],
                "button_text_color": WHITE,
                "border_radius": {"top": "4", "bottom": "4", "left": "4", "right": "4", "unit": "px"},
                "typography_typography": "custom",
                "typography_font_family": "Montserrat",
                "typography_font_size": {"size": 13, "unit": "px"},
                "typography_font_weight": "600",
                "button_padding": {"top": "12", "bottom": "12", "left": "24", "right": "24", "unit": "px"},
            }),
        ]
        if d.get("external_url"):
            btn_elems.append(widget("button", {
                "text": f"Visiter le site \u2197",
                "link": {"url": d["external_url"], "is_external": True},
                "background_color": "transparent",
                "button_text_color": "#64748B",
                "border_border": "solid",
                "border_width": {"top": "1", "bottom": "1", "left": "1", "right": "1", "unit": "px"},
                "border_color": "#CBD5E1",
                "border_radius": {"top": "4", "bottom": "4", "left": "4", "right": "4", "unit": "px"},
                "typography_typography": "custom",
                "typography_font_family": "Outfit",
                "typography_font_size": {"size": 13, "unit": "px"},
                "typography_font_weight": "500",
                "button_padding": {"top": "12", "bottom": "12", "left": "24", "right": "24", "unit": "px"},
            }))

        card_elems.append(inner_container(
            settings={"flex_direction": "row", "flex_gap": {"size": 12, "unit": "px"}, "flex_wrap": "wrap"},
            elements=btn_elems,
        ))

        return inner_container(
            settings={
                "background_background": "classic",
                "background_color": WHITE,
                "border_border": "solid",
                "border_width": {"top": "0", "bottom": "0", "left": "4", "right": "0", "unit": "px", "isLinked": False},
                "border_color": d["accent"],
                "box_shadow_box_shadow_type": "yes",
                "box_shadow_box_shadow": {"horizontal": 0, "vertical": 4, "blur": 25, "spread": 0, "color": "rgba(0,0,0,0.08)"},
                "border_radius": {"top": "8", "bottom": "8", "left": "8", "right": "8", "unit": "px"},
                "padding": {"top": "40", "bottom": "40", "left": "35", "right": "35", "unit": "px"},
                "flex_direction": "column",
                "flex_align_items": "flex-start",
                "flex_gap": {"size": 8, "unit": "px"},
                "_animation": "fadeInUp",
                "_animation_delay": delay,
                "_animation_duration": "slow",
                "custom_css": card_light_glow_css(d["accent"]),
            },
            elements=card_elems,
        )

    elements.append(container(
        settings={
            "content_width": "boxed",
            "background_background": "classic",
            "background_color": LIGHT_GREY,
            "flex_direction": "column",
            "flex_align_items": "center",
            "padding": {"top": "80", "bottom": "80", "left": "40", "right": "40", "unit": "px"},
            "custom_css": GRID_PATTERN_CSS,
        },
        elements=[
            inner_container(
                settings={
                    "flex_direction": "column",
                    "flex_gap": {"size": 35, "unit": "px"},
                    "width": {"size": 100, "unit": "%"},
                    "max_width": {"size": 800, "unit": "px"},
                },
                elements=[large_card(k, i * 100) for i, k in enumerate(["dimonoff", "spatium", "amotus", "vigilia"])],
            ),
        ],
    ))

    return elements


# ═══════════════════════════════════════
# CONTACT PAGE
# ═══════════════════════════════════════

def build_contact_page():
    elements = []

    elements.append(hero_section(
        "Contactez-nous",
        "Parlons de vos projets d\u2019infrastructure",
        full_height=False, show_bar=False,
    ))

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
                    # Left
                    inner_container(
                        settings={
                            "flex_direction": "column",
                            "flex_gap": {"size": 25, "unit": "px"},
                            "width": {"size": 350, "unit": "px"},
                            "_animation": "fadeInLeft",
                        },
                        elements=[
                            widget("image", {
                                "image": {"url": LOGOS["vectanor"], "id": LOGO_IDS["vectanor"]},
                                "image_size": "full",
                                "width": {"size": 180, "unit": "px"},
                                "_margin": {"top": "0", "bottom": "10", "left": "0", "right": "0", "unit": "px"},
                            }),
                            widget("icon-list", {
                                "icon_list": [
                                    {"_id": eid(), "text": "Qu\u00e9bec, Canada", "selected_icon": {"value": "fas fa-map-marker-alt", "library": "fa-solid"}, "link": {"url": ""}},
                                    {"_id": eid(), "text": "info@vectanor.com", "selected_icon": {"value": "fas fa-envelope", "library": "fa-solid"}, "link": {"url": "mailto:info@vectanor.com"}},
                                ],
                                "icon_color": ROYAL_BLUE,
                                "text_color": "#475569",
                                "typography_typography": "custom",
                                "typography_font_family": "Outfit",
                                "typography_font_size": {"size": 16, "unit": "px"},
                            }),
                            widget("text-editor", {
                                "editor": '<p style="font-size:16px; line-height:1.8; color:#475569;">Pour les demandes li\u00e9es \u00e0 une division sp\u00e9cifique, n\u2019h\u00e9sitez pas \u00e0 nous contacter. Nous vous dirigerons vers l\u2019\u00e9quipe appropri\u00e9e.</p>',
                            }),
                        ],
                    ),
                    # Right — styled HTML contact form
                    inner_container(
                        settings={
                            "flex_direction": "column",
                            "width": {"size": 450, "unit": "px"},
                            "background_background": "classic",
                            "background_color": LIGHT_GREY,
                            "border_radius": {"top": "12", "bottom": "12", "left": "12", "right": "12", "unit": "px"},
                            "padding": {"top": "35", "bottom": "35", "left": "35", "right": "35", "unit": "px"},
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
                                "_margin": {"top": "0", "bottom": "20", "left": "0", "right": "0", "unit": "px"},
                            }),
                            widget("html", {
                                "html": CONTACT_FORM_HTML,
                            }),
                        ],
                    ),
                ],
            ),
        ],
    ))

    return elements


# ═══════════════════════════════════════
# MAIN — REBUILD EVERYTHING
# ═══════════════════════════════════════

if __name__ == "__main__":
    import sys
    # Allow targeted rebuilds: python3 rebuild-wow.py contact vision
    # Or no args to rebuild everything
    targets = [a.lower() for a in sys.argv[1:]] if len(sys.argv) > 1 else []

    def wrap_page(page_key, page_id, elements):
        """Wrap page elements with font loader, header, and footer."""
        elements.insert(0, site_header("fr", page_key))
        elements.insert(0, font_loader())
        elements.append(site_footer("fr"))
        push_page(page_id, elements)

    all_pages = {
        "homepage": ("Homepage", lambda: wrap_page("homepage", PAGES["accueil"], build_homepage())),
        "vision": ("Vision page", lambda: wrap_page("vision", PAGES["vision"], build_vision_page())),
        "divisions": ("Divisions index", lambda: wrap_page("divisions", PAGES["divisions"], build_divisions_index())),
        "dimonoff": ("Dimonoff", lambda: wrap_page("dimonoff", PAGES["dimonoff"], build_division_page(**{k: DIVISIONS["dimonoff"][k] for k in ["name", "accent", "tagline", "description", "features", "logo_key", "external_url"]}))),
        "spatium": ("Spatium", lambda: wrap_page("spatium", PAGES["spatium"], build_division_page(**{k: DIVISIONS["spatium"][k] for k in ["name", "accent", "tagline", "description", "features", "logo_key", "external_url"]}))),
        "amotus": ("Amotus", lambda: wrap_page("amotus", PAGES["amotus"], build_division_page(**{k: DIVISIONS["amotus"][k] for k in ["name", "accent", "tagline", "description", "features", "logo_key", "external_url"]}))),
        "vigilia": ("Vigilia", lambda: wrap_page("vigilia", PAGES["vigilia"], build_division_page(**{k: DIVISIONS["vigilia"][k] for k in ["name", "accent", "tagline", "description", "features", "logo_key", "external_url"]}))),
        "contact": ("Contact page", lambda: wrap_page("contact", PAGES["contact"], build_contact_page())),
    }

    if targets:
        print(f"VECTANOR WEBSITE — Rebuilding: {', '.join(targets)}")
        print("=" * 50)
        for i, t in enumerate(targets, 1):
            if t in all_pages:
                name, fn = all_pages[t]
                print(f"\n[{i}/{len(targets)}] {name}...")
                fn()
            else:
                print(f"\n[!] Unknown target: {t} (available: {', '.join(all_pages.keys())})")
    else:
        print("=" * 50)
        print("VECTANOR WEBSITE — WOW REDESIGN (ALL PAGES)")
        print("=" * 50)
        for i, (key, (name, fn)) in enumerate(all_pages.items(), 1):
            print(f"\n[{i}/{len(all_pages)}] {name}...")
            fn()

    flush_elementor_cache()
    print("\n" + "=" * 50)
    print("DONE!")
    print("=" * 50)
