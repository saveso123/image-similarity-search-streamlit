# 🔎 Image Similarity Search – CBIR avec Streamlit

Projet académique développé dans le cadre de ma formation en **Programmation Web et Intelligence Artificielle**.

Cette application implémente un système de **recherche d’images basée sur le contenu (CBIR – Content-Based Image Retrieval)**.

L’utilisateur peut téléverser une image, sélectionner un descripteur visuel et une mesure de distance, puis afficher les images les plus similaires présentes dans le dataset.

## 🎯 Objectif du projet

L’objectif est de comparer une image requête avec une base d’images en utilisant plusieurs techniques d’extraction de caractéristiques et de calcul de similarité.

L’application permet notamment de :

- téléverser une image à rechercher ;
- choisir le nombre d’images similaires à afficher ;
- sélectionner un descripteur visuel ;
- sélectionner une mesure de distance ;
- calculer la similarité entre les images ;
- afficher les résultats avec leur classe et leur score de distance.

## 🧠 Descripteurs utilisés

Le projet utilise plusieurs méthodes d’extraction de caractéristiques :

- **GLCM RGB**
- **Haralick RGB**
- **BiT – Bio-Inspired Texture Descriptor**
- **Concaténation des descripteurs**

Les signatures pré-calculées sont enregistrées dans des fichiers `.npy` afin d’accélérer la recherche.

## 📏 Mesures de distance

Plusieurs mesures sont disponibles pour comparer les vecteurs de caractéristiques :

- Distance euclidienne
- Distance Manhattan
- Distance de Tchebychev
- Distance Canberra

## 🚀 Fonctionnement de l’application

L’utilisateur téléverse une image depuis l’interface Streamlit.

Il sélectionne ensuite :

1. le descripteur à utiliser ;
2. la mesure de distance ;
3. le nombre d’images similaires à afficher.

L’application extrait les caractéristiques de l’image requête, calcule les distances avec les signatures du dataset, trie les résultats et affiche les images les plus proches.

## 🖥️ Interface Streamlit

L’interface utilisateur a été développée avec **Streamlit**.

Elle permet :

- le téléversement d’images ;
- la prévisualisation de l’image requête ;
- la sélection du descripteur ;
- la sélection de la distance ;
- le choix du nombre de résultats ;
- l’affichage interactif des images similaires.

## 🗂️ Dataset

Le projet utilise un dataset d’images d’iris organisé en trois classes :

- `iris-setosa`
- `iris-versicolour`
- `iris-virginica`

Le dataset complet n’est pas inclus dans ce dépôt afin de garder le dépôt léger.

## 🧱 Structure du projet

```text
.
├── pages/
│   └── Docs.py
├── descripteur.py
├── distance.py
├── extraction.py
├── main.py
├── requirements.txt
├── signaturesBitdeskRGB.npy
├── signaturesConcatenationRGB.npy
├── signaturesGLCMRGB.npy
├── signaturesHaralickRGB.npy
└── .gitignore
```

## ⚙️ Technologies utilisées

- Python
- Streamlit
- NumPy
- Pandas
- OpenCV
- scikit-learn
- SciPy
- scikit-image
- Mahotas
- Pillow

## 📦 Installation locale

### 1. Cloner le dépôt

```bash
git clone https://github.com/saveso123/image-similarity-search-streamlit.git
```

### 2. Accéder au projet

```bash
cd image-similarity-search-streamlit
```

### 3. Créer un environnement virtuel

```bash
python -m venv venv
```

Sous Windows :

```bash
venv\Scripts\activate
```

### 4. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 5. Lancer l’application

```bash
streamlit run main.py
```

## 📚 Compétences mises en pratique

Ce projet m’a permis de renforcer mes compétences en :

- développement Python ;
- traitement et analyse d’images ;
- extraction de caractéristiques ;
- calcul de similarité ;
- manipulation de données avec NumPy ;
- développement d’interfaces interactives avec Streamlit ;
- structuration et documentation d’un projet logiciel.

## 👤 À propos

**Sandra Verónica Soto Polo**  
Développeuse logiciel junior – Montréal, Québec

Projet académique réalisé dans le cadre de ma formation en Programmation Web et Intelligence Artificielle.
