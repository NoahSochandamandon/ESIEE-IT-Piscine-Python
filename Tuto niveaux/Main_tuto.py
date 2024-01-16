import pygame, sys
from settings import *
from tiles import Tuile
from level import Niveau

# Config fenêtre
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Niveau(carte_niveau_1,screen)

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

# Fond noir ecran
    screen.fill('black')
    level.run()

    pygame.display.update()
    clock.tick(60)
