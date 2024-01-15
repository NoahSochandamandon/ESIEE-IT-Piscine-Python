import pygame
import random


class JeuModel:
    def __init__(self):
        self.joueur_position = [50, 50]
        self.obstacles = []
        self.ecran = 1  # 1 = démarrage, 2 = selection niveaux, 3 = lvl 1, 4 = lvl 2
        self.score = 0

    def get_ecran(self):
        return self.ecran

    def set_ecran(self, value):
        self.ecran = value

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
