<?php
/**
 * Plugin Name: Dimonoff Product Schema
 * Description: Injects Product JSON-LD schema on product pages.
 * Version: 1.0.0
 * Author: Dimonoff
 *
 * NOTE: Zero backslashes. Uses WordPress permalink instead of server vars.
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

/**
 * Inject Product JSON-LD on matching product pages.
 *
 * Matches the current URL path against known product slugs.
 * Uses WordPress functions only (no server superglobals) for WAF compatibility.
 *
 * @return void
 */
function dimonoff_product_schema() {
    if ( is_admin() ) {
        return;
    }

    $current_url = home_url( add_query_arg( array() ) );
    if ( empty( $current_url ) ) {
        $current_url = get_permalink();
    }
    if ( empty( $current_url ) ) {
        return;
    }

    $products = dimonoff_get_product_list();

    foreach ( $products as $product ) {
        if ( strpos( $current_url, $product["slug"] ) !== false ) {
            dimonoff_output_product_schema( $product );
            return;
        }
    }
}
add_action( 'wp_head', 'dimonoff_product_schema', 2 );

/**
 * Output the Product JSON-LD schema markup.
 *
 * @param array $product Product data array.
 * @return void
 */
function dimonoff_output_product_schema( $product ) {
    $site_url = get_site_url();
    $product_url = $site_url . $product["url"];

    $schema = array(
        "@context"     => "https://schema.org",
        "@type"        => "Product",
        "name"         => $product["name"],
        "description"  => $product["description"],
        "url"          => $product_url,
        "brand"        => array(
            "@type" => "Brand",
            "name"  => "Dimonoff",
        ),
        "manufacturer" => array(
            "@type" => "Organization",
            "name"  => "Dimonoff",
        ),
        "category"     => $product["category"],
    );

    $json = wp_json_encode( $schema, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT );

    echo '<script type="application/ld+json">' . PHP_EOL;
    echo $json . PHP_EOL;
    echo '</script>' . PHP_EOL;
}

/**
 * Return the list of Dimonoff products with their metadata.
 *
 * @return array
 */
function dimonoff_get_product_list() {
    return array(
        array(
            "slug"        => "scms",
            "name"        => "SCMS Platform",
            "description" => "Smart City Management System platform - comprehensive IoT solution for intelligent smart lighting and smart city applications",
            "url"         => "/solutions/smart-lighting-control/products/iot-platforms/scms/",
            "category"    => "IoT Platform",
        ),
        array(
            "slug"        => "doo-express",
            "name"        => "DOO Express Platform",
            "description" => "DOO Express - easy, cost-effective IoT asset management software platform for remotely controlling lights, cameras, sensors and connected devices",
            "url"         => "/solutions/smart-lighting-control/products/iot-platforms/doo-express/",
            "category"    => "IoT Platform",
        ),
        array(
            "slug"        => "mobile-application",
            "name"        => "Mobile Application",
            "description" => "Mobile application for smart lighting control and system management - iOS and Android compatible",
            "url"         => "/solutions/smart-lighting-control/products/iot-platforms/mobile-application/",
            "category"    => "Software",
        ),
        array(
            "slug"        => "g3",
            "name"        => "Gateway G3+",
            "description" => "Advanced IoT gateway for smart lighting control with enhanced connectivity and processing capabilities",
            "url"         => "/solutions/smart-lighting-control/products/iot-gateways/g3/",
            "category"    => "IoT Gateway",
        ),
        array(
            "slug"        => "rme-external-controller",
            "name"        => "RME: Smart Wireless Lighting Node",
            "description" => "RME-H3 smart wireless external lighting node - plugs into any photocell receptacle, compatible with LED, HPS, MH and MV fixtures. Multiple communication options including DigiMesh, LTE-M, NB-IoT, LoRaWAN",
            "url"         => "/solutions/smart-lighting-control/products/wireless-nodes/rme-external-controller/",
            "category"    => "Wireless Node",
        ),
        array(
            "slug"        => "rtm-internal-controller",
            "name"        => "RTM: Smart Wireless Lighting Node",
            "description" => "Wireless intelligent lighting control for decorative or architectural lighting systems, equipped with analog and digital I/O",
            "url"         => "/solutions/smart-lighting-control/products/wireless-nodes/rtm-internal-controller/",
            "category"    => "Wireless Node",
        ),
        array(
            "slug"        => "lnlv-low-voltage-controller",
            "name"        => "LNLV: Smart Wireless Lighting Node",
            "description" => "Low-voltage smart wireless lighting node for low-voltage lighting applications",
            "url"         => "/solutions/smart-lighting-control/products/wireless-nodes/lnlv-low-voltage-controller/",
            "category"    => "Wireless Node",
        ),
    );
}
