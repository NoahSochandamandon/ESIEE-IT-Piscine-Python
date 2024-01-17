import pygame
from os import walk


def import_folder(path):
    surface_list = []

    for _, __, img_files in walk(path):
        for image in img_files:
            full_path = path + "/" + image
            image_surface = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surface)

    return surface_list


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.import_character_assets()
        # suppression couleur de merde et ajout des trois lignes ci dessous
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations["stop"][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0, 0)

        # Player movement
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -16

        # Ajout player status
        self.status = "stop"

        # test
        self.fly = False

    def import_character_assets(self):
        character_path = ".\\sprites\\skin\\"
        self.animations = {"run": [], "stop": []}

        for animation in self.animations.keys():
            full_path = character_path + animation
            loaded_images = import_folder(full_path)
            scaled_images = [
                pygame.transform.scale(img, (64, 64)) for img in loaded_images
            ]
            self.animations[animation] = scaled_images

    # ajout fonction animate pour animer le perso
    def animate(self):
        animation = self.animations[self.status]

        # boucle d'animation
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]

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

    def get_status(self):
        if self.direction.x != 0:
            self.status = "run"
        else:
            self.status = "stop"

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        if self.direction.y == 0 or self.fly:
            self.direction.y = self.jump_speed

    def update(self):
        self.get_input()
        self.get_status()
        self.animate()
