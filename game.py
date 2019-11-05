import os
import pygame

from entities.knight import Knight


class Game:
    def __init__(self):
        self.entities = pygame.sprite.Group()
        self.backgrounds = {}
        self.current_bg = None
        self.playing = None
        self.width = 1000
        self.height = 700
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
        self.entities.add(Knight(0, 0))
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
        pygame.display.flip()


game = Game()
game.run()
