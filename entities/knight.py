import pygame
import os
from utility import spritesheet


class Knight(pygame.sprite.Sprite):
    def __init__(self, x, y, game):
        super(Knight, self).__init__()

        # Declare gameplay members
        self.x = x
        self.y = y
        self.game = game
        self.width = 125
        self.height = 125

        # Declare physics members
        self.move_vector = [0, 0]

        # Declare animation members
        self.animations = {}
        self.animation_time = 3
        self.animation_elapsed_time = 0
        self.animation_steps = 0
        self.load_animations()
        self.current_animation = 'idle'

        # Initial image state
        self.image = self.animations.get(self.current_animation)[0]
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self):
        # Handle logic
        self.move_vector[1] = 5
        self.move()

        # Handle animation
        self.animation_elapsed_time += 1
        if self.animation_elapsed_time % self.animation_time == 0:
            self.animation_steps += 1
        animation_index = self.animation_steps % len(self.animations['idle'])
        self.image = self.animations.get(self.current_animation)[animation_index]

    def move(self):
        test_rect = pygame.Rect(self.x + self.move_vector[0], self.y, self.width, self.height)
        if test_rect.collidelist([tile.rect for tile in self.game.tiles]) == -1:
            self.x += self.move_vector[0]
            self.move_vector[0] = 0
            self.updateRect()
        test_rect = pygame.Rect(self.x, self.y + self.move_vector[1], self.width, self.height)
        if test_rect.collidelist([tile.rect for tile in self.game.tiles]) == -1:
            self.y += self.move_vector[1]
            self.move_vector[1] = 0
            self.updateRect()


    def updateRect(self):
        self.rect.left = self.x
        self.rect.top = self.y
        self.rect.width = self.width
        self.rect.height = self.height

    def load_animations(self):
        animation_directory = os.path.abspath('img/entities/knight')
        ss = spritesheet.SpriteSheet(os.path.join(animation_directory, 'idle.png'))
        self.animations['idle'] = ss.load_strip(64, 64, 15, l_shrink=22, t_shrink=12)
        for key in self.animations.keys():
            for i in range(len(self.animations.get(key))):
                self.animations.get(key)[i] = pygame.transform.scale(self.animations.get(key)[i], (self.width, self.height))
