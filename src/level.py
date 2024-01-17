import pygame
from tiles import Tuile
from endPoint import End_Point
from modele import TILE_SIZE, LONGUEUR
from perso import Player


class Niveau:
    def __init__(self, level_data, surface):
        # Setup du niveau
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0
        self.player_life = True
        self.victory = False

    def get_player_life(self):
        return self.player_life

    def set_player_life(self, value):
        self.player_life = value

    def get_victory(self):
        return self.victory

    def set_victory(self, value):
        self.victory = value

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.end = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE

                if cell == "X":
                    tile = Tuile((x, y), TILE_SIZE)
                    self.tiles.add(tile)
                if cell == "P":
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)
                if cell == "E":
                    end_point = End_Point((x, y), TILE_SIZE)
                    self.end.add(end_point)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < LONGUEUR / 4 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > LONGUEUR / 2.2 and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
        for sprite in self.end.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    self.victory = True
                elif player.direction.x > 0:
                    self.victory = True

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.direction.y = 0
                    player.rect.bottom = sprite.rect.top
                elif player.direction.y < 0:
                    player.direction.y = 0
                    player.rect.top = sprite.rect.bottom
        for sprite in self.end.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    self.victory = True
                elif player.direction.y < 0:
                    self.victory = True

    def mort_chutte(self):
        player = self.player.sprite
        player_y = player.rect.centery
        if player_y > 704:
            self.player_life = False

    def run(self):
        # Cases du niveau
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.end.update(self.world_shift)
        self.end.draw(self.display_surface)
        self.scroll_x()

        # Player
        self.player.update()
        self.mort_chutte()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)
