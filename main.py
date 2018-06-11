import pygame
import time

pygame.init()

# set font for title and regular text
title_font = pygame.font.SysFont('Arial', 48)
my_font = pygame.font.SysFont('Consolas', 24)
# set display size (800*600)
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

# GRAPHICS
main_character = pygame.image.load('main character.png')
title_screen = pygame.image.load('title screen.png')
game_over_screen = pygame.image.load('cg-you failed.png')
# load and scale customer to fit the diplay rather than using it purely at its original size
customer1 = pygame.image.load('patrons-3.png')
customer1 = pygame.transform.scale(customer1, (200, 200))
pudding = pygame.image.load('food copy 3.png')

# COLOR PALATE
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# ♫ Music and Sound Fx ♫

# Seats; 0 means empty, 1 means taken
seated_customer = [0, 0, 0, 0]

game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('A NEET Cafe')
clock = pygame.time.Clock()

game_running = True
scene = 'main_menu'


class PlayerCharacter(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = main_character
        self.position = None
        self.x = 400
        self.y = 300

    def load_sprite(self):
        game_display.blit(self.image, (self.x, self.y))


class ServingTable:
    def __init__(self):
        self.serving_list = []

    def add_item(self, food):
        self.serving_list.append(food)

    def remove_item(self, food_name):
        self.serving_list.remove(food_name)


class Customer(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.img = image
        self.in_restaurant = True
        self.seat_position = -1

    def decide_seat(self):
        for seat in range(0, 4):
            if seated_customer[seat] == 0 and self.seat_position != -1:
                seated_customer[seat] = 1
                self.seat_position = seat

    def leave_seat(self):
        seated_customer[self.seat_position] = 0

    def load_sprite(self):
        game_display.blit(self.img, (0, 50))

    def leave_restaurant(self):
        self.in_restaurant = False


def get_mouse_coordinates():
    for event in pygame.event.get():
        if pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            print(mouse_x, mouse_y)


def game_loop():
    global scene
    key_refresh = False
    mouse_refresh = False
    current_pressed_key = None
    countdown = 10
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    player = PlayerCharacter()
    customer01 = Customer(customer1)
    while game_running:
        # Event Logic Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if scene == 'main_menu':
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not mouse_refresh:
                    mouse_x, mouse_y = pygame.mouse.get_pos()                                                           # Checks mouse x and y coodinates
                    if 300 < mouse_x < 500 and 400 < mouse_y < 480:                                                     # Condition, if the cursor is within the button when clicked
                        scene = 'in_game'                                                                               # Enters the Game
                        mouse_refresh = True

            if scene == 'game_over':
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not mouse_refresh:
                    scene = 'main_menu'
                    mouse_refresh = True

            if scene == 'in_game':
                if event.type == pygame.USEREVENT:
                    countdown -= 1
                    if countdown == 0:
                        scene = 'game_over'
                        countdown = 60
            if scene == 'pause_menu':
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not mouse_refresh:
                    scene = 'in_game'
                    mouse_refresh = True
                elif event.type == pygame.K_p and not key_refresh:
                    scene = 'in_game'
                    key_refresh = True

        # Scene Logic Loop
        if scene == 'main_menu':
            game_display.blit(title_screen, (0, 0))

            # Start Button
            pygame.draw.rect(game_display, BLACK, pygame.Rect(300, 400, 200, 80))
            start_button = title_font.render('START', 1, WHITE)
            game_display.blit(start_button, (340, 425))

        elif scene == 'in_game':
            game_display.fill(WHITE)
            pygame.draw.rect(game_display, BLUE, pygame.Rect(0, DISPLAY_HEIGHT * 0.4, DISPLAY_WIDTH, DISPLAY_HEIGHT / 8))
            player.load_sprite()
            customer01.decide_seat()
            customer01.load_sprite()
            pygame.draw.rect(game_display, BLUE, pygame.Rect(0, 500, DISPLAY_WIDTH, DISPLAY_HEIGHT / 6))
            pygame.draw.rect(game_display, BLUE, pygame.Rect(DISPLAY_WIDTH * 0.8, 0, DISPLAY_WIDTH * 0.2, DISPLAY_HEIGHT / 12))
            timer = my_font.render('Timer: ' + str(countdown), True, BLACK)
            game_display.blit(pudding, (0, 500))
            game_display.blit(timer, (DISPLAY_WIDTH * 0.8 + 10, 15))

            # Player Controls
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and pygame.KEYDOWN:
                player.x -= 10

            elif keys[pygame.K_RIGHT] and pygame.KEYDOWN:
                player.x += 10


        elif scene == 'pause_menu':
            pause = title_font.render('PAUSED', 1, BLACK)
            game_display.blit(pause, (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2))

        elif scene == 'game_over':
            game_display.blit(game_over_screen, (0, 0))
            game_over_title = title_font.render('GAME OVER', 1, WHITE)
            game_display.blit(game_over_title, (255, 400))

        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
