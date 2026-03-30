<?php
/*
Plugin Name: Dimonoff SEO Titles
Description: Override title tags for key pages via pre_get_document_title (bypasses SmartCrawl)
Version: 1.0
*/

function dimonoff_get_seo_titles() {
    return array(
        48318 => 'Smart City IoT Solutions for Lighting & Infrastructure | Dimonoff',
        79360 => 'Smart Street Lighting Control System | IoT Platform | Dimonoff',
        79365 => 'Systeme de Controle d Eclairage de Rue Intelligent | Dimonoff',
        79372 => 'Sistema de Control de Alumbrado Publico Inteligente | Dimonoff',
        3958  => 'About Dimonoff | Smart City IoT Pioneer Since 2008 | Quebec',
        60677 => 'A propos de Dimonoff | Pionnier IoT Ville Intelligente | Quebec',
        74215 => 'Acerca de Dimonoff | Pioneros en IoT Ciudad Inteligente',
        24    => 'Smart City Solutions | Lighting, Parking & Infrastructure | Dimonoff',
        4950  => 'Solutions Ville Intelligente | Eclairage & Stationnement | Dimonoff',
        74278 => 'Soluciones Ciudad Inteligente | Iluminacion y Estacionamiento | Dimonoff',
    );
}

add_filter('pre_get_document_title', function($title) {
    $titles = dimonoff_get_seo_titles();
    $page_id = get_queried_object_id();
    if (isset($titles[$page_id])) {
        return $titles[$page_id];
    }
    return $title;
}, 999);
