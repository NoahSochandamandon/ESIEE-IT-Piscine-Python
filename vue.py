import pygame
import os

FPS = 60
LONGUEUR = 1280
LANGUEUR = 720
FONT = "./font/8bit16.ttf"


class JeuVue:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.ecran = pygame.display.set_mode((LONGUEUR, LANGUEUR))
        self.fond = pygame.transform.scale(
            pygame.image.load("./sprites/background/wall.png"), (LONGUEUR, LANGUEUR)
        )

    def get_clock(self):
        return self.clock

    def set_clock(self, value):
        self.clock = value

    def afficher_screen_1(self, modele):
        self.ecran.blit(self.fond, (0, 0))
        pygame.display.set_caption("Jeu en style 8 bits")

        texte = "Appuyez sur espace pour commencer"
        couleur_texte = (255, 255, 255)
        police = pygame.font.Font(FONT, 36)

        surface_texte = police.render(texte, True, couleur_texte)
        position_texte = surface_texte.get_rect(center=(LONGUEUR / 2, LANGUEUR / 2))

        self.ecran.blit(surface_texte, position_texte)

        pygame.display.flip()

    def afficher_screen_2(self, modele):
        self.ecran.blit(self.fond, (0, 0))
        pygame.draw.rect(
            self.ecran,
            (0, 128, 255),
            pygame.Rect(modele.joueur_position[0], modele.joueur_position[1], 50, 50),
        )
        pygame.display.flip()

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
