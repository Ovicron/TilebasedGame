import pygame as pg
from constants import *


class Map:
    def __init__(self, filename):
        self.data = []
        with open(filename, 'r') as f:
            for line in f:
                self.data.append(line.strip())

        self.tilewidth = len(self.data[0])
        self.tileheight = len(self.data)
        self.width = self.tilewidth * TILESIZE
        self.height = self.tileheight * TILESIZE


class Camera:
    def __init__(self, width, height):
        # Creates the rectangle around the player
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        # Moves the camera rectangle, when the entity moves.
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        # Camera follows the sprite (target)
        x = -target.rect.x + int(WIDTH / 2)
        y = -target.rect.y + int(HEIGHT / 2)

        # limit map border scroll
        x = min(0, x)
        y = min(0, y)
        x = max(-(self.width - WIDTH), x)
        y = max(-(self.height - HEIGHT), y)
        self.camera = pg.Rect(x, y, self.width, self.height)
