<?php
/**
 * Plugin Name: Dimonoff Nodes ProductGroup Schema
 * Description: ProductGroup JSON-LD on wireless nodes overview page (EN/FR)
 * Version: 1.0.0
 * Author: Dimonoff
 *
 * NOTE: Zero backslashes. Uses permalink matching.
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

function dimonoff_nodes_productgroup_schema() {
    if ( ! is_singular() ) {
        return;
    }

    $current_url = get_permalink();
    if ( empty( $current_url ) ) {
        return;
    }

    $is_nodes_overview = ( strpos( $current_url, 'wireless-nodes' ) !== false
                        || strpos( $current_url, 'noeuds-sans-fil' ) !== false )
                      && strpos( $current_url, 'rme-' ) === false
                      && strpos( $current_url, 'rtm-' ) === false
                      && strpos( $current_url, 'lnlv-' ) === false;

    if ( ! $is_nodes_overview ) {
        return;
    }

    $site_url = get_site_url();

    $schema = array(
        "@context" => "https://schema.org",
        "@type" => "ProductGroup",
        "name" => "Smart Wireless Lighting Nodes",
        "description" => "Next-generation smart wireless lighting controllers for municipal street lighting. Wi-SUN FAN ready, ANSI C136.41 certified, multi-protocol connectivity.",
        "brand" => array(
            "@type" => "Brand",
            "name" => "Dimonoff"
        ),
        "manufacturer" => array(
            "@type" => "Organization",
            "name" => "Dimonoff",
            "url" => $site_url
        ),
        "hasVariant" => array(
            array(
                "@type" => "Product",
                "name" => "RME Smart Wireless Lighting Node",
                "description" => "External smart controller for retrofit street lighting. Plugs into any ANSI C136.41 or Zhaga Book 18 photocell receptacle. Compatible with LED, HPS, MH and MV fixtures.",
                "url" => $site_url . "/solutions/smart-lighting-control/products/wireless-nodes/rme-external-controller/",
                "category" => "Smart Lighting Controller",
                "additionalProperty" => array(
                    array( "@type" => "PropertyValue", "name" => "Controller Type", "value" => "External (retrofit)" ),
                    array( "@type" => "PropertyValue", "name" => "Connectivity", "value" => "DigiMesh, LTE-M, NB-IoT, LoRaWAN, Wi-SUN FAN" ),
                    array( "@type" => "PropertyValue", "name" => "Certification", "value" => "ANSI C136.41, Zhaga Book 18" ),
                    array( "@type" => "PropertyValue", "name" => "Fixture Compatibility", "value" => "LED, HPS, MH, MV" )
                )
            ),
            array(
                "@type" => "Product",
                "name" => "RTM Smart Wireless Lighting Node",
                "description" => "Internal smart controller for decorative and architectural lighting with RGBW capability and analog/digital I/O.",
                "url" => $site_url . "/solutions/smart-lighting-control/products/wireless-nodes/rtm-internal-controller/",
                "category" => "Smart Lighting Controller",
                "additionalProperty" => array(
                    array( "@type" => "PropertyValue", "name" => "Controller Type", "value" => "Internal (embedded)" ),
                    array( "@type" => "PropertyValue", "name" => "Special Feature", "value" => "RGBW architectural lighting" ),
                    array( "@type" => "PropertyValue", "name" => "I/O", "value" => "Analog and digital input/output" )
                )
            ),
            array(
                "@type" => "Product",
                "name" => "LNLV Smart Wireless Lighting Node",
                "description" => "Low-voltage smart wireless node for solar-powered and low-voltage lighting applications.",
                "url" => $site_url . "/solutions/smart-lighting-control/products/wireless-nodes/lnlv-low-voltage-controller/",
                "category" => "Smart Lighting Controller",
                "additionalProperty" => array(
                    array( "@type" => "PropertyValue", "name" => "Controller Type", "value" => "Low-voltage" ),
                    array( "@type" => "PropertyValue", "name" => "Application", "value" => "Solar-powered and low-voltage systems" )
                )
            )
        ),
        "offers" => array(
            "@type" => "Offer",
            "availability" => "https://schema.org/InStock",
            "seller" => array(
                "@type" => "Organization",
                "name" => "Dimonoff"
            )
        ),
        "award" => array(
            "2024 Smart City Product of the Year",
            "2024 IoT Security Excellence Award",
            "2025 Digi Green Tech Award"
        ),
        "isRelatedTo" => array(
            "@type" => "Product",
            "name" => "SCMS - Smart City Management System",
            "url" => $site_url . "/solutions/smart-lighting-control/products/iot-platforms/scms/"
        )
    );

    $json = wp_json_encode( $schema, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT );

    echo '<script type="application/ld+json">' . PHP_EOL;
    echo $json . PHP_EOL;
    echo '</script>' . PHP_EOL;
}
add_action( 'wp_head', 'dimonoff_nodes_productgroup_schema', 3 );
