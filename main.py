#
# Created following these tutorials: https://www.youtube.com/playlist?list=PLywhTYI3VhfJCkp_aQXFj_8-Ac496LmUm
# You are at the beginning of Part 4
#

import pygame, sys
from sounds import *
from player import *
from map_build import *
import maps
from sprites import *
from config import *

pygame.display.set_caption("")

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.terrainsheet = Spritesheet('terrain1.png')
        self.character_spritesheet = Spritesheet('character.png')

    def createTilemap(self, tilemap):
        build_map(self, tilemap)

    def new(self, tilemap):
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.createTilemap(tilemap)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill('Black')
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)

        pygame.display.update()

    def main(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()


TILEMAP = maps.world_1.stage_1
game = Game()
game.new(TILEMAP)
while game.running:
    game.main()

pygame.quit()
sys.exit()
