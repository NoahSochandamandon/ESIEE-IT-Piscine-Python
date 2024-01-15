import pygame

FPS = 60
LONGUEUR = 1280
LANGUEUR = 720


class JeuVue:
    def __init__(self):
        pygame.init()
        self.ecran = pygame.display.set_mode((LONGUEUR, LANGUEUR))

    def afficher(self, modele):
        self.ecran.fill((255, 255, 255))  # Fond blanc
        # Affiche le joueur
        pygame.draw.rect(
            self.ecran,
            (0, 128, 255),
            pygame.Rect(modele.joueur_position[0], modele.joueur_position[1], 50, 50),
        )
        # Affiche les obstacles
        for obstacle in modele.obstacles:
            pygame.draw.rect(
                self.ecran, (255, 0, 0), pygame.Rect(obstacle[0], obstacle[1], 20, 20)
            )
        # Affiche le score
        font = pygame.font.SysFont(None, 55)
        score_text = font.render(f"Score: {modele.score}", True, (0, 0, 0))
        self.ecran.blit(score_text, (10, 10))
        pygame.display.flip()
