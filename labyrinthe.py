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
E for wrong
S for the pour la sortie
M pour le
"""
import random

#### VARIABLES ####
# x y initialisation
x = 0
y = 0
# objects list
list_object = ['N', 'O', 'P']

# variable joueur
big_mac = 0
# compteur objets
comp_objets = 3


# chemin fichier labyrinthe
fichier_laby = "labyrinth.txt"

# variables directions
TOP = 'e'
DOWN = 'x'
gauche = 's'
droite = 'd'

# variables objets
ether = 'O'
aiguille = 'P'
tube = 'Q'

# concordance variables - lettres fichier texte
start = 'D'
out = 'S'
mur = 'M'


#### CLASSES ####
### classe permettant de représenter le labyrinthe
class Labyrinthe():
    def __init__(self, fichier_laby):
        self.x = 0
        self.y = 0
        self.list_all = self.lec_fichier(fichier_laby)


    def lec_fichier(self, a):
        """ fonction lecture du fichier """
        liste_all = []
        # si relance de la partie affichage de l'annonce
        with open(a, "r") as fichier:
            # découpage des lignes dans la variable lecture
            lecture = fichier.read().splitlines()
            # création d'un tableau, via la  liste_letter dans la liste_all

            for ligne in lecture:
                # découpe les caracteres de chaque ligne
                # intégration de ces caractères dans la liste liste_letter
                liste_letter = [i for i in ligne]
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
        if touch == gauche:
            # if left, x takes -1
            if 1 <= x <= 14:
                x -= 1
        if touch == droite:
            # if right, x takes +1
            if 0 <= x <= 13:
                x += 1
        return (x, y)


#### FONCTIONS ####







def annonce(nom):
    """ Print the announce """
    print("*** Hello " + nom + ", bienvenue dans le nouveau, super, fabuleux jeux de Mac Gyver!!! ***")
    print("Tu dois aider Mac Gyver (Big Mac pour les intimes) à sortir!")
    print("Tu devras recupérer tous les objets pour créer une")
    print("seringue et endormir le gardien à la sortie ;) .")
    print("Les touches directions sont e : Haut, x : bas, d : droite et s :gauche")
    print("Pour quitter, appuyer sur la touche q")


def saisie_objet(e):
    """ check objects took """
    global comp_objets
    if (e == ether or e == aiguille or e == tube):
        """ player comes to a case, if the case = 1 of 3 objects """
        print("C'est un objet")
        # la variable de controle est décrémentée de 1
        comp_objets -= 1
        print(comp_objets)
        return(comp_objets)


if __name__=='__main__':
    # control that is a first play

    # Creating of 'a' object
    a = Labyrinthe(fichier_laby)

#def objets_alea():
    # Recuperer les coordonnées de toutes les lettres C
 #   l = [i for i in a.liste_all]
#    print(random.choice(l))

    joueur = input("Quel est votre nom de joueur?\n")
    annonce(joueur)

    a.pos_object(list_object)

    a.__str__()

    while big_mac != out:
        # ask to user which direction he wants to go
        action = input("Quel direction?\n")
        # si action egale à une des directions
        if (action == TOP or action == DOWN or action == gauche or action == droite):
            # check the futur position is not a wall
            x2, y2 = a.mouvement(action, x, y)
            if a.position(x2,y2) == mur:
                print("C'est un mur!!! ")# + "*" +action + "*" +str(x) + " " + str(y) + " " + str(big_mac))
            else:
                # on MAJ les coordonnées de la variable big_mac
                x = x2
                y = y2
                big_mac = a.position(x, y)
                # fonction pour le controle des objets
                saisie_objet(big_mac)
                # modification de la lettre actuelle en C (apres verif mur et objets)
                a.list_all[y2][x2] = 'C'
                print("*" + action + "*" + str(x) + " " + str(y) + " "+big_mac)
            # verification sortie avec objets
            if big_mac == out and comp_objets != 0 :
                print(joueur + " tu n'avais pas tous les objets, RIP Mac Gyver!")
            elif big_mac == out and comp_objets == 0:
                print("Bravo " + joueur + ", Mac Gyver es libre!!!")
        else:
            print("Erreur de saisie!!!")
            print(action)

