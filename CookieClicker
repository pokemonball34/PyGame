import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

# Sets colours (R, G, B) <- values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

block_color = (53, 115, 255)
bird_width = 135
# Sets display size (in a tuple)
gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('Cookie Clicker')
clock = pygame.time.Clock()

cookie_img = pygame.image.load('cookie.png')
cookie_img = pygame.transform.scale(cookie_img, (400, 400))

def times_clicked(click_count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Clicked: " + str(click_count), True, BLACK)
    gameDisplay.blit(text, (0, 0))

def cookie(x, y):
    gameDisplay.blit(cookie_img, (x, y))

def game():
    x = 200
    y = 150
    key_refresh = False
    running = True
    score = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # When event.button is 1, it is a left click.
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if key_refresh == False:
                    score += 1
                    key_refresh = True

            elif event.type == pygame.MOUSEBUTTONUP:
                key_refresh = False

        gameDisplay.fill(WHITE)
        cookie(x, y)
        times_clicked(score)
        pygame.display.update()
        clock.tick(50)


game()
pygame.quit()
quit()
