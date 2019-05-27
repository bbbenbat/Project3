
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

liste_letter = []
liste_all = []


# chemin fichier labyrinthe
fichier_laby = "labyrinth.txt"

# variables directions
haut = 'e'
bas = 'x'
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

#### FONCTIONS ####
### fontion permettant de selectionner une position
# selon les axes y et x
def position(a,b):
    position = liste_all[b][a]
    return position

### fonction permettant de modifier les variables x et y
def mouvement(touch):
    global x, y
    x = X
    y = Y
    ## si selection touche bas
    # l'axe des y prend +1
    if touch == bas:
        if 0 <= y <= 13:
            y += 1
    ## si selection touche haut
    # l'axe des y prend -1
    if touch == haut:
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




# importation du fichier labyrinth.py dans la variable fichier
if __name__=='__main__':
    # on initie une variable qui permettra de verifier si c'est une premiere partie
    premiere_partie = 0


    # si relance de la partie affichage de l'annonce
    with open(fichier_laby,"r") as fichier:
        # découpage des lignes dans la variable lecture
        lecture = fichier.read().splitlines()
        # création d'un tableau, via la  liste_letter dans la liste_all

        for ligne in lecture:
        # découpe des caracteres de chaque ligne
        # intégration de ces caractères dans la liste liste_letter
            liste_letter = [i for i in ligne]
            # intégration de chaque liste dans la liste liste_all
            liste_all += [liste_letter]

        # annonce
        annonce()
        # boucle pour fin de partie
        #  des que la variable comp_objets arrive à 0, tous les objets sont saisis
        while big_mac != out and comp_objets != 0:
            # on demande à l'utilisateur quel direction il choisit
            action = input("Quel direction?\n")
            # si action egale à une des directions
            if (action == haut or action == bas or action == gauche or action == droite):
                # on verifie que la future position n'est pas un mur
                mouvement(action)
                if position(x,y) == mur:
                    print("C'est un mur!!! ")# + "*" +action + "*" +str(x) + " " + str(y) + " " + str(big_mac))

                else:
                    # on MAJ les coordonnées de la variable big_mac
                    X = x
                    Y = y
                    big_mac = position(x, y)
                    # fonction pour le controle des objets
                    saisie_objet(big_mac)
                    # modification de la lettre actuelle en C (car vérification mur et objets)
                    liste_all[Y][X] = 'C'
                    print("*" + action + "*" + str(x) + " " + str(y) + " "+big_mac)
                if big_mac == out:
                    print("Bravo Mac Gyver, tu es libre!!!")
            else:
                print("Erreur de saisie!!!")
                print(action)

