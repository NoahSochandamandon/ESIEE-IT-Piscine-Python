import pygame
import random

TILE_SIZE = 64
LONGUEUR = 1280
LARGEUR = 704
FONT = "./font/8bit16.ttf"
GAME_NAME = "Plateformer ESIEE-IT"


class JeuModel:
    def __init__(self):
        self.LVL_MAX = 2
        self.vivant = False

        self.ecran = 1  # 1 = démarrage, 2 = selection niveaux, 3 = mort, 4 = victoire, 5 = lvl 1, 6 = lvl 2
        self.selected_lvl = 1  # variable de selection de niveau
        self.selected_death_box = 1
        self.score = 0

    # setter and getter
    def get_selected_lvl(self):
        return self.selected_lvl

    def set_selected_lvl(self, value):
        if value > self.LVL_MAX:
            self.selected_lvl = 1
        elif value < 1:
            self.selected_lvl = self.LVL_MAX
        else:
            self.selected_lvl = value

    def get_selected_death_box(self):
        return self.selected_death_box

    def set_selected_death_box(self, value):
        if value > self.LVL_MAX:
            self.selected_death_box = 1
        elif value < 1:
            self.selected_death_box = 2
        else:
            self.selected_death_box = value

    def get_ecran(self):
        return self.ecran

    def set_ecran(self, value):
        self.ecran = value

    def get_vivant(self):
        return self.vivant

    def set_vivant(self, value):
        self.vivant = value

    # fonction utiles au jeu
    def ajouter_obstacle(self):
        # Ajoute un nouvel obstacle à une position aléatoire
        x = random.randint(0, 600)
        y = random.randint(0, 400)
        self.obstacles.append([x, y])

    def mise_a_jour(self):
        # Met à jour le jeu (par exemple, déplacer les obstacles, augmenter le score)
        self.score += 1
