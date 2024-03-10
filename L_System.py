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

    print(axiom)
    l_pos = []  # Liste pour sauvegarder la position de la tortue
    t.speed(0)
    t.down()
    t.left(90)
    lg = 15
    taille = len(axiom)
    for char in axiom:
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
        taille -= 1
        print(taille)

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
(
{
    "X" : "XF+XF+XF+",
    "F" : "FF",
},
"X",
120
)
]

print(len(systeme))
fractalisation(systeme[13],3)
t.ht()



print("fini")

t.speed(-1)
t.mainloop()
