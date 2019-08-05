""" Creating a labyrinth game.
MacGyver must go out with 3 objects.

Rules about labyrinthe.txt file
D for the start position
S for the ending
M for the wall
C for the way
E for the wrong way
S for the ending''
"""

import os
import random
import pygame.display
from pygame.locals import *

pygame.init()

#### VARIABLES ####
# x y initialisation
x = 0
y = 0

# player
BIG_MAC = 0

# screen size
SCREEN = 300
CASE_NUMBER = 15
CASE_SIZE = int(SCREEN / CASE_NUMBER)

# Labyrinth file's path
LABY_FILE = "labyrinth.txt"

# variables objects
ETHER = "N"
NEEDLE = "O"
TUBE = "P"

# beginning, ending, wall regarding letters of file
START = "D"
OUT = "S"
WALL = "M"


#### CLASS ####

# The Labyrinth class will contain all the information to create the structure of the labyrinth
class Labyrinthe:
    def __init__(self, fichier_laby):
        # x and y will contain the coordinates of the letters
        self.x = 0
        self.y = 0
        # list_all will be a list of list who contain the letters of the structure of the labyrinth
        self.list_all = self.lec_fichier(fichier_laby)
        # remaining_objects will permit to check items always in the labyrinth
        self.remaining_objects = {ETHER, NEEDLE, TUBE}
        # list to if case is an object
        self.list_object = ["N", "O", "P"]
        self.dimension = 15

    def lec_fichier(self, a):
        """ To read labyrinthe file """
        self.liste_all = []
        with open(a, "r") as fichier:
            # cut file by line
            reading = fichier.read().splitlines()
            # cut line by letter to creating a table 2 dimensions
            for line in reading:
                liste_letter = [i for i in line]
                self.liste_all += [liste_letter]
            return self.liste_all

    def position(self, a, b):
        """ to find a position in labyrinth regading x & y """
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
            if prev == "C":
                # if C, we change the letter of this position in list_all by one of 3 letter
                self.list_all[axe2][axe1] = x.pop()

    def mouvement(self, touch, x, y):
        """ to update x & y variables """
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
        if e == ETHER or e == NEEDLE or e == TUBE:
            """ player comes to a case, if the case = 1 of 3 objects """
            self.remaining_objects.remove(e)
            print(self.remaining_objects)


#### FONCTIONS ####


def pyg_laby():
    """ to create visual labyrinth structure"""
    laby_fenetre.blit(laby_background, (0, 0))
    laby_mini_background.blit(laby_mini_background, (0, SCREEN))
    x_lab = 0
    y_lab = 0
    while x_lab <= 14:
        while y_lab <= 14:
            # to create a wall
            if a.liste_all[y_lab][x_lab] == "M":
                laby_fenetre.blit(mur, (x_lab * CASE_SIZE, y_lab * CASE_SIZE))
            # to create an ether
            elif a.liste_all[y_lab][x_lab] == ETHER:
                laby_fenetre.blit(img_ether, (x_lab * CASE_SIZE, y_lab * CASE_SIZE))
            # to create an needle
            elif a.liste_all[y_lab][x_lab] == NEEDLE:
                laby_fenetre.blit(img_aiguille, (x_lab * CASE_SIZE, y_lab * CASE_SIZE))
            # to create a tube
            elif a.liste_all[y_lab][x_lab] == TUBE:
                laby_fenetre.blit(
                    img_tube_plastique, (x_lab * CASE_SIZE, y_lab * CASE_SIZE)
                )
            # to create the gardian
            elif a.liste_all[y_lab][x_lab] == "S":
                # print(str(x_lab) + " * " + str(y_lab))
                laby_fenetre.blit(mechant, (x_lab * CASE_SIZE, y_lab * CASE_SIZE))
            y_lab += 1
        # y must be reset for the next x
        y_lab = 0
        x_lab += 1
    x_lab = 0


def compt_obj():
    """ to print object if always in the labyrinth """
    if NEEDLE in a.remaining_objects:
        laby_fenetre.blit(img_mini_aiguille, (CASE_SIZE, SCREEN))
    if ETHER in a.remaining_objects:
        laby_fenetre.blit(img_mini_ether, (CASE_SIZE * 2, SCREEN))
    if TUBE in a.remaining_objects:
        laby_fenetre.blit(img_mini_tube_plastique, (CASE_SIZE * 3, SCREEN))
    if len(a.remaining_objects) == 0:
        laby_fenetre.blit(img_seringue, (CASE_SIZE * 4, SCREEN))


def get_true_filename(filename):
    """ function to permit to start the program in windows, linux or mac OS """
    try:
        # Hack for pyInstaller. Refer https://stackoverflow.com/a/13790741
        base = sys._MEIPASS
    except Exception:
        base = os.path.abspath(".")
    return os.path.join(base, filename)


if __name__ == "__main__":

    # pygame variable to print at the beginning
    laby_fenetre = pygame.display.set_mode((SCREEN, SCREEN + CASE_SIZE))
    laby_background = pygame.image.load(
        get_true_filename("background_test.jpg")
    ).convert()
    laby_background = pygame.transform.scale(laby_background, (SCREEN, SCREEN))
    laby_fenetre.blit(laby_background, (0, 0))

    laby_mini_background = pygame.image.load(get_true_filename("mur.jpeg")).convert()
    laby_mini_background = pygame.transform.scale(
        laby_mini_background, (SCREEN, CASE_SIZE)
    )
    laby_fenetre.blit(laby_mini_background, (0, SCREEN))

    mur = pygame.image.load(get_true_filename("mur.jpeg")).convert()
    mur = pygame.transform.scale(mur, (CASE_SIZE, CASE_SIZE))

    img_ether = pygame.image.load(get_true_filename("ether.png")).convert()
    img_ether = pygame.transform.scale(img_ether, (CASE_SIZE, CASE_SIZE))

    img_mini_ether = pygame.image.load(get_true_filename("ether.png")).convert()
    img_mini_ether = pygame.transform.scale(img_mini_ether, (CASE_SIZE, CASE_SIZE))

    img_aiguille = pygame.image.load(get_true_filename("aiguille.png")).convert()
    img_aiguille = pygame.transform.scale(img_aiguille, (CASE_SIZE, CASE_SIZE))

    img_mini_aiguille = pygame.image.load(get_true_filename("aiguille.png")).convert()
    img_mini_aiguille = pygame.transform.scale(
        img_mini_aiguille, (CASE_SIZE, CASE_SIZE)
    )

    img_tube_plastique = pygame.image.load(
        get_true_filename("tube_plastique.png")
    ).convert()
    img_tube_plastique = pygame.transform.scale(
        img_tube_plastique, (CASE_SIZE, CASE_SIZE)
    )

    img_mini_tube_plastique = pygame.image.load(
        get_true_filename("tube_plastique.png")
    ).convert()
    img_mini_tube_plastique = pygame.transform.scale(
        img_mini_tube_plastique, (CASE_SIZE, CASE_SIZE)
    )

    img_seringue = pygame.image.load(get_true_filename("seringue.png")).convert()
    img_seringue = pygame.transform.scale(img_seringue, (CASE_SIZE, CASE_SIZE))

    mcg = pygame.image.load(get_true_filename("MacGyver.png")).convert()
    mcg = pygame.transform.scale(mcg, (CASE_SIZE, CASE_SIZE))
    position_mcg = mcg.get_rect()
    laby_fenetre.blit(mcg, position_mcg)

    mechant = pygame.image.load(get_true_filename("Gardien.png")).convert()
    mechant = pygame.transform.scale(mechant, (CASE_SIZE, CASE_SIZE))

    rip = pygame.image.load(get_true_filename("Rip.jpg")).convert()
    rip = pygame.transform.scale(rip, (SCREEN, SCREEN + CASE_SIZE))

    mg_win = pygame.image.load(get_true_filename("mgwin.jpg")).convert()
    mg_win = pygame.transform.scale(mg_win, (SCREEN, SCREEN + CASE_SIZE))

    pygame.display.flip()

    # creating of 'a' object
    a = Labyrinthe(get_true_filename("labyrinth.txt"))

    # to put the objects in the labyrinth
    a.pos_object(a.list_object)

    # driving the user faster
    pygame.key.set_repeat(400, 30)

    # main loop
    while BIG_MAC != OUT:
        # to initiate winner or looser variable
        win_check = 0
        for event in pygame.event.get():
            # if player click on cross we close the program
            if event.type == QUIT:
                BIG_MAC = OUT
            if event.type == KEYDOWN:
                x2, y2 = a.mouvement(event.key, x, y)
                # if new position is a wall, we do nothing
                if a.position(x2, y2) == WALL:
                    x2 = x2
                else:
                    # to change player position on the screen
                    if event.key == K_DOWN and y < 14:
                        position_mcg = position_mcg.move(0, CASE_SIZE)
                    if event.key == K_LEFT and x > 0:
                        position_mcg = position_mcg.move(-CASE_SIZE, 0)
                    if event.key == K_RIGHT and x < 14:
                        position_mcg = position_mcg.move(CASE_SIZE, 0)
                    if event.key == K_UP and y > 0:
                        position_mcg = position_mcg.move(0, -CASE_SIZE)
                    x = x2
                    y = y2
                    BIG_MAC = a.position(x, y)

                    # to check if the player position is on an object
                    a.saisie_objet(BIG_MAC)
                    # to change the visual of the position for the next loop (it will be a way)
                    a.list_all[y2][x2] = "C"
                # if the player didn't take all objects
                if BIG_MAC == OUT and len(a.remaining_objects) != 0:
                    win_check = 1
                # if the player take all objects
                elif BIG_MAC == OUT and len(a.remaining_objects) == 0:
                    win_check = 2
            # to print the labyrinth
            pyg_laby()
            # to print the bottom window
            laby_fenetre.blit(laby_mini_background, (0, SCREEN))
            # to print the new player's position
            laby_fenetre.blit(mcg, position_mcg)
            # to print the objects always in the Labyrinth
            compt_obj()
        if win_check == 1:
            laby_fenetre.blit(rip, (0, 0))
        elif win_check == 2:
            laby_fenetre.blit(mg_win, (0, 0))
        pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()
