<?php
/**
 * Dimonoff Glossary DefinedTermSet Schema Plugin
 *
 * Injects DefinedTermSet JSON-LD schema on the glossary page
 * Defines key IoT, smart city, and product terminology
 *
 * @package Dimonoff_Glossary
 * @version 1.0.0
 */

defined('ABSPATH') || exit;

class Dimonoff_Glossary_Schema {

    private $glossary_terms = array();

    public function __construct() {
        $this->init_hooks();
        $this->setup_terms();
    }

    private function init_hooks() {
        add_action('wp_head', array($this, 'inject_schema'), 99);
    }

    private function setup_terms() {
        $this->glossary_terms = array(
            array(
                'name' => 'SCMS',
                'description' => 'Smart City Management System - Dimonoff unified platform for managing connected city infrastructure including lighting, parking, security, and environmental monitoring.',
                'url' => home_url('/solutions/'),
                'anchor' => 'SCMS',
            ),
            array(
                'name' => 'RME',
                'description' => 'Smart Wireless Lighting Node (external) - Plugs into any photocell receptacle on LED, HPS, MH or MV fixtures. Creates a wireless network for lighting control and IoT connectivity. Communication: DigiMesh, LTE-M, NB-IoT, LoRaWAN.',
                'url' => home_url('/products/led-controllers/'),
                'anchor' => 'RME',
            ),
            array(
                'name' => 'RTM',
                'description' => 'Smart Wireless Lighting Node (internal controller) - Wireless intelligent lighting control for decorative or architectural lighting systems, equipped with analog and digital I/O.',
                'url' => home_url('/products/led-controllers/'),
                'anchor' => 'RTM',
            ),
            array(
                'name' => 'LNLV',
                'description' => 'Smart Wireless Lighting Node (low-voltage controller) - Low-voltage smart wireless lighting node for low-voltage lighting applications.',
                'url' => home_url('/products/led-controllers/'),
                'anchor' => 'LNLV',
            ),
            array(
                'name' => 'Gateway G3+',
                'description' => 'Next-generation IoT gateway providing secure connectivity, data aggregation, and edge processing for Dimonoff SCMS.',
                'url' => home_url('/products/gateway/'),
                'anchor' => 'Gateway G3+',
            ),
            array(
                'name' => 'Spatium',
                'description' => 'Intelligent parking management platform integrated with SCMS. Provides real-time parking availability, dynamic pricing, and occupancy optimization.',
                'url' => home_url('/solutions/smart-parking/'),
                'anchor' => 'Spatium',
            ),
            array(
                'name' => 'CitySafe',
                'description' => 'Dimonoff security solution integrating surveillance, access control, and incident management with SCMS for comprehensive urban security.',
                'url' => home_url('/solutions/security/'),
                'anchor' => 'CitySafe',
            ),
            array(
                'name' => 'CitySense',
                'description' => 'Environmental monitoring solution tracking air quality, noise levels, temperature, and humidity across smart city infrastructure.',
                'url' => home_url('/solutions/environment/'),
                'anchor' => 'CitySense',
            ),
            array(
                'name' => 'CitySound',
                'description' => 'Acoustic management solution for urban areas, monitoring and controlling noise pollution with real-time alerts.',
                'url' => home_url('/solutions/experience/'),
                'anchor' => 'CitySound',
            ),
            array(
                'name' => 'DOO Express',
                'description' => 'IoT asset management software platform - easy, cost-effective alternative to SCMS for smaller applications. Remotely controls lights, cameras, GPS trackers, sensors and connected devices.',
                'url' => home_url('/solutions/'),
                'anchor' => 'DOO Express',
            ),
            array(
                'name' => 'IoT',
                'description' => 'Internet of Things - Network of interconnected physical devices embedded with sensors, software, and communication capabilities.',
                'url' => home_url('/about/'),
                'anchor' => 'IoT',
            ),
            array(
                'name' => 'Smart City',
                'description' => 'Urban area using IoT sensors, data analytics, and automated systems to optimize infrastructure, services, and citizen experience.',
                'url' => home_url('/solutions/'),
                'anchor' => 'Smart City',
            ),
            array(
                'name' => 'Edge Computing',
                'description' => 'Processing data at network edge (gateway/device level) rather than cloud, reducing latency and bandwidth requirements.',
                'url' => home_url('/products/gateway/'),
                'anchor' => 'Edge Computing',
            ),
            array(
                'name' => 'Real-Time Monitoring',
                'description' => 'Continuous collection and analysis of device data, providing immediate visibility into system performance and status.',
                'url' => home_url('/solutions/'),
                'anchor' => 'Real-Time Monitoring',
            ),
            array(
                'name' => 'Data Aggregation',
                'description' => 'Collecting and combining sensor data from multiple sources into unified datasets for analysis and decision-making.',
                'url' => home_url('/solutions/'),
                'anchor' => 'Data Aggregation',
            ),
            array(
                'name' => 'Connectivity',
                'description' => 'Ability of IoT devices to communicate using wireless or wired protocols including TALQ, DALI, and LoRaWAN.',
                'url' => home_url('/products/'),
                'anchor' => 'Connectivity',
            ),
            array(
                'name' => 'Occupancy Optimization',
                'description' => 'Using sensor data to understand and improve space utilization including parking availability and traffic flow.',
                'url' => home_url('/solutions/smart-parking/'),
                'anchor' => 'Occupancy Optimization',
            ),
            array(
                'name' => 'Adaptive Lighting',
                'description' => 'Dynamic control of street lighting intensity based on traffic, weather, and time - reducing energy while maintaining safety.',
                'url' => home_url('/solutions/smart-lighting/'),
                'anchor' => 'Adaptive Lighting',
            ),
            array(
                'name' => 'TALQ',
                'description' => 'Telecommunications and Lighting - Open standard for street lighting device communication and management.',
                'url' => home_url('/products/gateway/'),
                'anchor' => 'TALQ',
            ),
            array(
                'name' => 'DALI',
                'description' => 'Digital Addressable Lighting Interface - Protocol for controlling individual light fixtures with precise dimming and status feedback.',
                'url' => home_url('/products/led-controllers/'),
                'anchor' => 'DALI',
            ),
            array(
                'name' => 'Zhaga Book 18',
                'description' => 'Standard specifying smart outdoor lighting module interfaces, enabling interoperability between manufacturers.',
                'url' => home_url('/products/'),
                'anchor' => 'Zhaga Book 18',
            ),
            array(
                'name' => 'ANSI C136.41',
                'description' => 'American National Standard for wireless communication protocols in outdoor lighting and electrical delivery systems.',
                'url' => home_url('/products/'),
                'anchor' => 'ANSI C136.41',
            ),
            array(
                'name' => 'LoRaWAN',
                'description' => 'Long Range Wide Area Network - Low-power, wide-range wireless protocol ideal for IoT sensor networks in smart cities.',
                'url' => home_url('/solutions/'),
                'anchor' => 'LoRaWAN',
            ),
            array(
                'name' => 'MQTT',
                'description' => 'Message Queuing Telemetry Transport - Lightweight protocol for device-to-cloud communication with minimal bandwidth.',
                'url' => home_url('/products/gateway/'),
                'anchor' => 'MQTT',
            ),
            array(
                'name' => 'Smart Lighting',
                'description' => 'Connected street and facility lighting systems that automatically adjust brightness, color, and timing based on real-time conditions.',
                'url' => home_url('/solutions/smart-lighting/'),
                'anchor' => 'Smart Lighting',
            ),
            array(
                'name' => 'Energy Efficiency',
                'description' => 'Optimizing energy consumption while maintaining or improving service quality, core principle of Dimonoff solutions.',
                'url' => home_url('/solutions/'),
                'anchor' => 'Energy Efficiency',
            ),
            array(
                'name' => 'Dimming Control',
                'description' => 'Automatic reduction of light intensity based on traffic sensors, time of day, or weather conditions.',
                'url' => home_url('/products/led-controllers/'),
                'anchor' => 'Dimming Control',
            ),
            array(
                'name' => 'Power Management',
                'description' => 'Monitoring and optimizing power consumption across networked devices to reduce operating costs.',
                'url' => home_url('/solutions/'),
                'anchor' => 'Power Management',
            ),
        );
    }

    public function inject_schema() {
        if (!$this->is_glossary_page()) {
            return;
        }

        $schema = $this->build_defined_term_set();
        $json = wp_json_encode($schema);

        if (!$json) {
            error_log('Dimonoff Glossary: Failed to encode schema as JSON');
            return;
        }

        echo PHP_EOL . '<script type="application/ld+json">' . PHP_EOL;
        echo $json;
        echo PHP_EOL . '</script>' . PHP_EOL;
    }

    private function is_glossary_page() {
        if (is_admin()) {
            return false;
        }

        $current_url = home_url($this->get_current_path());

        $glossary_urls = array(
            home_url('/glossary/'),
            home_url('/fr/glossaire/'),
            home_url('/es/glosario/'),
        );

        foreach ($glossary_urls as $glossary_url) {
            if (strpos($current_url, $glossary_url) === 0) {
                return true;
            }
        }

        return false;
    }

    private function get_current_path() {
        // Use WordPress global instead of server superglobals (WAF-safe)
        global $wp;
        if ( isset( $wp->request ) && $wp->request !== '' ) {
            return '/' . $wp->request . '/';
        }
        return '/';
    }

    private function build_defined_term_set() {
        $glossary_url = home_url('/glossary/');

        $has_defined_terms = array();

        foreach ($this->glossary_terms as $term) {
            $has_defined_terms[] = array(
                '@type' => 'DefinedTerm',
                'name' => $term['name'],
                'description' => $term['description'],
                'url' => $glossary_url . '#' . sanitize_title($term['name']),
                'inDefinedTermSet' => $glossary_url,
            );
        }

        $schema = array(
            '@context' => 'https://schema.org',
            '@type' => 'DefinedTermSet',
            'name' => 'Smart City and IoT Glossary',
            'description' => 'Comprehensive definitions of key IoT, smart city, and lighting terminology used by Dimonoff.',
            'url' => $glossary_url,
            'inLanguage' => 'en',
            'hasDefinedTerm' => $has_defined_terms,
        );

        return $schema;
    }
}

if (!is_admin() || (defined('DOING_AJAX') && DOING_AJAX)) {
    new Dimonoff_Glossary_Schema();
}
