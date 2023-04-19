import pygame

import sys

from settings import gamesettings

from tiles import Tile
from levels import Level

screen = pygame.display.set_mode((gamesettings.screen_width, gamesettings.screen_height))
clock = pygame.time.Clock()
test_tile = pygame.sprite.Group(Tile((100, 100), 100))
level = Level(gamesettings.level_map, screen)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    player_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill('black')

        # pygame.draw.circle(screen, "red", player_pos, 40)
        test_tile.draw(screen)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            print(f"Keys pressed: {keys[pygame.K_w]}")
            player_pos.y -= 300 * dt

        level.run()
        pygame.display.update()
        clock.tick(60)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
