
#### VARIABLES ####
# définition de la position de départ
x = 0
y = 0
X = 0
Y = 0

# Position de départ du joueur
mac_gyver = { 'X' : 0, 'Y' : 0}
big_mac = 0

liste_letter = []
liste_all = []


# chemin fichier labyrinthe
fichier_laby = "labyrinth.txt"

haut = 'e'
bas = 'x'
gauche = 's'
droite = 'd'


start = 'D'
out = 'S'
mur = 'M'

#### FONCTIONS ####
### création de la fontion permettant de selectionner une position
# selon les axes y et x
def position(a,b):
    position = liste_all[b][a]
    #print(position)
    return position

### création de la fonction permettant de modifier les variables x et y
def mouvement(touch):
    ## si selection touche bas
    # l'axe des y prend +1
    global x, y
    x = X
    y = Y
    if touch == bas:
        y += 1
    # print(position(x,y))
    ## si selection touche haut
    # l'axe des y prend -1
    if touch == haut:
        y -= 1
    ## si selection touche gauche
    # l'axe des x prend -1
    if touch == gauche:
        x -= 1
    ## si selection touche droite
    # l'axe des x prend +1
    if touch == droite:
        x += 1
    #print(position)
    #print(x, y)

def annonce():
    print("*** Hello, bienvenue dans le nouveau, super, fabuleux jeux de Mac Gyver!!! ***")
    print("Tu dois aider Mac Gyver (Big Mac pour les intimes) à sortir!")
    print("Tu devras recupérer tous les objets pour créer une")
    print("seringue et endormir le gardien à la sortie ;) .")
    print("Les touches directions sont e : Haut, x : bas, d : droite et s :gauche")
    print("Pour quitter, appuyer sur la touche q")

# importation du fichier labyrinth.py dans la variable fichier
if __name__=='__main__':
    # on initie une variable qui permettra de verifier si c'est une premiere partie
    premiere_partie = 0


    # si relance de la partie affichage de l'annonce
    with open(fichier_laby,"r") as fichier:
        # découpage des lignes dans la variable lecture
        lecture = fichier.read().splitlines()
        # création d'un tableau, via la  liste_lettre dans la liste_all

        for ligne in lecture:
        # découpe des caracteres de chaque ligne
        # intégration de ces caractères dans la liste liste_lettre
            liste_letter = [i for i in ligne]
            # intégration de chaque liste dans la liste liste_all
            liste_all += [liste_letter]

            # annonce
        annonce()
        # on initialise le statut de départ
        big_mac = liste_all[0][0]
        print(position(x,y))
        #print(big_mac)
        while big_mac != out:
            # on demande à l'utilisateur quel direction il choisit
            action = input("Quel direction?\n")
            # si action egale à une des directions
            if (action == haut or action == bas or action == gauche or action == droite):
                # on verifie que la future position n'est pas un mur
                mouvement(action)
                if position(x,y) == mur:
                    print("C'est un mur!!! "+big_mac)
                else:
                    # on MAJ les coordonnées de la variable big_mac
                    X = x
                    Y = y
                    big_mac = position(x, y)
                    print(big_mac)


                #def verification(c):
                 #   mouvement(c)
                  #  if position(x,y) == mur:
                   #     return mur

                    #print("TEST "+big_mac)
                #pri = position(action)
                #print(pri)

                # position_future = mouvement(action)
                # print(position_future)
            else:
                print("Erreur de saisie!!!")
                print(action)







                #action = 'a'















"""


        # On crée une fonction pour définir l'environnement autour de big_mac
        def localisation(x):
            global nord, sud, est, ouest
            nord = liste_lettre[x-15]
            sud = liste_lettre[x+15]
            est = liste_lettre[x+1]
            ouest = liste_lettre[x-1]

        # intégration des lignes dans liste_ligne[]
        for ligne in lecture:
            liste_ligne.append(ligne)
            #print (liste_ligne)
            # intégration des lettres dans liste_lettre[]
            for lettre in ligne:
                liste_lettre.append(lettre)
                #print (liste_lettre)


        ##print (len(liste_ligne))
        ##print (liste_ligne[0])
        ##print (liste_lettre[3])
        ## test position
        ##print (liste_lettre[20])
        ## droite de la position
        ##print (liste_lettre[20+1])
        ## dessous de la position
        ##print (liste_lettre[20+15])
        ## gauche de la position
        ##print (liste_lettre[20-1])
        ## dessus de la position
        ##print (liste_lettre[20-15])

        

        # Mac Gyver (big_mac) doit commencer sur la position D
        global big_mac
        big_mac = D
        ##print (big_mac)
        ##est = liste_lettre[big_mac+1]
        ##print(est)



        # integrer toutes les coordonnées des murs dans la liste liste_mur
        for i,u in enumerate(liste_lettre):
            if u == 'M':
                liste_mur.append(i)

        print (liste_mur)

        # on integre une valeur sur chaque variables selon la position de Mac Gyver,
        # alias big_mac
        localisation(int(big_mac))
        
            if action == "e":
                # verifie que big_mac ne sort pas du jeu
                if (big_mac - 15) >= 0:
                    if (big_mac - 15) in liste_mur:
                        print ("c'est un mur!!!")
                    else:
                        big_mac = big_mac - 15
                        print("vous allez en haut!")
                        print (big_mac)
                # si hors labyrinthe, big_mac n'est mis à jour.
                else:
                    print("Cette direction est hors périmetre!")
            elif action == "x":
                # verifie que big_mac ne sort pas du jeu
                if (big_mac + 15) <= 225:
                    if (big_mac + 15) in liste_mur:
                        print ("c'est un mur!!!")
                    else:
                        big_mac = big_mac + 15
                        print("vous allez en bas!")
                        print (big_mac)
                # si hors labyrinthe, big_mac n'est mis à jour.
                else:
                    print("Cette direction est hors périmetre!")
            elif action == "d":
                # verifie que big_mac ne sort pas du jeu
                if (big_mac + 1) <= 225:
                    if (big_mac + 1) in liste_mur:
                        print ("c'est un mur!!!")
                    else:
                        big_mac = big_mac + 1
                        print ("vous allez à droite!")
                        print (big_mac)
                # si hors labyrinthe, big_mac n'est mis à jour.
                else:
                    print("Cette direction est hors périmetre!")
            elif action == "s":
                # verifie que big_mac ne sort pas du jeu
                if (big_mac - 1) >= 0:
                    if (big_mac - 1) in liste_mur:
                        print ("c'est un mur!!!")
                    else:
                        big_mac = big_mac - 1
                        print ("vous allez à gauche!")
                        print (big_mac)
                # si hors labyrinthe, big_mac n'est mis à jour.
                else:
                    print("Cette direction est hors périmetre!")
            # si le joueur veut quiiter le jeu
            elif action == "q":
                confirmation = input("Etes-vous sur de vouloir quitter ou recommencer le jeu? Q pour quitter, R pour recommencer \n")
                if confirmation == "Q":
                    exit()
                elif confirmation == "R":
                    premiere_partie = 1
            # sinon le joueur n'a pas choisi la bonne touche!
            else:
                print ("!!! Vous n'avez pas saisie une des quatres touches !!!")
                print ("pour rappel:")
                print ("e pour aller en haut")
                print ("x pour aller en bas")
                print ("d pour aller à droite")
                print ("s pour aller à gauche")


    # on integre tous les emplacements des murs dans une liste

"""


