import pygame


class Entity(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()

        self.game = game

        # Physics attributes
        self.move_vector = []
        self.move_speed = 0

        # Physical attributes
        self.width = 0
        self.height = 0

        # Image attributes
        self.image = None
        self.rect = None
        self.facing = None


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
