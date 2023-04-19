import pygame
from tiles import Tile
from settings import gamesettings
from player import Player

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for row_index, row in enumerate(layout):
            for cell_index, cell in enumerate(row):
                y = row_index * gamesettings.tile_size
                x = cell_index * gamesettings.tile_size
                if cell == 'X':
                    tile = Tile((x, y), gamesettings.tile_size)
                    self.tiles.add(tile)
                if cell == 'P':
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < gamesettings.screen_width/4 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > gamesettings.screen_width - (gamesettings.screen_width / 4) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 3

    def horizontal_movmement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                if player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0 # To negate the increase in gravity for player being idle on the tile
                if player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0 # Makes sure the player falls down after collision with the tile

    def run(self):
        # tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x()

        # player
        self.vertical_movement_collision()
        self.horizontal_movmement_collision()
        self.player.update()
        self.player.draw(self.display_surface)
