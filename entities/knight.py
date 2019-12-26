import pygame
import os

from components.animated.gravity import Gravity
from components.animated.animate import Animate
from components.animated.flip_image import FlipImage
from components.animated.running_animation import RunningAnimation
from utility import spritesheet


class Knight(pygame.sprite.Sprite):
    def __init__(self, x, y, game):
        super(Knight, self).__init__()

        # Declare gameplay members
        self.game = game
        self.width = 125
        self.height = 125

        # Declare physics members
        self.move_vector = [0, 0]
        self.move_speed = 9

        # Declare animation members
        self.animations = {}
        self.animation_time = 3
        self.animation_elapsed_time = 0
        self.animation_steps = 0
        self.load_animations()
        self.current_animation = 'idle'

        # Declare image variables
        self.image = self.animations.get(self.current_animation)[0]
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.facing = 'RIGHT'

        # Attach components
        self.components = {}
        self.components['flip_image'] = FlipImage(self)
        self.components['animate'] = Animate(self)
        self.components['running_animation'] = RunningAnimation(self)
        self.components['gravity'] = Gravity(self)

    def update(self):
        # Handle logic

        self.move()
        for component in self.components.values():
            component.update()


    def attack(self):
        pass

    def jump(self):
        pass

    def load_animations(self):
        animation_directory = os.path.abspath('img/entities/knight')
        ss = spritesheet.SpriteSheet(os.path.join(animation_directory, 'idle.png'))
        self.animations['idle'] = ss.load_strip(64, 64, 15, l_shrink=22, r_shrink=15, t_shrink=12, d_shrink=20)
        ss = spritesheet.SpriteSheet(os.path.join(animation_directory, 'run.png'))
        self.animations['run'] = ss.load_strip(96, 64, 8, l_shrink=40, r_shrink=32, t_shrink=15, d_shrink=20)
        ss = spritesheet.SpriteSheet(os.path.join(animation_directory, 'attack.png'))
        self.animations['attack'] = ss.load_strip(144, 64, 22)
        for key in self.animations.keys():
            for i in range(len(self.animations.get(key))):
                self.animations.get(key)[i] = pygame.transform.scale(self.animations.get(key)[i],
                                                                     (self.width, self.height))


    def move(self):
        if self.move_vector[0] != 0:
            tiles = [tile.rect for tile in self.game.tiles]
            move_amount = self.move_vector[0] * self.move_speed
            test_rect = self.rect.copy()

            if self.move_vector[0] == -1:
                test_rect.left += move_amount
                if test_rect.collidelist(tiles) == -1:
                    self.rect.left = test_rect.left
                else:
                    test_rect.left -= move_amount
                    while test_rect.collidelist(tiles) == -1:
                        test_rect.left += self.move_vector[0]
                    self.rect.left = test_rect.left
            elif self.move_vector[0] == 1:
                test_rect.right += move_amount
                if test_rect.collidelist(tiles) == -1:
                    self.rect.right = test_rect.right
                else:
                    test_rect.right -= move_amount
                    while test_rect.collidelist(tiles) == -1:
                        test_rect.right += self.move_vector[0]
                    self.rect.right = test_rect.right

        if self.move_vector[1] != 0:
            test_rect = pygame.Rect(self.rect.left, self.rect.top + self.move_vector[1] + self.rect.height,
                                    self.rect.width, 2)
            if test_rect.collidelist([tile.rect for tile in self.game.tiles]) == -1:
                self.rect.top += self.move_vector[1]
            else:
                closest_movement = 0
                test_rect = pygame.Rect(self.rect.left, self.rect.top + closest_movement + self.rect.height,
                                        self.rect.width, 2)
                while test_rect.collidelist([tile.rect for tile in self.game.tiles]) == -1:
                    test_rect.top += closest_movement
                    closest_movement += 1
                self.rect.top += closest_movement
        else:
            # Apply gravity if necessary
            self.move_vector[1] = 1
