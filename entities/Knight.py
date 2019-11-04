import pygame
import os
from utility import spritesheet

class Knight(pygame.sprite.Sprite):
    def __init__(self):
        super(Knight, self).__init__()
        self.animations = {}
        self.animation_index = 0
        self.rect = pygame.Rect((64, 64))
        self.load_animations()

    def load_animations(self):
        animation_directory = os.path.abspath('img/entities/knight')
        ss = spritesheet.SpriteSheet(os.path.join(animation_directory, 'idle'))
        self.animations['idle'] = spritesheet.SpriteSheet().load_strip(self.rect, 15)

    def draw(self):
        pass



