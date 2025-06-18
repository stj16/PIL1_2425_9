# Exécuter un projet Vue.js en local : étapes détaillées

1. **Installer Node.js**
    - Télécharger Node.js depuis [nodejs.org](https://nodejs.org/).
    - Installer Node.js (inclut npm, le gestionnaire de paquets).

2. **Vérifier l'installation**
    ```bash
    node -v
    npm -v
    ```
    Les deux commandes doivent afficher une version.

3. **Cloner ou copier le projet**
    - Copier le dossier du projet sur le PC ou utiliser `git clone` si le projet est sur un dépôt Git.

4. **Ouvrir un terminal dans le dossier du projet**
    - Naviguer dans le dossier du projet :
      ```bash
      cd chemin/vers/ton/projet
      ```

5. **Installer les dépendances**
    ```bash
    npm install
    ```
    Cette commande télécharge toutes les dépendances listées dans `package.json`.

6. **Lancer le serveur de développement**
    ```bash
    npm run server
    ```
    (ou `npm run dev` selon la configuration du projet)

7. **Accéder à l'application**
    - Ouvrir un navigateur et aller à l'adresse indiquée dans le terminal (souvent `http://localhost:8080`).

**Remarque :**  
Si tu rencontres des erreurs, vérifie la version de Node.js requise dans la documentation du projet ou le fichier `package.json`.


Backend Django – Guide de démarrage

Prérequis
- Python 3.12 (https://www.python.org/downloads/)
- Git
- (Recommandé) VS Code ou PyCharm
- Accès aux identifiants de la base de données (voir ci-dessous)

Installation Backend
1. Cloner le projet
   git clone <URL_DU_DEPOT>
   cd ifri_comotorage/ifri_como_back_end

2. Créer et activer un environnement virtuel
   python -m venv venv
   venv\Scripts\activate

3. Installer les dépendances
   pip install --upgrade pip
   pip install -r requirements.txt

4. Configurer la base de données
   
   - Exemple de contenu :
     DB_NAME=nom_de_la_base
     DB_USER=utilisateur
     DB_PASSWORD=mot_de_passe
     DB_HOST=localhost
     DB_PORT=5432
   - Renseignez les identifiants fournis par le responsable du projet.

5. Lancer les migrations
   python manage.py migrate

6. Démarrer le serveur
   python manage.py runserver


Frontend Vue.js – Guide de démarrage

Prérequis
- Node.js (https://nodejs.org/) (version 18 ou supérieure recommandée)
- Git
- (Recommandé) VS Code

voici les identifiants de la base de  donnée 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ifri_comotorage',
        'USER': 'ifri_user',
        'PASSWORD': 'motdepassefort',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
