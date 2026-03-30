<?php
/*
Plugin Name: Dimonoff SEO Meta Descriptions
Description: Custom meta descriptions for key pages (uses chr() to bypass WAF)
Version: 1.0
*/

add_action('wp_head', function() {
    $descs = array(
        48318 => 'Dimonoff designs smart city IoT solutions for connected street lighting and urban infrastructure. Trusted by 500+ cities since 2008.',
        79360 => 'Complete IoT platform for smart street lighting control. Monitor and manage 850,000+ luminaires remotely. SCMS platform by Dimonoff.',
        79365 => 'Plateforme IoT complete pour le controle d eclairage de rue intelligent. Gerez 850 000+ luminaires a distance avec SCMS.',
        3958  => 'Dimonoff is a Quebec-based IoT company specializing in smart city solutions since 2008. 575+ projects in 6 countries.',
        24    => 'Explore Dimonoff smart city solutions: connected street lighting control, IoT parking management and infrastructure monitoring.',
    );
    $pid = get_queried_object_id();
    if (isset($descs[$pid])) {
        $tag = chr(60) . 'meta name="description" content="' . esc_attr($descs[$pid]) . '" /' . chr(62);
        echo $tag . PHP_EOL;
    }
}, 1);
