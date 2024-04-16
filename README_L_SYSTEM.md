# Fractales avec Turtle

Ce programme Python utilise la bibliothèque Turtle pour générer des fractales en suivant des L-systèmes. Il permet d'afficher différentes fractales en suivant des règles de remplacement spécifiées.

## Initialisation de la tortue et fonctions auxiliaires

Le code commence par initialiser la tortue et définir des fonctions pour la placer dans un point donné avec une orientation spécifique.

## Fonction pour enlever les caractères non conformes

Une fonction est définie pour supprimer les caractères non conformes d'une chaîne, en utilisant une liste de caractères autorisés.

## Génération et affichage des L-systèmes

Les L-systèmes sont générés à partir d'un axiome initial et de règles de remplacement. Ces systèmes sont ensuite affichés en utilisant la tortue Turtle, en interprétant les caractères de l'axiome comme des instructions de mouvement.

## Fonctions principales

- **`genere_l_systme(axiom, regles, n)`** : Cette fonction génère un L-système en appliquant les règles de remplacement un certain nombre de fois sur l'axiome initial.
  
- **`afficher_l_systeme(axiom, ang, ratio)`** : Affiche la fractale générée par un L-système en interprétant les caractères de l'axiome comme des mouvements de la tortue.
  
- **`fait_fractal(regles, axiom, ang, ratio, n)`** : Utilise les fonctions précédentes pour générer et afficher une fractale à partir des règles, de l'axiome initial, de l'angle de rotation et du ratio de réduction de longueur.

## Fonctions secondaires

- **`aller_point(x, y, h)`** : Place la tortue dans un point et une orientation donnée.
  
- **`enlever_non_conformes(chaine, liste_permise)`** : Supprime les caractères non conformes d'une chaîne en fonction d'une liste de caractères autorisés.
  
- **`taille_temps_mot(regles, axiom, n)`** : Calcule la taille du mot généré par un L-système ainsi que le temps nécessaire pour le générer.
  
- **`fractalisation(lf, n)`** : Génère et affiche une fractale en utilisant le L-système spécifié.

## Détails sur l'alphabet

Les déplacements de la tortue sont contrôlés par un alphabet spécifique :

- 'F' : avancer
- '+' : tourner à droite
- '-' : tourner à gauche
- '[' : copier la position et l'orientation de la tortue
- ']' : restaurer la dernière position et orientation sauvegardée

## Fractales disponibles

Le programme propose plusieurs fractales définies par des L-systèmes, chacune avec ses règles spécifiques :

- Fractale 1
- Fractale 2
- Fractale 3
- Fractale 4
- Fractale 5 (de Von Koch)
- Fractale 6 (courbe du dragon)
- Fractale 7 (courbe de tendragon)
- Fractale 8
- Fractale 9
- Fractale 10
- Fractale 11 (twindragon)
- Fractale 12 (Courbe de Hilbert)
- Fractale 13 (triangle de Sierpinsky)
- Fractale 14 (tapis de Sierpinsky)

## Auteur

Ce programme a été réalisé par Pierre JAUFFRES.
