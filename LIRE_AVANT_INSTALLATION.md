# Quants Court Studio — rooms unifiées (V4)

Cette mise à jour conserve le design Studio de Quants Court, les 37 notions, les révisions, les ateliers Python et les contenus originaux des neuf rooms F0–F8.

## Nouveautés

- **Rooms** : cartes illustrées dans le même style que les six thèmes de l’accueil.
- **F0–F8** : page d’ensemble du module, liste de chapitres, un chapitre plein écran à la fois, boutons précédent/suivant.
- **Exercices intégrés** : QCM, numérique, mots-clés, associations, étapes à ordonner et code Python utilisent la même interface.
- **Progression** : reprend la sauvegarde existante `quanthack.phase1.v1`, donc conserve les anciennes réponses et XP. Même seuil de 80 % pour les prérequis et la validation.
- **Retour à l’accueil** : le menu Studio reste accessible. L’ancienne interface reste disponible via `classic.html` à titre de secours.
- Le bouton mode sombre/clair, le nom, les couleurs, le logo et la mascotte sont inchangés.

## Publication sur GitHub Pages

1. **Sauvegarder d’abord** les données de progression depuis l’ancien lecteur (export JSON).
2. Ouvrir le dépôt `alessia-vda/quanthack-ipad` sur GitHub.
3. `Code → Add file → Upload files`, puis téléverser **les quatre fichiers à la racine**, en remplaçant les fichiers qui portent déjà le même nom :
   - `index.html`
   - `studio-rooms.js` (nouveau)
   - `studio-rooms.css` (nouveau)
   - `service-worker.js`
4. Valider avec **Commit changes**.
5. Dans `Actions`, vérifier la publication GitHub Pages. Dans Safari, ouvrir `https://alessia-vda.github.io/quanthack-ipad/` ; depuis l’app installée, utiliser ↻ pour actualiser.

**Ne pas supprimer** `rooms.js`, `app.js`, `style.css`, `studio-upgrades.js`, les fichiers d’icônes ou la mascotte.

## Contrôles effectués

- Syntaxe JavaScript vérifiée avec Node.
- Test des routes Studio : accueil, rooms, F0/F1, lecteur, QCM, associations, tri, code, lexique, parcours.
- Source inchangée des 84 tâches et des 9 rooms ; le stockage de progression classique est conservé.

**Limite :** la vérification visuelle dans un vrai navigateur Safari/iPad reste à faire sur l’appareil. Le navigateur automatisé de l’environnement est restreint par une politique administrateur, donc je ne revendique pas un test navigateur complet pour cette V4.
