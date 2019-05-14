"""
29/04/19
Intégration du fichier
traitement des caracteres dans des listes
localisation des endroits importants (entree, sortie, 3 objets)

30/04/19
Gestion des déplacement de Mac Gyver (varible big_mac)
Gestion des touches de saisie pour déplacement
Gestion du périmetre de déplacement
Gestion du redemarrage ou sortie du jeu
Integration des emplacements murs dans liste_mur[]
J'update directement sur GitHub

14/05/19
With pour la gestion du fichier
if __name__='__main__' pour l'appel des fonctions sans execution du script
"""



# importation du fichier labyrinth.py dans la variable fichier
if __name__=='__main__':

    x = 0

    with open("labyrinth.txt","r") as fichier:

        # découpage des lignes dans la variable lecture
        lecture = fichier.read().splitlines()
        # création d'un tableau, via la  liste_lettre dans la liste_ligne
        def creation_laby():
            liste_all = []
            liste_lettre = []
            for ligne in lecture:
            # découpe des caracteres de chaque ligne
            # intégration de ces caractères dans la liste liste_lettre
                liste_lettre = [i for i in ligne]
                # intégration de chaque liste dans la liste liste_all
                liste_all += [liste_lettre]
            print(liste_all)

        creation_laby()





        #print(liste_ligne[1])
            #for lettre in liste_ligne







        """

        liste_ligne = []
        liste_lettre = []
        liste_mur = []


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

        # Recherche des positions importantes
        # entrée = D
        D = (liste_lettre.index('D'))
        # sortie = S
        S = (liste_lettre.index('S'))
        # aiguille = O
        O = (liste_lettre.index('O'))
        # tube = P
        P = (liste_lettre.index('P'))
        # ether = Q
        Q = (liste_lettre.index('Q'))

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
        # on initie une variable qui permettra de verifier si c'est une premiere partie
        premiere_partie = 0
        # annonce du jeu
        print("*** Hello, bienvenue dans le nouveau, super, fabuleux jeux de Mac Gyver!!! ***")
        print("Tu dois aider Mac Gyver (Big Mac pour les intimes) à sortir!")
        print("Tu devras recupérer tous les objets pour créer une")
        print ("seringue et endormir le gardien à la sortie ;) .")
        print ("Les touches directions sont e : Haut, x : bas, d : droite et s :gauche")
        print ("Pour quitter, appuyer sur la touche q")

        while big_mac != S:
            # si relance de la partie affichage de l'annonce
            if premiere_partie == 1:
                print("*** Hello, bienvenue dans le nouveau, super, fabuleux jeux de Mac Gyver!!! ***")
                print("Tu dois aider Mac Gyver (Big Mac pour les intimes) à sortir!")
                print("Tu devras recupérer tous les objets pour créer une")
                print ("seringue et endormir le gardien à la sortie ;) .")
                print ("Les touches directions sont e : Haut, x : bas, d : droite et s :gauche")
                print ("Pour quitter, appuyer sur la touche q")
            # on demande à l'utilisateur quel direction il choisit
            action = input("Quel direction?\n")
            ##print(action)
            # si action egale à une des quatres lettres
            # on maj la valeur de big_mac

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


