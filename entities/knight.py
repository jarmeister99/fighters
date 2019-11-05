import pygame
import os
from utility import spritesheet


class Knight(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Knight, self).__init__()
        self.x = x
        self.y = y
        self.width = 125
        self.height = 125
        self.animations = {}
        self.animation_count = 0
        self.load_animations()
        self.current_animation = 'idle'
        self.image = self.animations.get(self.current_animation)[0]
        self.rect = (self.x, self.y, self.width, self.height)

    def update(self):
        self.animation_count += 1
        animation_index = self.animation_count % len(self.animations['idle'])
        self.image = self.animations.get(self.current_animation)[animation_index]

    def load_animations(self):
        animation_directory = os.path.abspath('img/entities/knight')
        ss = spritesheet.SpriteSheet(os.path.join(animation_directory, 'idle.png'))
        self.animations['idle'] = ss.load_strip(64, 64, 15, l_shrink=22, t_shrink=12)
        for key in self.animations.keys():
            for i in range(len(self.animations.get(key))):
                self.animations.get(key)[i] = pygame.transform.scale(self.animations.get(key)[i], (self.width, self.height))
