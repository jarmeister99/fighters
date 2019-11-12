import os
import pygame

from entities.knight import Knight
from stages.stage import StageBuilder

GAME_WIDTH = 1000
GAME_HEIGHT = 700

class Game:
    def __init__(self):
        self.entities = pygame.sprite.Group()
        self.tiles = None
        self.stage_builder = None
        self.backgrounds = {}
        self.current_bg = None
        self.playing = False
        self.width = GAME_WIDTH
        self.height = GAME_HEIGHT
        self.win = pygame.display.set_mode((self.width, self.height))
        self.load_backgrounds()

    def load_backgrounds(self):
        for filename in os.listdir('img/backgrounds'):
            bg = pygame.image.load(os.path.join("img", "backgrounds", filename))
            bg = pygame.transform.scale(bg, (self.width, self.height))
            self.backgrounds[os.path.splitext(filename)[0]] = bg

    def run(self):
        self.playing = True
        self.current_bg = self.backgrounds.get("day_sky")
        clock = pygame.time.Clock()
        self.entities.add(Knight(0, 0, self))
        self.stage_builder = StageBuilder(self.width, self.height)
        self.tiles = self.stage_builder.load_stage('GOLDEN_PLATFORM')

        while self.playing:
            clock.tick(60)
            self.process_input()
            self.process_logic()
            self.process_rendering()
        pygame.quit()

    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def process_logic(self):
        self.entities.update()

    def process_rendering(self):
        self.win.blit(self.current_bg, (0, 0))
        self.entities.draw(self.win)
        self.tiles.draw(self.win)
        pygame.display.flip()


game = Game()
game.run()
