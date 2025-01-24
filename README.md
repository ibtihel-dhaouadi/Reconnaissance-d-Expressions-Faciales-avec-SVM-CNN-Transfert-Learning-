<h1 align="left">Reconnaissance d'Expressions Faciales avec RAF-DB (SVM, CNN, TL)</h1>

###


<h3 align="left">🎯 Contexte du Projet</h3>

###

<p align="left">Le RAF-DB (Real-World Affective Face Database) est un dataset regroupant des images de visages humains étiquetées selon sept émotions :</p>

###


<p align="center">⭑ Bonheur (Happy)<br>⭑ Colère (Angry)<br>⭑ Tristesse (Sad)<br>⭑ Peur (Fear)<br>⭑ Dégoût (Disgust)<br>⭑ Surprise (Surprise)<br>⭑ Neutre (Neutral)</p>

###

<p align="left">Ces émotions sont essentielles dans des domaines comme l'interaction homme-machine, la psychologie et l'informatique affective. La reconnaissance des émotions faciales (FER - Facial Emotion Recognition) trouve des applications pratiques dans divers secteurs :<br><br>➜ Service client : analyse en temps réel de la satisfaction des clients.<br>➜ Sécurité : détection d'individus suspects ou menaçants.<br>➜ Santé : suivi des états émotionnels des patients, notamment ceux ayant des troubles psychologiques.<br>➜ Interaction humain-robot : amélioration de la communication homme-robot.<br><br>Un défi majeur de ce projet est le déséquilibre des classes dans le dataset, certaines émotions étant plus représentées que d'autres, ce qui peut influencer les performances des modèles.</p>

###

<p align="left"></p>

###

<br clear="both">

<h3 align="left">📝 Objectifs du Projet</h3>

###

<br clear="both">

<p align="left">L'objectif principal est de classifier les expressions faciales issues du dataset RAF-DB en sept catégories d'émotions. Les étapes incluent :<br><br>✨ Prétraitement des données : Chargement, redimensionnement et normalisation des images tout en gérant le déséquilibre des classes.<br><br>✨ Construction et comparaison de modèles :<br> 🇴 SVM (Support Vector Machine) : Modèle traditionnel de machine learning utilisé comme référence.<br> 🇴 CNN (Convolutional Neural Network) : Réseau profond capable d'apprendre automatiquement les caractéristiques des images.<br> 🇴 Apprentissage par Transfert (DenseNet) : Modèles pré-entraînés sur de grands datasets (comme ImageNet), adaptés à la tâche de reconnaissance des émotions.</p>

###

<div align="center">
  <img height="250" src="https://github.com/ibtihel-dhaouadi/Reconnaissance-d-Expressions-Faciales-avec-SVM-CNN-Transfert-Learning-/blob/main/result%20models.png"  />
</div>

###

<h3 align="left">⚙️ Fonctionnalités</h3>

###

<h4 align="left">1 - Notebook principal : <a href="https://www.kaggle.com/code/dhaouadiibtihel98/raf-db-facial-expression-recognition-svm-cnn-tl">[Lien vers le notebook]</a>  <br>➜ Préparation des données, entraînement des modèles et comparaison des performances.<br><br>2 - Application interactive avec test en temps réel :<br>➜ Fichier TestEmotionDetector.py permettant  de tester le modèle CNN en temps réel grâce à une webcam. L’application détecte les visages, prédit l’émotion correspondante et l’affiche à l’écran. </h4>

###

<div align="center">
  <img height="400" src="https://github.com/ibtihel-dhaouadi/Reconnaissance-d-Expressions-Faciales-avec-SVM-CNN-Transfert-Learning-/blob/main/result%20test.png"  />
</div>

###

<br clear="both">

<h3 align="left">👨🏻‍💻 Technologies utilisées :</h3>

###

<div align="right">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg" height="40" alt="vscode logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="40" alt="python logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/kaggle/kaggle-original.svg" height="40" alt="kaggle logo"  />
</div>

###

<p align="left">✔️  Langage principal: Langage principal pour la manipulation et l'analyse des données.<br><br>✔️ Bibliothèques principales :<br>- TensorFlow/Keras : Développement des modèles CNN et transfert d'apprentissage.<br>- OpenCV : Détection des visages et traitement des flux vidéo.<br>- Tkinter : Création d'une interface utilisateur pour tester le modèle en temps réel.<br><br>✔️ Outils et environnements :<br>➜ kaggle Notebook : Utilisé pour l’entraînement des modèles sur GPU, accélérant considérablement les calculs.<br>➜ Visual Studio Code : Environnement de développement intégré (IDE) pour le développement et les tests.</p>

###

<br clear="both">

<h3 align="left">📌 Résultats:</h3>

###

<p align="left">Le projet a permis de comparer les performances de trois approches différentes (SVM, CNN et transfert d'apprentissage). L'application interactive montre les prédictions en temps réel, facilitant une meilleure compréhension et utilisation des modèles développés.</p>

###

<br clear="both">

<h3 align="left">🔚 Conclusion :</h3>

###

<p align="left">Ce projet démontre l'efficacité des approches basées sur l'apprentissage profond, en particulier avec l'apprentissage par transfert, pour résoudre les problèmes complexes de reconnaissance d'expressions faciales. L'application interactive constitue un outil utile pour visualiser les résultats en action.</p>

###

<p align="center">Le code, les résultats détaillés et le fichier interactif sont disponibles dans les répertoires suivants :<br><br>Notebook d'analyse : <a href="https://www.kaggle.com/code/dhaouadiibtihel98/raf-db-facial-expression-recognition-svm-cnn-tl">[Lien vers le notebook]</a> <br>Fichier interactif : testEmotionDetector.py</p>

###

<p align="center">Téléchargez également le fichier du meilleur modèle (best_model.h5) depuis l'output du notebook.</p>

###

<h6 align="center">🔗 N’hésitez pas à consulter les fichiers attaché à ce dépôt pour plus de détails. Vos commentaires et suggestions sont les bienvenus !</h6>

###
