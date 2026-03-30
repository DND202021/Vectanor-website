<?php
/*
Plugin Name: Dimonoff Accessibility Fixes
Description: WCAG AA contrast fixes and aria-label for unlabeled inputs
Version: 1.0
*/

add_action('wp_head', function() {
    $tag = chr(60) . 'style id="dimonoff-a11y"' . chr(62);
    echo $tag . PHP_EOL;
    echo '.elementor-icon-list-text{color:#c0c8d2}' . PHP_EOL;
    echo '.elementor-widget-icon-list a{color:#c0c8d2}' . PHP_EOL;
    echo '.site-footer a,.footer-widget a{color:#c0c8d2}' . PHP_EOL;
    echo '.skip-link:focus,a.screen-reader-text:focus{clip:auto!important;display:block!important;height:auto;width:auto;position:fixed!important;top:7px;left:7px;z-index:100000;background:#0a1628;color:#fff;padding:15px 23px;font-size:14px;text-decoration:none;box-shadow:0 0 2px 2px rgba(0,0,0,.3)}' . PHP_EOL;
    echo chr(60) . '/style' . chr(62) . PHP_EOL;
}, 2);

add_action('wp_footer', function() {
    if (is_admin()) return;
    $s = chr(60) . 'script id="dimonoff-a11y-aria"' . chr(62);
    $s .= '!function(){var a=document.querySelectorAll("input,textarea");a.forEach(function(e){if(!e.getAttribute("aria-label")){var p=e.getAttribute("placeholder");if(p)e.setAttribute("aria-label",p)}})}()';
    $s .= chr(60) . '/script' . chr(62);
    echo $s . PHP_EOL;
}, 99);
