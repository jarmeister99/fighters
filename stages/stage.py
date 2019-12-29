import pygame

from tiles.SolidTile import SolidTile


class StageBuilder():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def load_stage(self, stage_key):
        tiles = pygame.sprite.Group()
        if stage_key == 'GRASS_PLATFORM':
            for i in range(self.width // 64 + 1):
                tiles.add(SolidTile(i * 64, self.height - 64, 64, 64, 'grass.png'))
        tiles.add(SolidTile(275, (self.height / 2) + 110, self.width - 550, 25, 'gold.png'))
        return tiles
