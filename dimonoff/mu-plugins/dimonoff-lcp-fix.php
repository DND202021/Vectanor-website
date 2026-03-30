<?php
/*
Plugin Name: Dimonoff LCP Fix
Description: Preload hero image and optimize fonts for LCP
Version: 1.0
*/

add_action("wp_head", function() {
    if (is_front_page()) {
        $hero_url = "/wp-content/uploads/2024/09/Remote-Control-Asset-Management-Lighting-1024x715.png";
        echo '<link rel="preload" as="image" href="' . esc_url($hero_url) . '" type="image/png">' . PHP_EOL;
    }
}, 1);

add_filter("style_loader_src", function($val) {
    if (strpos($val, "fonts.googleapis.com") !== false) {
        $val = str_replace("display=swap", "display=optional", $val);
    }
    return $val;
}, 100);
