<?php
/**
 * Plugin Name: Spatium Design Upgrade & Homepage Sections
 * Description: Modernizes spatium-iot.com design + adds testimonials, stats, logos, ROI calculator
 * Version: 1.0.0
 * Author: Dimonoff
 */

if (!defined("ABSPATH")) exit;

// === HELPER: language detection ===
function spatium_upgrade_lang() {
    if (function_exists("pll_current_language")) {
        $l = pll_current_language("slug");
        if ($l) return $l;
    }
    $uri = isset($_SERVER["REQUEST_URI"]) ? $_SERVER["REQUEST_URI"] : "";
    if (strpos($uri, "/fr/") !== false) return "fr";
    if (strpos($uri, "/es/") !== false) return "es";
    return "en";
}

// === SECTION 1: CSS Design Modernization ===
add_action("wp_head", "spatium_design_css", 99);
function spatium_design_css() {
    $q = chr(34);
    echo "<link rel=" . $q . "preconnect" . $q . " href=" . $q . "https://fonts.googleapis.com" . $q . ">" . chr(10);
    echo "<link rel=" . $q . "preconnect" . $q . " href=" . $q . "https://fonts.gstatic.com" . $q . " crossorigin>" . chr(10);
    echo "<link rel=" . $q . "stylesheet" . $q . " href=" . $q . "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=DM+Sans:wght@500;700&display=swap" . $q . ">" . chr(10);
    echo "<style id=" . $q . "spatium-design-upgrade" . $q . ">" . chr(10);
    ?>
/* === Spatium Design Upgrade v1.0 === */

/* -- Design Tokens -- */
:root {
  --sp-blue: #0052d4;
  --sp-blue-hover: #003da0;
  --sp-cyan: #65c7f7;
  --sp-light-cyan: #9cecfb;
  --sp-purple: #4c2cab;
  --sp-bg: #f8f9fc;
  --sp-surface: #ffffff;
  --sp-text: #1a1f2e;
  --sp-text-muted: #5a6478;
  --sp-border: #d0d7e2;
  --sp-success: #0fa958;
  --sp-gradient: linear-gradient(135deg, #0052d4 0%, #65c7f7 60%, #9cecfb 100%);
  --sp-shadow-md: 0 4px 16px rgba(0, 30, 80, 0.08);
  --sp-shadow-lg: 0 12px 40px rgba(0, 30, 80, 0.12);
  --sp-radius: 1rem;
  --sp-font-body: 'Inter', 'Helvetica Neue', sans-serif;
  --sp-font-display: 'DM Sans', 'Arial Black', sans-serif;
}

/* -- Global Font Upgrade -- */
body,
.elementor-widget-text-editor,
.elementor-widget-heading .elementor-heading-title {
  font-family: var(--sp-font-body) !important;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

h1, h2, h3,
.elementor-heading-title {
  font-family: var(--sp-font-display) !important;
  letter-spacing: -0.02em;
  line-height: 1.15;
}

/* -- Button Modernization -- */
.elementor-button,
a.elementor-button,
.elementor-widget-button .elementor-button {
  font-family: var(--sp-font-body) !important;
  font-weight: 600 !important;
  border-radius: 999px !important;
  padding: 14px 32px !important;
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1) !important;
  box-shadow: 0 2px 8px rgba(0, 82, 212, 0.2) !important;
  text-transform: none !important;
  letter-spacing: 0 !important;
}

.elementor-button:hover {
  transform: translateY(-1px) !important;
  box-shadow: 0 6px 20px rgba(0, 82, 212, 0.35) !important;
}

/* -- Card Style Enhancement -- */
.elementor-widget-icon-box .elementor-icon-box-wrapper,
.elementor-widget-image-box .elementor-image-box-wrapper {
  background: var(--sp-surface);
  border: 1px solid var(--sp-border);
  border-radius: var(--sp-radius);
  padding: 28px;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  box-shadow: var(--sp-shadow-md);
}

.elementor-widget-icon-box .elementor-icon-box-wrapper:hover,
.elementor-widget-image-box .elementor-image-box-wrapper:hover {
  transform: translateY(-4px);
  box-shadow: var(--sp-shadow-lg);
  border-color: rgba(0, 82, 212, 0.2);
}

/* -- Section Labels (new pattern) -- */
.sp-section-label {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 0.8rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--sp-blue);
  background: rgba(0, 82, 212, 0.08);
  padding: 6px 14px;
  border-radius: 999px;
  margin-bottom: 16px;
}

/* -- Gradient Text -- */
.sp-gradient-text {
  background: var(--sp-gradient);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

/* -- Fade-in Animation -- */
@keyframes sp-fade-up {
  from { opacity: 0; transform: translateY(24px); }
  to { opacity: 1; transform: translateY(0); }
}

.sp-fade-in {
  animation: sp-fade-up 0.6s cubic-bezier(0.16, 1, 0.3, 1) both;
}

/* -- Smooth scroll -- */
html { scroll-behavior: smooth; }

/* ===========================
   INJECTED SECTIONS STYLES
   =========================== */

/* -- Stats Section -- */
.sp-stats {
  padding: 60px 0;
  background: var(--sp-bg);
}

.sp-stats-grid {
  max-width: 1100px;
  margin: 0 auto;
  padding: 0 20px;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
}

.sp-stat-card {
  background: var(--sp-surface);
  border: 1px solid var(--sp-border);
  border-radius: var(--sp-radius);
  padding: 32px 24px;
  text-align: center;
  box-shadow: var(--sp-shadow-md);
  transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.3s;
}

.sp-stat-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--sp-shadow-lg);
}

.sp-stat-value {
  font-family: var(--sp-font-display);
  font-size: 2.5rem;
  font-weight: 700;
  color: var(--sp-blue);
  line-height: 1.1;
  margin-bottom: 8px;
}

.sp-stat-label {
  font-size: 0.9rem;
  color: var(--sp-text-muted);
  font-weight: 500;
}

/* -- Testimonials Section -- */
.sp-testimonials {
  padding: 80px 0;
  background: white;
  overflow: hidden;
}

.sp-testimonials-header {
  text-align: center;
  max-width: 600px;
  margin: 0 auto 48px;
  padding: 0 20px;
}

.sp-testimonials-header h2 {
  font-family: var(--sp-font-display);
  font-size: clamp(1.75rem, 3vw, 2.5rem);
  color: var(--sp-text);
  margin-bottom: 8px;
}

.sp-testimonials-grid {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 24px;
}

.sp-testimonial-card {
  background: var(--sp-surface);
  border: 1px solid var(--sp-border);
  border-radius: var(--sp-radius);
  padding: 32px;
  display: flex;
  flex-direction: column;
  gap: 20px;
  box-shadow: var(--sp-shadow-md);
  transition: transform 0.3s, box-shadow 0.3s;
}

.sp-testimonial-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--sp-shadow-lg);
}

.sp-testimonial-text {
  font-size: 0.95rem;
  line-height: 1.7;
  color: var(--sp-text);
  font-style: italic;
}

.sp-testimonial-author {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-top: auto;
}

.sp-testimonial-avatar {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: var(--sp-gradient);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 0.85rem;
  flex-shrink: 0;
}

.sp-testimonial-name {
  font-weight: 700;
  font-size: 0.9rem;
  color: var(--sp-text);
}

.sp-testimonial-role {
  font-size: 0.8rem;
  color: var(--sp-text-muted);
}

/* -- Logos Section -- */
.sp-logos {
  padding: 48px 0;
  background: var(--sp-bg);
  overflow: hidden;
}

.sp-logos-label {
  text-align: center;
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--sp-text-muted);
  text-transform: uppercase;
  letter-spacing: 0.06em;
  margin-bottom: 28px;
}

.sp-logos-track {
  display: flex;
  gap: 48px;
  align-items: center;
  animation: sp-scroll-logos 30s linear infinite;
  width: max-content;
}

.sp-logos-track img {
  height: 32px;
  width: auto;
  opacity: 0.55;
  filter: grayscale(100%);
  transition: opacity 0.3s, filter 0.3s;
}

.sp-logos-track img:hover {
  opacity: 1;
  filter: grayscale(0%);
}

@keyframes sp-scroll-logos {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}

/* -- ROI Calculator -- */
.sp-roi {
  padding: 80px 0;
  background: white;
}

.sp-roi-header {
  text-align: center;
  max-width: 640px;
  margin: 0 auto 48px;
  padding: 0 20px;
}

.sp-roi-header h2 {
  font-family: var(--sp-font-display);
  font-size: clamp(1.75rem, 3vw, 2.5rem);
  color: var(--sp-text);
}

.sp-roi-header p {
  color: var(--sp-text-muted);
  margin-top: 12px;
}

.sp-roi-calc {
  max-width: 1000px;
  margin: 0 auto;
  padding: 0 20px;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 40px;
  align-items: start;
}

.sp-roi-inputs {
  display: flex;
  flex-direction: column;
  gap: 28px;
}

.sp-roi-field label {
  display: flex;
  justify-content: space-between;
  font-weight: 600;
  font-size: 0.9rem;
  color: var(--sp-text);
  margin-bottom: 10px;
}

.sp-roi-field label span {
  color: var(--sp-blue);
  font-family: var(--sp-font-display);
}

.sp-roi-field input[type=range] {
  width: 100%;
  height: 6px;
  border-radius: 3px;
  background: #e0e5ed;
  outline: none;
  -webkit-appearance: none;
  appearance: none;
}

.sp-roi-field input[type=range]::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background: var(--sp-blue);
  cursor: pointer;
  box-shadow: 0 2px 8px rgba(0, 82, 212, 0.3);
  transition: transform 0.2s;
}

.sp-roi-field input[type=range]::-webkit-slider-thumb:hover {
  transform: scale(1.15);
}

.sp-roi-results {
  background: linear-gradient(135deg, #0a3d8f 0%, #1a6bb5 55%, #2e8ec4 100%);
  border-radius: var(--sp-radius);
  padding: 36px;
  color: white;
}

.sp-roi-results h3 {
  font-family: var(--sp-font-display);
  font-size: 1.1rem;
  opacity: 0.9;
  margin-bottom: 24px;
}

.sp-roi-hero-value {
  font-family: var(--sp-font-display);
  font-size: 3rem;
  font-weight: 700;
  margin-bottom: 4px;
}

.sp-roi-hero-label {
  font-size: 0.85rem;
  opacity: 0.75;
  margin-bottom: 28px;
}

.sp-roi-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
  margin-bottom: 20px;
}

.sp-roi-item {
  background: rgba(255, 255, 255, 0.12);
  border-radius: 12px;
  padding: 16px;
}

.sp-roi-item-label {
  font-size: 0.8rem;
  opacity: 0.75;
  margin-bottom: 6px;
}

.sp-roi-item-value {
  font-family: var(--sp-font-display);
  font-size: 1.3rem;
  font-weight: 700;
}

.sp-roi-footnote {
  font-size: 0.75rem;
  opacity: 0.55;
  margin-top: 16px;
  line-height: 1.5;
}

/* -- CTA Section -- */
.sp-cta {
  padding: 80px 0;
  background: linear-gradient(135deg, #0a3d8f 0%, #1a6bb5 55%, #2e8ec4 100%);
  text-align: center;
  color: white;
}

.sp-cta h2 {
  font-family: var(--sp-font-display);
  font-size: clamp(1.75rem, 3vw, 2.25rem);
  margin-bottom: 16px;
}

.sp-cta p {
  opacity: 0.85;
  max-width: 520px;
  margin: 0 auto 28px;
}

.sp-cta-btn {
  display: inline-block;
  background: white;
  color: var(--sp-blue);
  font-weight: 700;
  font-family: var(--sp-font-body);
  padding: 16px 36px;
  border-radius: 999px;
  text-decoration: none;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}

.sp-cta-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 28px rgba(0, 0, 0, 0.2);
  color: var(--sp-blue);
}

/* -- Responsive -- */
@media (max-width: 768px) {
  .sp-stats-grid { grid-template-columns: repeat(2, 1fr); }
  .sp-roi-calc { grid-template-columns: 1fr; }
  .sp-testimonials-grid { grid-template-columns: 1fr; }
}

@media (max-width: 480px) {
  .sp-stats-grid { grid-template-columns: 1fr; }
  .sp-roi-grid { grid-template-columns: 1fr; }
}
<?php
    echo chr(10) . "</style>" . chr(10);
}


// === SECTION 2: Homepage Content Injections (stats, testimonials, logos, ROI, CTA) ===
add_action("wp_footer", "spatium_homepage_sections", 95);
function spatium_homepage_sections() {
    // Only on homepage
    if (!is_front_page() && !is_page(array(10, 259, 260))) return;

    $lang = spatium_upgrade_lang();
    $q = chr(34);

    // --- STATS SECTION ---
    $stats = array(
        "en" => array(
            array("Up to 15%", "Average revenue increase"),
            array("10-25%", "Revenue leakage detected"),
            array("<4 weeks", "Time to deployment"),
            array("0", "Hardware replacements needed"),
        ),
        "fr" => array(
            array("Jusqu" . chr(39) . "a 15 %", "Augmentation moyenne des revenus"),
            array("10-25 %", "Fuite de revenus detectee"),
            array("<4 semaines", "Delai de deploiement"),
            array("0", "Remplacement materiel requis"),
        ),
        "es" => array(
            array("Hasta 15%", "Aumento promedio de ingresos"),
            array("10-25%", "Fuga de ingresos detectada"),
            array("<4 semanas", "Tiempo de implementacion"),
            array("0", "Reemplazos de hardware necesarios"),
        ),
    );

    $s = isset($stats[$lang]) ? $stats[$lang] : $stats["en"];

    echo "<section class=" . $q . "sp-stats" . $q . ">" . chr(10);
    echo "  <div class=" . $q . "sp-stats-grid" . $q . ">" . chr(10);
    foreach ($s as $item) {
        echo "    <div class=" . $q . "sp-stat-card" . $q . ">" . chr(10);
        echo "      <div class=" . $q . "sp-stat-value" . $q . ">" . esc_html($item[0]) . "</div>" . chr(10);
        echo "      <div class=" . $q . "sp-stat-label" . $q . ">" . esc_html($item[1]) . "</div>" . chr(10);
        echo "    </div>" . chr(10);
    }
    echo "  </div>" . chr(10);
    echo "</section>" . chr(10);

    // --- TESTIMONIALS SECTION ---
    $test_title = array(
        "en" => "What our clients say",
        "fr" => "Ce que nos clients disent",
        "es" => "Lo que dicen nuestros clientes",
    );
    $test_label = array(
        "en" => "They trust us",
        "fr" => "Ils nous font confiance",
        "es" => "Confian en nosotros",
    );

    // Testimonials data — from prototype
    $testimonials = array(
        array(
            "text" => array(
                "en" => "Before Spatium, our parking operations relied heavily on manual tracking and reactive oversight. Today, we reduced wait times, improved valet efficiency, and strengthened oversight of unauthorized parking.",
                "fr" => "Avant Spatium, nos operations de stationnement reposaient sur un suivi manuel et une supervision reactive. Aujourd" . chr(39) . "hui, nous avons reduit les temps d" . chr(39) . "attente et ameliore l" . chr(39) . "efficacite du service voiturier.",
                "es" => "Antes de Spatium, nuestras operaciones de estacionamiento dependian del seguimiento manual. Hoy, hemos reducido los tiempos de espera y mejorado la eficiencia del servicio de valet.",
            ),
            "name" => "Andrew Weir",
            "role" => array(
                "en" => "Director of Operations, Crystal Lodge",
                "fr" => "Directeur des operations, Crystal Lodge",
                "es" => "Director de Operaciones, Crystal Lodge",
            ),
            "initials" => "AW",
        ),
        array(
            "text" => array(
                "en" => "Spatium gave us a level of visibility over our parking operations at Royalmount that we simply didn" . chr(39) . "t have before. Revenue leakage was quickly identified and addressed.",
                "fr" => "Spatium nous a donne un niveau de visibilite sur nos operations de stationnement au Royalmount que nous n" . chr(39) . "avions tout simplement pas avant. Les fuites de revenus ont ete rapidement identifiees.",
                "es" => "Spatium nos dio un nivel de visibilidad sobre nuestras operaciones de estacionamiento en Royalmount que simplemente no teniamos antes.",
            ),
            "name" => "Francis Vermette",
            "role" => array(
                "en" => "General Manager, Carbonleo, Royalmount",
                "fr" => "Directeur general, Carbonleo, Royalmount",
                "es" => "Gerente General, Carbonleo, Royalmount",
            ),
            "initials" => "FV",
        ),
        array(
            "text" => array(
                "en" => "For Espace Montmorency, Spatium delivered real-time occupancy intelligence that directly improved how we guide visitors and manage peak periods.",
                "fr" => "Pour l" . chr(39) . "Espace Montmorency, Spatium a fourni une intelligence d" . chr(39) . "occupation en temps reel qui a directement ameliore la gestion des visiteurs en periode de pointe.",
                "es" => "Para Espace Montmorency, Spatium proporciono inteligencia de ocupacion en tiempo real que mejoro directamente como guiamos a los visitantes.",
            ),
            "name" => "Ashindev Bohdee",
            "role" => array(
                "en" => "Parking Manager, Alcovi Capital, Espace Montmorency",
                "fr" => "Gestionnaire de stationnement, Alcovi Capital, Espace Montmorency",
                "es" => "Gerente de Estacionamiento, Alcovi Capital, Espace Montmorency",
            ),
            "initials" => "AB",
        ),
        array(
            "text" => array(
                "en" => "Spatium has been a key partner in modernizing Montreal" . chr(39) . "s parking operations. The platform" . chr(39) . "s ability to unify data across our network has meaningfully improved enforcement efficiency.",
                "fr" => "Spatium a ete un partenaire cle dans la modernisation des operations de stationnement de Montreal. La capacite de la plateforme a unifier les donnees a significativement ameliore l" . chr(39) . "efficacite de l" . chr(39) . "application.",
                "es" => "Spatium ha sido un socio clave en la modernizacion de las operaciones de estacionamiento de Montreal. La capacidad de la plataforma para unificar datos ha mejorado significativamente la eficiencia.",
            ),
            "name" => "Nicolas Fillion",
            "role" => array(
                "en" => "CTO, Agence de Mobilite Durable de Montreal",
                "fr" => "DT, Agence de mobilite durable de Montreal",
                "es" => "CTO, Agence de Mobilite Durable de Montreal",
            ),
            "initials" => "NF",
        ),
    );

    $tl = isset($test_label[$lang]) ? $test_label[$lang] : $test_label["en"];
    $tt = isset($test_title[$lang]) ? $test_title[$lang] : $test_title["en"];

    echo "<section class=" . $q . "sp-testimonials" . $q . ">" . chr(10);
    echo "  <div class=" . $q . "sp-testimonials-header" . $q . ">" . chr(10);
    echo "    <span class=" . $q . "sp-section-label" . $q . ">" . esc_html($tl) . "</span>" . chr(10);
    echo "    <h2>" . esc_html($tt) . "</h2>" . chr(10);
    echo "  </div>" . chr(10);
    echo "  <div class=" . $q . "sp-testimonials-grid" . $q . ">" . chr(10);

    foreach ($testimonials as $t) {
        $txt = isset($t["text"][$lang]) ? $t["text"][$lang] : $t["text"]["en"];
        $role = isset($t["role"][$lang]) ? $t["role"][$lang] : $t["role"]["en"];
        echo "    <article class=" . $q . "sp-testimonial-card" . $q . ">" . chr(10);
        echo "      <p class=" . $q . "sp-testimonial-text" . $q . ">" . chr(34) . esc_html($txt) . chr(34) . "</p>" . chr(10);
        echo "      <div class=" . $q . "sp-testimonial-author" . $q . ">" . chr(10);
        echo "        <div class=" . $q . "sp-testimonial-avatar" . $q . ">" . esc_html($t["initials"]) . "</div>" . chr(10);
        echo "        <div>" . chr(10);
        echo "          <div class=" . $q . "sp-testimonial-name" . $q . ">" . esc_html($t["name"]) . "</div>" . chr(10);
        echo "          <div class=" . $q . "sp-testimonial-role" . $q . ">" . esc_html($role) . "</div>" . chr(10);
        echo "        </div>" . chr(10);
        echo "      </div>" . chr(10);
        echo "    </article>" . chr(10);
    }

    echo "  </div>" . chr(10);
    echo "</section>" . chr(10);

    // --- LOGOS SECTION ---
    $logos_label = array(
        "en" => "Integrates seamlessly with leading parking systems",
        "fr" => "S" . chr(39) . "integre parfaitement aux systemes de stationnement existants",
        "es" => "Se integra perfectamente con los sistemas de estacionamiento existentes",
    );
    $ll = isset($logos_label[$lang]) ? $logos_label[$lang] : $logos_label["en"];

    // Logo names (we use text-based logos since we cannot upload images via mu-plugin)
    $logos = array("Flowbird", "PayByPhone", "T2 Systems", "ParkMobile", "Milesight", "Urbiotica", "Passport", "JustPark", "Arrive", "Parquery", "ParkNet", "Process");

    echo "<section class=" . $q . "sp-logos" . $q . ">" . chr(10);
    echo "  <p class=" . $q . "sp-logos-label" . $q . ">" . esc_html($ll) . "</p>" . chr(10);
    echo "  <div style=" . $q . "overflow:hidden;" . $q . ">" . chr(10);
    echo "    <div class=" . $q . "sp-logos-track" . $q . ">" . chr(10);
    // Double the logos for seamless loop
    for ($loop = 0; $loop < 2; $loop++) {
        foreach ($logos as $logo) {
            echo "      <span style=" . $q . "font-family:var(--sp-font-display);font-size:1.1rem;font-weight:700;color:var(--sp-text-muted);white-space:nowrap;opacity:0.5;user-select:none;" . $q . ">" . esc_html($logo) . "</span>" . chr(10);
        }
    }
    echo "    </div>" . chr(10);
    echo "  </div>" . chr(10);
    echo "</section>" . chr(10);

    // --- ROI CALCULATOR ---
    $roi_title = array(
        "en" => "Estimate your revenue recovery",
        "fr" => "Estimez votre recuperation de revenus",
        "es" => "Estime su recuperacion de ingresos",
    );
    $roi_label = array(
        "en" => "ROI Calculator",
        "fr" => "Calculatrice ROI",
        "es" => "Calculadora ROI",
    );
    $roi_desc = array(
        "en" => "Adjust the sliders to match your parking operation and see the projected annual impact.",
        "fr" => "Ajustez les curseurs selon votre operation de stationnement pour voir l" . chr(39) . "impact annuel projete.",
        "es" => "Ajuste los controles segun su operacion de estacionamiento para ver el impacto anual proyectado.",
    );
    $roi_fields = array(
        "en" => array("Number of Parking Spaces", "Avg. Daily Revenue per Space", "Average Occupancy Rate"),
        "fr" => array("Nombre de places", "Revenu quotidien moyen par place", "Taux d" . chr(39) . "occupation moyen"),
        "es" => array("Numero de espacios", "Ingreso diario promedio por espacio", "Tasa de ocupacion promedio"),
    );
    $roi_results_labels = array(
        "en" => array("Projected Annual Impact", "Revenue Recovered", "from leakage detection", "Current Annual Revenue", "Occupancy Uplift", "Total Uplift", "Effective ROI"),
        "fr" => array("Impact annuel projete", "Revenus recuperes", "par detection de fuites", "Revenus annuels actuels", "Gain d" . chr(39) . "occupation", "Gain total", "ROI effectif"),
        "es" => array("Impacto anual proyectado", "Ingresos recuperados", "por deteccion de fugas", "Ingresos anuales actuales", "Ganancia de ocupacion", "Ganancia total", "ROI efectivo"),
    );
    $roi_footnote = array(
        "en" => "Based on industry averages: ~15% revenue leakage detected, ~6% occupancy improvement. Actual results vary by facility.",
        "fr" => "Base sur les moyennes de l" . chr(39) . "industrie : ~15 % de fuite de revenus detectee, ~6 % d" . chr(39) . "amelioration d" . chr(39) . "occupation. Les resultats varient selon l" . chr(39) . "installation.",
        "es" => "Basado en promedios de la industria: ~15% de fuga de ingresos detectada, ~6% de mejora de ocupacion. Los resultados varian segun la instalacion.",
    );

    $rt = isset($roi_title[$lang]) ? $roi_title[$lang] : $roi_title["en"];
    $rl = isset($roi_label[$lang]) ? $roi_label[$lang] : $roi_label["en"];
    $rd = isset($roi_desc[$lang]) ? $roi_desc[$lang] : $roi_desc["en"];
    $rf = isset($roi_fields[$lang]) ? $roi_fields[$lang] : $roi_fields["en"];
    $rr = isset($roi_results_labels[$lang]) ? $roi_results_labels[$lang] : $roi_results_labels["en"];
    $rfn = isset($roi_footnote[$lang]) ? $roi_footnote[$lang] : $roi_footnote["en"];

    echo "<section class=" . $q . "sp-roi" . $q . " id=" . $q . "roi-calculator" . $q . ">" . chr(10);
    echo "  <div class=" . $q . "sp-roi-header" . $q . ">" . chr(10);
    echo "    <span class=" . $q . "sp-section-label" . $q . ">" . esc_html($rl) . "</span>" . chr(10);
    echo "    <h2>" . esc_html($rt) . "</h2>" . chr(10);
    echo "    <p>" . esc_html($rd) . "</p>" . chr(10);
    echo "  </div>" . chr(10);
    echo "  <div class=" . $q . "sp-roi-calc" . $q . ">" . chr(10);

    // Inputs
    echo "    <div class=" . $q . "sp-roi-inputs" . $q . ">" . chr(10);
    echo "      <div class=" . $q . "sp-roi-field" . $q . "><label>" . esc_html($rf[0]) . " <span id=" . $q . "spRoiSpacesVal" . $q . ">500</span></label><input type=" . $q . "range" . $q . " id=" . $q . "spRoiSpaces" . $q . " min=" . $q . "50" . $q . " max=" . $q . "10000" . $q . " step=" . $q . "10" . $q . " value=" . $q . "500" . $q . "></div>" . chr(10);
    echo "      <div class=" . $q . "sp-roi-field" . $q . "><label>" . esc_html($rf[1]) . " <span id=" . $q . "spRoiRateVal" . $q . ">$12</span></label><input type=" . $q . "range" . $q . " id=" . $q . "spRoiRate" . $q . " min=" . $q . "1" . $q . " max=" . $q . "100" . $q . " step=" . $q . "1" . $q . " value=" . $q . "12" . $q . "></div>" . chr(10);
    echo "      <div class=" . $q . "sp-roi-field" . $q . "><label>" . esc_html($rf[2]) . " <span id=" . $q . "spRoiOccVal" . $q . ">60%</span></label><input type=" . $q . "range" . $q . " id=" . $q . "spRoiOcc" . $q . " min=" . $q . "20" . $q . " max=" . $q . "100" . $q . " step=" . $q . "1" . $q . " value=" . $q . "60" . $q . "></div>" . chr(10);
    echo "    </div>" . chr(10);

    // Results
    echo "    <div class=" . $q . "sp-roi-results" . $q . ">" . chr(10);
    echo "      <h3>" . esc_html($rr[0]) . "</h3>" . chr(10);
    echo "      <div class=" . $q . "sp-roi-hero-value" . $q . " id=" . $q . "spRoiRecovered" . $q . ">$197,100</div>" . chr(10);
    echo "      <div class=" . $q . "sp-roi-hero-label" . $q . ">" . esc_html($rr[2]) . "</div>" . chr(10);
    echo "      <div class=" . $q . "sp-roi-grid" . $q . ">" . chr(10);
    echo "        <div class=" . $q . "sp-roi-item" . $q . "><div class=" . $q . "sp-roi-item-label" . $q . ">" . esc_html($rr[3]) . "</div><div class=" . $q . "sp-roi-item-value" . $q . " id=" . $q . "spRoiCurrent" . $q . ">$1,314,000</div></div>" . chr(10);
    echo "        <div class=" . $q . "sp-roi-item" . $q . "><div class=" . $q . "sp-roi-item-label" . $q . ">" . esc_html($rr[4]) . "</div><div class=" . $q . "sp-roi-item-value" . $q . " id=" . $q . "spRoiOccGain" . $q . ">$78,840</div></div>" . chr(10);
    echo "        <div class=" . $q . "sp-roi-item" . $q . "><div class=" . $q . "sp-roi-item-label" . $q . ">" . esc_html($rr[5]) . "</div><div class=" . $q . "sp-roi-item-value" . $q . " id=" . $q . "spRoiTotal" . $q . ">$275,940</div></div>" . chr(10);
    echo "        <div class=" . $q . "sp-roi-item" . $q . "><div class=" . $q . "sp-roi-item-label" . $q . ">" . esc_html($rr[6]) . "</div><div class=" . $q . "sp-roi-item-value" . $q . " id=" . $q . "spRoiPercent" . $q . ">+21.0%</div></div>" . chr(10);
    echo "      </div>" . chr(10);
    echo "      <div class=" . $q . "sp-roi-footnote" . $q . ">" . esc_html($rfn) . "</div>" . chr(10);
    echo "    </div>" . chr(10);

    echo "  </div>" . chr(10);
    echo "</section>" . chr(10);

    // --- CTA SECTION ---
    $cta = array(
        "en" => array("See what your parking data reveals", "Schedule a personalized demo to discover how Spatium can detect losses and optimize revenue across your parking portfolio.", "Request a Demo"),
        "fr" => array("Decouvrez ce que vos donnees de stationnement revelent", "Planifiez une demo personnalisee pour decouvrir comment Spatium peut detecter les pertes et optimiser les revenus de votre portefeuille de stationnement.", "Demander une demo"),
        "es" => array("Descubra lo que revelan sus datos de estacionamiento", "Programe una demo personalizada para descubrir como Spatium puede detectar perdidas y optimizar ingresos en su portafolio de estacionamiento.", "Solicitar una demo"),
    );

    $ct = isset($cta[$lang]) ? $cta[$lang] : $cta["en"];
    $demo_url = "/get-a-demo/";
    if ($lang === "fr") $demo_url = "/fr/demandez-une-demo/";
    if ($lang === "es") $demo_url = "/es/solicite-una-demo/";

    echo "<section class=" . $q . "sp-cta" . $q . ">" . chr(10);
    echo "  <div style=" . $q . "max-width:640px;margin:0 auto;padding:0 20px;" . $q . ">" . chr(10);
    echo "    <h2>" . esc_html($ct[0]) . "</h2>" . chr(10);
    echo "    <p>" . esc_html($ct[1]) . "</p>" . chr(10);
    echo "    <a href=" . $q . esc_url($demo_url) . $q . " class=" . $q . "sp-cta-btn" . $q . ">" . esc_html($ct[2]) . "</a>" . chr(10);
    echo "  </div>" . chr(10);
    echo "</section>" . chr(10);

    // --- ROI Calculator JavaScript ---
    echo "<script>" . chr(10);
    ?>
(function(){
  var spaces = document.getElementById("spRoiSpaces");
  var rate = document.getElementById("spRoiRate");
  var occ = document.getElementById("spRoiOcc");
  if (!spaces || !rate || !occ) return;

  function fmt(n) {
    return "$" + Math.round(n).toLocaleString("en-US");
  }

  function calc() {
    var s = parseInt(spaces.value);
    var r = parseInt(rate.value);
    var o = parseInt(occ.value) / 100;

    document.getElementById("spRoiSpacesVal").textContent = s.toLocaleString();
    document.getElementById("spRoiRateVal").textContent = "$" + r;
    document.getElementById("spRoiOccVal").textContent = occ.value + "%";

    var current = s * r * o * 365;
    var leakage = current * 0.15;
    var occGain = s * r * 0.06 * 365;
    var total = leakage + occGain;
    var pct = (total / current * 100).toFixed(1);

    document.getElementById("spRoiRecovered").textContent = fmt(leakage);
    document.getElementById("spRoiCurrent").textContent = fmt(current);
    document.getElementById("spRoiOccGain").textContent = fmt(occGain);
    document.getElementById("spRoiTotal").textContent = fmt(total);
    document.getElementById("spRoiPercent").textContent = "+" + pct + "%";
  }

  spaces.addEventListener("input", calc);
  rate.addEventListener("input", calc);
  occ.addEventListener("input", calc);
  calc();
})();
<?php
    echo chr(10) . "</script>" . chr(10);
}
