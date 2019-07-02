"""
Création d'un jeu de labyrinthe.
Mac Gyver doit sortir du labyrinthe avec les 3 objets.
S'il sort sans les 3 objets, il meurt!
Le joueur pet se déplacer à la verticale et horizontale.
Le labyrinthe est un carré de 15 sprints.

Rules about labyrinthe.txt file
D for the start position
S for the ending
M for the wall
C for the way
E for the wrong way
S for the ending
"""


#Tous les objets du labyrinthe doivent être dans la classe
#position de mcgyver comme attribut de la classe
#saisie_object devient une methode de Labyrinth
#verification de saisie de tous les objects avec len de self.remining_object
#maj position de mcgyver sans x et y, position dans la class

import random
from copy import deepcopy

#### VARIABLES ####
# x y initialisation
x = 0
y = 0


# player
BIG_MAC = 0

# Labyrinth file's path
LABY_FILE = "labyrinth.txt"

# Directional keys
TOP = 'e'
DOWN = 'x'
LEFT = 's'
RIGHT = 'd'

# variables objets
ETHER = 'O'
NEEDLE = 'P'
TUBE = 'Q'

# concordance variables - lettres fichier texte
START = 'D'
OUT = 'S'
WALL = 'M'


#### CLASSES ####
### classe permettant de représenter le labyrinthe
class Labyrinthe():
    def __init__(self, fichier_laby):
        self.x = 0
        self.y = 0
        self.list_all = self.lec_fichier(fichier_laby)
        self.remining_objetcts = {ETHER, NEEDLE, TUBE}
        self.list_object = ['N', 'O', 'P']
        #self.list_position_mcgyver = self.position_mcgyver(x, y)

    def lec_fichier(self, a):
        """ To read labyrinthe file """
        liste_all = []
        # si relance de la partie affichage de l'annonce
        with open(a, "r") as fichier:
            # découpage des lignes dans la variable lecture
            reading = fichier.read().splitlines()
            # création d'un tableau, via la  liste_letter dans la liste_all

            for line in reading:
                # découpe les caracteres de chaque ligne
                # intégration de ces caractères dans la liste liste_letter
                liste_letter = [i for i in line]
                # intégration de chaque liste dans la liste liste_all
                liste_all += [liste_letter]
            return (liste_all)

    def position(self, a, b):
        """ fontion permettant de selectionner une position selon les axes y et x """
        position = self.list_all[b][a]
        return position

    def __str__(self):
        for line in self.list_all:
            print(line)

    def pos_object(self, x):
        while len(x) > 0:
            # run all index of liste_object
            axe1 = random.randint(0, 14)
            axe2 = random.randint(0, 14)
            # select with random 1 position
            prev = self.position(axe1, axe2)
            if prev == 'C':
                # if C, we change the letter of this position in liste_all by one of 3 letter
                self.list_all[axe2][axe1] = x.pop()

    def mouvement(self, touch, x, y):
        # to change x & y variables
        if touch == DOWN:
            # if down, y takes +1
            if 0 <= y <= 13:
                y += 1
        if touch == TOP:
            # if top, y takes -1
            if 1 <= y <= 14:
                y -= 1
        if touch == LEFT:
            # if left, x takes -1
            if 1 <= x <= 14:
                x -= 1
        if touch == RIGHT:
            # if right, x takes +1
            if 0 <= x <= 13:
                x += 1
        return (x, y)

    def saisie_objet(self, e):
        """ check objects took """
        if (e == ETHER or e == NEEDLE or e == TUBE):
            """ player comes to a case, if the case = 1 of 3 objects """
            print("C'est un objet")
            self.list_object(e)

    def macgyver_visual(self, y2, x2):
        show_laby = deepcopy(a.list_all)
        show_laby[y2][x2] = "X"
        print(show_laby)


#### FONCTIONS ####
def annonce(nom):
    """ Print the announce """
    print("*** Hello " + nom + ", bienvenue dans le nouveau, super, fabuleux jeux de Mac Gyver!!! ***")
    print("Tu dois aider Mac Gyver (Big Mac pour les intimes) à sortir!")
    print("Tu devras recupérer tous les objets pour créer une")
    print("seringue et endormir le gardien à la sortie ;) .")
    print("Les touches directions sont e : Haut, x : bas, d : droite et s :gauche")
    print("Pour quitter, appuyer sur la touche q")



if __name__=='__main__':
    # control that is a first play

    # Creating of 'a' object
    a = Labyrinthe(LABY_FILE)

#def objets_alea():
    # Recuperer les coordonnées de toutes les lettres C
 #   l = [i for i in a.liste_all]
#    print(random.choice(l))

    joueur = input("Quel est votre nom de joueur?\n")
    annonce(joueur)

    a.pos_object(a.list_object)

    #a.__str__()

    while BIG_MAC != OUT:
        # ask to user which direction he wants to go
        action = input("Quel direction?\n")
        # si action egale à une des directions
        if (action == TOP or action == DOWN or action == LEFT or action == RIGHT):
            # check the futur position is not a wall
            x2, y2 = a.mouvement(action, x, y)
            if a.position(x2,y2) == WALL:
                print("C'est un mur!!! ")# + "*" +action + "*" +str(x) + " " + str(y) + " " + str(big_mac))
            else:
                # on MAJ les coordonnées de la variable big_mac
                x = x2
                y = y2
                BIG_MAC = a.position(x, y)
                # fonction pour le controle des objets
                a.saisie_objet(BIG_MAC)
                # modification de la lettre actuelle en C (apres verif mur et objets)
                a.list_all[y2][x2] = 'C'
                print("*" + action + "*" + str(x) + " " + str(y) + " " + BIG_MAC)
                a.macgyver_visual(y2, x2)
                # position actuelle de mcgyver sur la case X
            # verification sortie avec objets
            if BIG_MAC == OUT and len(a.list_object) != 0 :
                print(joueur + " tu n'avais pas tous les objets, RIP Mac Gyver!")
            elif BIG_MAC == OUT and len(a.list_object) == 0:
                print("Bravo " + joueur + ", Mac Gyver es libre!!!")
        else:
            print("Erreur de saisie!!!")
            print(action)

