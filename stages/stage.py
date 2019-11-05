import pygame

from tiles.gold import Gold


class StageBuilder():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def load_stage(self, stage_key):
        tiles = pygame.sprite.Group()
        if stage_key == 'GOLDEN_PLATFORM':
            for i in range(self.width // 64):
                tiles.add(Gold(i * 64 + 20, self.height - 64, 64, 64))
        return tiles
