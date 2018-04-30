import pygame
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class App:
    def __init__(self):
        self._running = True
        self._game_display = None
        self._game_title = None
        self.size = self.weight, self.height = 640, 400

    def on_init(self):
        pygame.init()
        self._game_display = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._game_title = pygame.display.set_caption('A Game')
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        pygame.display.update()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            for event in pygame.event.get():
                
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
