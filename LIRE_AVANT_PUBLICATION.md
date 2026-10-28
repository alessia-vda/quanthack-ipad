# Quants Court Studio V3 — installation iPad / GitHub Pages

## Ce qui change
- Le design Studio actuel est conservé, sombre par défaut, clair disponible.
- Les 9 rooms F0 à F8 sont intégrées dans Studio, avec un accès retour visible, sans quitter l’application.
- Une carte du parcours montre des ronds et une mascotte qui avance quand une room classique atteint 80 % de réussite.
- Le nouveau logo est pris en charge par l’icône iPad et le manifeste PWA.
- 8 exercices numériques, 6 exercices Python progressifs (Pyodide), références professionnelles, feuille de route des 3 métiers quant.
- Les 37 notions, 74 QCM et 111 flashcards existants sont conservés.

## Publication
1. Sauvegarder sa progression **avant** la mise à jour (export depuis la version classique).
2. Sur GitHub, aller au dépôt `alessia-vda/quanthack-ipad`, onglet `Code` > `Add file` > `Upload files`.
3. Importer les **fichiers à la racine** (pas le dossier ni l’archive ZIP). Remplacer ceux de même nom et conserver les fichiers non concernés.
4. Cliquer sur `Commit changes` sur `main`. Attendre une coche verte dans `Actions` (publication GitHub Pages).
5. Ouvrir le site dans Safari pour vérifier, puis fermer/réouvrir l’application de l’écran d’accueil. Si elle conserve l’ancienne version, rafraîchir via le bouton ↻.

## Important
L’assistant connecté à GitHub n’a actuellement **pas la permission d’écriture** (erreur HTTP 403). Les archives ci-jointes ont donc été préparées localement, pas publiées sur ton dépôt.
La section `Expliquer soi-même` est une auto-évaluation selon des critères, **pas** une correction par IA. Une correction IA nécessiterait une API derrière un serveur sécurisé, non une clé OpenAI dans GitHub Pages.
La progression Studio et celle de l’application classique ont deux sauvegardes différentes, inchangées pour assurer la continuité.
Python utilise Pyodide et charge des fichiers externes, avec connexion requise pour le premier lancement.
Les parcours quant avancés sont encore une feuille de route, pas un cursus complet déjà disponible.
Les références professionnelles sont thématiques : aucune certification ni validation officielle n’est revendiquée.

## Version complète ou mise à jour ?
- `Quants_Court_V3_MAJ_GitHub.zip`: utiliser pour mettre à jour le dépôt existant, 11 fichiers.
- `Quants_Court_V3_SITE_COMPLET.zip`: 18 fichiers, installation complète.
