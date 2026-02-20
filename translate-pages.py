#!/usr/bin/env python3
"""
Vectanor Website — English and Spanish Content Push
Pushes all translated (EN/ES) page content to WordPress.

Usage:
    python3 translate-pages.py en    # Push all 8 English pages
    python3 translate-pages.py es    # Push all 8 Spanish pages
    python3 translate-pages.py both  # Push all 16 pages

Prerequisites:
    1. Fill in EN_PAGES and ES_PAGES IDs below (after WP Admin stub creation)
    2. Run: python3 translate-pages.py en|es|both
"""

import importlib.util
import os
import sys
import json
import requests

# ═══════════════════════════════════════
# Import builder infrastructure from rebuild-wow.py
# ═══════════════════════════════════════
_spec = importlib.util.spec_from_file_location(
    "rebuild_wow",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "rebuild-wow.py"),
)
rebuild_wow = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rebuild_wow)

# Re-export builder utilities for convenience
push_page = rebuild_wow.push_page
widget = rebuild_wow.widget
container = rebuild_wow.container
inner_container = rebuild_wow.inner_container
eid = rebuild_wow.eid
section_heading = rebuild_wow.section_heading
hero_section = rebuild_wow.hero_section
card_glow_css = rebuild_wow.card_glow_css
card_light_glow_css = rebuild_wow.card_light_glow_css
button_hover_css = rebuild_wow.button_hover_css
flush_elementor_cache = rebuild_wow.flush_elementor_cache

# New redesign components
font_loader = rebuild_wow.font_loader
seo_head = rebuild_wow.seo_head
seo_head_html = rebuild_wow.seo_head_html
site_header = rebuild_wow.site_header
site_footer = rebuild_wow.site_footer
site_header_html = rebuild_wow.site_header_html
site_footer_html = rebuild_wow.site_footer_html

# Brand colors (same as rebuild-wow.py)
NAVY = rebuild_wow.NAVY
ROYAL_BLUE = rebuild_wow.ROYAL_BLUE
SKY_BLUE = rebuild_wow.SKY_BLUE
NEAR_BLACK = rebuild_wow.NEAR_BLACK
DARK_NAVY = rebuild_wow.DARK_NAVY
SLATE = rebuild_wow.SLATE
LIGHT_GREY = rebuild_wow.LIGHT_GREY
WHITE = rebuild_wow.WHITE
AMBER = rebuild_wow.AMBER
GREEN = rebuild_wow.GREEN
PURPLE = rebuild_wow.PURPLE
PINK = rebuild_wow.PINK
MID_DARK = rebuild_wow.MID_DARK

# Logos (same as rebuild-wow.py)
LOGOS = rebuild_wow.LOGOS
LOGO_IDS = rebuild_wow.LOGO_IDS

# CSS constants
HERO_TITLE_CSS = rebuild_wow.HERO_TITLE_CSS
FADE_DOWN_CSS = rebuild_wow.FADE_DOWN_CSS
TAGLINE_REVEAL_CSS = rebuild_wow.TAGLINE_REVEAL_CSS
CTA_BUTTON_CSS = rebuild_wow.CTA_BUTTON_CSS
FOUR_COLOR_BAR_HTML = rebuild_wow.FOUR_COLOR_BAR_HTML
GRAIN_OVERLAY_CSS = rebuild_wow.GRAIN_OVERLAY_CSS
GRID_PATTERN_CSS = rebuild_wow.GRID_PATTERN_CSS
HERO_GLOW_CSS = rebuild_wow.HERO_GLOW_CSS
DIAGONAL_ACCENT_CSS = rebuild_wow.DIAGONAL_ACCENT_CSS
ORBITAL_RINGS_HTML = rebuild_wow.ORBITAL_RINGS_HTML

# API config (same credentials as rebuild-wow.py)
WP_URL = rebuild_wow.WP_URL
AUTH = rebuild_wow.AUTH

# ═══════════════════════════════════════
# PAGE ID CONFIG — Fill these in after WP Admin stub creation
# ═══════════════════════════════════════
EN_PAGES = {
    "homepage":  30,    # /en/ (accueil-english)
    "vision":    42,    # /en/our-vision/
    "divisions": 43,    # /en/our-divisions/
    "dimonoff":  44,    # /en/our-divisions/dimonoff/
    "spatium":   45,    # /en/our-divisions/spatium/
    "amotus":    46,    # /en/our-divisions/amotus/
    "contact":   47,    # /en/contact-us/
    "vigilia":   48,    # /en/our-divisions/vigilia/
}

ES_PAGES = {
    "homepage":  31,    # /es/ (accueil-espanol)
    "vision":    49,    # /es/nuestra-vision/
    "divisions": 50,    # /es/nuestras-divisiones/
    "dimonoff":  51,    # /es/nuestras-divisiones/dimonoff/
    "spatium":   52,    # /es/nuestras-divisiones/spatium/
    "amotus":    53,    # /es/nuestras-divisiones/amotus/
    "contact":   54,    # /es/contactenos/
    "vigilia":   55,    # /es/nuestras-divisiones/vigilia/
}

# ═══════════════════════════════════════
# RAW HTML PUSH (for contact page)
# ═══════════════════════════════════════

def push_raw_html(page_id, html):
    """Push raw HTML to a WordPress page, bypassing Elementor caching."""
    resp = requests.post(f"{WP_URL}/pages/{page_id}", auth=AUTH, json={
        "content": html,
        "status": "publish",
        "meta": {"_elementor_edit_mode": "", "_elementor_data": ""}
    })
    d = resp.json()
    print(f"  -> {d.get('title', {}).get('rendered', '?')}: raw HTML [{d.get('status', '?')}]")
    return resp


# ═══════════════════════════════════════
# CONTACT FORM HTML — English
# ═══════════════════════════════════════

EN_CONTACT_FORM_HTML = """
<form action="https://formsubmit.co/info@vectanor.com" method="POST" style="display:flex;flex-direction:column;gap:14px;">
  <input type="hidden" name="_subject" value="New message via vectanor.com">
  <input type="hidden" name="_captcha" value="false">
  <input type="hidden" name="_next" value="https://vectanor.com/en/contact-us/?sent=1">
  <input type="hidden" name="_template" value="table">
  <input type="text" name="_honey" style="display:none">
  <div>
    <label style="display:block;font-family:Inter,sans-serif;font-size:14px;color:#CBD5E1;margin-bottom:5px;font-weight:500;">Name <span style="color:#EF4444;">*</span></label>
    <input type="text" name="name" placeholder="Your full name" required
      style="width:100%;padding:10px 14px;border:1px solid rgba(255,255,255,0.12);border-radius:6px;font-family:Inter,sans-serif;font-size:14px;color:#E2E8F0;background:rgba(255,255,255,0.06);outline:none;transition:border-color 0.2s;"
      onfocus="this.style.borderColor='#3B82F6'" onblur="this.style.borderColor='rgba(255,255,255,0.12)'">
  </div>
  <div>
    <label style="display:block;font-family:Inter,sans-serif;font-size:14px;color:#CBD5E1;margin-bottom:5px;font-weight:500;">Email <span style="color:#EF4444;">*</span></label>
    <input type="email" name="email" placeholder="your@email.com" required
      style="width:100%;padding:10px 14px;border:1px solid rgba(255,255,255,0.12);border-radius:6px;font-family:Inter,sans-serif;font-size:14px;color:#E2E8F0;background:rgba(255,255,255,0.06);outline:none;transition:border-color 0.2s;"
      onfocus="this.style.borderColor='#3B82F6'" onblur="this.style.borderColor='rgba(255,255,255,0.12)'">
  </div>
  <div>
    <label style="display:block;font-family:Inter,sans-serif;font-size:14px;color:#CBD5E1;margin-bottom:5px;font-weight:500;">Subject</label>
    <select name="subject"
      style="width:100%;padding:10px 14px;border:1px solid rgba(255,255,255,0.12);border-radius:6px;font-family:Inter,sans-serif;font-size:14px;color:#E2E8F0;background:rgba(255,255,255,0.06);outline:none;transition:border-color 0.2s;cursor:pointer;"
      onfocus="this.style.borderColor='#3B82F6'" onblur="this.style.borderColor='rgba(255,255,255,0.12)'">
      <option value="General Inquiry">General Inquiry</option>
      <option value="Partnership">Partnership</option>
      <option value="Media">Media</option>
      <option value="Other">Other</option>
    </select>
  </div>
  <div>
    <label style="display:block;font-family:Inter,sans-serif;font-size:14px;color:#CBD5E1;margin-bottom:5px;font-weight:500;">Message <span style="color:#EF4444;">*</span></label>
    <textarea name="message" placeholder="Your message..." required rows="4"
      style="width:100%;padding:10px 14px;border:1px solid #CBD5E1;border-radius:6px;font-family:Outfit,sans-serif;font-size:14px;color:#0F172A;background:#FFFFFF;outline:none;resize:vertical;transition:border-color 0.2s;"
      onfocus="this.style.borderColor='#3B82F6'" onblur="this.style.borderColor='rgba(255,255,255,0.12)'"></textarea>
  </div>
  <button type="submit"
    style="width:100%;padding:14px;background:#2563EB;color:#FFFFFF;border:none;border-radius:6px;font-family:Montserrat,sans-serif;font-size:14px;font-weight:600;cursor:pointer;transition:all 0.3s;letter-spacing:0.5px;"
    onmouseover="this.style.transform='translateY(-2px)';this.style.boxShadow='0 8px 25px rgba(59,130,246,0.4)'"
    onmouseout="this.style.transform='translateY(0)';this.style.boxShadow='none'">
    Send
  </button>
</form>
<script>
if(new URLSearchParams(window.location.search).get('sent')==='1'){
  document.querySelector('form[action*="formsubmit"]').innerHTML='<div style="text-align:center;padding:40px 20px;"><div style="font-size:28px;margin-bottom:12px;">&#10003;</div><p style="font-family:Outfit,sans-serif;font-size:16px;color:#FFFFFF;font-weight:500;">Thank you for your message!</p><p style="font-family:Outfit,sans-serif;font-size:14px;color:#64748B;margin-top:8px;">We will get back to you shortly.</p></div>';
}
</script>
"""

# ═══════════════════════════════════════
# CONTACT FORM HTML — Spanish
# ═══════════════════════════════════════

ES_CONTACT_FORM_HTML = """
<form action="https://formsubmit.co/info@vectanor.com" method="POST" style="display:flex;flex-direction:column;gap:14px;">
  <input type="hidden" name="_subject" value="Nuevo mensaje via vectanor.com">
  <input type="hidden" name="_captcha" value="false">
  <input type="hidden" name="_next" value="https://vectanor.com/es/contactenos/?sent=1">
  <input type="hidden" name="_template" value="table">
  <input type="text" name="_honey" style="display:none">
  <div>
    <label style="display:block;font-family:Inter,sans-serif;font-size:14px;color:#CBD5E1;margin-bottom:5px;font-weight:500;">Nombre <span style="color:#EF4444;">*</span></label>
    <input type="text" name="name" placeholder="Su nombre completo" required
      style="width:100%;padding:10px 14px;border:1px solid rgba(255,255,255,0.12);border-radius:6px;font-family:Inter,sans-serif;font-size:14px;color:#E2E8F0;background:rgba(255,255,255,0.06);outline:none;transition:border-color 0.2s;"
      onfocus="this.style.borderColor='#3B82F6'" onblur="this.style.borderColor='rgba(255,255,255,0.12)'">
  </div>
  <div>
    <label style="display:block;font-family:Inter,sans-serif;font-size:14px;color:#CBD5E1;margin-bottom:5px;font-weight:500;">Correo electr&#243;nico <span style="color:#EF4444;">*</span></label>
    <input type="email" name="email" placeholder="su@correo.com" required
      style="width:100%;padding:10px 14px;border:1px solid rgba(255,255,255,0.12);border-radius:6px;font-family:Inter,sans-serif;font-size:14px;color:#E2E8F0;background:rgba(255,255,255,0.06);outline:none;transition:border-color 0.2s;"
      onfocus="this.style.borderColor='#3B82F6'" onblur="this.style.borderColor='rgba(255,255,255,0.12)'">
  </div>
  <div>
    <label style="display:block;font-family:Inter,sans-serif;font-size:14px;color:#CBD5E1;margin-bottom:5px;font-weight:500;">Asunto</label>
    <select name="subject"
      style="width:100%;padding:10px 14px;border:1px solid rgba(255,255,255,0.12);border-radius:6px;font-family:Inter,sans-serif;font-size:14px;color:#E2E8F0;background:rgba(255,255,255,0.06);outline:none;transition:border-color 0.2s;cursor:pointer;"
      onfocus="this.style.borderColor='#3B82F6'" onblur="this.style.borderColor='rgba(255,255,255,0.12)'">
      <option value="Consulta general">Consulta general</option>
      <option value="Asociaci&#243;n">Asociaci&#243;n</option>
      <option value="Medios">Medios</option>
      <option value="Otro">Otro</option>
    </select>
  </div>
  <div>
    <label style="display:block;font-family:Inter,sans-serif;font-size:14px;color:#CBD5E1;margin-bottom:5px;font-weight:500;">Mensaje <span style="color:#EF4444;">*</span></label>
    <textarea name="message" placeholder="Su mensaje..." required rows="4"
      style="width:100%;padding:10px 14px;border:1px solid #CBD5E1;border-radius:6px;font-family:Outfit,sans-serif;font-size:14px;color:#0F172A;background:#FFFFFF;outline:none;resize:vertical;transition:border-color 0.2s;"
      onfocus="this.style.borderColor='#3B82F6'" onblur="this.style.borderColor='rgba(255,255,255,0.12)'"></textarea>
  </div>
  <button type="submit"
    style="width:100%;padding:14px;background:#2563EB;color:#FFFFFF;border:none;border-radius:6px;font-family:Montserrat,sans-serif;font-size:14px;font-weight:600;cursor:pointer;transition:all 0.3s;letter-spacing:0.5px;"
    onmouseover="this.style.transform='translateY(-2px)';this.style.boxShadow='0 8px 25px rgba(59,130,246,0.4)'"
    onmouseout="this.style.transform='translateY(0)';this.style.boxShadow='none'">
    Enviar
  </button>
</form>
<script>
if(new URLSearchParams(window.location.search).get('sent')==='1'){
  document.querySelector('form[action*="formsubmit"]').innerHTML='<div style="text-align:center;padding:40px 20px;"><div style="font-size:28px;margin-bottom:12px;">&#10003;</div><p style="font-family:Outfit,sans-serif;font-size:16px;color:#FFFFFF;font-weight:500;">&#161;Gracias por su mensaje!</p><p style="font-family:Outfit,sans-serif;font-size:14px;color:#64748B;margin-top:8px;">Le responderemos a la brevedad.</p></div>';
}
</script>
"""

# ═══════════════════════════════════════
# DIVISION DATA — English
# ═══════════════════════════════════════

DIVISIONS_EN = {
    "dimonoff": {
        "name": "Dimonoff",
        "accent": AMBER,
        "tagline": "Smart lighting and connected urban infrastructure",
        "description": (
            "Dimonoff is the reference in smart lighting management and connected urban infrastructure. "
            "For over a decade, Dimonoff has deployed large-scale remote management solutions for municipalities "
            "and infrastructure operators, enabling precise control, reduced energy consumption, and predictive "
            "maintenance of thousands of light points."
        ),
        "features": [
            {"icon": "fas fa-lightbulb", "title": "Lighting Remote Management", "desc": "Intelligent control of municipal lighting networks at scale with real-time monitoring."},
            {"icon": "fas fa-city", "title": "Smart City", "desc": "Integrated platforms for managing connected urban assets and optimizing municipal operations."},
            {"icon": "fas fa-bolt", "title": "Energy Efficiency", "desc": "Measurable reduction in energy consumption through context-adaptive dimming algorithms."},
            {"icon": "fas fa-tools", "title": "Predictive Maintenance", "desc": "Proactive fault detection and optimized field intervention planning."},
        ],
        "logo_key": "dimonoff",
        "external_url": "https://dimonoff.com",
    },
    "spatium": {
        "name": "Spatium",
        "accent": GREEN,
        "tagline": "Smart mobility and parking",
        "description": (
            "Spatium addresses urban mobility challenges with integrated smart parking and dynamic flow "
            "management solutions. By combining IoT sensors, advanced analytics, and multi-platform integration, "
            "Spatium enables cities and operators to transform parking from an urban irritant into a lever for "
            "sustainable mobility."
        ),
        "features": [
            {"icon": "fas fa-parking", "title": "Smart Parking", "desc": "Real-time availability detection, dynamic guidance, and occupancy rate optimization."},
            {"icon": "fas fa-route", "title": "Mobility Management", "desc": "Traffic flow analysis and decision-support tools for urban planners."},
            {"icon": "fas fa-wifi", "title": "IoT & Sensors", "desc": "Connected sensor networks for a complete, real-time view of urban space."},
            {"icon": "fas fa-chart-line", "title": "Analytics & Data", "desc": "Dashboards and reports to measure performance and guide mobility investments."},
        ],
        "logo_key": "spatium",
        "external_url": "https://dimonoff.com",
    },
    "amotus": {
        "name": "Amotus",
        "accent": PURPLE,
        "tagline": "Design House and industrial innovation catalyst",
        "description": (
            "Amotus acts as the Design House within Groupe Vectanor, designing custom technology solutions for "
            "demanding industrial environments. From electronic design to systems integration, Amotus transforms "
            "complex technical challenges into reliable, certified, production-ready products."
        ),
        "features": [
            {"icon": "fas fa-microchip", "title": "Electronic Design", "desc": "Circuit board design, firmware, and embedded systems for critical industrial applications."},
            {"icon": "fas fa-cogs", "title": "Systems Integration", "desc": "Assembly and integration of complex subsystems into turnkey industrial solutions."},
            {"icon": "fas fa-flask", "title": "R&D and Prototyping", "desc": "From concept to functional prototype, accelerating the innovation cycle with a pragmatic approach."},
            {"icon": "fas fa-certificate", "title": "Certification & Quality", "desc": "Support for industrial certifications (CE, UL, CSA) and production quality management."},
        ],
        "logo_key": "amotus",
        "external_url": "https://amotus.com",
    },
    "vigilia": {
        "name": "Vigilia",
        "accent": PINK,
        "tagline": "Critical infrastructure monitoring and surveillance",
        "description": (
            "Vigilia is the Groupe Vectanor division dedicated to monitoring and surveillance of critical "
            "infrastructure. Through smart sensors, MQTT communication systems, and a real-time analytics "
            "platform, Vigilia enables operators to detect anomalies, anticipate failures, and ensure the "
            "operational continuity of their most sensitive installations."
        ),
        "features": [
            {"icon": "fas fa-eye", "title": "Real-time Monitoring", "desc": "Continuous monitoring of critical parameters with instant alerts and operational dashboards."},
            {"icon": "fas fa-broadcast-tower", "title": "IoT & Communication", "desc": "Sensor networks connected via MQTT for reliable, low-latency data collection."},
            {"icon": "fas fa-brain", "title": "Predictive Analytics", "desc": "AI algorithms to anticipate failures before they occur."},
            {"icon": "fas fa-database", "title": "Data Logging & Reports", "desc": "Long-term storage of performance data and automated compliance report generation."},
        ],
        "logo_key": "vigilia",
        "external_url": None,
    },
}

# ═══════════════════════════════════════
# DIVISION DATA — Spanish
# ═══════════════════════════════════════

DIVISIONS_ES = {
    "dimonoff": {
        "name": "Dimonoff",
        "accent": AMBER,
        "tagline": "Iluminaci\u00f3n inteligente e infraestructura urbana conectada",
        "description": (
            "Dimonoff es la referencia en gesti\u00f3n de iluminaci\u00f3n inteligente e infraestructura urbana conectada. "
            "Durante m\u00e1s de una d\u00e9cada, Dimonoff ha desplegado soluciones de gesti\u00f3n remota a gran escala para "
            "municipios y operadores de infraestructura, permitiendo un control preciso, reducci\u00f3n del consumo "
            "energ\u00e9tico y mantenimiento predictivo de miles de puntos de luz."
        ),
        "features": [
            {"icon": "fas fa-lightbulb", "title": "Gesti\u00f3n remota de iluminaci\u00f3n", "desc": "Control inteligente de redes de alumbrado municipal a gran escala con monitoreo en tiempo real."},
            {"icon": "fas fa-city", "title": "Ciudad inteligente", "desc": "Plataformas integradas para la gesti\u00f3n de activos urbanos conectados y la optimizaci\u00f3n de operaciones municipales."},
            {"icon": "fas fa-bolt", "title": "Eficiencia energ\u00e9tica", "desc": "Reducci\u00f3n medible del consumo energ\u00e9tico mediante algoritmos de atenuaci\u00f3n adaptados al contexto."},
            {"icon": "fas fa-tools", "title": "Mantenimiento predictivo", "desc": "Detecci\u00f3n proactiva de fallas y planificaci\u00f3n optimizada de intervenciones en campo."},
        ],
        "logo_key": "dimonoff",
        "external_url": "https://dimonoff.com",
    },
    "spatium": {
        "name": "Spatium",
        "accent": GREEN,
        "tagline": "Movilidad inteligente y estacionamiento inteligente",
        "description": (
            "Spatium aborda los desaf\u00edos de movilidad urbana con soluciones integradas de estacionamiento "
            "inteligente y gesti\u00f3n din\u00e1mica de flujos. Al combinar sensores IoT, anal\u00edtica avanzada e "
            "integraci\u00f3n multiplataforma, Spatium permite a las ciudades y operadores transformar el "
            "estacionamiento de un problema urbano en un motor de movilidad sostenible."
        ),
        "features": [
            {"icon": "fas fa-parking", "title": "Estacionamiento inteligente", "desc": "Detecci\u00f3n en tiempo real de disponibilidad, gu\u00eda din\u00e1mica y optimizaci\u00f3n de la tasa de ocupaci\u00f3n."},
            {"icon": "fas fa-route", "title": "Gesti\u00f3n de movilidad", "desc": "An\u00e1lisis de flujos de tr\u00e1fico y herramientas de apoyo a la decisi\u00f3n para planificadores urbanos."},
            {"icon": "fas fa-wifi", "title": "IoT & Sensores", "desc": "Redes de sensores conectados para una visi\u00f3n completa y en tiempo real del espacio urbano."},
            {"icon": "fas fa-chart-line", "title": "Anal\u00edtica & Datos", "desc": "Paneles de control e informes para medir el rendimiento y orientar las inversiones en movilidad."},
        ],
        "logo_key": "spatium",
        "external_url": "https://dimonoff.com",
    },
    "amotus": {
        "name": "Amotus",
        "accent": PURPLE,
        "tagline": "Design House y catalizador de innovaci\u00f3n industrial",
        "description": (
            "Amotus act\u00faa como Design House dentro de Groupe Vectanor, dise\u00f1ando soluciones tecnol\u00f3gicas a "
            "medida para entornos industriales exigentes. Desde el dise\u00f1o electr\u00f3nico hasta la integraci\u00f3n de "
            "sistemas, Amotus transforma desaf\u00edos t\u00e9cnicos complejos en productos confiables, certificados y "
            "listos para producci\u00f3n."
        ),
        "features": [
            {"icon": "fas fa-microchip", "title": "Dise\u00f1o electr\u00f3nico", "desc": "Dise\u00f1o de tarjetas electr\u00f3nicas, firmware y sistemas embebidos para aplicaciones industriales cr\u00edticas."},
            {"icon": "fas fa-cogs", "title": "Integraci\u00f3n de sistemas", "desc": "Ensamblaje e integraci\u00f3n de subsistemas complejos en soluciones industriales llave en mano."},
            {"icon": "fas fa-flask", "title": "I+D y prototipado", "desc": "Del concepto al prototipo funcional, acelerando el ciclo de innovaci\u00f3n con un enfoque pragm\u00e1tico."},
            {"icon": "fas fa-certificate", "title": "Certificaci\u00f3n y calidad", "desc": "Apoyo para certificaciones industriales (CE, UL, CSA) y gesti\u00f3n de la calidad de producci\u00f3n."},
        ],
        "logo_key": "amotus",
        "external_url": "https://amotus.com",
    },
    "vigilia": {
        "name": "Vigilia",
        "accent": PINK,
        "tagline": "Monitoreo y vigilancia de infraestructuras cr\u00edticas",
        "description": (
            "Vigilia es la divisi\u00f3n de Groupe Vectanor dedicada al monitoreo y vigilancia de infraestructuras "
            "cr\u00edticas. A trav\u00e9s de sensores inteligentes, sistemas de comunicaci\u00f3n MQTT y una plataforma de "
            "an\u00e1lisis en tiempo real, Vigilia permite a los operadores detectar anomal\u00edas, anticipar fallas y "
            "garantizar la continuidad operacional de sus instalaciones m\u00e1s sensibles."
        ),
        "features": [
            {"icon": "fas fa-eye", "title": "Monitoreo en tiempo real", "desc": "Supervisi\u00f3n continua de par\u00e1metros cr\u00edticos con alertas instant\u00e1neas y paneles operacionales."},
            {"icon": "fas fa-broadcast-tower", "title": "IoT & Comunicaci\u00f3n", "desc": "Redes de sensores conectados v\u00eda MQTT para recolecci\u00f3n de datos confiable y de baja latencia."},
            {"icon": "fas fa-brain", "title": "An\u00e1lisis predictivo", "desc": "Algoritmos de inteligencia artificial para anticipar fallas antes de que ocurran."},
            {"icon": "fas fa-database", "title": "Historizaci\u00f3n & Informes", "desc": "Almacenamiento a largo plazo de datos de rendimiento y generaci\u00f3n automatizada de informes de conformidad."},
        ],
        "logo_key": "vigilia",
        "external_url": None,
    },
}


# ═══════════════════════════════════════
# REUSABLE BACK-TO-GROUP CTA (language-specific)
# ═══════════════════════════════════════

def back_to_group_cta_en():
    """Footer CTA for English division pages — links back to /en/."""
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
                "title": "A division of Groupe Vectanor",
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
                "text": "\u2190 Back to group",
                "link": {"url": "/en/", "is_external": False},
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


def back_to_group_cta_es():
    """Footer CTA for Spanish division pages — links back to /es/."""
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
                "title": "Una divisi\u00f3n de Groupe Vectanor",
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
                "text": "\u2190 Volver al grupo",
                "link": {"url": "/es/", "is_external": False},
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
# HOMEPAGE BUILDERS
# ═══════════════════════════════════════

def build_homepage_en():
    """English homepage — mirrors build_homepage() with EN strings and /en/ links."""
    elements = []

    # HERO
    elements.append(hero_section(
        "VECTANOR",
        "Sets the direction. Divisions advance. Systems follow.",
        full_height=True, show_cta=True,
        cta_text="Discover our divisions", cta_link="/en/our-divisions/",
        ghost_cta_text="Our approach \u2192", ghost_cta_link="/en/our-vision/",
    ))

    # VISION BRIEF
    elements.append(container(
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
            inner_container(
                settings={
                    "flex_direction": "row",
                    "flex_wrap": "wrap",
                    "flex_gap": {"size": 40, "unit": "px"},
                    "flex_justify_content": "center",
                    "flex_align_items": "flex-start",
                    "width": {"size": 100, "unit": "%"},
                    "max_width": {"size": 1100, "unit": "px"},
                },
                elements=[
                    inner_container(
                        settings={
                            "width": {"size": 35, "unit": "%"},
                            "min_width": {"size": 280, "unit": "px"},
                            "flex_direction": "column",
                        },
                        elements=[*section_heading("Orchestrating Complexity")],
                    ),
                    inner_container(
                        settings={
                            "width": {"size": 58, "unit": "%"},
                            "min_width": {"size": 300, "unit": "px"},
                            "flex_direction": "column",
                        },
                        elements=[
                            widget("text-editor", {
                                "editor": (
                                    '<div style="max-width:560px;">'
                                    '<p style="font-size:16px; line-height:1.9; color:#334155; margin-bottom:20px; border-left:6px solid #3B82F6; padding-left:24px; font-family:Inter,sans-serif;">'
                                    'Cities, infrastructure, and industrial environments have become complex systems, often managed '
                                    'in silos. <strong>Groupe Vectanor</strong> acts as a steering structure capable of aligning '
                                    'specialized expertise toward a common goal: making urban and industrial systems more reliable, '
                                    'more efficient, and more sustainable.'
                                    '</p>'
                                    '<p style="font-size:16px; line-height:1.9; color:#334155; font-family:Inter,sans-serif;">'
                                    'From smart lighting to urban mobility, from electronic design to critical infrastructure '
                                    'monitoring \u2014 our divisions cover the entire technology value chain for the cities and '
                                    'industries of tomorrow.'
                                    '</p>'
                                    '</div>'
                                ),
                                "css_classes": "v-reveal",
                            }),
                        ],
                    ),
                ],
            ),
        ],
    ))

    # KEY FIGURES
    def stat_block_en(number, label, delay=0):
        return inner_container(
            settings={
                "flex_direction": "column",
                "flex_align_items": "center",
                "padding": {"top": "24", "bottom": "24", "left": "28", "right": "28", "unit": "px"},
                "css_classes": "v-reveal",
                "background_background": "classic",
                "background_color": "rgba(255,255,255,0.03)",
                "border_border": "solid",
                "border_width": {"top": "1", "bottom": "1", "left": "1", "right": "1", "unit": "px"},
                "border_color": "rgba(255,255,255,0.06)",
                "border_radius": {"top": "12", "bottom": "12", "left": "12", "right": "12", "unit": "px"},
            },
            elements=[
                widget("heading", {
                    "title": number,
                    "header_size": "h3",
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

    elements.append(container(
        settings={
            "content_width": "boxed",
            "background_background": "gradient",
            "background_color": NEAR_BLACK,
            "background_color_b": DARK_NAVY,
            "background_gradient_angle": {"size": 90, "unit": "deg"},
            "flex_direction": "column",
            "flex_align_items": "center",
            "padding": {"top": "40", "bottom": "40", "left": "40", "right": "40", "unit": "px"},
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
                    stat_block_en("4", "Specialized divisions", 0),
                    stat_block_en("18+", "Years of expertise", 100),
                    stat_block_en("850K+", "Devices deployed", 200),
                    stat_block_en("15", "Countries", 300),
                ],
            ),
        ],
    ))

    # DIVISIONS — Dark glassmorphism section
    def division_card(name, desc, color, link, logo_key, delay, highlights=None):
        card_elems = [
            widget("image", {
                "image": {"url": LOGOS[logo_key], "id": LOGO_IDS[logo_key]},
                "image_size": "full",
                "width": {"size": 140, "unit": "px"},
                "alt": f"{name} logo",
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
                "editor": f'<p style="font-size:15px; line-height:1.75; color:#CBD5E1;">{desc}</p>',
            }),
        ]
        if highlights:
            bullets_html = ''.join(
                f'<li style="font-size:13px;line-height:1.6;color:#CBD5E1;padding:4px 0;display:flex;align-items:center;">'
                f'<span style="display:inline-block;width:6px;height:6px;border-right:2px solid {color};border-top:2px solid {color};transform:rotate(45deg);margin-right:10px;flex-shrink:0;"></span>{h}</li>'
                for h in highlights
            )
            card_elems.append(widget("html", {
                "html": f'<ul style="list-style:none;padding:0;margin:8px 0 4px;">{bullets_html}</ul>',
            }))
        btn_elems = [
            widget("button", {
                "text": "Learn more",
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
                "css_classes": "v-reveal",
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
                "Our divisions",
                "Each entity in the group is autonomous in its market, yet integrated into a global architecture.",
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
                        "Smart lighting and connected urban infrastructure.",
                        AMBER, "/en/our-divisions/dimonoff/", "dimonoff", 0,
                        highlights=[
                            "Large-scale municipal remote management",
                            "Measurable energy reduction",
                            "Multi-site SaaS platform",
                        ],
                    ),
                    division_card(
                        "Spatium",
                        "Smart mobility and parking.",
                        GREEN, "/en/our-divisions/spatium/", "spatium", 100,
                        highlights=[
                            "Real-time detection and guidance",
                            "Low-power IoT sensors",
                            "Mobility flow analytics",
                        ],
                    ),
                    division_card(
                        "Amotus",
                        "Design House and industrial innovation catalyst.",
                        PURPLE, "/en/our-divisions/amotus/", "amotus", 200,
                        highlights=[
                            "Custom electronic design",
                            "From prototype to certification",
                            "Industrial embedded systems",
                        ],
                    ),
                    division_card(
                        "Vigilia",
                        "Critical infrastructure monitoring and surveillance.",
                        PINK, "/en/our-divisions/vigilia/", "vigilia", 300,
                        highlights=[
                            "24/7 infrastructure monitoring",
                            "AI-powered predictive alerts",
                            "Secure MQTT communication",
                        ],
                    ),
                ],
            ),
        ],
    )
    elements.append(divisions_section)

    # APPROACH — Dark numbered cards
    def value_card_en(title, desc, accent_color, number, delay_class):
        return inner_container(
            settings={
                "background_background": "classic",
                "background_color": MID_DARK,
                "border_border": "solid",
                "border_width": {"top": "3", "bottom": "0", "left": "0", "right": "0", "unit": "px", "isLinked": False},
                "border_color": accent_color,
                "border_radius": {"top": "12", "bottom": "12", "left": "12", "right": "12", "unit": "px"},
                "padding": {"top": "40", "bottom": "40", "left": "30", "right": "30", "unit": "px"},
                "flex_direction": "column",
                "flex_align_items": "flex-start",
                "flex_gap": {"size": 8, "unit": "px"},
                "css_classes": f"v-reveal {delay_class}",
                "position": "relative",
                "custom_css": f"""selector {{ transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94); }}
selector:hover {{ transform: translateY(-8px); box-shadow: 0 20px 60px -15px {accent_color}30; }}""",
            },
            elements=[
                widget("html", {
                    "html": f'<span style="font-size:64px;font-weight:800;color:transparent;-webkit-text-stroke:1px rgba(255,255,255,0.06);position:absolute;top:12px;right:20px;font-family:Montserrat,sans-serif;">{number}</span>',
                }),
                widget("heading", {
                    "title": title,
                    "header_size": "h4",
                    "title_color": WHITE,
                    "typography_typography": "custom",
                    "typography_font_family": "Montserrat",
                    "typography_font_size": {"size": 22, "unit": "px"},
                    "typography_font_weight": "700",
                    "_margin": {"top": "8", "bottom": "5", "left": "0", "right": "0", "unit": "px"},
                }),
                widget("text-editor", {
                    "editor": f'<p style="font-size:15px; line-height:1.8; color:#CBD5E1;">{desc}</p>',
                }),
            ],
        )

    approach = container(
        settings={
            "content_width": "boxed",
            "background_background": "gradient",
            "background_color": NEAR_BLACK,
            "background_color_b": DARK_NAVY,
            "background_gradient_angle": {"size": 145, "unit": "deg"},
            "flex_direction": "column",
            "flex_align_items": "center",
            "padding": {"top": "90", "bottom": "90", "left": "40", "right": "40", "unit": "px"},
            "custom_css": GRAIN_OVERLAY_CSS,
        },
        elements=[
            *section_heading("Our approach", dark=True),
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
                    value_card_en(
                        "Interoperability",
                        "Systems designed to communicate openly, without vendor lock-in.",
                        ROYAL_BLUE, "01", "v-reveal",
                    ),
                    value_card_en(
                        "Reliability",
                        "Dependable, secure infrastructure built to last.",
                        "#10B981", "02", "v-reveal-d1",
                    ),
                    value_card_en(
                        "Scalability",
                        "Modular architecture that evolves without disruption.",
                        PURPLE, "03", "v-reveal-d2",
                    ),
                ],
            ),
        ],
    )
    elements.append(approach)

    # CTA SECTION
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
            "padding": {"top": "80", "bottom": "80", "left": "40", "right": "40", "unit": "px"},
            "custom_css": GRID_PATTERN_CSS,
        },
        elements=[
            widget("heading", {
                "title": "Ready to shape the future?",
                "header_size": "h2",
                "align": "center",
                "title_color": WHITE,
                "typography_typography": "custom",
                "typography_font_family": "Montserrat",
                "typography_font_size": {"size": 40, "unit": "px"},
                "typography_font_weight": "700",
                "_margin": {"top": "0", "bottom": "20", "left": "0", "right": "0", "unit": "px"},
                "css_classes": "v-reveal",
            }),
            widget("text-editor", {
                "editor": (
                    '<p style="text-align:center; font-size:16px; color:#CBD5E1; max-width:600px; margin:0 auto; font-family:Inter,sans-serif;">'
                    'Contact us to discover how Groupe Vectanor can support your infrastructure and technology '
                    'transformation projects.'
                    '</p>'
                ),
                "css_classes": "v-reveal",
            }),
            inner_container(
                settings={
                    "flex_direction": "row",
                    "flex_justify_content": "center",
                    "flex_align_items": "center",
                    "flex_gap": {"size": 16, "unit": "px"},
                    "_margin": {"top": "32", "bottom": "0", "left": "0", "right": "0", "unit": "px"},
                },
                elements=[
                    widget("button", {
                        "text": "Contact us",
                        "link": {"url": "/en/contact-us/", "is_external": False},
                        "align": "center",
                        "background_color": ROYAL_BLUE,
                        "button_text_color": WHITE,
                        "typography_typography": "custom",
                        "typography_font_family": "Montserrat",
                        "typography_font_size": {"size": 14, "unit": "px"},
                        "typography_font_weight": "600",
                        "button_padding": {"top": "18", "bottom": "18", "left": "44", "right": "44", "unit": "px"},
                        "custom_css": CTA_BUTTON_CSS,
                    }),
                    widget("button", {
                        "text": "Our divisions \u2192",
                        "link": {"url": "/en/our-divisions/", "is_external": False},
                        "align": "center",
                        "button_text_color": WHITE,
                        "typography_typography": "custom",
                        "typography_font_family": "Montserrat",
                        "typography_font_size": {"size": 14, "unit": "px"},
                        "typography_font_weight": "600",
                        "button_padding": {"top": "18", "bottom": "18", "left": "44", "right": "44", "unit": "px"},
                        "custom_css": """selector .elementor-button {
    background: transparent !important;
    border: 1px solid rgba(255,255,255,0.3) !important;
    border-radius: 8px !important;
    transition: all 0.3s ease;
}
selector .elementor-button:hover {
    border-color: rgba(255,255,255,0.6) !important;
    background: rgba(255,255,255,0.05) !important;
}""",
                    }),
                ],
            ),
            widget("text-editor", {
                "editor": (
                    '<p style="text-align:center; font-size:13px; color:#64748B; margin-top:24px; font-family:Inter,sans-serif; letter-spacing:0.5px;">'
                    'Qu\u00e9bec, Canada \u00b7 18+ years of expertise \u00b7 15 countries'
                    '</p>'
                ),
            }),
        ],
    )
    elements.append(cta)

    return elements


def build_homepage_es():
    """Spanish homepage — mirrors build_homepage() with ES strings and /es/ links."""
    elements = []

    # HERO
    elements.append(hero_section(
        "VECTANOR",
        "Marca la direcci\u00f3n. Las divisiones avanzan. Los sistemas siguen.",
        full_height=True, show_cta=True,
        cta_text="Descubrir nuestras divisiones", cta_link="/es/nuestras-divisiones/",
        ghost_cta_text="Nuestro enfoque \u2192", ghost_cta_link="/es/nuestra-vision/",
    ))

    # VISION BRIEF
    elements.append(container(
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
            inner_container(
                settings={
                    "flex_direction": "row",
                    "flex_wrap": "wrap",
                    "flex_gap": {"size": 40, "unit": "px"},
                    "flex_justify_content": "center",
                    "flex_align_items": "flex-start",
                    "width": {"size": 100, "unit": "%"},
                    "max_width": {"size": 1100, "unit": "px"},
                },
                elements=[
                    inner_container(
                        settings={
                            "width": {"size": 35, "unit": "%"},
                            "min_width": {"size": 280, "unit": "px"},
                            "flex_direction": "column",
                        },
                        elements=[*section_heading("Orquestando la complejidad")],
                    ),
                    inner_container(
                        settings={
                            "width": {"size": 58, "unit": "%"},
                            "min_width": {"size": 300, "unit": "px"},
                            "flex_direction": "column",
                        },
                        elements=[
                            widget("text-editor", {
                                "editor": (
                                    '<div style="max-width:560px;">'
                                    '<p style="font-size:16px; line-height:1.9; color:#334155; margin-bottom:20px; border-left:6px solid #3B82F6; padding-left:24px; font-family:Inter,sans-serif;">'
                                    'Las ciudades, las infraestructuras y los entornos industriales se han convertido en sistemas '
                                    'complejos, a menudo gestionados en silos. <strong>Groupe Vectanor</strong> act\u00faa como una '
                                    'estructura de direcci\u00f3n capaz de alinear experiencias especializadas hacia un objetivo '
                                    'com\u00fan: hacer los sistemas urbanos e industriales m\u00e1s fiables, m\u00e1s eficientes y '
                                    'm\u00e1s sostenibles.'
                                    '</p>'
                                    '<p style="font-size:16px; line-height:1.9; color:#334155; font-family:Inter,sans-serif;">'
                                    'Desde la iluminaci\u00f3n inteligente hasta la movilidad urbana, desde el dise\u00f1o '
                                    'electr\u00f3nico hasta el monitoreo de infraestructuras cr\u00edticas \u2014 nuestras divisiones '
                                    'cubren toda la cadena de valor tecnol\u00f3gica de las ciudades e industrias del ma\u00f1ana.'
                                    '</p>'
                                    '</div>'
                                ),
                                "css_classes": "v-reveal",
                            }),
                        ],
                    ),
                ],
            ),
        ],
    ))

    # KEY FIGURES
    def stat_block_es(number, label, delay=0):
        return inner_container(
            settings={
                "flex_direction": "column",
                "flex_align_items": "center",
                "padding": {"top": "24", "bottom": "24", "left": "28", "right": "28", "unit": "px"},
                "css_classes": "v-reveal",
                "background_background": "classic",
                "background_color": "rgba(255,255,255,0.03)",
                "border_border": "solid",
                "border_width": {"top": "1", "bottom": "1", "left": "1", "right": "1", "unit": "px"},
                "border_color": "rgba(255,255,255,0.06)",
                "border_radius": {"top": "12", "bottom": "12", "left": "12", "right": "12", "unit": "px"},
            },
            elements=[
                widget("heading", {
                    "title": number,
                    "header_size": "h3",
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

    elements.append(container(
        settings={
            "content_width": "boxed",
            "background_background": "gradient",
            "background_color": NEAR_BLACK,
            "background_color_b": DARK_NAVY,
            "background_gradient_angle": {"size": 90, "unit": "deg"},
            "flex_direction": "column",
            "flex_align_items": "center",
            "padding": {"top": "40", "bottom": "40", "left": "40", "right": "40", "unit": "px"},
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
                    stat_block_es("4", "Divisiones especializadas", 0),
                    stat_block_es("18+", "A\u00f1os de experiencia", 100),
                    stat_block_es("850K+", "Dispositivos desplegados", 200),
                    stat_block_es("15", "Pa\u00edses", 300),
                ],
            ),
        ],
    ))

    # DIVISIONS
    def division_card(name, desc, color, link, logo_key, delay, highlights=None):
        card_elems = [
            widget("image", {
                "image": {"url": LOGOS[logo_key], "id": LOGO_IDS[logo_key]},
                "image_size": "full",
                "width": {"size": 140, "unit": "px"},
                "alt": f"{name} logo",
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
                "editor": f'<p style="font-size:15px; line-height:1.75; color:#CBD5E1;">{desc}</p>',
            }),
        ]
        if highlights:
            bullets_html = ''.join(
                f'<li style="font-size:13px;line-height:1.6;color:#CBD5E1;padding:4px 0;display:flex;align-items:center;">'
                f'<span style="display:inline-block;width:6px;height:6px;border-right:2px solid {color};border-top:2px solid {color};transform:rotate(45deg);margin-right:10px;flex-shrink:0;"></span>{h}</li>'
                for h in highlights
            )
            card_elems.append(widget("html", {
                "html": f'<ul style="list-style:none;padding:0;margin:8px 0 4px;">{bullets_html}</ul>',
            }))
        btn_elems = [
            widget("button", {
                "text": "M\u00e1s informaci\u00f3n",
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
                "css_classes": "v-reveal",
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
                "Nuestras divisiones",
                "Cada entidad del grupo es aut\u00f3noma en su mercado, pero integrada en una arquitectura global.",
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
                        "Iluminaci\u00f3n inteligente e infraestructura urbana conectada.",
                        AMBER, "/es/nuestras-divisiones/dimonoff/", "dimonoff", 0,
                        highlights=[
                            "Telegesti\u00f3n municipal a gran escala",
                            "Reducci\u00f3n energ\u00e9tica medible",
                            "Plataforma SaaS multi-sitio",
                        ],
                    ),
                    division_card(
                        "Spatium",
                        "Movilidad inteligente y estacionamiento inteligente.",
                        GREEN, "/es/nuestras-divisiones/spatium/", "spatium", 100,
                        highlights=[
                            "Detecci\u00f3n y orientaci\u00f3n en tiempo real",
                            "Sensores IoT de bajo consumo",
                            "An\u00e1lisis de flujos de movilidad",
                        ],
                    ),
                    division_card(
                        "Amotus",
                        "Design House y catalizador de innovaci\u00f3n industrial.",
                        PURPLE, "/es/nuestras-divisiones/amotus/", "amotus", 200,
                        highlights=[
                            "Dise\u00f1o electr\u00f3nico a medida",
                            "Del prototipo a la certificaci\u00f3n",
                            "Sistemas embebidos industriales",
                        ],
                    ),
                    division_card(
                        "Vigilia",
                        "Monitoreo y vigilancia de infraestructuras cr\u00edticas.",
                        PINK, "/es/nuestras-divisiones/vigilia/", "vigilia", 300,
                        highlights=[
                            "Monitoreo 24/7 de infraestructuras",
                            "Alertas predictivas con IA",
                            "Comunicaci\u00f3n MQTT segura",
                        ],
                    ),
                ],
            ),
        ],
    )
    elements.append(divisions_section)

    # APPROACH — Dark numbered cards
    def value_card_es(title, desc, accent_color, number, delay_class):
        return inner_container(
            settings={
                "background_background": "classic",
                "background_color": MID_DARK,
                "border_border": "solid",
                "border_width": {"top": "3", "bottom": "0", "left": "0", "right": "0", "unit": "px", "isLinked": False},
                "border_color": accent_color,
                "border_radius": {"top": "12", "bottom": "12", "left": "12", "right": "12", "unit": "px"},
                "padding": {"top": "40", "bottom": "40", "left": "30", "right": "30", "unit": "px"},
                "flex_direction": "column",
                "flex_align_items": "flex-start",
                "flex_gap": {"size": 8, "unit": "px"},
                "css_classes": f"v-reveal {delay_class}",
                "position": "relative",
                "custom_css": f"""selector {{ transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94); }}
selector:hover {{ transform: translateY(-8px); box-shadow: 0 20px 60px -15px {accent_color}30; }}""",
            },
            elements=[
                widget("html", {
                    "html": f'<span style="font-size:64px;font-weight:800;color:transparent;-webkit-text-stroke:1px rgba(255,255,255,0.06);position:absolute;top:12px;right:20px;font-family:Montserrat,sans-serif;">{number}</span>',
                }),
                widget("heading", {
                    "title": title,
                    "header_size": "h4",
                    "title_color": WHITE,
                    "typography_typography": "custom",
                    "typography_font_family": "Montserrat",
                    "typography_font_size": {"size": 22, "unit": "px"},
                    "typography_font_weight": "700",
                    "_margin": {"top": "8", "bottom": "5", "left": "0", "right": "0", "unit": "px"},
                }),
                widget("text-editor", {
                    "editor": f'<p style="font-size:15px; line-height:1.8; color:#CBD5E1;">{desc}</p>',
                }),
            ],
        )

    approach = container(
        settings={
            "content_width": "boxed",
            "background_background": "gradient",
            "background_color": NEAR_BLACK,
            "background_color_b": DARK_NAVY,
            "background_gradient_angle": {"size": 145, "unit": "deg"},
            "flex_direction": "column",
            "flex_align_items": "center",
            "padding": {"top": "90", "bottom": "90", "left": "40", "right": "40", "unit": "px"},
            "custom_css": GRAIN_OVERLAY_CSS,
        },
        elements=[
            *section_heading("Nuestro enfoque", dark=True),
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
                    value_card_es(
                        "Interoperabilidad",
                        "Sistemas dise\u00f1ados para comunicarse abiertamente, sin dependencia de un proveedor.",
                        ROYAL_BLUE, "01", "v-reveal",
                    ),
                    value_card_es(
                        "Confiabilidad",
                        "Infraestructura confiable y segura, construida para durar.",
                        "#10B981", "02", "v-reveal-d1",
                    ),
                    value_card_es(
                        "Escalabilidad",
                        "Arquitectura modular que evoluciona sin interrupciones.",
                        PURPLE, "03", "v-reveal-d2",
                    ),
                ],
            ),
        ],
    )
    elements.append(approach)

    # CTA SECTION
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
            "padding": {"top": "80", "bottom": "80", "left": "40", "right": "40", "unit": "px"},
            "custom_css": GRID_PATTERN_CSS,
        },
        elements=[
            widget("heading", {
                "title": "\u00bfListo para estructurar el futuro?",
                "header_size": "h2",
                "align": "center",
                "title_color": WHITE,
                "typography_typography": "custom",
                "typography_font_family": "Montserrat",
                "typography_font_size": {"size": 40, "unit": "px"},
                "typography_font_weight": "700",
                "_margin": {"top": "0", "bottom": "20", "left": "0", "right": "0", "unit": "px"},
                "css_classes": "v-reveal",
            }),
            widget("text-editor", {
                "editor": (
                    '<p style="text-align:center; font-size:16px; color:#CBD5E1; max-width:600px; margin:0 auto; font-family:Inter,sans-serif;">'
                    'Cont\u00e1ctenos para descubrir c\u00f3mo Groupe Vectanor puede acompa\u00f1ar sus proyectos '
                    'de infraestructura y transformaci\u00f3n tecnol\u00f3gica.'
                    '</p>'
                ),
                "css_classes": "v-reveal",
            }),
            inner_container(
                settings={
                    "flex_direction": "row",
                    "flex_justify_content": "center",
                    "flex_align_items": "center",
                    "flex_gap": {"size": 16, "unit": "px"},
                    "_margin": {"top": "32", "bottom": "0", "left": "0", "right": "0", "unit": "px"},
                },
                elements=[
                    widget("button", {
                        "text": "Cont\u00e1ctenos",
                        "link": {"url": "/es/contactenos/", "is_external": False},
                        "align": "center",
                        "background_color": ROYAL_BLUE,
                        "button_text_color": WHITE,
                        "typography_typography": "custom",
                        "typography_font_family": "Montserrat",
                        "typography_font_size": {"size": 14, "unit": "px"},
                        "typography_font_weight": "600",
                        "button_padding": {"top": "18", "bottom": "18", "left": "44", "right": "44", "unit": "px"},
                        "custom_css": CTA_BUTTON_CSS,
                    }),
                    widget("button", {
                        "text": "Nuestras divisiones \u2192",
                        "link": {"url": "/es/nuestras-divisiones/", "is_external": False},
                        "align": "center",
                        "button_text_color": WHITE,
                        "typography_typography": "custom",
                        "typography_font_family": "Montserrat",
                        "typography_font_size": {"size": 14, "unit": "px"},
                        "typography_font_weight": "600",
                        "button_padding": {"top": "18", "bottom": "18", "left": "44", "right": "44", "unit": "px"},
                        "custom_css": """selector .elementor-button {
    background: transparent !important;
    border: 1px solid rgba(255,255,255,0.3) !important;
    border-radius: 8px !important;
    transition: all 0.3s ease;
}
selector .elementor-button:hover {
    border-color: rgba(255,255,255,0.6) !important;
    background: rgba(255,255,255,0.05) !important;
}""",
                    }),
                ],
            ),
            widget("text-editor", {
                "editor": (
                    '<p style="text-align:center; font-size:13px; color:#64748B; margin-top:24px; font-family:Inter,sans-serif; letter-spacing:0.5px;">'
                    'Qu\u00e9bec, Canad\u00e1 \u00b7 18+ a\u00f1os de experiencia \u00b7 15 pa\u00edses'
                    '</p>'
                ),
            }),
        ],
    )
    elements.append(cta)

    return elements


# ═══════════════════════════════════════
# VISION PAGE BUILDERS
# ═══════════════════════════════════════

def build_vision_page_en():
    """English vision page."""
    elements = []

    elements.append(hero_section(
        "Our vision",
        "Giving direction to complex systems",
        full_height=False,
    ))

    # Story
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
            *section_heading("The story of Groupe Vectanor"),
            widget("text-editor", {
                "editor": (
                    '<div style="max-width:800px; margin:0 auto; font-size:17px; line-height:1.9; color:#475569; font-family:Outfit,sans-serif;">'
                    '<p>Groupe Vectanor was born from a simple observation: cities, infrastructure, and industrial '
                    'environments have become complex, fragmented systems, often managed in silos. Yet their '
                    'performance rests on one fundamental thing: the ability to orchestrate flows \u2014 energy, '
                    'data, mobility, security, operations \u2014 coherently and intelligently.</p>'
                    '<p>The name <strong>Vectanor</strong> comes from the concept of a <em>vector</em>: a direction, '
                    'a force, a controlled movement. It embodies the idea that a technology group must not only '
                    'provide tools, but give direction.</p>'
                    '</div>'
                ),
                "css_classes": "v-reveal",
            }),
        ],
    ))

    # Philosophy
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
            *section_heading("Our philosophy", dark=True),
            widget("text-editor", {
                "editor": (
                    '<div style="max-width:800px; margin:0 auto; font-size:17px; line-height:1.9; color:#94A3B8; font-family:Outfit,sans-serif;">'
                    '<p>Groupe Vectanor acts as a strategic parent company, designed to allow each division to focus '
                    'on its area of excellence while benefiting from a shared vision, solid technology governance, '
                    'and common execution capability.</p>'
                    '<p>The group favors a pragmatic approach: proven technologies, mastered integration, and a deep '
                    'understanding of operational constraints in the field.</p>'
                    '</div>'
                ),
                "css_classes": "v-reveal",
            }),
        ],
    ))

    # Quote
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
                    '<p>\u00ab\u00a0The systems that structure our cities and industries must be designed as trust '
                    'infrastructure, capable of evolving without disruption and without unnecessary '
                    'dependency.\u00a0\u00bb</p>'
                    '</blockquote>'
                ),
                "css_classes": "v-reveal",
            }),
        ],
    ))

    return elements


def build_vision_page_es():
    """Spanish vision page."""
    elements = []

    elements.append(hero_section(
        "Nuestra visi\u00f3n",
        "Dar direcci\u00f3n a los sistemas complejos",
        full_height=False,
    ))

    # Story
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
            *section_heading("La historia de Groupe Vectanor"),
            widget("text-editor", {
                "editor": (
                    '<div style="max-width:800px; margin:0 auto; font-size:17px; line-height:1.9; color:#475569; font-family:Outfit,sans-serif;">'
                    '<p>Groupe Vectanor naci\u00f3 de una observaci\u00f3n simple: las ciudades, las infraestructuras y '
                    'los entornos industriales se han convertido en sistemas complejos y fragmentados, a menudo '
                    'gestionados en silos. Sin embargo, su rendimiento descansa en una cosa fundamental: la '
                    'capacidad de orquestar flujos \u2014energ\u00eda, datos, movilidad, seguridad, '
                    'operaciones\u2014 de manera coherente e inteligente.</p>'
                    '<p>El nombre <strong>Vectanor</strong> proviene del concepto de <em>vector</em>: una '
                    'direcci\u00f3n, una fuerza, un movimiento controlado. Encarna la idea de que un grupo '
                    'tecnol\u00f3gico no debe solo proporcionar herramientas, sino dar direcci\u00f3n.</p>'
                    '</div>'
                ),
                "css_classes": "v-reveal",
            }),
        ],
    ))

    # Philosophy
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
            *section_heading("Nuestra filosof\u00eda", dark=True),
            widget("text-editor", {
                "editor": (
                    '<div style="max-width:800px; margin:0 auto; font-size:17px; line-height:1.9; color:#94A3B8; font-family:Outfit,sans-serif;">'
                    '<p>Groupe Vectanor act\u00faa como una empresa matriz estrat\u00e9gica, dise\u00f1ada para '
                    'permitir que cada divisi\u00f3n se concentre en su \u00e1rea de excelencia mientras se '
                    'beneficia de una visi\u00f3n compartida, una gobernanza tecnol\u00f3gica s\u00f3lida y una '
                    'capacidad de ejecuci\u00f3n com\u00fan.</p>'
                    '<p>El grupo privilegia un enfoque pragm\u00e1tico: tecnolog\u00edas probadas, integraci\u00f3n '
                    'controlada y una comprensi\u00f3n profunda de las restricciones operativas en el campo.</p>'
                    '</div>'
                ),
                "css_classes": "v-reveal",
            }),
        ],
    ))

    # Quote
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
                    '<p>\u00ab\u00a0Los sistemas que estructuran nuestras ciudades e industrias deben dise\u00f1arse '
                    'como infraestructura de confianza, capaz de evolucionar sin interrupciones y sin dependencias '
                    'innecesarias.\u00a0\u00bb</p>'
                    '</blockquote>'
                ),
                "css_classes": "v-reveal",
            }),
        ],
    ))

    return elements


# ═══════════════════════════════════════
# DIVISIONS INDEX BUILDERS
# ═══════════════════════════════════════

def build_divisions_index_en():
    """English divisions index page."""
    elements = []

    elements.append(hero_section(
        "Our divisions",
        "An ecosystem of aligned expertise",
        full_height=False,
    ))

    def large_card(div_key, delay=0):
        d = DIVISIONS_EN[div_key]
        card_elems = [
            widget("image", {
                "image": {"url": LOGOS[d["logo_key"]], "id": LOGO_IDS[d["logo_key"]]},
                "image_size": "full",
                "width": {"size": 160, "unit": "px"},
                "alt": f"{d['name']} logo",
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
        btn_elems = [
            widget("button", {
                "text": f"Discover {d['name']} \u2192",
                "link": {"url": f"/en/our-divisions/{div_key}/", "is_external": False},
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
                "text": "Visit website \u2197",
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
                "css_classes": "v-reveal",
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


def build_divisions_index_es():
    """Spanish divisions index page."""
    elements = []

    elements.append(hero_section(
        "Nuestras divisiones",
        "Un ecosistema de experiencias alineadas",
        full_height=False,
    ))

    def large_card(div_key, delay=0):
        d = DIVISIONS_ES[div_key]
        card_elems = [
            widget("image", {
                "image": {"url": LOGOS[d["logo_key"]], "id": LOGO_IDS[d["logo_key"]]},
                "image_size": "full",
                "width": {"size": 160, "unit": "px"},
                "alt": f"{d['name']} logo",
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
        btn_elems = [
            widget("button", {
                "text": f"Descubrir {d['name']} \u2192",
                "link": {"url": f"/es/nuestras-divisiones/{div_key}/", "is_external": False},
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
                "text": "Visitar el sitio \u2197",
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
                "css_classes": "v-reveal",
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
# DIVISION PAGE BUILDERS
# ═══════════════════════════════════════

def build_division_page_en(name, accent, tagline, description, features, logo_key, external_url=None):
    """English division page — mirrors build_division_page() with EN strings."""
    elements = []

    # HERO with division logo
    hero_elems = [
        widget("image", {
            "image": {"url": LOGOS[logo_key], "id": LOGO_IDS[logo_key]},
            "image_size": "full",
            "width": {"size": 180, "unit": "px"},
            "align": "center",
            "alt": f"{name} logo",
            "_margin": {"top": "0", "bottom": "25", "left": "0", "right": "0", "unit": "px"},
            "custom_css": "selector img { filter: brightness(0) invert(1); }",
            "css_classes": "v-reveal",
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
            "css_classes": "v-reveal",
        }),
    ]
    if external_url:
        hero_elems.append(widget("button", {
            "text": f"Visit {external_url.replace('https://','')} \u2197",
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

    # ABOUT
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
            *section_heading(f"About {name}"),
            widget("text-editor", {
                "editor": f'<p style="text-align:center; max-width:800px; margin:0 auto; font-size:18px; line-height:1.9; color:#475569; font-family:Outfit,sans-serif;">{description}</p>',
                "css_classes": "v-reveal",
            }),
        ],
    ))

    # FEATURES
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
                "css_classes": f"v-reveal v-reveal-d{i+1}" if i < 3 else "v-reveal",
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
            *section_heading("Areas of expertise", dark=True),
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

    elements.append(back_to_group_cta_en())
    return elements


def build_division_page_es(name, accent, tagline, description, features, logo_key, external_url=None):
    """Spanish division page — mirrors build_division_page() with ES strings."""
    elements = []

    # HERO with division logo
    hero_elems = [
        widget("image", {
            "image": {"url": LOGOS[logo_key], "id": LOGO_IDS[logo_key]},
            "image_size": "full",
            "width": {"size": 180, "unit": "px"},
            "align": "center",
            "alt": f"{name} logo",
            "_margin": {"top": "0", "bottom": "25", "left": "0", "right": "0", "unit": "px"},
            "custom_css": "selector img { filter: brightness(0) invert(1); }",
            "css_classes": "v-reveal",
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
            "css_classes": "v-reveal",
        }),
    ]
    if external_url:
        hero_elems.append(widget("button", {
            "text": f"Visitar {external_url.replace('https://','')} \u2197",
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

    # ABOUT
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
            *section_heading(f"Acerca de {name}"),
            widget("text-editor", {
                "editor": f'<p style="text-align:center; max-width:800px; margin:0 auto; font-size:18px; line-height:1.9; color:#475569; font-family:Outfit,sans-serif;">{description}</p>',
                "css_classes": "v-reveal",
            }),
        ],
    ))

    # FEATURES
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
                "css_classes": f"v-reveal v-reveal-d{i+1}" if i < 3 else "v-reveal",
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
            *section_heading("\u00c1reas de especializaci\u00f3n", dark=True),
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

    elements.append(back_to_group_cta_es())
    return elements


# ═══════════════════════════════════════
# CONTACT PAGE BUILDERS (raw HTML)
# ═══════════════════════════════════════

def build_contact_page_en():
    """English contact page — returns full raw HTML string (not Elementor elements)."""
    return f"""
<div style="background:{NEAR_BLACK}; min-height:400px; padding:80px 40px; box-sizing:border-box;">
  <div style="max-width:900px; margin:0 auto; display:flex; flex-wrap:wrap; gap:60px; justify-content:center;">

    <!-- Left panel -->
    <div style="flex:0 0 350px; display:flex; flex-direction:column; gap:25px; animation:fadeInLeft 0.8s ease both;">
      <img src="{LOGOS['vectanor']}" alt="Groupe Vectanor" style="width:180px; margin-bottom:10px;">
      <div>
        <h2 style="font-family:Montserrat,sans-serif; font-size:24px; font-weight:700; color:{WHITE}; margin:0 0 8px 0;">Contact us</h2>
        <p style="font-family:Inter,sans-serif; font-size:16px; color:#CBD5E1; margin:0;">Our team is here to answer your questions.</p>
      </div>
      <ul style="list-style:none; margin:0; padding:0; display:flex; flex-direction:column; gap:12px;">
        <li style="display:flex; align-items:center; gap:12px; font-family:Inter,sans-serif; font-size:16px; color:#CBD5E1;">
          <i class="fas fa-map-marker-alt" style="color:{ROYAL_BLUE}; width:20px;"></i>
          410-1015 Wilfrid Pelletier, Qu&eacute;bec, QC, Canada G1W 0C4
        </li>
        <li style="display:flex; align-items:center; gap:12px; font-family:Inter,sans-serif; font-size:16px; color:#CBD5E1;">
          <i class="fas fa-phone" style="color:{ROYAL_BLUE}; width:20px;"></i>
          <a href="tel:4186823636" style="color:#CBD5E1; text-decoration:none;">418-682-3636</a>
        </li>
        <li style="display:flex; align-items:center; gap:12px; font-family:Inter,sans-serif; font-size:16px; color:#CBD5E1;">
          <i class="fas fa-envelope" style="color:{ROYAL_BLUE}; width:20px;"></i>
          <a href="mailto:info@vectanor.com" style="color:#CBD5E1; text-decoration:none;">info@vectanor.com</a>
        </li>
      </ul>
      <p style="font-family:Inter,sans-serif; font-size:16px; line-height:1.8; color:#CBD5E1; margin:0;">
        For inquiries related to a specific division, feel free to contact us. We will direct you to the appropriate team.
      </p>
    </div>

    <!-- Right panel: form -->
    <div style="flex:0 0 450px; background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.08); border-radius:12px; padding:35px; box-sizing:border-box; animation:fadeInRight 0.8s ease both;">
      <h4 style="font-family:Montserrat,sans-serif; font-size:20px; font-weight:600; color:{WHITE}; margin:0 0 20px 0;">Send us a message</h4>
      {EN_CONTACT_FORM_HTML}
    </div>

  </div>
</div>
<style>
@keyframes fadeInLeft {{
  from {{ opacity:0; transform:translateX(-20px); }}
  to   {{ opacity:1; transform:translateX(0); }}
}}
@keyframes fadeInRight {{
  from {{ opacity:0; transform:translateX(20px); }}
  to   {{ opacity:1; transform:translateX(0); }}
}}
</style>
"""


def build_contact_page_es():
    """Spanish contact page — returns full raw HTML string (not Elementor elements)."""
    return f"""
<div style="background:{NEAR_BLACK}; min-height:400px; padding:80px 40px; box-sizing:border-box;">
  <div style="max-width:900px; margin:0 auto; display:flex; flex-wrap:wrap; gap:60px; justify-content:center;">

    <!-- Left panel -->
    <div style="flex:0 0 350px; display:flex; flex-direction:column; gap:25px; animation:fadeInLeft 0.8s ease both;">
      <img src="{LOGOS['vectanor']}" alt="Groupe Vectanor" style="width:180px; margin-bottom:10px;">
      <div>
        <h2 style="font-family:Montserrat,sans-serif; font-size:24px; font-weight:700; color:{WHITE}; margin:0 0 8px 0;">Cont&aacute;ctenos</h2>
        <p style="font-family:Inter,sans-serif; font-size:16px; color:#CBD5E1; margin:0;">Nuestro equipo est&aacute; aqu&iacute; para responder sus preguntas.</p>
      </div>
      <ul style="list-style:none; margin:0; padding:0; display:flex; flex-direction:column; gap:12px;">
        <li style="display:flex; align-items:center; gap:12px; font-family:Inter,sans-serif; font-size:16px; color:#CBD5E1;">
          <i class="fas fa-map-marker-alt" style="color:{ROYAL_BLUE}; width:20px;"></i>
          410-1015 Wilfrid Pelletier, Qu&eacute;bec, QC, Canad&aacute; G1W 0C4
        </li>
        <li style="display:flex; align-items:center; gap:12px; font-family:Inter,sans-serif; font-size:16px; color:#CBD5E1;">
          <i class="fas fa-phone" style="color:{ROYAL_BLUE}; width:20px;"></i>
          <a href="tel:4186823636" style="color:#CBD5E1; text-decoration:none;">418-682-3636</a>
        </li>
        <li style="display:flex; align-items:center; gap:12px; font-family:Inter,sans-serif; font-size:16px; color:#CBD5E1;">
          <i class="fas fa-envelope" style="color:{ROYAL_BLUE}; width:20px;"></i>
          <a href="mailto:info@vectanor.com" style="color:#CBD5E1; text-decoration:none;">info@vectanor.com</a>
        </li>
      </ul>
      <p style="font-family:Inter,sans-serif; font-size:16px; line-height:1.8; color:#CBD5E1; margin:0;">
        Para consultas relacionadas con una divisi&oacute;n espec&iacute;fica, no dude en contactarnos. Lo dirigiremos al equipo adecuado.
      </p>
    </div>

    <!-- Right panel: form -->
    <div style="flex:0 0 450px; background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.08); border-radius:12px; padding:35px; box-sizing:border-box; animation:fadeInRight 0.8s ease both;">
      <h4 style="font-family:Montserrat,sans-serif; font-size:20px; font-weight:600; color:{WHITE}; margin:0 0 20px 0;">Env&iacute;enos un mensaje</h4>
      {ES_CONTACT_FORM_HTML}
    </div>

  </div>
</div>
<style>
@keyframes fadeInLeft {{
  from {{ opacity:0; transform:translateX(-20px); }}
  to   {{ opacity:1; transform:translateX(0); }}
}}
@keyframes fadeInRight {{
  from {{ opacity:0; transform:translateX(20px); }}
  to   {{ opacity:1; transform:translateX(0); }}
}}
</style>
"""


# ═══════════════════════════════════════
# MAIN ENTRY POINT
# ═══════════════════════════════════════

if __name__ == "__main__":
    lang = sys.argv[1].lower() if len(sys.argv) > 1 else "both"

    if lang not in ("en", "es", "both"):
        print(f"ERROR: Unknown language '{lang}'. Use: en | es | both")
        sys.exit(1)

    # Validate all IDs are filled in
    if lang in ("en", "both"):
        missing = [k for k, v in EN_PAGES.items() if v is None]
        if missing:
            print(f"ERROR: EN page IDs not filled in for: {', '.join(missing)}")
            print("Fill in the EN_PAGES dict at the top of this file after creating WP Admin stubs.")
            sys.exit(1)

    if lang in ("es", "both"):
        missing = [k for k, v in ES_PAGES.items() if v is None]
        if missing:
            print(f"ERROR: ES page IDs not filled in for: {', '.join(missing)}")
            print("Fill in the ES_PAGES dict at the top of this file after creating WP Admin stubs.")
            sys.exit(1)

    def wrap_page(lang_code, page_key, page_id, elements):
        """Wrap page elements with font loader, SEO meta, header, and footer."""
        elements.insert(0, site_header(lang_code, page_key))
        elements.insert(0, seo_head(page_key, lang_code))
        elements.insert(0, font_loader())
        elements.append(site_footer(lang_code))
        push_page(page_id, elements)

    if lang in ("en", "both"):
        print("\n" + "=" * 50)
        print("Pushing English pages...")
        print("=" * 50)

        print("\n[1/8] EN Homepage...")
        wrap_page("en", "homepage", EN_PAGES["homepage"], build_homepage_en())

        print("\n[2/8] EN Vision page...")
        wrap_page("en", "vision", EN_PAGES["vision"], build_vision_page_en())

        print("\n[3/8] EN Divisions index...")
        wrap_page("en", "divisions", EN_PAGES["divisions"], build_divisions_index_en())

        print("\n[4/8] EN Dimonoff...")
        wrap_page("en", "dimonoff", EN_PAGES["dimonoff"], build_division_page_en(**{k: DIVISIONS_EN["dimonoff"][k] for k in ["name", "accent", "tagline", "description", "features", "logo_key", "external_url"]}))

        print("\n[5/8] EN Spatium...")
        wrap_page("en", "spatium", EN_PAGES["spatium"], build_division_page_en(**{k: DIVISIONS_EN["spatium"][k] for k in ["name", "accent", "tagline", "description", "features", "logo_key", "external_url"]}))

        print("\n[6/8] EN Amotus...")
        wrap_page("en", "amotus", EN_PAGES["amotus"], build_division_page_en(**{k: DIVISIONS_EN["amotus"][k] for k in ["name", "accent", "tagline", "description", "features", "logo_key", "external_url"]}))

        print("\n[7/8] EN Vigilia...")
        wrap_page("en", "vigilia", EN_PAGES["vigilia"], build_division_page_en(**{k: DIVISIONS_EN["vigilia"][k] for k in ["name", "accent", "tagline", "description", "features", "logo_key", "external_url"]}))

        print("\n[8/8] EN Contact (raw HTML)...")
        push_raw_html(EN_PAGES["contact"], site_header_html("en", "contact") + build_contact_page_en() + site_footer_html("en"))

    if lang in ("es", "both"):
        print("\n" + "=" * 50)
        print("Pushing Spanish pages...")
        print("=" * 50)

        print("\n[1/8] ES Homepage...")
        wrap_page("es", "homepage", ES_PAGES["homepage"], build_homepage_es())

        print("\n[2/8] ES Vision page...")
        wrap_page("es", "vision", ES_PAGES["vision"], build_vision_page_es())

        print("\n[3/8] ES Divisions index...")
        wrap_page("es", "divisions", ES_PAGES["divisions"], build_divisions_index_es())

        print("\n[4/8] ES Dimonoff...")
        wrap_page("es", "dimonoff", ES_PAGES["dimonoff"], build_division_page_es(**{k: DIVISIONS_ES["dimonoff"][k] for k in ["name", "accent", "tagline", "description", "features", "logo_key", "external_url"]}))

        print("\n[5/8] ES Spatium...")
        wrap_page("es", "spatium", ES_PAGES["spatium"], build_division_page_es(**{k: DIVISIONS_ES["spatium"][k] for k in ["name", "accent", "tagline", "description", "features", "logo_key", "external_url"]}))

        print("\n[6/8] ES Amotus...")
        wrap_page("es", "amotus", ES_PAGES["amotus"], build_division_page_es(**{k: DIVISIONS_ES["amotus"][k] for k in ["name", "accent", "tagline", "description", "features", "logo_key", "external_url"]}))

        print("\n[7/8] ES Vigilia...")
        wrap_page("es", "vigilia", ES_PAGES["vigilia"], build_division_page_es(**{k: DIVISIONS_ES["vigilia"][k] for k in ["name", "accent", "tagline", "description", "features", "logo_key", "external_url"]}))

        print("\n[8/8] ES Contact (raw HTML)...")
        push_raw_html(ES_PAGES["contact"], site_header_html("es", "contact") + build_contact_page_es() + site_footer_html("es"))

    flush_elementor_cache()
    print("\n" + "=" * 50)
    print("DONE!")
    print("=" * 50)
