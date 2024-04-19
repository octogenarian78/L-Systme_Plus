"""
@author : Pierre JAUFFRES
@Version ; 1.0
"""

import turtle as t
import time as u

# Initialise la tortue
t.speed(0)
t.left(45)



def aller_point(x, y, h):
    """
    Place la tortue dans un point et une orientation donnée.

    Paramètres :
        x (float) : Coordonnée x du point.
        y (float) : Coordonnée y du point.
        h (float) : Orientation de la tortue.

    Renvoi :
        Aucun.
    """
    t.penup()
    t.goto(x, y)
    t.setheading(h)
    t.pendown()

# Place la tortue dans un point initial
aller_point(0, -100, 90)

def enlever_non_conformes(chaine, liste_permise):
    # Initialise une chaîne vide pour stocker les caractères conformes
    chaine_conforme = ""
    
    # Variable de suivi pour détecter le cas spécial
    remplacer_f = False

    # Parcourt chaque caractère de la chaîne
    for i in range(len(chaine)):
        caractere = chaine[i]
        
        # Si on rencontre un 'F' et le prochain caractère est 'f'
        if caractere == 'F' and i < len(chaine) - 1 and chaine[i + 1] == 'f':
            # On le remplace par 'f' et on saute le prochain caractère
            chaine_conforme += 'f'
            remplacer_f = True
            continue

        # Si le caractère doit être remplacé par 'f' (cas spécial)
        if remplacer_f:
            chaine_conforme += 'f'
            remplacer_f = False
            continue

        # Vérifie si le caractère est présent dans la liste_permise
        if caractere in liste_permise:
            # Si oui, l'ajoute à la chaîne conforme
            chaine_conforme += caractere

    # Retourne la chaîne conforme
    return chaine_conforme

# Exemple d'utilisation
chaine = "Bonjour ! Comment ça va ? Ff"
liste_permise = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "

# Appel de la fonction pour enlever les caractères non conformes
chaine_conforme = enlever_non_conformes(chaine, liste_permise)

print("Chaîne d'origine:", chaine)
print("Chaîne après suppression des caractères non conformes:", chaine_conforme)




def genere_l_systme(axiom, regles, n):
    """
    Génère un L-système grâce à un axiom et aux règles fournies.

    Paramètres :
        axiom (str) : Axiom initial.
        regles (dict) : Règles de remplacement.
        n (int) : Nombre d'itérations.

    Renvoi :
        axiom (str) : Axiom final après les itérations.
    """
    new_axiom = ''
    for i in range(n):
        for char in axiom:
            new_axiom += regles.get(char, char)
        axiom = new_axiom
        new_axiom = ''
    return axiom




def afficher_l_systeme(axiom, ang, ratio):
    """
    Affiche la fractale générée par un L-système.

    Paramètres :
        axiom (str) : Axiom du L-système.
        ang (float) : Angle de rotation.
        ratio (float) : Ratio de réduction de longueur.

    Renvoi :
        Affiche la fractale.
    """
    liste_permise = ["F", "f", "+", "-", "[", "]", "|"]
    axiom = enlever_non_conformes(axiom, liste_permise)
    print(axiom)
    
    l_pos = []  # Liste pour sauvegarder la position de la tortue
    t.speed(-1)
    t.down()
    t.left(90)
    lg = 1
    t.ht()
    taille = len(axiom)
    progress = 0
    
    progress_bar = "[" + "-" * 20 + "]"
    print(f"\r{progress_bar} {progress}%", end="")
    
    for index, char in enumerate(axiom):
        if char == 'F' or char == 'f':
            t.forward(lg)
            
        elif char == '+':
            t.right(ang)
        elif char == '-':
            t.left(ang)
        elif char == '[':
            lg *= ratio
            l_pos.append((t.xcor(), t.ycor(), t.heading()))
        elif char == ']':
            lg /= ratio
            lp = l_pos.pop()
            aller_point(lp[0], lp[1], lp[2])
        elif char == "|":
            t.left(180)
        
        # Mise à jour de la barre de progression
        progress = (index + 1) / taille
        completed_length = int(50 * progress)
        progress_bar = "[" + "#" * completed_length + "-" * (50 - completed_length) + "]"
        print(f"\r{progress_bar} {int(progress * 100)}%", end="")

    # Nouvelle ligne après la fin de la boucle
    print()


def fait_fractal(regles, axiom, ang, ratio, n):
    """
    Utilise les fonctions précédemment définies pour réaliser une fractale et l'afficher.

    Paramètres :
        regles (dict) : Règles du L-système.
        axiom (str) : Axiom initial.
        ang (float) : Angle de rotation.
        ratio (float) : Ratio de réduction de longueur.
        n (int) : Nombre d'itérations.

    Renvoi :
        Crée et affiche une fractale.
    """
    axiom = genere_l_systme(axiom, regles, n)
    print(len(axiom))
    afficher_l_systeme(axiom, ang, ratio)

def taille_temps_mot(regles, axiom, n):
    """
    Calcule la taille du mot et le temps pour générer le L-système.

    Paramètres :
        regles (dict) : Règles du L-système.
        axiom (str) : Axiom initial.
        n (int) : Nombre d'itérations.

    Renvoi :
        size (int) : Taille du mot généré.
        time (float) : Temps pour générer le mot.
    """
    d = u.time()
    mot = genere_l_systme(axiom, regles, n)
    f = u.time()
    return len(mot), f - d

def fractalisation(lf, n):
    """
    Génère et affiche la fractale en utilisant le L-système spécifié.

    Paramètres :
        lf (tuple) : Tuple contenant les règles, l'axiom, l'angle et le ratio.
        n (int) : Nombre d'itérations.

    Renvoi :
        Crée et affiche la fractale.
    """
    if len(lf) < 4:
        fait_fractal(lf[0], lf[1], lf[2], 1, n)
    else:
        fait_fractal(lf[0], lf[1], lf[2], lf[3], n)


systeme = [(#fractal 1
{
    'F': 'FF',
    'X': 'F[-X][X]F[-X]+X', #définition des regle
    'Y': 'F[+Y]-Y',
},
'X' #définition de l'axiom de départ
,22.5
),
(#fractal 2
{
    'F':'F+F-F-FF+F+F-F'
},
'F+F+F+F',
90
),
(#fractal 3
{
    'F':'FF+F-F+F+FF'
},
'F+F+F+F',
90
),
(#fractal 4
{
'F':'-F-F+F-F-F+F-F-F+F-F-F+F'
},
'F+F+F+F',
90
),
(#fractal 5: de Von Koch
{
    'F':'F-F++F-F'
},
'F++F++F++',
60
),
(# fractal 6: courbe du dragon
{
    'X':'X+YF+',
    'Y':'-FX-Y'
},
'FX',
90
),
(# fractal 7: courbe de tendragon
{
    'F':'F+F-F'
},
'F',
120
),
(# fractal 8
{
    'F':'f-F-f',
    'f':'F+f+F'
},
'F',
60
),
(#fractal 9
{
    'F':'-F++F-'
},
'F',
45
),
(#fractal 10
{
    "X" : "F+[[X]-X]-F[-FX]+X"
,
    "F" : "FF"
},
'X',
25,
(2/3)
),
(#fractal 11: twindragon
{
    "X" : "X+YF",
    "Y" : "FX-Y"
},
"FX+FX+",
90
),
(
{
    "F" : "+F--F+"
},
"F",
45
),
(#fractal 12: Courbe de Hilbert
{
    "L" : "-RF+LFL+FR-",
    "R" : "+LF-RFR-FL+"
},
"L",
90
),
(#fractal 13: triangle de Sierpinsky
{
    "X" : "XF+XF+XF+",
    "F" : "FF",
},
"X",
120
),
(#tapis de Sierpinsky
{
    "X" : "XFXFXF+XFXFXF+XFXFXF+XFXFXF+",
    "F" : "FFF"
},
"XFXFXF+XFXFXF+XFXFXF+XFXFXF+",
90
)
]

print(len(systeme))
fractalisation(systeme[#number of l_systeme],#number for fractalization)
t.ht()



print("fini")

t.speed(-1)
t.mainloop()
