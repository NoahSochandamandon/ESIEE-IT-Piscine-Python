import pygame
import random


class JeuModel:
    def __init__(self, perso):
        self.perso = perso
        self.LVL_MAX = 2

        self.joueur_position = [50, 50]
        self.obstacles = []
        self.ecran = 1  # 1 = démarrage, 2 = selection niveaux, 3 = lvl 1, 4 = lvl 2
        self.selected_lvl = 1  # variable de selection de niveau
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

    def get_ecran(self):
        return self.ecran

    def set_ecran(self, value):
        self.ecran = value

    # fonction utiles au jeu
    def ajouter_obstacle(self):
        # Ajoute un nouvel obstacle à une position aléatoire
        x = random.randint(0, 600)
        y = random.randint(0, 400)
        self.obstacles.append([x, y])

    def deplacer_joueur(self, dx, dy):
        # Déplace le joueur
        self.joueur_position[0] += dx
        self.joueur_position[1] += dy

    def mise_a_jour(self):
        # Met à jour le jeu (par exemple, déplacer les obstacles, augmenter le score)
        self.score += 1
