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
S pour la sortie
M pour le
"""

#### VARIABLES ####
# définition de la position de départ
x = 0
y = 0
X = 0
Y = 0

# variable joueur
big_mac = 0
# compteur objets
comp_objets = 3


# chemin fichier labyrinthe
fichier_laby = "labyrinth.txt"

# variables directions
HAUT = 'e'
BAS = 'x'
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
        self.liste_all = self.lec_fichier(fichier_laby)


    def lec_fichier(self, a):
        ''' fonction lecture du fichier '''
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
        '''fontion permettant de selectionner une position selon les axes y et x '''
        position = self.liste_all[b][a]
        return position

    def __str__(self):
        for line in self.liste_all:
            print(line)


#### FONCTIONS ####





### fonction permettant de modifier les variables x et y
def mouvement(touch, x, y):
    ## si selection touche bas
    # l'axe des y prend +1
    if touch == BAS:
        if 0 <= y <= 13:
            y += 1
    ## si selection touche haut
    # l'axe des y prend -1
    if touch == HAUT:
        if 1 <= y <= 14:
            y -= 1
    ## si selection touche gauche
    # l'axe des x prend -1
    if touch == gauche:
        if 1 <= x <= 14:
            x -= 1
    ## si selection touche droite
    # l'axe des x prend +1
    if touch == droite:
        if 0 <= x <= 13:
            x += 1
    return(x, y)
#### fonction pour l'annonce
def annonce():
    print("*** Hello, bienvenue dans le nouveau, super, fabuleux jeux de Mac Gyver!!! ***")
    print("Tu dois aider Mac Gyver (Big Mac pour les intimes) à sortir!")
    print("Tu devras recupérer tous les objets pour créer une")
    print("seringue et endormir le gardien à la sortie ;) .")
    print("Les touches directions sont e : Haut, x : bas, d : droite et s :gauche")
    print("Pour quitter, appuyer sur la touche q")
    #print(liste_all)

### fonction de controle de saisie des objets
def saisie_objet(e):
    global comp_objets
    # lorsque le joueur arrive sur une case
    # si cette case est egale à un des 3 objets
    if (e == ether or e == aiguille or e == tube):
        print("C'est un objet")
        # la variable de controle est décrémentée de 1
        comp_objets -= 1
        print(comp_objets)
        return(comp_objets)

if __name__=='__main__':
 # importation du fichier labyrinth.py dans la variable fichier
    # on initie une variable qui permettra de verifier si c'est une premiere partie
    premiere_partie = 0

    #liste_all =   (fichier_laby)
    a = Labyrinthe(fichier_laby)

    annonce()

    while big_mac != out:
        # on demande à l'utilisateur quel direction il choisit
        action = input("Quel direction?\n")
        # si action egale à une des directions
        if (action == HAUT or action == BAS or action == gauche or action == droite):
            # on verifie que la future position n'est pas un mur
            x2, y2 = mouvement(action, x, y)
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
                a.liste_all[y2][x2] = 'C'
                print("*" + action + "*" + str(x) + " " + str(y) + " "+big_mac)
            # verification sortie avec objets
            if big_mac == out and comp_objets != 0 :
                print("Tu n'avais pas tous les objets, RIP Mac Gyver!")
            elif big_mac == out and comp_objets == 0:
                print("Bravo, Mac Gyver es libre!!!")
        else:
            print("Erreur de saisie!!!")
            print(action)

