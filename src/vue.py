import pygame
import os

FPS = 60
LONGUEUR = 1280
LARGEUR = 720
FONT = "./font/8bit16.ttf"
GAME_NAME = "Plateformer ESIEE-IT"


class JeuVue:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.ecran = pygame.display.set_mode((LONGUEUR, LARGEUR))
        self.fond = pygame.transform.scale(
            pygame.image.load("./sprites/background/wall.png"), (LONGUEUR, LARGEUR)
        )
        self.police = pygame.font.Font(FONT, 36)
        self.couleur_texte = (255, 255, 255)

    def get_clock(self):
        return self.clock

    def set_clock(self, value):
        self.clock = value

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
        self.fond = pygame.transform.scale(
            pygame.image.load("./sprites/background/wall2.png"), (LONGUEUR, LARGEUR)
        )
        self.ecran.blit(self.fond, (0, 0))

        self.ecran.fill((0, 0, 0))  # Effacer l'écran
        self.ecran.blit(
            pygame.transform.scale(
                pygame.image.load(modele.perso.get_sprite_actuel()), (100, 100)
            ).convert_alpha(),
            (modele.perso.get_x(), modele.perso.get_y()),
        )

        pygame.display.flip()

    def creer_text_box(self, texte, x, y, largeur, hauteur):
        rect = pygame.Rect(x, y, largeur, hauteur)
        text_surface = self.police.render(texte, True, self.couleur_texte)
        return rect, text_surface

    # def afficher(self, modele):
    #     self.ecran.blit(self.fond, (0, 0))
    #     # Affiche le joueur
    #     pygame.draw.rect(
    #         self.ecran,
    #         (0, 128, 255),
    #         pygame.Rect(modele.joueur_position[0], modele.joueur_position[1], 50, 50),
    #     )
    #     # Affiche les obstacles
    #     for obstacle in modele.obstacles:
    #         pygame.draw.rect(
    #             self.ecran, (255, 0, 0), pygame.Rect(obstacle[0], obstacle[1], 20, 20)
    #         )
    #     # Affiche le score
    #     font = pygame.font.SysFont(None, 55)
    #     score_text = font.render(f"Score: {modele.score}", True, (0, 0, 0))
    #     self.ecran.blit(score_text, (10, 10))
    #     pygame.display.flip()
