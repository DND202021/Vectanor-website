# Regles de deploiement — Groupe Vectanor

## Regles critiques

1. **Ne JAMAIS inventer** de definitions, acronymes ou faits. Verifier sur le site ou demander a Daniel.

2. **Ne JAMAIS deployer** quand l'equipe IT est indisponible (lunch, apres les heures). Confirmer la disponibilite IT avant tout deploiement.

3. **Ne JAMAIS editer `_elementor_data`** directement. Utiliser l'editeur visuel Elementor via Chrome.

4. **Mu-plugins via elFinder** : les fichiers PHP doivent contenir ZERO backslash (a cause de `stripslashes()`).

5. **Tester d'abord** : deployer un mu-plugin "hello world" minimal avant tout nouveau deploiement important.

6. **Fichiers > 10KB** : doivent etre encodes en base64 et splits en chunks ~9100 chars pour elFinder.

## Methode de deploiement elFinder

1. Ecrire le PHP localement
2. Valider : zero backslashes, pas de patterns WAF (`$_SERVER`)
3. Encoder en Base64
4. Dans Chrome console : `atob()` + `TextDecoder('utf-8')` pour decoder
5. elFinder `put` pour ecrire le fichier
6. Verifier que la taille serveur correspond
7. Health check HTTP sur le site

## Patterns WAF a eviter (HostGator)

- `$_SERVER['REQUEST_URI']` → utiliser `global $wp; $wp->request` ou `get_permalink()`
- Certains patterns de code inline peuvent declencher ModSecurity HTTP 406

## Cache Elementor

`Elementor\Plugin::$instance->files_manager->clear_cache()` est le SEUL moyen fiable de purger le cache de rendu. Hummingbird, "Clear Files & Data", et les transients ne suffisent PAS.

## Derniere mise a jour
2026-03-27
