<?php
/**
 * Plugin Name: Dimonoff FAQ Schema
 * Description: Injects FAQPage JSON-LD schema on Solutions and Contact pages (EN/FR/ES).
 * Version: 1.1.0
 * Author: Dimonoff
 *
 * DEPLOYMENT: Upload to wp-content/mu-plugins/dimonoff-faq-schema.php
 * NOTE: This file contains ZERO backslash characters to survive stripslashes().
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

/**
 * Output FAQPage JSON-LD schema on specific pages.
 *
 * Each page ID maps to an array of Q&A pairs in the appropriate language.
 * Only fires on singular page views matching known IDs.
 *
 * @return void
 */
function dimonoff_faq_schema() {
    if ( ! is_singular( 'page' ) ) {
        return;
    }

    $page_id = get_the_ID();

    // FAQ data keyed by WordPress page ID
    $faq_data = dimonoff_get_faq_data();

    if ( ! isset( $faq_data[ $page_id ] ) ) {
        return;
    }

    $faqs = $faq_data[ $page_id ];
    $main_entity = array();

    foreach ( $faqs as $faq ) {
        $main_entity[] = array(
            '@type'          => 'Question',
            'name'           => $faq['q'],
            'acceptedAnswer' => array(
                '@type' => 'Answer',
                'text'  => $faq['a'],
            ),
        );
    }

    $schema = array(
        '@context'   => 'https://schema.org',
        '@type'      => 'FAQPage',
        'mainEntity' => $main_entity,
    );

    echo '<script type="application/ld+json">' . PHP_EOL;
    echo wp_json_encode( $schema, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT );
    echo PHP_EOL . '</script>' . PHP_EOL;
}
add_action( 'wp_head', 'dimonoff_faq_schema', 2 );

/**
 * Return FAQ data for all target pages.
 *
 * Page IDs:
 *   Solutions: EN=24, FR=4950, ES=74278
 *   Contact:   EN=17, FR=4954, ES=74091
 *
 * IMPORTANT: All strings use double quotes to avoid backslash-escaped apostrophes.
 * This prevents corruption by PHP stripslashes() in the elFinder connector.
 *
 * @return array Associative array keyed by page ID.
 */
function dimonoff_get_faq_data() {
    return array(
        // --- Solutions EN (ID: 24) ---
        24 => array(
            array(
                "q" => "What is the SCMS platform?",
                "a" => "The Smart City Management System (SCMS) is Dimonoff's centralized IoT platform for managing connected urban infrastructure including street lighting, parking, environmental sensors, and mass notification systems. It is trusted by municipalities across North America.",
            ),
            array(
                "q" => "What smart lighting solutions does Dimonoff offer?",
                "a" => "Dimonoff provides end-to-end smart street lighting solutions including LED controllers, dimming schedules, real-time monitoring, energy reporting, and fault detection. Our solutions are compatible with major luminaire manufacturers and use open standards like TALQ and DALI.",
            ),
            array(
                "q" => "Does Dimonoff offer smart parking solutions?",
                "a" => "Yes, through our Spatium platform, Dimonoff offers intelligent parking management including real-time occupancy detection, indoor and on-street parking guidance, mobile payment integration, and analytics dashboards for parking operators.",
            ),
            array(
                "q" => "What is DooExpress?",
                "a" => "DooExpress is Dimonoff's rapid-deployment IoT platform with integrated mapping capabilities. It allows cities to quickly deploy and manage connected devices across their infrastructure with minimal setup time.",
            ),
            array(
                "q" => "In which regions does Dimonoff operate?",
                "a" => "Dimonoff operates across Canada and the United States, with smart city deployments in cities including Laval, Montreal, Varennes, Grand Rapids (Michigan), Columbus (Ohio), and many more municipalities.",
            ),
        ),

        // --- Solutions FR (ID: 4950) ---
        4950 => array(
            array(
                "q" => "Qu'est-ce que la plateforme SCMS ?",
                "a" => "Le Smart City Management System (SCMS) est la plateforme IoT centralisée de Dimonoff pour gérer les infrastructures urbaines connectées incluant l'éclairage de rue, le stationnement, les capteurs environnementaux et les systèmes de notification de masse. Elle est utilisée par des municipalités partout en Amérique du Nord.",
            ),
            array(
                "q" => "Quelles solutions d'éclairage intelligent Dimonoff offre-t-il ?",
                "a" => "Dimonoff fournit des solutions complètes d'éclairage de rue intelligent incluant des contrôleurs LED, des horaires de gradation, la surveillance en temps réel, des rapports énergétiques et la détection de pannes. Nos solutions sont compatibles avec les principaux fabricants de luminaires.",
            ),
            array(
                "q" => "Dimonoff offre-t-il des solutions de stationnement intelligent ?",
                "a" => "Oui, via notre plateforme Spatium, Dimonoff offre la gestion intelligente du stationnement incluant la détection d'occupation en temps réel, le guidage intérieur et extérieur, l'intégration de paiement mobile et des tableaux de bord analytiques.",
            ),
            array(
                "q" => "Qu'est-ce que DooExpress ?",
                "a" => "DooExpress est la plateforme IoT de déploiement rapide de Dimonoff avec cartographie intégrée. Elle permet aux villes de déployer et gérer rapidement des appareils connectés à travers leur infrastructure.",
            ),
            array(
                "q" => "Dans quelles régions Dimonoff opère-t-il ?",
                "a" => "Dimonoff opère à travers le Canada et les États-Unis, avec des déploiements dans des villes comme Laval, Montréal, Varennes, Grand Rapids (Michigan), Columbus (Ohio) et de nombreuses autres municipalités.",
            ),
        ),

        // --- Solutions ES (ID: 74278) ---
        74278 => array(
            array(
                "q" => "¿Qué es la plataforma SCMS?",
                "a" => "El Smart City Management System (SCMS) es la plataforma IoT centralizada de Dimonoff para gestionar infraestructura urbana conectada incluyendo alumbrado público, estacionamiento, sensores ambientales y sistemas de notificación masiva.",
            ),
            array(
                "q" => "¿Qué soluciones de iluminación inteligente ofrece Dimonoff?",
                "a" => "Dimonoff proporciona soluciones completas de alumbrado público inteligente incluyendo controladores LED, programación de atenuación, monitoreo en tiempo real, informes de energía y detección de fallas.",
            ),
            array(
                "q" => "¿Ofrece Dimonoff soluciones de estacionamiento inteligente?",
                "a" => "Sí, a través de nuestra plataforma Spatium, Dimonoff ofrece gestión inteligente de estacionamiento incluyendo detección de ocupación en tiempo real, guía de estacionamiento interior y exterior, e integración de pago móvil.",
            ),
            array(
                "q" => "¿En qué regiones opera Dimonoff?",
                "a" => "Dimonoff opera en Canadá y Estados Unidos, con implementaciones en ciudades como Laval, Montreal, Varennes, Grand Rapids (Michigan), Columbus (Ohio) y muchas más municipalidades.",
            ),
        ),

        // --- Contact EN (ID: 17) ---
        17 => array(
            array(
                "q" => "Where is Dimonoff located?",
                "a" => "Dimonoff is headquartered at 2820, rue Einstein, Quebec City, QC G1X 4B7, Canada. We serve municipalities and utilities across North America.",
            ),
            array(
                "q" => "How can I request a demo of the SCMS platform?",
                "a" => "You can request a demo by filling out the contact form on this page, calling us at +1-418-877-7555, or emailing info@dimonoff.com. Our team will schedule a personalized demonstration of the Smart City Management System.",
            ),
            array(
                "q" => "Does Dimonoff offer pilot projects for municipalities?",
                "a" => "Yes, Dimonoff regularly works with municipalities on pilot projects to demonstrate the value of smart city solutions before full-scale deployment. Contact us to discuss your specific needs.",
            ),
        ),

        // --- Contact FR (ID: 4954) ---
        4954 => array(
            array(
                "q" => "Où est situé Dimonoff ?",
                "a" => "Dimonoff a son siège social au 2820, rue Einstein, Québec, QC G1X 4B7, Canada. Nous desservons les municipalités et les services publics à travers l'Amérique du Nord.",
            ),
            array(
                "q" => "Comment puis-je demander une démo de la plateforme SCMS ?",
                "a" => "Vous pouvez demander une démo en remplissant le formulaire de contact sur cette page, en nous appelant au +1-418-877-7555, ou en écrivant à info@dimonoff.com. Notre équipe organisera une démonstration personnalisée du Smart City Management System.",
            ),
            array(
                "q" => "Dimonoff offre-t-il des projets pilotes ?",
                "a" => "Oui, Dimonoff travaille régulièrement avec les municipalités sur des projets pilotes pour démontrer la valeur des solutions de ville intelligente avant un déploiement à grande échelle. Contactez-nous pour discuter de vos besoins.",
            ),
        ),

        // --- Contact ES (ID: 74091) ---
        74091 => array(
            array(
                "q" => "¿Dónde está ubicado Dimonoff?",
                "a" => "Dimonoff tiene su sede en 2820, rue Einstein, Quebec City, QC G1X 4B7, Canadá. Servimos a municipalidades y servicios públicos en toda América del Norte.",
            ),
            array(
                "q" => "¿Cómo puedo solicitar una demostración de la plataforma SCMS?",
                "a" => "Puede solicitar una demostración completando el formulario de contacto en esta página, llamándonos al +1-418-877-7555, o enviando un correo a info@dimonoff.com.",
            ),
        ),
    );
}
