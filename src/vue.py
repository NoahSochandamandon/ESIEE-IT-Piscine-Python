import pygame
from level import Niveau
from map.map import *
from modele import LONGUEUR, LARGEUR, FONT, GAME_NAME
import os


class JeuVue:
    def __init__(self):
        pygame.init()
        self.ecran = pygame.display.set_mode((LONGUEUR, LARGEUR))
        self.fond = pygame.transform.scale(
            pygame.image.load("./sprites/background/wall.png"), (LONGUEUR, LARGEUR)
        )
        self.police = pygame.font.Font(FONT, 36)
        self.couleur_texte = (255, 255, 255)

    # vue des menus : screen 1 et 2
    def afficher_screen_1(self, modele):
        self.ecran.blit(self.fond, (0, 0))
        pygame.display.set_caption(GAME_NAME)

        texte = "Appuyez sur espace pour commencer"

        surface_texte = self.police.render(texte, True, self.couleur_texte)
        position_texte = surface_texte.get_rect(
            center=(LONGUEUR / 2, LARGEUR / 2 + 100)
        )

        self.ecran.blit(surface_texte, position_texte)

        pygame.display.update()

    def afficher_screen_2(self, modele):
        self.fond = pygame.transform.scale(
            pygame.image.load("./sprites/background/wall2.png"), (LONGUEUR, LARGEUR)
        )
        self.ecran.blit(self.fond, (0, 0))

        text_boxes = [
            self.creer_text_box("niveau 1", LONGUEUR // 2, LARGEUR // 2 - 50, 300, 60),
            self.creer_text_box("niveau 2", LONGUEUR // 2, LARGEUR // 2 + 50, 300, 60),
            self.creer_text_box("Quitter", LONGUEUR // 2, LARGEUR // 2 + 250, 250, 60),
        ]

        for index, (rect, text_surface) in enumerate(text_boxes):
            pygame.draw.rect(self.ecran, (60, 60, 60), rect)
            rect_contour = rect.inflate(10, 10)
            if (index + 1) == modele.get_selected_lvl():
                pygame.draw.rect(self.ecran, (255, 255, 255), rect_contour, 8)
            self.ecran.blit(
                text_surface,
                (
                    rect.x + (rect.width - text_surface.get_width()) // 2,
                    rect.y + (rect.height - text_surface.get_height()) // 2,
                ),
            )

        pygame.display.update()

    # vue des niveau in game
    def afficher_screen_5(self, modele):
        self.ecran.fill("black")
        if not modele.get_vivant():
            self.initialiser_niveau(carte_niveau_1)
            modele.set_vivant(True)

        if not self.level.get_player_life():
            modele.set_ecran(3)
            modele.set_vivant(False)

        if self.level.get_victory():
            modele.set_ecran(4)
            modele.set_vivant(False)

        self.level.run()

    def afficher_screen_6(self, modele):
        self.ecran.fill("black")
        if not modele.get_vivant():
            self.initialiser_niveau(carte_niveau_2)
            modele.set_vivant(True)

        if not self.level.get_player_life():
            modele.set_ecran(3)
            modele.set_vivant(False)

        if self.level.get_victory():
            modele.set_ecran(4)
            modele.set_vivant(False)

        self.level.run()

    def afficher_screen_death(self, modele):
        self.ecran.blit(self.fond, (0, 0))
        pygame.display.set_caption(GAME_NAME)

        texte = "C'est grave comment t'es trop nul"

        text_boxes = [
            self.creer_text_box("Reessayer", LONGUEUR // 2, LARGEUR // 2 + 50, 300, 60),
            self.creer_text_box(
                "Selection des niveaux",
                LONGUEUR // 2,
                LARGEUR // 2 + 150,
                600,
                60,
            ),
            self.creer_text_box("Quitter", LONGUEUR // 2, LARGEUR // 2 + 250, 250, 60),
        ]

        for index, (rect, text_surface) in enumerate(text_boxes):
            pygame.draw.rect(self.ecran, (60, 60, 60), rect)
            rect_contour = rect.inflate(10, 10)
            if (index + 1) == modele.get_selected_death_box():
                pygame.draw.rect(self.ecran, (255, 255, 255), rect_contour, 8)
            self.ecran.blit(
                text_surface,
                (
                    rect.x + (rect.width - text_surface.get_width()) // 2,
                    rect.y + (rect.height - text_surface.get_height()) // 2,
                ),
            )

        surface_texte = self.police.render(texte, True, self.couleur_texte)
        position_texte = surface_texte.get_rect(
            center=(LONGUEUR / 2, LARGEUR / 2 - 150)
        )

        self.ecran.blit(surface_texte, position_texte)

        pygame.display.update()

    def afficher_screen_victory(self, modele):
        self.ecran.blit(
            pygame.transform.scale(
                pygame.image.load("./sprites/background/victoire.jpg"),
                (LONGUEUR, LARGEUR),
            ),
            (0, 0),
        )
        pygame.display.set_caption(GAME_NAME)

        texte = "Et c'est la win, GG"

        text_boxes = [
            self.creer_text_box("Reessayer", LONGUEUR // 2, LARGEUR // 2 + 50, 300, 60),
            self.creer_text_box(
                "Selection des niveaux",
                LONGUEUR // 2,
                LARGEUR // 2 + 150,
                600,
                60,
            ),
            self.creer_text_box("Quitter", LONGUEUR // 2, LARGEUR // 2 + 250, 250, 60),
        ]

        for index, (rect, text_surface) in enumerate(text_boxes):
            pygame.draw.rect(self.ecran, (60, 60, 60), rect)
            rect_contour = rect.inflate(10, 10)
            if (index + 1) == modele.get_selected_death_box():
                pygame.draw.rect(self.ecran, (255, 255, 255), rect_contour, 8)
            self.ecran.blit(
                text_surface,
                (
                    rect.x + (rect.width - text_surface.get_width()) // 2,
                    rect.y + (rect.height - text_surface.get_height()) // 2,
                ),
            )

        surface_texte = self.police.render(texte, True, self.couleur_texte)
        position_texte = surface_texte.get_rect(
            center=(LONGUEUR / 2, LARGEUR / 2 - 150)
        )

        self.ecran.blit(surface_texte, position_texte)

        pygame.display.update()

    def initialiser_niveau(self, carte):
        self.level = Niveau(carte, self.ecran)

    def creer_text_box(self, texte, x, y, largeur, hauteur):
        rect = pygame.Rect(x - (largeur / 2), y, largeur, hauteur)
        text_surface = self.police.render(texte, True, self.couleur_texte)
        return rect, text_surface
