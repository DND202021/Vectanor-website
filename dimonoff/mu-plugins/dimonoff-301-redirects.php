<?php
/*
Plugin Name: Dimonoff 301 Redirects
Description: Pattern-based 301 redirects for old deleted pages
Version: 1.0
*/

add_action('template_redirect', function() {
    if (!is_404()) return;

    $path = trim(wp_parse_url(add_query_arg(array()), PHP_URL_PATH), '/');

    if (strpos($path, 'resources/business-cases') === 0) {
        wp_redirect(home_url('/resources/'), 301);
        exit;
    }
    if (strpos($path, 'fr/ressources/etudes-de-cas') === 0) {
        wp_redirect(home_url('/fr/ressources/'), 301);
        exit;
    }
    if (strpos($path, 'news/') === 0) {
        wp_redirect(home_url('/news/'), 301);
        exit;
    }
    if (strpos($path, 'fr/nouvelles/') === 0) {
        wp_redirect(home_url('/fr/nouvelles/'), 301);
        exit;
    }
    if (strpos($path, 'es/noticias/') === 0) {
        wp_redirect(home_url('/es/noticias/'), 301);
        exit;
    }
    if (strpos($path, 'products/') === 0) {
        wp_redirect(home_url('/solutions/'), 301);
        exit;
    }
    if (strpos($path, 'category/') === 0) {
        wp_redirect(home_url('/news/'), 301);
        exit;
    }
    if ($path === 'about-dimonoff') {
        wp_redirect(home_url('/about-us/'), 301);
        exit;
    }
});
