import pygame
from modele import JeuModel
from vue import JeuVue
from controleur import JeuControleur


def main():
    MODELE = JeuModel()
    VUE = JeuVue()
    CONTROLEUR = JeuControleur(MODELE, VUE)
    CONTROLEUR.jouer()
    pygame.quit()


if __name__ == "__main__":
    main()
