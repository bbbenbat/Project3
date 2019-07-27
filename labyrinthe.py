
''' Creating a labyrinth game.
MacGyver must go out with 3 objects.

Rules about labyrinthe.txt file
D for the start position
S for the ending
M for the wall
C for the way
E for the wrong way
S for the ending''
'''

import random
import pygame
from pygame.locals import *
pygame.init()


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

# variables objects
ETHER = 'N'
NEEDLE = 'O'
TUBE = 'P'

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
        self.remaining_objects = {ETHER, NEEDLE, TUBE}
        self.list_object = ['N', 'O', 'P']
        #self.list_position_mcgyver = self.position_mcgyver(x, y)
        self.dimension = 15

    def lec_fichier(self, a):
        """ To read labyrinthe file """
        self.liste_all = []
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
                self.liste_all += [liste_letter]
            return(self.liste_all)


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
        if touch == K_DOWN:
            # if down, y takes +1
            if 0 <= y <= 13:
                y += 1
        if touch == K_UP:
            # if top, y takes -1
            if 1 <= y <= 14:
                y -= 1
        if touch == K_LEFT:
            # if left, x takes -1
            if 1 <= x <= 14:
                x -= 1
        if touch == K_RIGHT:
            # if right, x takes +1
            if 0 <= x <= 13:
                x += 1
        return (x, y)

    def saisie_objet(self, e):
        """ check objects took """
        if (e == ETHER or e == NEEDLE or e == TUBE):
            """ player comes to a case, if the case = 1 of 3 objects """
            print("C'est un objet")
            self.remaining_objects.remove(e)
            #self.list_object(e)
            print(self.remaining_objects)

    def macgyver_visual(self, y2, x2):
        show_laby = deepcopy(a.list_all)
        show_laby[y2][x2] = "X"
        for r in show_laby:
            print(r)


#### FONCTIONS ####
def annonce(nom):
    """ Print the announce """
    print("*** Hello " + nom + ", bienvenue dans le nouveau, super, fabuleux jeux de Mac Gyver!!! ***")
    print("Tu dois aider Mac Gyver (Big Mac pour les intimes) à sortir!")
    print("Tu devras recupérer tous les objets pour créer une")
    print("seringue et endormir le gardien à la sortie ;) .")
    print("Les touches directions sont e : Haut, x : bas, d : droite et s :gauche")
    print("Pour quitter, appuyer sur la touche q")

def pyg_laby():
    laby_fenetre.blit(laby_background, (0, 0))
    x_lab = 0
    y_lab = 0
    while x_lab <= 14:
        while y_lab <= 14:
            if a.liste_all[y_lab][x_lab] == 'M':
                #print(str(x_lab) + " * " + str(y_lab))
                laby_fenetre.blit(mur, (x_lab * 60, y_lab * 60))
            elif a.liste_all[y_lab][x_lab] == ETHER:
                #print(str(x_lab) + " * " + str(y_lab))
                laby_fenetre.blit(img_ether, (x_lab * 60, y_lab * 60))
            elif a.liste_all[y_lab][x_lab] == NEEDLE:
                #print(str(x_lab) + " * " + str(y_lab))
                laby_fenetre.blit(img_aiguille, (x_lab * 60, y_lab * 60))
            elif a.liste_all[y_lab][x_lab] == TUBE:
                #print(str(x_lab) + " * " + str(y_lab))
                laby_fenetre.blit(img_tube_plastique, (x_lab * 60, y_lab * 60))
            elif a.liste_all[y_lab][x_lab] == 'S':
                #print(str(x_lab) + " * " + str(y_lab))
                laby_fenetre.blit(mechant, (x_lab * 60, y_lab * 60))
            y_lab += 1
        y_lab = 0
        x_lab += 1
    x_lab = 0


if __name__=='__main__':

    # pygame variable
    laby_fenetre = pygame.display.set_mode((900, 900))
    laby_background = pygame.image.load("background_test.jpg").convert()
    laby_background = pygame.transform.scale(laby_background, (900, 900))
    laby_fenetre.blit(laby_background, (0, 0))
    mur = pygame.image.load("mur.jpeg").convert()
    mur = pygame.transform.scale(mur, (60, 60))

    img_ether = pygame.image.load("ether.png").convert()
    img_ether = pygame.transform.scale(img_ether, (60, 60))

    img_aiguille = pygame.image.load("aiguille.png").convert()
    img_aiguille = pygame.transform.scale(img_aiguille, (60, 60))

    img_tube_plastique = pygame.image.load("tube_plastique.png").convert()
    img_tube_plastique = pygame.transform.scale(img_tube_plastique, (60, 60))

    mcg = pygame.image.load("MacGyver.png").convert()
    mcg = pygame.transform.scale(mcg, (60, 60))
    position_mcg = mcg.get_rect()
    laby_fenetre.blit(mcg, position_mcg)

    mechant = pygame.image.load("Gardien.png").convert()
    mechant = pygame.transform.scale(mechant, (60, 60))

    rip = pygame.image.load("Rip.jpg").convert()
    rip = pygame.transform.scale(rip, (600, 600))

    mg_win = pygame.image.load("mgwin.jpg").convert()
    mg_win = pygame.transform.scale(mg_win, (600, 600))

    pygame.display.flip()

    # control that is a first play

    # Creating of 'a' object
    a = Labyrinthe(LABY_FILE)

    a.pos_object(a.list_object)

        #pygame.display.flip()

    #joueur = input("Quel est votre nom de joueur?\n")
    #annonce(joueur)

    while BIG_MAC != OUT:
        rip_check = 0
        win_check = 0
        for event in pygame.event.get():
            if event.type == QUIT:
                BIG_MAC = OUT
            if event.type == KEYDOWN:
                x2, y2 = a.mouvement(event.key, x, y)
                if a.position(x2, y2) == WALL:
                    print("C'est un mur!!! ")  # + "*" +action + "*" +str(x) + " " + str(y) + " " + str(big_mac))
                else:
                    # on MAJ les coordonnées de la variable big_mac
                    print(x2)
                    if event.key == K_DOWN and y < 14:
                        position_mcg = position_mcg.move(0, 60)
                    if event.key == K_LEFT and x > 0:
                        position_mcg = position_mcg.move(-60, 0)
                    if event.key == K_RIGHT and x < 14:
                        position_mcg = position_mcg.move(60, 0)
                    if event.key == K_UP and y > 0:
                        position_mcg = position_mcg.move(0, -60)
                    x = x2
                    y = y2
                    BIG_MAC = a.position(x, y)
                    #print(position_mcg)

                        # fonction pour le controle des objets
                    a.saisie_objet(BIG_MAC)
                        # modification de la lettre actuelle en C (apres verif mur et objets)
                    a.list_all[y2][x2] = 'C'
                        #print("*" + action + "*" + str(x) + " " + str(y) + " " + BIG_MAC)
                        #a.macgyver_visual(y2, x2)
                        # position actuelle de mcgyver sur la case X
                        # verification sortie avec objets
                if BIG_MAC == OUT and len(a.remaining_objects) != 0:
                    #print("Tu n'avais pas tous les objets, RIP Mac Gyver!")
                    rip_check = 1
                elif BIG_MAC == OUT and len(a.remaining_objects) == 0:
                    #print("Bravo , Mac Gyver a endormi le gardin, il est libre!!!")
                    win_check = 1

        pyg_laby()
        laby_fenetre.blit(mcg, position_mcg)
        if rip_check == 1:
            laby_fenetre.blit(rip, (150,150))
        elif win_check == 1:
            laby_fenetre.blit(mg_win, (150, 150))
        pygame.display.flip()
    pygame.time.wait(5000)
    pygame.quit()

