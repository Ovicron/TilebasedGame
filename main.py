import pygame as pg
from constants import *
from sprites import *
from map import *


class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        pg.display.set_caption('Game')
        self.window = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.running = True
        self.playing = True
        self.load_data()

    def load_data(self):
        self.map = Map('map.txt')

    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)
        self.camera = Camera(self.map.width, self.map.height)

    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
            self.running = False

    def update(self):
        self.all_sprites.update()
        self.camera.update(target=self.player)

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.window, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.window, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        pg.display.set_caption('{:.2f}'.format(self.clock.get_fps()))  # Displays FPS
        self.window.fill(DARKGREY)
        self.draw_grid()
        for sprite in self.all_sprites:
            self.window.blit(sprite.image, self.camera.apply(sprite))
        pg.display.flip()


g = Game()
while g.running:
    g.new()
    g.run()

pg.quit()
