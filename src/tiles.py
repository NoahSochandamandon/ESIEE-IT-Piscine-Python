import pygame


class Tuile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.blit(
            pygame.transform.scale(
                pygame.image.load("./sprites/block/block.png"),
                (size, size),
            ),
            (0, 0),
        )
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift
