<?php
/**
 * Plugin Name: Dimonoff Font Preload
 * Description: Preloads critical Google Fonts (Poppins, Roboto, Nunito) to improve LCP and reduce FOIT/FOUT.
 * Version: 1.0.0
 * Author: Dimonoff
 *
 * HOW IT WORKS:
 * - Adds <link rel="preload"> tags in <head> for the most-used font weights
 * - Browsers download these fonts early, before CSS parsing triggers them
 * - Only preloads Regular (400) weights to avoid over-fetching
 * - The fonts already use font-display:swap via Google Fonts CSS
 *
 * DEPLOYMENT:
 * Upload this file to: wp-content/mu-plugins/dimonoff-font-preload.php
 * It activates automatically (mu-plugins are always active).
 *
 * SECURITY:
 * - No user input processed
 * - No database queries
 * - Output is hardcoded and escaped
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit; // Prevent direct access
}

/**
 * Outputs preload link tags for critical font files.
 *
 * We preload only the Regular (400) weight of each family since:
 * - It's the most commonly used weight on the page
 * - Preloading too many fonts wastes bandwidth
 * - Other weights load normally via font-display:swap
 *
 * @return void
 */
function dimonoff_preload_critical_fonts() {
    // Critical font files to preload (Regular 400 weight, Latin subset)
    // These URLs point to Google Fonts' CDN (fonts.gstatic.com)
    $fonts = array(
        array(
            'family' => 'Poppins',
            'url'    => 'https://fonts.gstatic.com/s/poppins/v23/pxiByp8kv8JHgFVrLDz8Z1xlEA.ttf',
            'type'   => 'font/ttf',
        ),
        array(
            'family' => 'Roboto',
            'url'    => 'https://fonts.gstatic.com/s/roboto/v48/KFOMCnqEu92Fr1ME7kSn66aGLdTylUAMQXC89YmC2DPNWuaabVmUiA8.ttf',
            'type'   => 'font/ttf',
        ),
        array(
            'family' => 'Nunito',
            'url'    => 'https://fonts.gstatic.com/s/nunito/v31/XRXI3I6Li01BKofiOc5wtlZ2di8HDshdTQ3ig.ttf',
            'type'   => 'font/ttf',
        ),
    );

    echo "\n<!-- Dimonoff: Critical Font Preloading -->\n";
    foreach ( $fonts as $font ) {
        printf(
            '<link rel="preload" href="%s" as="font" type="%s" crossorigin="anonymous"> <!-- %s 400 -->' . "\n",
            esc_url( $font['url'] ),
            esc_attr( $font['type'] ),
            esc_html( $font['family'] )
        );
    }
    echo "<!-- /Dimonoff: Critical Font Preloading -->\n\n";
}

// Hook early in wp_head (priority 1) so preload hints appear before stylesheets
add_action( 'wp_head', 'dimonoff_preload_critical_fonts', 1 );
