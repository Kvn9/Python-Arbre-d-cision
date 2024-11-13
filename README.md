🌳 Arbre de Décision sur les Personnages de Dragon Ball Z
Ce projet entraîne un modèle d'arbre de décision pour prédire la transformation de personnages de Dragon Ball Z en fonction de caractéristiques comme leur race, niveau de puissance, attaque spéciale, etc.

🗂️ Fichiers
dragon_ball_z.csv : Fichier de données contenant les informations sur les personnages (race, niveau de puissance, attaque spéciale, transformation, etc.).
script.py : Script Python pour entraîner et visualiser l'arbre de décision.
🛠️ Prérequis
Assurez-vous d'avoir Python installé ainsi que les bibliothèques suivantes :

pip install pandas scikit-learn matplotlib

🚀 Lancer le Projet
Cloner le projet ou télécharger les fichiers.

Placer le fichier dragon_ball_z.csv dans le même dossier que le script.

Exécuter le script :

python python-data.py

Visualiser l'arbre de décision : Une fois le script exécuté, un graphique s'affiche montrant les décisions de l'arbre selon les caractéristiques des personnages.

🧩 Explications du Code
Chargement des données 📥 : Le fichier CSV est chargé et préparé.
Encodage des données 🔢 : Les textes (ex : noms d'attaque) sont convertis en nombres pour être compris par le modèle.
Entraînement du modèle 🏋️ : Un arbre de décision est construit à partir des colonnes importantes.
Visualisation 📊 : L'arbre est affiché pour montrer comment les transformations sont prédites en fonction des caractéristiques.

📈 Résultat
L'arbre de décision montre comment différentes caractéristiques influencent la transformation d'un personnage. Vous pouvez explorer les différentes branches pour comprendre les conditions qui mènent à chaque transformation.

