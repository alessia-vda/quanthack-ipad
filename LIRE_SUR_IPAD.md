# QuantHack — version iPad (phase 1)

**Ce dossier contient la version sans serveur**, à héberger comme un site web statique : Safari / iPad et ordinateurs.

## Utilisation depuis un iPad

Le moyen fiable est d'ouvrir QuantHack via **une adresse HTTPS**. Le simple fichier `.html` téléchargé dans l'app Fichiers n'est pas garanti de fonctionner dans l'aperçu iPad (JavaScript / stockage).

### Publication gratuite sur GitHub Pages (depuis iPad ou ordinateur)

1. Crée un dépôt GitHub public (par exemple `quanthack-ipad`). Attention : **la publication est publique**. Le dossier ne contient pas de données personnelles ni ta progression.
2. Décompresse `QuantHack_iPad_SITE.zip` et envoie à la **racine** du dépôt **tous** les fichiers du zip : `index.html`, `app.js`, `rooms.js`, `style.css`, les fichiers PNG, `manifest.webmanifest`, `register-sw.js`, `service-worker.js`, `.nojekyll`, etc. Le dépôt doit afficher directement `index.html`, pas un sous-dossier.
3. Dans GitHub : **Settings → Pages → Build and deployment → Deploy from a branch → main → /(root) → Save**.
4. Dans Pages clique sur `Visit site` lorsque la publication est prête ; l'adresse ressemble à `https://utilisateur.github.io/quanthack-ipad/`.
5. Sur iPad dans **Safari**, ouvre cette adresse, bouton **Partager → Sur l'écran d'accueil → Ouvrir comme app web → Ajouter**.

Tu peux aussi tester `QuantHack_iPad.html` (un seul fichier) à partir du lien dans ChatGPT. Si ton iPad n'exécute pas les scripts dans l'aperçu, utilise la version publiée HTTPS.

## Fonctionnement

- Les **8 rooms F1 à F8**, les **56 tâches** et les **81 flashcards** sont inchangées.
- Les tâches Python utilisent **Pyodide dans le navigateur**. Le premier lancement nécessite Internet pour récupérer le moteur depuis jsDelivr. Ce n'est **pas** une exécution Python sur un serveur personnel.
- Les cours, quiz et cartes fonctionnent hors ligne sur un site installé après mise en cache, sous réserve des règles de stockage de Safari. Le mode Python hors ligne n'est pas garanti.
- XP et progression : stockage sur l'appareil dans Safari. Utiliser **Exporter JSON** pour sauvegarder / transférer (la version installée peut avoir un stockage distinct).
- MathJax et la police peuvent nécessiter Internet ; les équations restent lisibles en mode de secours.
- La phase 2 n'a pas été ajoutée.

## Vérification

Lancer un serveur web statique pour les tests (pas obligatoire sur l'iPad) : `python3 -m http.server 8000`, puis ouvrir `http://localhost:8000/` ; **sur ce serveur de test, sélectionner Pyodide** car l'endpoint Python `/api/python` n'existe pas. Sur GitHub Pages et les autres hébergements HTTPS, Pyodide est choisi automatiquement.

Ne pas publier l'ancienne version `server.py` sur un serveur public : elle exécute du code Python arbitraire.
