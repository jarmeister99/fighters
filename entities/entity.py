import pygame

from phys.collision import is_on_ground


class Entity(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()

        self.game = game

        # Physics attributes
        self.move_vector = [0, 0]
        self.move_speed = 0

        # Physical attributes
        self.width = 0
        self.height = 0

        # Image attributes
        self.image = None
        self.rect = None
        self.facing = None

        # Components
        self.components = {}

    def update(self):
        for component in self.components.values():
            component.update()
        self.move()

    def move(self):
        if self.move_vector[0] != 0:
            terrain = [terrain.rect for terrain in self.game.terrain]
            move_amount = self.move_vector[0] * self.move_speed
            test_rect = self.rect.copy()

            if self.move_vector[0] == -1:
                test_rect.left += move_amount
                if test_rect.collidelist(terrain) == -1:
                    self.rect.left = test_rect.left
                else:
                    test_rect.left -= move_amount
                    while test_rect.collidelist(terrain) == -1:
                        test_rect.left += self.move_vector[0]
                    self.rect.left = test_rect.left
            elif self.move_vector[0] == 1:
                test_rect.right += move_amount
                if test_rect.collidelist(terrain) == -1:
                    self.rect.right = test_rect.right
                else:
                    test_rect.right -= move_amount
                    while test_rect.collidelist(terrain) == -1:
                        test_rect.right += self.move_vector[0]
                    self.rect.right = test_rect.right

        if self.move_vector[1] != 0:

            test_rect = self.rect.copy()
            test_rect.top += self.move_vector[1]

            if not is_on_ground(test_rect, [terrain.rect for terrain in self.game.terrain]):
                self.rect.top += self.move_vector[1]

            else:
                closest_movement = 0
                test_rect = self.rect.copy()
                while not is_on_ground(test_rect, [terrain.rect for terrain in self.game.terrain]):
                    test_rect.top += closest_movement
                    closest_movement += 1
                self.rect.top += closest_movement
