import pygame
from level import Niveau
from map.map_1 import *
from modele import LONGUEUR, LARGEUR, FONT, GAME_NAME
import os
from pygame.mixer import *

# LONGUEUR = 1280
# LARGEUR = 704
# FONT = "./font/8bit16.ttf"
# GAME_NAME = "Plateformer ESIEE-IT"


class JeuVue:
    def __init__(self):
        
        pygame.init()
        
        self.ecran = pygame.display.set_mode((LONGUEUR, LARGEUR))
        self.fond = pygame.transform.scale(
            pygame.image.load("./sprites/background/wall.png"), (LONGUEUR, LARGEUR)
        )
        self.police = pygame.font.Font(FONT, 36)
        self.couleur_texte = (255, 255, 255)
        self.level_1 = Niveau(carte_niveau_1, self.ecran)
        
        pygame.mixer.init()
        
       
        
        pygame.mixer.music.load("Espada.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)
     

        pygame.display.flip()
         
    # vue des menus
    def afficher_screen_1(self, modele):
        self.ecran.blit(self.fond, (0, 0))
        pygame.display.set_caption(GAME_NAME)

        texte = "Appuyez sur espace pour commencer"

        surface_texte = self.police.render(texte, True, self.couleur_texte)
        position_texte = surface_texte.get_rect(center=(LONGUEUR / 2, LARGEUR / 2))

        self.ecran.blit(surface_texte, position_texte)

        pygame.display.flip()

    def afficher_screen_2(self, modele):
        self.fond = pygame.transform.scale(
            pygame.image.load("./sprites/background/wall2.png"), (LONGUEUR, LARGEUR)
        )
        self.ecran.blit(self.fond, (0, 0))
        pygame.display.set_caption(GAME_NAME)

        text_boxes = [
            self.creer_text_box(
                "niveau 1", LONGUEUR // 2 - 100, LARGEUR // 2 - 50, 200, 50
            ),
            self.creer_text_box(
                "niveau 2", LONGUEUR // 2 - 100, LARGEUR // 2 + 50, 200, 50
            ),
        ]

        for index, (rect, text_surface) in enumerate(text_boxes):
            pygame.draw.rect(self.ecran, (60, 60, 60), rect)
            if (index + 1) == modele.get_selected_lvl():
                pygame.draw.rect(self.ecran, (255, 255, 255), rect, 8)
            self.ecran.blit(
                text_surface,
                (
                    rect.x + (rect.width - text_surface.get_width()) // 2,
                    rect.y + (rect.height - text_surface.get_height()) // 2,
                ),
            )

        pygame.display.flip()

    # vue des niveau in game
    def afficher_screen_3(self, modele):
        self.ecran.fill("black")
        self.level_1.run()

        pygame.display.update()
        # self.clock.tick(60)

    def creer_text_box(self, texte, x, y, largeur, hauteur):
        rect = pygame.Rect(x, y, largeur, hauteur)
        text_surface = self.police.render(texte, True, self.couleur_texte)
        return rect, text_surface