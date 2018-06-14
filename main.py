import pygame
import random
import time
import sprites

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
# set font for title and regular text
title_font = pygame.font.SysFont('Arial', 48)
my_font = pygame.font.SysFont('Consolas', 24)
# set display size (800*600)
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

# COLOR PALATE
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# ♫ Music and Sound Fx ♫
roundabout = pygame.mixer.music.load('music/jojo.mp3')
casual_music = pygame.mixer.music.load('music/mii plaza.mp3')
baccano = pygame.mixer.music.load('music/baccano.mp3')

# Checks current time
current_time = time.time()

# creating the game string; when game is opened, it creates the window to start game
game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
# caption on the window says 'A NEET Cafe'
pygame.display.set_caption('A NEET Cafe')
# set clock variable as Clock object
clock = pygame.time.Clock()

# set game running with Boolean variable true
game_running = True
day = 0
# sets up object serving table, which food can be added to
serving_table = []
cooking_queue = []

# This is the player character with the properties of a sprite
class PlayerCharacter(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprites.main_character
        self.position = None
        self.x = 400
        self.y = 300
        self.item_held = 'Pudding'
        self.order_queue = []

    # what main character can do (what it cannot is undefined)
    def load_sprite(self):
        game_display.blit(self.image, (self.x, self.y))

    def get_item(self, food_item):
        self.item_held = food_item


class Customer(object):
    def __init__(self):
        self.img = None
        self.seat_number = 0
        self.pause = 0
        self.in_restaurant = False
        self.food_order = None
        self.order_taken = False

    def set_delay(self):
        self.pause = 5

    def enter_restaurant(self):
        if self.pause == 0:
            self.in_restaurant = True

    def decide_food_item(self):
        global day
        if day == 0:
            self.food_order = sprites.pudding
        elif day == 1:
            self.food_order = random.choice([sprites.pudding, sprites.hamburger])
        elif day == 2:
            self.food_order = random.choice([sprites.pudding, sprites.hamburger, sprites.spaghetti])
        else:
            self.food_order = random.choice(sprites.food_list)

    def take_order(self):
        global serving_table
        self.order_taken = True

    def load_sprite(self):
        self.img = random.choice(sprites.customer_list)

    def update(self):
        if self.in_restaurant:
            game_display.blit(self.img, (0, 50))
        if self.order_taken:
            game_display.blit(sprites.cloud, (DISPLAY_WIDTH * 0.4 + 10, DISPLAY_HEIGHT * 0.25 * self.seat_number))

    def leave_restaurant(self):
        self.in_restaurant = False


# Obtains the mouse coordinates of where the player clicks
def get_mouse_coordinates():
    for event in pygame.event.get():
        if pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            print(mouse_x, mouse_y)


# Define main game loop
def game_loop():
    scene = 'in_game'
    key_refresh = False
    mouse_refresh = False
    pygame.mixer.music.play(-1)
    # creates timer; 120 seconds for each level
    countdown = 120
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    player = PlayerCharacter()
    customer01 = Customer()
    customer01.load_sprite()
    customer01.seat_number = 0
    customer02 = Customer()
    customer02.seat_number = 1
    customer03 = Customer()
    customer03.seat_number = 2
    customer04 = Customer()
    customer04.seat_number = 3
    while game_running:
        # Event Logic Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_refresh = False

            if scene == 'main_menu':
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not mouse_refresh:
                    mouse_x, mouse_y = pygame.mouse.get_pos()  # Checks mouse x and y coordinates
                    # Condition, if the cursor is within the button when clicked
                    if 300 < mouse_x < 500 and 400 < mouse_y < 480:
                        scene = 'intro_scene'  # Enters the Game
                        mouse_refresh = True

            if scene == 'intro_scene':
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not mouse_refresh:
                    scene = 'in_game'
                    pygame.mixer.music.stop()

            if scene == 'game_over':
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not mouse_refresh:
                    scene = 'main_menu'
                    mouse_refresh = True

            if scene == 'in_game':
                if event.type == pygame.USEREVENT:
                    countdown -= 1
                    if customer01.pause >= 0:
                        customer01.pause -= 1
                        customer01.enter_restaurant()
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
            game_display.blit(sprites.title_screen, (0, 0))
            # Start Button
            pygame.draw.rect(game_display, BLACK, pygame.Rect(300, 400, 200, 80))
            start_button = title_font.render('START', 1, WHITE)
            game_display.blit(start_button, (340, 425))

        # Introduction scene
        elif scene == 'intro_scene':
            game_display.blit(sprites.house_screen, (0, 0))

        # Main Game
        elif scene == 'in_game':
            pygame.mixer.music.play()
            game_display.fill(WHITE)
            pygame.draw.rect(game_display,
                             BLUE, pygame.Rect(0, DISPLAY_HEIGHT * 0.4, DISPLAY_WIDTH, DISPLAY_HEIGHT / 8))
            player.load_sprite()
            pygame.draw.rect(game_display, BLUE, pygame.Rect(0, 500, DISPLAY_WIDTH, DISPLAY_HEIGHT / 6))
            pygame.draw.rect(game_display, BLUE,
                             pygame.Rect(DISPLAY_WIDTH * 0.8, 0, DISPLAY_WIDTH * 0.2, DISPLAY_HEIGHT / 12))
            pygame.draw.rect(game_display, BLACK, pygame.Rect(500, 500, 100, 100))
            timer = my_font.render('Timer: ' + str(countdown), True, BLACK)
            for food in range(0, len(serving_table)):
                game_display.blit(serving_table[food], (110 * food, 500))
            game_display.blit(timer, (DISPLAY_WIDTH * 0.8 + 10, 15))

            # Updates the customer sprite
            customer01.enter_restaurant()
            customer01.update()

            # Player Controls
            keys = pygame.key.get_pressed()
            if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and pygame.KEYDOWN and player.x > 0:
                player.x -= 10

            elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and pygame.KEYDOWN and player.x < DISPLAY_WIDTH:
                player.x += 10

            if keys[pygame.K_SPACE] and pygame.KEYDOWN and not key_refresh and 0 <= player.x <= 200 and \
                    not customer01.order_taken:
                if customer01.food_order == sprites.pudding:
                    serving_table.append(sprites.pudding)
                elif customer01.food_order == sprites.spaghetti:
                    player.order_queue.append(sprites.spaghetti)
                elif customer01.food_order == sprites.rice_bowl:
                    player.order_queue.append(sprites.rice_bowl)
                elif customer01.food_order == sprites.hamburger:
                    player.order_queue.append(sprites.hamburger)

            elif keys[pygame.K_SPACE] and pygame.KEYDOWN and not key_refresh and player.item_held == \
                    customer01.food_order and 0 <= player.x <= 200 and customer01.order_taken:
                customer01.leave_restaurant()
                customer01.set_delay()
                player.item_held = "Nothing"
                key_refresh = True

            if pygame.KEYUP and key_refresh:
                key_refresh = False

        elif scene == 'pause_menu':
            pause = title_font.render('PAUSED', 1, BLACK)
            game_display.blit(pause, (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2))

        elif scene == 'game_over':
            game_display.blit(sprites.game_over_screen, (0, 0))
            game_over_title = title_font.render('GAME OVER', 1, WHITE)
            game_display.blit(game_over_title, (255, 400))

        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
