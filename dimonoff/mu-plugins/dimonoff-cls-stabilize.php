<?php
/*
Plugin Name: Dimonoff CLS Stabilization
Description: Reduce CLS on desktop by stabilizing Elementor sections
Version: 1.0
*/

add_action("wp_head", function() {
    echo '<style id="dimonoff-cls-stabilize">
.elementor-section-wrap>.elementor-section,.elementor>.e-con{contain:layout style}
.elementor-section-wrap>.elementor-section:first-child,.elementor>.e-con:first-child{min-height:600px}
.elementor-widget{contain:layout style}
.elementor-widget-image img{content-visibility:auto}
@media(min-width:1025px){
.elementor-section-wrap>.elementor-section~.elementor-section~.elementor-section~.elementor-section,
.elementor>.e-con~.e-con~.e-con~.e-con{content-visibility:auto;contain-intrinsic-size:auto 500px}
}
</style>' . PHP_EOL;
}, 1);
