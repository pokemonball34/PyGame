import pygame
import time

pygame.init()
pygame.mixer.init()
# set font for title and regular text
title_font = pygame.font.SysFont('Arial', 48)
my_font = pygame.font.SysFont('Consolas', 24)
# set display size (800*600)
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

# GRAPHICS
main_character = pygame.image.load('main character.png')
title_screen = pygame.image.load('title screen.png')
house_scene = pygame.image.load('home.png')
game_over_screen = pygame.image.load('cg-you failed.png')
# load and scale customer to fit the diplay rather than using it purely at its original size
blond_female_customer = pygame.image.load('patrons-3.png')
blond_female_customer = pygame.transform.scale(blond_female_customer, (200, 200))
pudding = pygame.image.load('food copy 3.png')

# COLOR PALATE
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# ♫ Music and Sound Fx ♫

# Seats; 0 means empty, 1 means taken
seated_customer = [0, 0, 0, 0]

# Food Table
food_list = ('Pudding', 'Spaghetti', 'Hamburger')
customer_list = (blond_female_customer, )

# creating the game string; when game is opened, it creates the window to start game
game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
# caption on the window says 'A NEET Cafe'
pygame.display.set_caption('A NEET Cafe')
# set clock variable as Clock object
clock = pygame.time.Clock()

#set game running with Boolean variable true and the scene as a string
game_running = True
scene = 'in_game'


# This is the player character with the properties of a sprite
class PlayerCharacter(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = main_character
        self.position = None
        self.x = 400
        self.y = 300
        self.item_held = 'Nothing'

 # what main character can do (what it cannot is undefined)
    def load_sprite(self):
        game_display.blit(self.image, (self.x, self.y))

    def get_item(self, food_item):
        self.item_held = food_item

        
# sets up object serving table, which food can be added to 
class ServingTable:
    def __init__(self):
        self.serving_list = []

    def add_item(self, food):
        self.serving_list.append(food)

    def remove_item(self, food_name):
        self.serving_list.remove(food_name)


# sets up object that creates customers
class Customer(pygame.sprite.Sprite):

    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.img = image
        self.in_restaurant = True
        self.seat_position = -1
        self.food_order = food_list[0]

    def decide_seat(self):
        self.seat_position = 1

    def decide_food_item(self):
        pass

    def leave_seat(self):
        seated_customer[self.seat_position] = 0

    def load_sprite(self):
        game_display.blit(self.img, (0, 50))

    def leave_restaurant(self):
        self.in_restaurant = False


        # sets up game fuctions for mouse co-ordinates on screen
def get_mouse_coordinates():
    for event in pygame.event.get():
        if pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            print(mouse_x, mouse_y)


# Define main game loop
def game_loop():
    global scene
    key_refresh = False
    mouse_refresh = False
    # creates timer; 120 seconds for each level
    countdown = 120
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    player = PlayerCharacter()
    # Define the object 'customer01' as a variable
    customer01 = Customer(customer_list[0])
    customer01.decide_seat()
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
                    mouse_x, mouse_y = pygame.mouse.get_pos()                                                           # Checks mouse x and y coodinates
                    if 300 < mouse_x < 500 and 400 < mouse_y < 480:                                                     # Condition, if the cursor is within the button when clicked
                        scene = 'intro_scene'                                                                           # Enters the Game
                        mouse_refresh = True

            if scene == 'intro_scene':
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not mouse_refresh:
                    scene = 'in_game'

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

            # introduction scene
        elif scene == 'intro_scene':
            game_display.blit(house_scene, (0, 0))

            # game
        elif scene == 'in_game':
            game_display.fill(WHITE)
            pygame.draw.rect(game_display, BLUE, pygame.Rect(0, DISPLAY_HEIGHT * 0.4, DISPLAY_WIDTH, DISPLAY_HEIGHT / 8))
            player.load_sprite()
            pygame.draw.rect(game_display, BLUE, pygame.Rect(0, 500, DISPLAY_WIDTH, DISPLAY_HEIGHT / 6))
            pygame.draw.rect(game_display, BLUE, pygame.Rect(DISPLAY_WIDTH * 0.8, 0, DISPLAY_WIDTH * 0.2, DISPLAY_HEIGHT / 12))
            pygame.draw.rect(game_display, BLACK, pygame.Rect(500, 500, 100, 100))
            timer = my_font.render('Timer: ' + str(countdown), True, BLACK)
            game_display.blit(pudding, (0, 500))
            game_display.blit(timer, (DISPLAY_WIDTH * 0.8 + 10, 15))
            customer01.load_sprite()

            # Player Controls
            keys = pygame.key.get_pressed()
            if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and pygame.KEYDOWN and player.x > 0:
                player.x -= 10

            elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and pygame.KEYDOWN and player.x < DISPLAY_WIDTH:
                player.x += 10

            elif keys[pygame.K_SPACE] and pygame.KEYDOWN and not key_refresh and player.item_held == "Nothing":
                player.get_item()
                key_refresh = True
                print(player.item_held)

            elif keys[pygame.K_SPACE] and pygame.KEYDOWN and not key_refresh and player.item_held != "Nothing":
                player.item_held = "Nothing"
                key_refresh = True
                print(player.item_held)

            if keys[pygame.K_SPACE] and pygame.KEYUP and key_refresh:
                key_refresh = False

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
