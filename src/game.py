import pygame as pg
import pymunk as pm

class Game():
    def __init__(self):
        self.caption = 'Kepler-452'
        self.fps = 60
        self.camera_width = 400
        self.camera_height = 600

    def game_initialize(self):
        pg.init()
        camera = pg.display.set_mode((self.camera_width, self.camera_height))
        pg.display.set_caption(self.caption)
        clock = pg.time.Clock()
        self.game_run(camera, clock)

    def game_run(self, camera, clock):

        space = pm.Space()

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        quit()

            space.step(1/self.fps)

            camera.fill([250, 250, 250])

            pg.display.flip()
            clock.tick(self.fps)

if __name__ == '__main__':
    new_game = Game()
    new_game.game_initialize()

