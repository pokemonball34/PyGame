import pygame
import random
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Creep:
    def __init__(self, color):
        self.x = random.randrange(0, self.width)
        self.y = random.randrange(0, self.height)
        self.size = random.randrange(4, 8)
        self.color = color

    def move(self):
        self.move_x = random.randrange(-1, 2)
        self.move_y = random.randrange(-1, 2)
        self.x += self.move_x
        self.y += self.move_y

        if self.x < 0:
            self.x = 0
        elif self.x > self.width:
            self.x = self.width

        if self.y < 0:
            self.y = 0
        elif self.y > self.height:
            self.y = self.height

class App:
    def __init__(self):
        self._running = True
        self._game_display = None
        self._game_title = None
        self.clock = None
        self.size = self.width, self.height = 640, 400

    def on_init(self):
        pygame.init()
        self._game_display = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._game_display.fill(WHITE)
        self._game_title = pygame.display.set_caption('Python Game (Name subject to change)')
        self.clock = pygame.time.Clock()
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        self.clock.tick(60)

    def on_render(self):
        pygame.draw.circle(self._game_display, Creep.color, [Creep.x, Creep.y], Creep.size)
        pygame.display.update()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while self._running:
            black_creep = Creep(BLACK)
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


class Player:
    def __init__(self):
        self.x = None
        self.y = None
        self.move_x = None
        self.move_y = None

    def controls(self):

        self.x += self.move_x
        self.y += self.move_y

        # Checks if player character reaches the left border
        if self.x < 0:
            self.x = 0
        # Checks if player character reaches right border
        elif self.x > self.width:
            self.x = self.width
        # Checks if player character reaches top border
        if self.y < 0:
            self.y = 0
        # Checks if player character reaches bottom border
        elif self.y > self.height:
            self.y = self.height




if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
