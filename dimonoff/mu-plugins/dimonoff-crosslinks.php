<?php
/**
 * Dimonoff Cross-Links — Groupe Vectanor Ecosystem
 *
 * Injects a lightweight footer bar linking to Groupe Vectanor
 * subsidiaries (Spatium, Amotus, Vectanor).
 * Language is detected via Polylang; defaults to English.
 *
 * @package Dimonoff_CrossLinks
 * @version 1.0.0
 */

defined('ABSPATH') || exit;

/**
 * Render the Groupe Vectanor ecosystem bar just before wp_footer.
 *
 * Hooked at priority 5 so it appears before most footer scripts
 * but after the theme footer template.
 *
 * @return void
 */
function dimonoff_crosslinks_footer() {

    // Skip admin and REST/AJAX contexts
    if ( is_admin() ) {
        return;
    }

    $lang = dimonoff_crosslinks_get_lang();

    $labels = dimonoff_crosslinks_labels( $lang );

    // Build the HTML bar
    // Using inline styles to avoid dependency on theme CSS
    echo '<div id="vectanor-ecosystem" style="background:#1a1a2e;padding:18px 0;text-align:center;font-family:inherit;font-size:13px;border-top:1px solid #2d2d44;">';
    echo '<div style="max-width:1200px;margin:0 auto;padding:0 20px;">';

    // Heading
    echo '<span style="color:#8892b0;margin-right:16px;">' . esc_html( $labels['heading'] ) . '</span>';

    // Links
    $links = dimonoff_crosslinks_links( $labels );
    $separator = ' <span style="color:#4a4a6a;margin:0 8px;">|</span> ';

    $link_html = array();
    foreach ( $links as $link ) {
        $link_html[] = '<a href="' . esc_url( $link['url'] ) . '" '
            . 'rel="noopener" '
            . 'target="_blank" '
            . 'style="color:#ccd6f6;text-decoration:none;transition:color 0.2s;" '
            . 'onmouseover="this.style.color=\'#64ffda\'" '
            . 'onmouseout="this.style.color=\'#ccd6f6\'">'
            . esc_html( $link['label'] )
            . '</a>';
    }

    echo implode( $separator, $link_html );

    echo '</div>';
    echo '</div>';
}
add_action( 'wp_footer', 'dimonoff_crosslinks_footer', 5 );


/**
 * Detect the current page language via Polylang.
 *
 * Falls back to 'en' when Polylang is not active.
 *
 * @return string Two-letter language code (en, fr, es).
 */
function dimonoff_crosslinks_get_lang() {
    if ( function_exists( 'pll_current_language' ) ) {
        $lang = pll_current_language( 'slug' );
        if ( in_array( $lang, array( 'en', 'fr', 'es' ), true ) ) {
            return $lang;
        }
    }
    return 'en';
}


/**
 * Return translated labels for the ecosystem bar.
 *
 * @param string $lang Two-letter language code.
 * @return array Associative array of labels.
 */
function dimonoff_crosslinks_labels( $lang ) {

    $all = array(
        'en' => array(
            'heading'  => 'Part of Groupe Vectanor:',
            'vectanor' => 'Groupe Vectanor',
            'spatium'  => 'Intelligent Parking (Spatium)',
            'amotus'   => 'IoT Engineering (Amotus)',
        ),
        'fr' => array(
            'heading'  => 'Membre du Groupe Vectanor :',
            'vectanor' => 'Groupe Vectanor',
            'spatium'  => 'Stationnement intelligent (Spatium)',
            'amotus'   => 'Ingenierie IoT (Amotus)',
        ),
        'es' => array(
            'heading'  => 'Parte del Grupo Vectanor:',
            'vectanor' => 'Grupo Vectanor',
            'spatium'  => 'Estacionamiento inteligente (Spatium)',
            'amotus'   => 'Ingenieria IoT (Amotus)',
        ),
    );

    return isset( $all[ $lang ] ) ? $all[ $lang ] : $all['en'];
}


/**
 * Return the link data for the ecosystem bar.
 *
 * @param array $labels The translated labels.
 * @return array List of link arrays with 'url' and 'label' keys.
 */
function dimonoff_crosslinks_links( $labels ) {
    return array(
        array(
            'url'   => 'https://vectanor.com',
            'label' => $labels['vectanor'],
        ),
        array(
            'url'   => 'https://spatium-iot.com',
            'label' => $labels['spatium'],
        ),
        array(
            'url'   => 'https://amotus.com',
            'label' => $labels['amotus'],
        ),
    );
}
