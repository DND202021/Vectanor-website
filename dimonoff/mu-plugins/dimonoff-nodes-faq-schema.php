<?php
/**
 * Plugin Name: Dimonoff Nodes FAQ Schema
 * Description: FAQPage JSON-LD on wireless nodes landing page (EN/FR) for AEO/GEO
 * Version: 1.0.0
 * Author: Dimonoff
 *
 * NOTE: Zero backslashes. Uses permalink matching.
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

function dimonoff_nodes_faq_schema() {
    if ( ! is_singular() ) {
        return;
    }

    $current_url = get_permalink();
    if ( empty( $current_url ) ) {
        return;
    }

    $is_en = strpos( $current_url, 'wireless-nodes' ) !== false
          && strpos( $current_url, 'rme-' ) === false
          && strpos( $current_url, 'rtm-' ) === false
          && strpos( $current_url, 'lnlv-' ) === false;

    $is_fr = strpos( $current_url, 'noeuds-sans-fil' ) !== false
          && strpos( $current_url, 'rme-' ) === false
          && strpos( $current_url, 'rtm-' ) === false
          && strpos( $current_url, 'lnlv-' ) === false;

    if ( ! $is_en && ! $is_fr ) {
        return;
    }

    if ( $is_fr ) {
        $faq = dimonoff_nodes_faq_fr();
    } else {
        $faq = dimonoff_nodes_faq_en();
    }

    $json = wp_json_encode( $faq, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT );

    echo '<script type="application/ld+json">' . PHP_EOL;
    echo $json . PHP_EOL;
    echo '</script>' . PHP_EOL;
}
add_action( 'wp_head', 'dimonoff_nodes_faq_schema', 3 );

function dimonoff_nodes_faq_en() {
    return array(
        "@context" => "https://schema.org",
        "@type" => "FAQPage",
        "mainEntity" => array(
            array(
                "@type" => "Question",
                "name" => "What is the difference between the RME, RTM and LNLV smart lighting nodes?",
                "acceptedAnswer" => array(
                    "@type" => "Answer",
                    "text" => "The RME is an external retrofit controller that plugs into standard ANSI C136.41 or Zhaga Book 18 photocell receptacles, compatible with LED, HPS, MH and MV fixtures. The RTM is an internal controller designed for decorative and architectural lighting with RGBW capability. The LNLV is a low-voltage node for solar-powered and off-grid lighting applications. All three connect to the SCMS cloud platform for centralized management."
                )
            ),
            array(
                "@type" => "Question",
                "name" => "Are Dimonoff smart lighting nodes compatible with Wi-SUN FAN?",
                "acceptedAnswer" => array(
                    "@type" => "Answer",
                    "text" => "Yes. As a Contributing Member of the Wi-SUN Alliance, Dimonoff is integrating Wi-SUN FAN connectivity into its next-generation node series. Wi-SUN FAN provides self-forming, self-healing mesh networking based on open IEEE 802.15.4 and IPv6 standards, with enterprise-grade security including X.509 certificates and AES-CCM encryption."
                )
            ),
            array(
                "@type" => "Question",
                "name" => "How do Dimonoff nodes prevent vendor lock-in?",
                "acceptedAnswer" => array(
                    "@type" => "Answer",
                    "text" => "Dimonoff nodes are certified to open industry standards (ANSI C136.41, Zhaga Book 18, Wi-SUN FAN) ensuring interoperability with other certified equipment. Cities are not locked into a single vendor ecosystem. The SCMS platform open API architecture further enables integration with third-party systems and data platforms."
                )
            ),
            array(
                "@type" => "Question",
                "name" => "What is the typical ROI for smart street lighting with Dimonoff nodes?",
                "acceptedAnswer" => array(
                    "@type" => "Answer",
                    "text" => "Municipalities typically achieve ROI within 3 to 5 years, with up to 50% reduction in electricity costs and 40% reduction in maintenance costs. For example, the City of Laval saves CA 2.75 million annually across 37,000 luminaires, and the FQM collective project covering 145,000 streetlights generates 6.8 million in annual savings."
                )
            ),
            array(
                "@type" => "Question",
                "name" => "Can I purchase Dimonoff nodes through a government cooperative contract?",
                "acceptedAnswer" => array(
                    "@type" => "Answer",
                    "text" => "Yes. Dimonoff solutions are available through the Sourcewell cooperative purchasing contract #041525-DIMN, valid through July 2029. This enables government agencies across North America to procure without lengthy RFP processes."
                )
            ),
            array(
                "@type" => "Question",
                "name" => "What communication protocols do Dimonoff wireless nodes support?",
                "acceptedAnswer" => array(
                    "@type" => "Answer",
                    "text" => "Dimonoff nodes support multiple protocols to match your infrastructure requirements: DigiMesh for proven mesh networking, LoRaWAN for long-range LPWAN, LTE-M and NB-IoT for cellular IoT, and Wi-SUN FAN for open-standard interoperable mesh. The Gateway G3+ aggregates up to 1,000 nodes with NEMA 4X (IP66) protection."
                )
            ),
        ),
    );
}

function dimonoff_nodes_faq_fr() {
    return array(
        "@context" => "https://schema.org",
        "@type" => "FAQPage",
        "mainEntity" => array(
            array(
                "@type" => "Question",
                "name" => "Quelle est la difference entre les noeuds intelligents RME, RTM et LNLV?",
                "acceptedAnswer" => array(
                    "@type" => "Answer",
                    "text" => "Le RME est un controleur externe de retrofit qui se branche dans les receptacles de photocellules standards ANSI C136.41 ou Zhaga Book 18, compatible avec les luminaires DEL, HPS, MH et MV. Le RTM est un controleur interne concu pour l eclairage decoratif et architectural avec capacite RGBW. Le LNLV est un noeud basse tension pour les applications d eclairage solaire et hors reseau. Les trois se connectent a la plateforme cloud SCMS pour une gestion centralisee."
                )
            ),
            array(
                "@type" => "Question",
                "name" => "Les noeuds d eclairage intelligent Dimonoff sont-ils compatibles Wi-SUN FAN?",
                "acceptedAnswer" => array(
                    "@type" => "Answer",
                    "text" => "Oui. En tant que membre contributeur de la Wi-SUN Alliance, Dimonoff integre la connectivite Wi-SUN FAN dans sa serie de noeuds de nouvelle generation. Wi-SUN FAN fournit un reseau maille auto-formant et auto-reparateur base sur les standards ouverts IEEE 802.15.4 et IPv6, avec une securite de grade entreprise incluant les certificats X.509 et le chiffrement AES-CCM."
                )
            ),
            array(
                "@type" => "Question",
                "name" => "Comment les noeuds Dimonoff previennent-ils la dependance fournisseur?",
                "acceptedAnswer" => array(
                    "@type" => "Answer",
                    "text" => "Les noeuds Dimonoff sont certifies selon des standards industriels ouverts (ANSI C136.41, Zhaga Book 18, Wi-SUN FAN) assurant l interoperabilite avec d autres equipements certifies. Les villes ne sont pas enfermees dans l ecosysteme d un seul fournisseur. L architecture API ouverte de la plateforme SCMS permet aussi l integration avec des systemes et plateformes de donnees tiers."
                )
            ),
            array(
                "@type" => "Question",
                "name" => "Quel est le ROI typique pour l eclairage de rue intelligent avec les noeuds Dimonoff?",
                "acceptedAnswer" => array(
                    "@type" => "Answer",
                    "text" => "Les municipalites atteignent typiquement un ROI en 3 a 5 ans, avec une reduction de 50% des couts d electricite et de 40% des couts de maintenance. Par exemple, la Ville de Laval economise 2,75 M CA annuellement sur 37 000 luminaires, et le projet collectif FQM couvrant 145 000 lampadaires genere 6,8 M en economies annuelles."
                )
            ),
            array(
                "@type" => "Question",
                "name" => "Peut-on acheter les noeuds Dimonoff via un contrat d achat cooperatif gouvernemental?",
                "acceptedAnswer" => array(
                    "@type" => "Answer",
                    "text" => "Oui. Les solutions Dimonoff sont disponibles via le contrat d achat cooperatif Sourcewell #041525-DIMN, valide jusqu en juillet 2029. Ceci permet aux agences gouvernementales a travers l Amerique du Nord de se procurer les solutions sans processus d appel d offres prolonge."
                )
            ),
            array(
                "@type" => "Question",
                "name" => "Quels protocoles de communication les noeuds sans fil Dimonoff supportent-ils?",
                "acceptedAnswer" => array(
                    "@type" => "Answer",
                    "text" => "Les noeuds Dimonoff supportent de multiples protocoles pour correspondre a vos besoins d infrastructure : DigiMesh pour le reseau maille eprouve, LoRaWAN pour le LPWAN longue portee, LTE-M et NB-IoT pour l IoT cellulaire, et Wi-SUN FAN pour le reseau maille interoperable a standard ouvert. La passerelle G3+ agregue jusqu a 1 000 noeuds avec une protection NEMA 4X (IP66)."
                )
            ),
        ),
    );
}
