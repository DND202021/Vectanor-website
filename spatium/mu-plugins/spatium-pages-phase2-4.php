<?php
/**
 * Plugin Name: Spatium Content Pages & Trust Sections
 * Description: Phase 2 (Indoor/Outdoor + Curbside content) & Phase 4 (certifications, FAQ schema, about)
 * Version: 1.0.0
 * Author: Dimonoff
 */

if (!defined("ABSPATH")) exit;

// === HELPER: language detection (safe re-declare check) ===
if (!function_exists("spatium_p2_lang")) {
    function spatium_p2_lang() {
        if (function_exists("pll_current_language")) {
            $l = pll_current_language("slug");
            if ($l) return $l;
        }
        $uri = isset($_SERVER["REQUEST_URI"]) ? $_SERVER["REQUEST_URI"] : "";
        if (strpos($uri, "/fr/") !== false) return "fr";
        if (strpos($uri, "/es/") !== false) return "es";
        return "en";
    }
}

// =====================================================================
// PHASE 2: INJECT CONTENT INTO INDOOR/OUTDOOR (ID 20) & CURBSIDE (21)
// =====================================================================
add_action("wp_footer", "spatium_page_content_sections", 90);
function spatium_page_content_sections() {
    $page_id = get_the_ID();
    if (!is_page()) return;

    // Build list of Indoor/Outdoor and Curbside page IDs (EN + translations)
    $indoor_ids = array(20);
    $curbside_ids = array(21);

    if (function_exists("pll_get_post")) {
        $fr20 = pll_get_post(20, "fr");
        $es20 = pll_get_post(20, "es");
        if ($fr20) $indoor_ids[] = $fr20;
        if ($es20) $indoor_ids[] = $es20;
        $fr21 = pll_get_post(21, "fr");
        $es21 = pll_get_post(21, "es");
        if ($fr21) $curbside_ids[] = $fr21;
        if ($es21) $curbside_ids[] = $es21;
    }

    if (in_array($page_id, $indoor_ids)) {
        spatium_render_indoor_outdoor();
    } elseif (in_array($page_id, $curbside_ids)) {
        spatium_render_curbside();
    }
}

// --- PAGE CSS (shared for both content pages) ---
add_action("wp_head", "spatium_pages_css", 100);
function spatium_pages_css() {
    $page_id = get_the_ID();
    if (!is_page()) return;

    $target_ids = array(20, 21);
    if (function_exists("pll_get_post")) {
        foreach (array("fr", "es") as $lg) {
            $t20 = pll_get_post(20, $lg);
            $t21 = pll_get_post(21, $lg);
            if ($t20) $target_ids[] = $t20;
            if ($t21) $target_ids[] = $t21;
        }
    }
    // Also homepage for Phase 4 sections
    $target_ids = array_merge($target_ids, array(10, 259, 260));

    if (!in_array($page_id, $target_ids)) return;

    $q = chr(34);
    echo "<style id=" . $q . "spatium-pages-phase2-4" . $q . ">" . chr(10);
    ?>
/* === Phase 2: Content Page Styles === */
.sp-page-hero {
  padding: 80px 0 60px;
  background: linear-gradient(135deg, #0a3d8f 0%, #1a6bb5 55%, #2e8ec4 100%);
  color: white;
  text-align: center;
}

.sp-page-hero h1 {
  font-family: var(--sp-font-display, 'DM Sans', sans-serif);
  font-size: clamp(2rem, 4vw, 3rem);
  margin-bottom: 16px;
  line-height: 1.15;
}

.sp-page-hero p {
  max-width: 640px;
  margin: 0 auto;
  opacity: 0.9;
  font-size: 1.1rem;
  line-height: 1.7;
}

.sp-page-container {
  max-width: 1100px;
  margin: 0 auto;
  padding: 0 20px;
}

.sp-page-features {
  padding: 80px 0;
  background: #f8f9fc;
}

.sp-page-features h2 {
  font-family: var(--sp-font-display, 'DM Sans', sans-serif);
  font-size: clamp(1.5rem, 2.5vw, 2rem);
  text-align: center;
  margin-bottom: 48px;
  color: #1a1f2e;
}

.sp-features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 28px;
}

.sp-feature-card {
  background: white;
  border: 1px solid #d0d7e2;
  border-radius: 1rem;
  padding: 32px 24px;
  text-align: center;
  box-shadow: 0 4px 16px rgba(0, 30, 80, 0.08);
  transition: transform 0.3s, box-shadow 0.3s;
}

.sp-feature-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 40px rgba(0, 30, 80, 0.12);
}

.sp-feature-icon {
  font-size: 2.5rem;
  margin-bottom: 16px;
}

.sp-feature-card h3 {
  font-family: var(--sp-font-display, 'DM Sans', sans-serif);
  font-size: 1.15rem;
  color: #1a1f2e;
  margin-bottom: 10px;
}

.sp-feature-card p {
  font-size: 0.9rem;
  color: #5a6478;
  line-height: 1.6;
}

.sp-page-usecases {
  padding: 80px 0;
  background: white;
}

.sp-page-usecases h2 {
  font-family: var(--sp-font-display, 'DM Sans', sans-serif);
  font-size: clamp(1.5rem, 2.5vw, 2rem);
  text-align: center;
  margin-bottom: 16px;
  color: #1a1f2e;
}

.sp-page-usecases > .sp-page-container > p {
  text-align: center;
  color: #5a6478;
  max-width: 640px;
  margin: 0 auto 40px;
}

.sp-usecases-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 24px;
}

.sp-usecase {
  background: #f8f9fc;
  border-radius: 1rem;
  padding: 28px;
  border-left: 4px solid #0052d4;
}

.sp-usecase h3 {
  font-family: var(--sp-font-display, 'DM Sans', sans-serif);
  font-size: 1.05rem;
  color: #0052d4;
  margin-bottom: 8px;
}

.sp-usecase p {
  font-size: 0.9rem;
  color: #5a6478;
  line-height: 1.6;
}

.sp-page-cta {
  padding: 60px 0;
  text-align: center;
  background: linear-gradient(135deg, #0a3d8f 0%, #1a6bb5 55%, #2e8ec4 100%);
  color: white;
}

.sp-page-cta h2 {
  font-family: var(--sp-font-display, 'DM Sans', sans-serif);
  font-size: clamp(1.5rem, 2.5vw, 2rem);
  margin-bottom: 16px;
}

.sp-page-cta p {
  opacity: 0.85;
  max-width: 520px;
  margin: 0 auto 24px;
}

/* === Phase 4: Trust & FAQ Styles === */
.sp-trust {
  padding: 48px 0;
  background: #f8f9fc;
  text-align: center;
}

.sp-trust-label {
  font-size: 0.85rem;
  font-weight: 600;
  color: #5a6478;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  margin-bottom: 24px;
}

.sp-trust-badges {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 32px;
  max-width: 900px;
  margin: 0 auto;
}

.sp-badge {
  display: flex;
  align-items: center;
  gap: 10px;
  background: white;
  border: 1px solid #d0d7e2;
  border-radius: 12px;
  padding: 14px 24px;
  box-shadow: 0 2px 8px rgba(0, 30, 80, 0.06);
}

.sp-badge-icon {
  font-size: 1.5rem;
}

.sp-badge-text {
  font-size: 0.85rem;
  font-weight: 600;
  color: #1a1f2e;
}

.sp-faq {
  padding: 80px 0;
  background: white;
}

.sp-faq h2 {
  font-family: var(--sp-font-display, 'DM Sans', sans-serif);
  font-size: clamp(1.5rem, 2.5vw, 2rem);
  text-align: center;
  margin-bottom: 40px;
  color: #1a1f2e;
}

.sp-faq-list {
  max-width: 800px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.sp-faq-item {
  border: 1px solid #d0d7e2;
  border-radius: 12px;
  overflow: hidden;
  background: white;
}

.sp-faq-q {
  padding: 20px 24px;
  font-weight: 600;
  color: #1a1f2e;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
  transition: background 0.2s;
}

.sp-faq-q:hover {
  background: #f8f9fc;
}

.sp-faq-a {
  padding: 0 24px 20px;
  color: #5a6478;
  line-height: 1.7;
  font-size: 0.95rem;
  display: none;
}

.sp-faq-item.sp-open .sp-faq-a {
  display: block;
}

.sp-faq-item.sp-open .sp-faq-arrow {
  transform: rotate(180deg);
}

.sp-faq-arrow {
  transition: transform 0.3s;
  color: #0052d4;
}

.sp-about {
  padding: 80px 0;
  background: #f8f9fc;
}

.sp-about-inner {
  max-width: 800px;
  margin: 0 auto;
  text-align: center;
}

.sp-about h2 {
  font-family: var(--sp-font-display, 'DM Sans', sans-serif);
  font-size: clamp(1.5rem, 2.5vw, 2rem);
  color: #1a1f2e;
  margin-bottom: 20px;
}

.sp-about p {
  color: #5a6478;
  line-height: 1.8;
  font-size: 1rem;
  margin-bottom: 16px;
}

.sp-about-highlight {
  display: inline-block;
  color: #0052d4;
  font-weight: 600;
}

@media (max-width: 768px) {
  .sp-usecases-grid { grid-template-columns: 1fr; }
  .sp-trust-badges { flex-direction: column; align-items: center; }
}
<?php
    echo chr(10) . "</style>" . chr(10);
}


// =====================================================
// INDOOR/OUTDOOR PARKING CONTENT
// =====================================================
function spatium_render_indoor_outdoor() {
    $lang = spatium_p2_lang();
    $q = chr(34);

    // --- HERO ---
    $hero = array(
        "en" => array("Indoor & Outdoor Parking Management", "Real-time visibility, revenue protection, and operational intelligence for parking lots of any size. Spatium transforms your parking infrastructure into a connected, data-driven operation."),
        "fr" => array("Gestion de stationnement interieur et exterieur", "Visibilite en temps reel, protection des revenus et intelligence operationnelle pour les stationnements de toute taille. Spatium transforme votre infrastructure en une operation connectee et basee sur les donnees."),
        "es" => array("Gestion de estacionamiento interior y exterior", "Visibilidad en tiempo real, proteccion de ingresos e inteligencia operacional para estacionamientos de cualquier tamano. Spatium transforma su infraestructura en una operacion conectada basada en datos."),
    );
    $h = isset($hero[$lang]) ? $hero[$lang] : $hero["en"];

    echo "<section class=" . $q . "sp-page-hero" . $q . ">" . chr(10);
    echo "  <div class=" . $q . "sp-page-container" . $q . ">" . chr(10);
    echo "    <h1>" . esc_html($h[0]) . "</h1>" . chr(10);
    echo "    <p>" . esc_html($h[1]) . "</p>" . chr(10);
    echo "  </div>" . chr(10);
    echo "</section>" . chr(10);

    // --- FEATURES ---
    $feat_title = array(
        "en" => "Platform capabilities",
        "fr" => "Capacites de la plateforme",
        "es" => "Capacidades de la plataforma",
    );
    $features = array(
        "en" => array(
            array("&#128202;", "Occupancy Monitoring", "Track real-time space availability across indoor and outdoor zones. Guide drivers to open spots and reduce cruising time."),
            array("&#128176;", "Revenue Protection", "Detect and quantify revenue leakage from unauthorized parking, tailgating, and payment non-compliance. Recover 10-25% of lost revenue."),
            array("&#128274;", "Enforcement Automation", "Automate violation detection and integrate with existing LPR and ticketing systems. Reduce manual patrols while improving compliance."),
            array("&#128200;", "Analytics Dashboard", "Unified view of occupancy trends, revenue performance, and operational KPIs across your entire portfolio. Exportable reports for stakeholders."),
            array("&#128268;", "Hardware Agnostic", "Works with your existing sensors, cameras, and access control. No hardware replacement required. Deploy in under 4 weeks."),
            array("&#127760;", "Multi-site Management", "Manage multiple facilities from a single dashboard. Compare performance, standardize operations, and scale effortlessly."),
        ),
        "fr" => array(
            array("&#128202;", "Surveillance d" . chr(39) . "occupation", "Suivez la disponibilite des places en temps reel dans les zones interieures et exterieures. Guidez les conducteurs vers les places libres."),
            array("&#128176;", "Protection des revenus", "Detectez et quantifiez les fuites de revenus dues au stationnement non autorise et au non-paiement. Recuperez 10 a 25 % des revenus perdus."),
            array("&#128274;", "Automatisation de l" . chr(39) . "application", "Automatisez la detection des infractions et integrez-vous aux systemes LPR et de billetterie existants. Reduisez les patrouilles manuelles."),
            array("&#128200;", "Tableau de bord analytique", "Vue unifiee des tendances d" . chr(39) . "occupation, de la performance des revenus et des KPI operationnels. Rapports exportables."),
            array("&#128268;", "Agnostique au materiel", "Fonctionne avec vos capteurs, cameras et controles d" . chr(39) . "acces existants. Aucun remplacement materiel. Deploiement en moins de 4 semaines."),
            array("&#127760;", "Gestion multi-sites", "Gerez plusieurs installations depuis un seul tableau de bord. Comparez les performances et standardisez les operations."),
        ),
        "es" => array(
            array("&#128202;", "Monitoreo de ocupacion", "Rastree la disponibilidad de espacios en tiempo real en zonas interiores y exteriores. Guie a los conductores a espacios libres."),
            array("&#128176;", "Proteccion de ingresos", "Detecte y cuantifique fugas de ingresos por estacionamiento no autorizado y falta de pago. Recupere 10-25% de ingresos perdidos."),
            array("&#128274;", "Automatizacion de cumplimiento", "Automatice la deteccion de infracciones e integrese con sistemas LPR y de multas existentes. Reduzca patrullas manuales."),
            array("&#128200;", "Panel analitico", "Vista unificada de tendencias de ocupacion, rendimiento de ingresos y KPIs operacionales. Informes exportables."),
            array("&#128268;", "Agnostico al hardware", "Funciona con sus sensores, camaras y controles de acceso existentes. Sin reemplazo de hardware. Implementacion en menos de 4 semanas."),
            array("&#127760;", "Gestion multi-sitio", "Administre multiples instalaciones desde un solo panel. Compare rendimiento y estandarice operaciones."),
        ),
    );

    $ft = isset($feat_title[$lang]) ? $feat_title[$lang] : $feat_title["en"];
    $ff = isset($features[$lang]) ? $features[$lang] : $features["en"];

    echo "<section class=" . $q . "sp-page-features" . $q . ">" . chr(10);
    echo "  <div class=" . $q . "sp-page-container" . $q . ">" . chr(10);
    echo "    <h2>" . esc_html($ft) . "</h2>" . chr(10);
    echo "    <div class=" . $q . "sp-features-grid" . $q . ">" . chr(10);
    foreach ($ff as $f) {
        echo "      <div class=" . $q . "sp-feature-card" . $q . ">" . chr(10);
        echo "        <div class=" . $q . "sp-feature-icon" . $q . ">" . $f[0] . "</div>" . chr(10);
        echo "        <h3>" . esc_html($f[1]) . "</h3>" . chr(10);
        echo "        <p>" . esc_html($f[2]) . "</p>" . chr(10);
        echo "      </div>" . chr(10);
    }
    echo "    </div>" . chr(10);
    echo "  </div>" . chr(10);
    echo "</section>" . chr(10);

    // --- USE CASES ---
    $uc_title = array(
        "en" => "Who uses Spatium for parking lots?",
        "fr" => "Qui utilise Spatium pour les stationnements?",
        "es" => "Quien usa Spatium para estacionamientos?",
    );
    $uc_desc = array(
        "en" => "From commercial properties to healthcare campuses, Spatium adapts to any parking environment.",
        "fr" => "Des proprietes commerciales aux campus de sante, Spatium s" . chr(39) . "adapte a tout environnement de stationnement.",
        "es" => "Desde propiedades comerciales hasta campus de salud, Spatium se adapta a cualquier entorno de estacionamiento.",
    );
    $usecases = array(
        "en" => array(
            array("Commercial Real Estate", "Shopping centers, office towers, and mixed-use developments benefit from occupancy intelligence that drives tenant satisfaction and revenue optimization."),
            array("Hospitality & Resorts", "Hotels and resorts use Spatium to streamline valet operations, monitor guest parking, and reduce unauthorized usage."),
            array("Healthcare Campuses", "Hospitals and clinics gain real-time parking visibility to improve patient experience and manage staff, visitor, and emergency vehicle zones."),
            array("Airports & Transit Hubs", "High-volume facilities leverage Spatium for capacity management, dynamic pricing support, and seamless passenger guidance."),
        ),
        "fr" => array(
            array("Immobilier commercial", "Centres commerciaux, tours de bureaux et developpements a usage mixte beneficient d" . chr(39) . "une intelligence d" . chr(39) . "occupation qui ameliore la satisfaction des locataires."),
            array("Hotellerie et villegiature", "Les hotels utilisent Spatium pour optimiser le service voiturier, surveiller le stationnement des clients et reduire l" . chr(39) . "utilisation non autorisee."),
            array("Campus de sante", "Les hopitaux gagnent une visibilite en temps reel pour ameliorer l" . chr(39) . "experience patient et gerer les zones de personnel et de visiteurs."),
            array("Aeroports et centres de transit", "Les installations a fort volume utilisent Spatium pour la gestion de capacite et le guidage des passagers."),
        ),
        "es" => array(
            array("Bienes raices comerciales", "Centros comerciales, torres de oficinas y desarrollos de uso mixto se benefician de la inteligencia de ocupacion para la satisfaccion de inquilinos."),
            array("Hospitalidad y resorts", "Hoteles y resorts usan Spatium para optimizar operaciones de valet y reducir el uso no autorizado."),
            array("Campus de salud", "Hospitales ganan visibilidad en tiempo real para mejorar la experiencia del paciente y gestionar zonas de personal y visitantes."),
            array("Aeropuertos y centros de transito", "Instalaciones de alto volumen usan Spatium para gestion de capacidad y guia de pasajeros."),
        ),
    );

    $ut = isset($uc_title[$lang]) ? $uc_title[$lang] : $uc_title["en"];
    $ud = isset($uc_desc[$lang]) ? $uc_desc[$lang] : $uc_desc["en"];
    $uu = isset($usecases[$lang]) ? $usecases[$lang] : $usecases["en"];

    echo "<section class=" . $q . "sp-page-usecases" . $q . ">" . chr(10);
    echo "  <div class=" . $q . "sp-page-container" . $q . ">" . chr(10);
    echo "    <h2>" . esc_html($ut) . "</h2>" . chr(10);
    echo "    <p>" . esc_html($ud) . "</p>" . chr(10);
    echo "    <div class=" . $q . "sp-usecases-grid" . $q . ">" . chr(10);
    foreach ($uu as $u) {
        echo "      <div class=" . $q . "sp-usecase" . $q . ">" . chr(10);
        echo "        <h3>" . esc_html($u[0]) . "</h3>" . chr(10);
        echo "        <p>" . esc_html($u[1]) . "</p>" . chr(10);
        echo "      </div>" . chr(10);
    }
    echo "    </div>" . chr(10);
    echo "  </div>" . chr(10);
    echo "</section>" . chr(10);

    // --- CTA ---
    spatium_render_page_cta($lang);
}


// =====================================================
// CURBSIDE PARKING CONTENT
// =====================================================
function spatium_render_curbside() {
    $lang = spatium_p2_lang();
    $q = chr(34);

    // --- HERO ---
    $hero = array(
        "en" => array("Curbside & On-Street Parking Management", "Transform your city" . chr(39) . "s curb space into a smart, data-driven asset. Spatium provides municipalities and operators with real-time curbside intelligence for better enforcement, revenue, and citizen experience."),
        "fr" => array("Gestion du stationnement sur rue", "Transformez les espaces de bordure de votre ville en un actif intelligent base sur les donnees. Spatium offre aux municipalites une intelligence de bordure en temps reel."),
        "es" => array("Gestion de estacionamiento en la calle", "Transforme los espacios de acera de su ciudad en un activo inteligente basado en datos. Spatium proporciona a los municipios inteligencia de acera en tiempo real."),
    );
    $h = isset($hero[$lang]) ? $hero[$lang] : $hero["en"];

    echo "<section class=" . $q . "sp-page-hero" . $q . ">" . chr(10);
    echo "  <div class=" . $q . "sp-page-container" . $q . ">" . chr(10);
    echo "    <h1>" . esc_html($h[0]) . "</h1>" . chr(10);
    echo "    <p>" . esc_html($h[1]) . "</p>" . chr(10);
    echo "  </div>" . chr(10);
    echo "</section>" . chr(10);

    // --- FEATURES ---
    $feat_title = array(
        "en" => "Curbside intelligence features",
        "fr" => "Fonctionnalites d" . chr(39) . "intelligence de bordure",
        "es" => "Funciones de inteligencia de acera",
    );
    $features = array(
        "en" => array(
            array("&#9200;", "Turnover Analytics", "Measure parking duration, turnover rates, and compliance by zone. Identify overstays and optimize time-limit policies."),
            array("&#128176;", "Meter Compliance", "Detect payment non-compliance in real time. Integrate with meter systems to flag expired sessions and support enforcement."),
            array("&#128506;", "Zone Management", "Define and monitor parking zones with custom rules: time limits, pricing tiers, permitted vehicles, and peak-hour restrictions."),
            array("&#128663;", "Dynamic Availability", "Provide real-time curb availability to drivers via apps and signage. Reduce cruising time and double-parking."),
            array("&#127961;", "Smart City Integration", "Connect with traffic management, public transit, and environmental monitoring systems for a holistic urban mobility approach."),
            array("&#128200;", "Revenue Intelligence", "Track revenue by zone, time period, and payment method. Identify underperforming areas and optimize pricing strategies."),
        ),
        "fr" => array(
            array("&#9200;", "Analytique de rotation", "Mesurez la duree de stationnement, les taux de rotation et la conformite par zone. Identifiez les depassements et optimisez les politiques."),
            array("&#128176;", "Conformite des parcometes", "Detectez le non-paiement en temps reel. Integrez-vous aux systemes de parcometres pour signaler les sessions expirees."),
            array("&#128506;", "Gestion de zones", "Definissez et surveillez les zones avec des regles personnalisees : limites de temps, tarification, vehicules permis."),
            array("&#128663;", "Disponibilite dynamique", "Fournissez la disponibilite en temps reel aux conducteurs via des applications et la signalisation. Reduisez le temps de recherche."),
            array("&#127961;", "Integration ville intelligente", "Connectez-vous a la gestion du trafic, au transport en commun et aux systemes de surveillance pour une approche de mobilite urbaine holistique."),
            array("&#128200;", "Intelligence des revenus", "Suivez les revenus par zone, periode et methode de paiement. Identifiez les zones sous-performantes."),
        ),
        "es" => array(
            array("&#9200;", "Analitica de rotacion", "Mida la duracion del estacionamiento, tasas de rotacion y cumplimiento por zona. Identifique excesos y optimice politicas."),
            array("&#128176;", "Cumplimiento de parquimetros", "Detecte falta de pago en tiempo real. Integrese con sistemas de parquimetros para senalar sesiones expiradas."),
            array("&#128506;", "Gestion de zonas", "Defina y monitoree zonas con reglas personalizadas: limites de tiempo, precios, vehiculos permitidos."),
            array("&#128663;", "Disponibilidad dinamica", "Proporcione disponibilidad en tiempo real a conductores via aplicaciones y senalizacion. Reduzca tiempo de busqueda."),
            array("&#127961;", "Integracion ciudad inteligente", "Conectese con gestion de trafico, transporte publico y sistemas de monitoreo para un enfoque de movilidad urbana."),
            array("&#128200;", "Inteligencia de ingresos", "Rastree ingresos por zona, periodo y metodo de pago. Identifique areas de bajo rendimiento."),
        ),
    );

    $ft = isset($feat_title[$lang]) ? $feat_title[$lang] : $feat_title["en"];
    $ff = isset($features[$lang]) ? $features[$lang] : $features["en"];

    echo "<section class=" . $q . "sp-page-features" . $q . ">" . chr(10);
    echo "  <div class=" . $q . "sp-page-container" . $q . ">" . chr(10);
    echo "    <h2>" . esc_html($ft) . "</h2>" . chr(10);
    echo "    <div class=" . $q . "sp-features-grid" . $q . ">" . chr(10);
    foreach ($ff as $f) {
        echo "      <div class=" . $q . "sp-feature-card" . $q . ">" . chr(10);
        echo "        <div class=" . $q . "sp-feature-icon" . $q . ">" . $f[0] . "</div>" . chr(10);
        echo "        <h3>" . esc_html($f[1]) . "</h3>" . chr(10);
        echo "        <p>" . esc_html($f[2]) . "</p>" . chr(10);
        echo "      </div>" . chr(10);
    }
    echo "    </div>" . chr(10);
    echo "  </div>" . chr(10);
    echo "</section>" . chr(10);

    // --- USE CASES ---
    $uc_title = array(
        "en" => "Who uses Spatium for curbside?",
        "fr" => "Qui utilise Spatium pour le stationnement sur rue?",
        "es" => "Quien usa Spatium para estacionamiento en calle?",
    );
    $usecases = array(
        "en" => array(
            array("Municipal Parking Authorities", "City agencies use Spatium to optimize curb utilization, improve enforcement efficiency, and maximize parking revenue across thousands of metered spaces."),
            array("Downtown Business Districts", "BIDs and commercial corridors benefit from better turnover, happier shoppers who find parking faster, and data to support economic development decisions."),
            array("University Campuses", "Campus parking offices use zone-based management to balance student, staff, and visitor parking needs across distributed facilities."),
            array("Event & Venue Districts", "Manage surge demand during events with dynamic zone control, real-time wayfinding, and post-event analytics."),
        ),
        "fr" => array(
            array("Autorites municipales de stationnement", "Les agences municipales utilisent Spatium pour optimiser l" . chr(39) . "utilisation des bordures, ameliorer l" . chr(39) . "application et maximiser les revenus."),
            array("Quartiers commerciaux du centre-ville", "Les corridors commerciaux beneficient d" . chr(39) . "une meilleure rotation, de clients satisfaits et de donnees pour soutenir le developpement economique."),
            array("Campus universitaires", "Les bureaux de stationnement de campus utilisent la gestion par zone pour equilibrer les besoins de stationnement des etudiants, du personnel et des visiteurs."),
            array("Quartiers d" . chr(39) . "evenements", "Gerez la demande accrue lors d" . chr(39) . "evenements avec un controle de zone dynamique et le guidage en temps reel."),
        ),
        "es" => array(
            array("Autoridades municipales de estacionamiento", "Las agencias municipales usan Spatium para optimizar el uso de acera, mejorar la aplicacion y maximizar los ingresos."),
            array("Distritos comerciales del centro", "Los corredores comerciales se benefician de mejor rotacion, clientes satisfechos y datos para apoyar decisiones de desarrollo economico."),
            array("Campus universitarios", "Las oficinas de estacionamiento de campus usan gestion por zonas para equilibrar necesidades de estudiantes, personal y visitantes."),
            array("Distritos de eventos", "Gestione la demanda durante eventos con control de zona dinamico y orientacion en tiempo real."),
        ),
    );

    $ut = isset($uc_title[$lang]) ? $uc_title[$lang] : $uc_title["en"];
    $uu = isset($usecases[$lang]) ? $usecases[$lang] : $usecases["en"];

    echo "<section class=" . $q . "sp-page-usecases" . $q . ">" . chr(10);
    echo "  <div class=" . $q . "sp-page-container" . $q . ">" . chr(10);
    echo "    <h2>" . esc_html($ut) . "</h2>" . chr(10);
    echo "    <div class=" . $q . "sp-usecases-grid" . $q . ">" . chr(10);
    foreach ($uu as $u) {
        echo "      <div class=" . $q . "sp-usecase" . $q . ">" . chr(10);
        echo "        <h3>" . esc_html($u[0]) . "</h3>" . chr(10);
        echo "        <p>" . esc_html($u[1]) . "</p>" . chr(10);
        echo "      </div>" . chr(10);
    }
    echo "    </div>" . chr(10);
    echo "  </div>" . chr(10);
    echo "</section>" . chr(10);

    // --- CTA ---
    spatium_render_page_cta($lang);
}


// --- Shared page CTA ---
function spatium_render_page_cta($lang) {
    $q = chr(34);
    $cta = array(
        "en" => array("Ready to transform your parking operations?", "Schedule a personalized demo and see how Spatium can work for your facility.", "Request a Demo"),
        "fr" => array("Pret a transformer vos operations de stationnement?", "Planifiez une demo personnalisee et decouvrez comment Spatium peut fonctionner pour votre installation.", "Demander une demo"),
        "es" => array("Listo para transformar sus operaciones de estacionamiento?", "Programe una demo personalizada y vea como Spatium puede funcionar para su instalacion.", "Solicitar una demo"),
    );
    $ct = isset($cta[$lang]) ? $cta[$lang] : $cta["en"];
    $demo_url = "/get-a-demo/";
    if ($lang === "fr") $demo_url = "/fr/demandez-une-demo/";
    if ($lang === "es") $demo_url = "/es/solicite-una-demo/";

    echo "<section class=" . $q . "sp-page-cta" . $q . ">" . chr(10);
    echo "  <div class=" . $q . "sp-page-container" . $q . ">" . chr(10);
    echo "    <h2>" . esc_html($ct[0]) . "</h2>" . chr(10);
    echo "    <p>" . esc_html($ct[1]) . "</p>" . chr(10);
    echo "    <a href=" . $q . esc_url($demo_url) . $q . " class=" . $q . "sp-cta-btn" . $q . ">" . esc_html($ct[2]) . "</a>" . chr(10);
    echo "  </div>" . chr(10);
    echo "</section>" . chr(10);
}


// =====================================================
// PHASE 4: TRUST BADGES, FAQ, ABOUT (HOMEPAGE)
// =====================================================
add_action("wp_footer", "spatium_phase4_sections", 96);
function spatium_phase4_sections() {
    if (!is_front_page() && !is_page(array(10, 259, 260))) return;

    $lang = spatium_p2_lang();
    $q = chr(34);

    // --- TRUST / COMPLIANCE BADGES ---
    $trust_label = array(
        "en" => "Built for enterprise-grade operations",
        "fr" => "Concu pour des operations de niveau entreprise",
        "es" => "Disenado para operaciones de nivel empresarial",
    );
    $badges = array(
        "en" => array(
            array("&#128274;", "SOC 2 Aligned"),
            array("&#127968;", "ParkSmart Ready"),
            array("&#128196;", "APDS Compatible"),
            array("&#127760;", "GDPR Compliant"),
            array("&#9989;", "99.9% Uptime SLA"),
        ),
        "fr" => array(
            array("&#128274;", "Aligne SOC 2"),
            array("&#127968;", "ParkSmart Ready"),
            array("&#128196;", "Compatible APDS"),
            array("&#127760;", "Conforme RGPD"),
            array("&#9989;", "SLA 99,9 % disponibilite"),
        ),
        "es" => array(
            array("&#128274;", "Alineado SOC 2"),
            array("&#127968;", "ParkSmart Ready"),
            array("&#128196;", "Compatible APDS"),
            array("&#127760;", "Cumple GDPR"),
            array("&#9989;", "SLA 99.9% disponibilidad"),
        ),
    );

    $tl = isset($trust_label[$lang]) ? $trust_label[$lang] : $trust_label["en"];
    $bb = isset($badges[$lang]) ? $badges[$lang] : $badges["en"];

    echo "<section class=" . $q . "sp-trust" . $q . ">" . chr(10);
    echo "  <p class=" . $q . "sp-trust-label" . $q . ">" . esc_html($tl) . "</p>" . chr(10);
    echo "  <div class=" . $q . "sp-trust-badges" . $q . ">" . chr(10);
    foreach ($bb as $b) {
        echo "    <div class=" . $q . "sp-badge" . $q . ">" . chr(10);
        echo "      <span class=" . $q . "sp-badge-icon" . $q . ">" . $b[0] . "</span>" . chr(10);
        echo "      <span class=" . $q . "sp-badge-text" . $q . ">" . esc_html($b[1]) . "</span>" . chr(10);
        echo "    </div>" . chr(10);
    }
    echo "  </div>" . chr(10);
    echo "</section>" . chr(10);

    // --- ABOUT SECTION ---
    $about_title = array(
        "en" => "About Spatium",
        "fr" => "A propos de Spatium",
        "es" => "Acerca de Spatium",
    );
    $about_text = array(
        "en" => array(
            "Spatium is a division of Dimonoff, a Quebec City-based IoT company with over 15 years of experience deploying smart infrastructure solutions across North America.",
            "Born from the realization that parking operations generate massive amounts of underutilized data, Spatium was built to bridge the gap between physical infrastructure and operational intelligence.",
            "Our platform is hardware-agnostic, connecting to existing sensors, cameras, and payment systems to deliver actionable insights without costly infrastructure replacement. From private parking lots to municipal curbside networks, we help operators see what they have been missing.",
        ),
        "fr" => array(
            "Spatium est une division de Dimonoff, une entreprise IoT basee a Quebec avec plus de 15 ans d" . chr(39) . "experience dans le deploiement de solutions d" . chr(39) . "infrastructure intelligente en Amerique du Nord.",
            "Nee de la realisation que les operations de stationnement generent d" . chr(39) . "enormes quantites de donnees sous-utilisees, Spatium a ete construite pour combler l" . chr(39) . "ecart entre l" . chr(39) . "infrastructure physique et l" . chr(39) . "intelligence operationnelle.",
            "Notre plateforme est agnostique au materiel, se connectant aux capteurs, cameras et systemes de paiement existants pour fournir des informations exploitables sans remplacement couteux d" . chr(39) . "infrastructure.",
        ),
        "es" => array(
            "Spatium es una division de Dimonoff, una empresa IoT con sede en la ciudad de Quebec con mas de 15 anos de experiencia implementando soluciones de infraestructura inteligente en America del Norte.",
            "Nacida de la comprension de que las operaciones de estacionamiento generan cantidades masivas de datos subutilizados, Spatium fue construida para cerrar la brecha entre la infraestructura fisica y la inteligencia operacional.",
            "Nuestra plataforma es agnostica al hardware, conectandose a sensores, camaras y sistemas de pago existentes para ofrecer informacion accionable sin costosos reemplazos de infraestructura.",
        ),
    );

    $at = isset($about_title[$lang]) ? $about_title[$lang] : $about_title["en"];
    $ax = isset($about_text[$lang]) ? $about_text[$lang] : $about_text["en"];

    echo "<section class=" . $q . "sp-about" . $q . ">" . chr(10);
    echo "  <div class=" . $q . "sp-about-inner sp-page-container" . $q . ">" . chr(10);
    echo "    <span class=" . $q . "sp-section-label" . $q . ">" . esc_html($at) . "</span>" . chr(10);
    echo "    <h2>410-1015 ave. Wilfrid-Pelletier, Quebec, QC</h2>" . chr(10);
    foreach ($ax as $p) {
        echo "    <p>" . esc_html($p) . "</p>" . chr(10);
    }
    echo "  </div>" . chr(10);
    echo "</section>" . chr(10);

    // --- FAQ SECTION ---
    $faq_title = array(
        "en" => "Frequently asked questions",
        "fr" => "Questions frequemment posees",
        "es" => "Preguntas frecuentes",
    );
    $faqs = array(
        "en" => array(
            array("What is Spatium?", "Spatium is an IoT smart parking management platform that provides real-time occupancy monitoring, revenue protection, and operational analytics for indoor, outdoor, and curbside parking operations."),
            array("Do I need to replace my existing hardware?", "No. Spatium is hardware-agnostic and integrates with your existing sensors, cameras, LPR systems, and payment infrastructure. Typical deployment takes less than 4 weeks."),
            array("How does Spatium detect revenue leakage?", "Spatium cross-references occupancy data, payment records, and access logs to identify discrepancies such as unauthorized parking, tailgating, and payment non-compliance. Clients typically recover 10-25% of previously lost revenue."),
            array("What parking environments does Spatium support?", "Spatium supports indoor and outdoor parking lots (commercial, hospitality, healthcare, airports) as well as curbside and on-street parking for municipalities and business districts."),
            array("Is Spatium available in multiple languages?", "Yes. The Spatium platform and dashboard are available in English, French, and Spanish, with additional languages available on request."),
            array("How is Spatium priced?", "Spatium uses a SaaS subscription model based on the number of monitored spaces. Contact us for a personalized quote based on your facility size and requirements."),
        ),
        "fr" => array(
            array("Qu" . chr(39) . "est-ce que Spatium?", "Spatium est une plateforme IoT de gestion intelligente du stationnement qui fournit la surveillance d" . chr(39) . "occupation en temps reel, la protection des revenus et l" . chr(39) . "analytique operationnelle."),
            array("Dois-je remplacer mon equipement existant?", "Non. Spatium est agnostique au materiel et s" . chr(39) . "integre a vos capteurs, cameras, systemes LPR et infrastructure de paiement existants. Le deploiement prend moins de 4 semaines."),
            array("Comment Spatium detecte-t-il les fuites de revenus?", "Spatium croise les donnees d" . chr(39) . "occupation, les enregistrements de paiement et les journaux d" . chr(39) . "acces pour identifier les ecarts. Les clients recuperent generalement 10 a 25 % des revenus perdus."),
            array("Quels environnements Spatium supporte-t-il?", "Spatium supporte les stationnements interieurs et exterieurs (commercial, hotellerie, sante, aeroports) ainsi que le stationnement sur rue pour les municipalites."),
            array("Spatium est-il disponible en plusieurs langues?", "Oui. La plateforme Spatium est disponible en anglais, francais et espagnol, avec des langues supplementaires sur demande."),
            array("Comment Spatium est-il tarife?", "Spatium utilise un modele d" . chr(39) . "abonnement SaaS base sur le nombre de places surveillees. Contactez-nous pour un devis personnalise."),
        ),
        "es" => array(
            array("Que es Spatium?", "Spatium es una plataforma IoT de gestion inteligente de estacionamiento que proporciona monitoreo de ocupacion en tiempo real, proteccion de ingresos y analitica operacional."),
            array("Necesito reemplazar mi hardware existente?", "No. Spatium es agnostico al hardware y se integra con sus sensores, camaras, sistemas LPR e infraestructura de pago existentes. La implementacion toma menos de 4 semanas."),
            array("Como detecta Spatium las fugas de ingresos?", "Spatium cruza datos de ocupacion, registros de pago y registros de acceso para identificar discrepancias. Los clientes recuperan tipicamente 10-25% de ingresos perdidos."),
            array("Que entornos soporta Spatium?", "Spatium soporta estacionamientos interiores y exteriores (comercial, hospitalidad, salud, aeropuertos) asi como estacionamiento en calle para municipios."),
            array("Spatium esta disponible en varios idiomas?", "Si. La plataforma Spatium esta disponible en ingles, frances y espanol, con idiomas adicionales disponibles bajo solicitud."),
            array("Como se tarifa Spatium?", "Spatium utiliza un modelo de suscripcion SaaS basado en el numero de espacios monitoreados. Contactenos para una cotizacion personalizada."),
        ),
    );

    $fqt = isset($faq_title[$lang]) ? $faq_title[$lang] : $faq_title["en"];
    $fql = isset($faqs[$lang]) ? $faqs[$lang] : $faqs["en"];

    echo "<section class=" . $q . "sp-faq" . $q . ">" . chr(10);
    echo "  <div class=" . $q . "sp-page-container" . $q . ">" . chr(10);
    echo "    <h2>" . esc_html($fqt) . "</h2>" . chr(10);
    echo "    <div class=" . $q . "sp-faq-list" . $q . ">" . chr(10);
    foreach ($fql as $fq) {
        echo "      <div class=" . $q . "sp-faq-item" . $q . ">" . chr(10);
        echo "        <div class=" . $q . "sp-faq-q" . $q . " onclick=" . $q . "this.parentElement.classList.toggle(" . chr(39) . "sp-open" . chr(39) . ")" . $q . ">" . chr(10);
        echo "          <span>" . esc_html($fq[0]) . "</span>" . chr(10);
        echo "          <span class=" . $q . "sp-faq-arrow" . $q . ">&#9660;</span>" . chr(10);
        echo "        </div>" . chr(10);
        echo "        <div class=" . $q . "sp-faq-a" . $q . ">" . esc_html($fq[1]) . "</div>" . chr(10);
        echo "      </div>" . chr(10);
    }
    echo "    </div>" . chr(10);
    echo "  </div>" . chr(10);
    echo "</section>" . chr(10);

    // --- FAQ SCHEMA (JSON-LD) ---
    $faq_en = isset($faqs["en"]) ? $faqs["en"] : array();
    echo "<script type=" . $q . "application/ld+json" . $q . ">" . chr(10);
    echo "{" . chr(10);
    echo "  " . $q . "@context" . $q . ": " . $q . "https://schema.org" . $q . "," . chr(10);
    echo "  " . $q . "@type" . $q . ": " . $q . "FAQPage" . $q . "," . chr(10);
    echo "  " . $q . "mainEntity" . $q . ": [" . chr(10);
    $count = count($faq_en);
    for ($i = 0; $i < $count; $i++) {
        echo "    {" . chr(10);
        echo "      " . $q . "@type" . $q . ": " . $q . "Question" . $q . "," . chr(10);
        echo "      " . $q . "name" . $q . ": " . $q . esc_attr($faq_en[$i][0]) . $q . "," . chr(10);
        echo "      " . $q . "acceptedAnswer" . $q . ": {" . chr(10);
        echo "        " . $q . "@type" . $q . ": " . $q . "Answer" . $q . "," . chr(10);
        echo "        " . $q . "text" . $q . ": " . $q . esc_attr($faq_en[$i][1]) . $q . chr(10);
        echo "      }" . chr(10);
        echo "    }";
        if ($i < $count - 1) echo ",";
        echo chr(10);
    }
    echo "  ]" . chr(10);
    echo "}" . chr(10);
    echo "</script>" . chr(10);
}
