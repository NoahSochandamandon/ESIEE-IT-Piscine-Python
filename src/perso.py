import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((32, 64))
        self.image.fill("red")
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0, 0)

        # Player movement
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -16

        # test
        self.fly = False

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE]:
            self.jump()

        if keys[pygame.K_f] and self.fly:
            self.fly = False
        elif keys[pygame.K_f] and not self.fly:
            self.fly = True

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        if self.direction.y == 0 or self.fly:
            self.direction.y = self.jump_speed

    def update(self):
        self.get_input()
