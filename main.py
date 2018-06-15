import pygame
import random
import sprites

# Initialization of Pygame
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
# set font for title and regular text
title_font = pygame.font.SysFont('Arial', 48)
my_font = pygame.font.SysFont('Consolas', 24)

# Set display size (800 by 600)
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

# COLOR PALATE
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# ♫ Music and Sound Fx ♫
roundabout = 'music/jojo.mp3'
casual_music = 'music/mii plaza.mp3'
baccano = 'music/baccano.mp3'
plates_clacking = pygame.mixer.Sound('music/plate sound.wav')

# Creating the game screen parameters
game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

# Caption on the window bar says: A NEET Cafe
pygame.display.set_caption('A NEET Cafe')

# Set clock variable as Clock object
clock = pygame.time.Clock()

# Set game running with Boolean variable true
game_running = True

# Set total_score to 0
total_score = 0

# Set score to 0
score = 0

# Set day to 1
day = 1

# Sets up serving_table as a list, which food can be added to
serving_table = [sprites.hamburger, sprites.rice_bowl]


# This is the player character with the properties of a sprite
class PlayerCharacter:
    # Initialize variables onto the object
    def __init__(self):
        self.image = sprites.main_character
        self.position = None
        self.x = 400
        self.y = 300
        self.item_held = 'Nothing'

    # Loads sprite onto screen
    def load_sprite(self):
        game_display.blit(self.image, (self.x, self.y))
        # Checks if player is holding anything. If so, display the item
        if self.item_held != 'Nothing':
            game_display.blit(self.item_held, (self.x, self.y + 90))

    # Allows the player to collect food from the serving table
    def get_item(self, food_item):
        self.item_held = food_item


# The Customer objects that creates a Customer that can order, show itself on screen and delete itself
class Customer(object):
    # Initialize parameters and traits of a Customer
    def __init__(self):
        self.img = None
        self.seat_number = 0
        self.pause = -1
        self.in_restaurant = False
        self.food_order = None
        self.order_taken = False
        self.patience = -1

    # Sets a delay between a new customer
    def set_delay(self):
        self.pause = 5

    # Lets the customer enter the restaurant
    def enter_restaurant(self):
        # Checks if it can enter the restaurant
        if self.pause == 0:
            self.in_restaurant = True
            self.patience = 10
            self.order_taken = False
            self.decide_food_item()
            self.load_sprite()
            self.pause = -1

    # Lets the customer leave the restaurant
    def leave_restaurant(self):
        self.in_restaurant = False
        self.food_order = None
        self.set_delay()

    # From a set of food dependant on day, the customer randomly picks one to order
    def decide_food_item(self):
        global day
        if day == 1:
            self.food_order = random.choice([sprites.pudding, sprites.hamburger])
        elif day == 2:
            self.food_order = random.choice([sprites.pudding, sprites.hamburger, sprites.spaghetti])
        else:
            self.food_order = random.choice(sprites.food_list)

    # Gives the customer a random sprite from a list of sprites
    def load_sprite(self):
        self.img = random.choice(sprites.customer_list)

    # Updates the customer on the screen
    def update(self):
        # Checks if the customer is still in restaurant
        if self.in_restaurant:
            # Displays the customer on screen
            game_display.blit(self.img, (200 * self.seat_number, 50))
            # Patience Bar, it shrinks dependant on how much patience the customer has in seconds
            pygame.draw.rect(game_display, RED, pygame.Rect(190 * self.seat_number, DISPLAY_HEIGHT * 0.4
                                                            - self.patience * 10, 20, self.patience * 10))
            # Checks if the customer's order is taken
            if self.order_taken:
                # Displays a thought bubble of what the customer desires
                game_display.blit(sprites.cloud, (200 * self.seat_number, DISPLAY_HEIGHT * 0.3))
                game_display.blit(self.food_order, (200 * self.seat_number, DISPLAY_HEIGHT * 0.35))

            # Checks if the customer's patience ran out
            if self.patience == 0:
                self.leave_restaurant()


# Main game loop as a function
def game_loop():
    # Refers back to the global score, day and total_score
    global score
    global day
    global total_score
    # Sets a variable screen to decide what to display to the user
    scene = 'main_menu'
    # A boolean variable to check if the key is lifted
    key_refresh = False
    # A boolean variable to check if the mouse click is lifted
    mouse_refresh = False
    # A boolean to check if the game has been set up yet
    game_setup = False
    # Creates Timer; 60 seconds for each level
    countdown = 60
    # Sets the timer to tick every second
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    # Defines the player from the PlayerCharacter object
    player = PlayerCharacter()
    # Plays music
    pygame.mixer.music.load(casual_music)
    pygame.mixer.music.play(-1)

    # Defines the customers from the Customer object and initializes them
    customer01 = Customer()
    customer01.load_sprite()
    customer01.seat_number = 0
    customer02 = Customer()
    customer02.seat_number = 1
    customer03 = Customer()
    customer03.seat_number = 2
    customer04 = Customer()
    customer04.seat_number = 3

    # Main Game Loop
    while game_running:
        # Event Logic Loop
        for event in pygame.event.get():
            # Checks if the player is exiting the game
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Checks if the player lifted the left mouse button
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_refresh = False

            # Checks the input from the scene main_menu
            if scene == 'main_menu':
                # Checks if the left mouse button is clicked
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not mouse_refresh:
                    # Checks mouse x and y coordinates
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    # Condition, if the cursor is within the button when clicked
                    if 300 < mouse_x < 500 and 400 < mouse_y < 480:
                        # Enters the instruction screen
                        scene = 'instructions'
                        # Prevents accidental inputs that use the same key on another scene
                        mouse_refresh = True

            elif scene == 'instructions':
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not mouse_refresh:
                    scene = 'intro_scene'
                    mouse_refresh = True

            # Checks if the scene is the intro scene
            if scene == 'intro_scene':
                # Checks if it is a left click to transition to the next scene.
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not mouse_refresh:
                    scene = 'in_game'
                    # Stops the music
                    pygame.mixer.music.stop()

            # Game over Screen
            if scene == 'game_over':
                # Checks for a left mouse click, returns the player to the main menu
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not mouse_refresh:
                    scene = 'main_menu'
                    mouse_refresh = True

            # Checks if the screen is in the game play screen
            if scene == 'in_game':
                # Keeps track of time by 1 second
                if event.type == pygame.USEREVENT:
                    # Reduces timer by 1 second
                    countdown -= 1

                    # Checks the customer's patience and wait time
                    if customer01.pause >= 0:
                        customer01.pause -= 1
                    if customer01.patience > 0:
                        customer01.patience -= 1

                    if customer02.pause >= 0:
                        customer02.pause -= 1
                    if customer02.patience > 0:
                        customer02.patience -= 1

                    if customer03.pause >= 0:
                        customer03.pause -= 1
                    if customer03.patience == 0:
                        customer03.patience -= 1

                    if customer04.pause >= 0:
                        customer04.pause -= 1
                    if customer04.patience > 0:
                        customer04.patience -= 1
                    if customer04.patience == 0:
                        customer04.patience -= 1

                    # Checks if the timer ran out
                    if countdown == 0:
                        # Checks what day it is, if they manage to pass the require score, they move onto the next day
                        if day == 1 and score >= 1000:
                                day = 2
                                total_score += score
                                score = 0
                                scene = 'end_day_1'
                                game_setup = False
                        elif day == 2 and score >= 1200:
                                day = 3
                                total_score += score
                                score = 0
                                scene = 'end_day_2'
                                game_setup = False
                        elif day == 3 and score >= 1500:
                                day = 4
                                total_score += score
                                score = 0
                                scene = 'end_day_3'
                                game_setup = False
                        elif day == 4 and score >= 2000:
                                day = 1
                                total_score += score
                                score = 0
                                scene = 'end_day_4'
                                game_setup = False
                        # If they fail to reach the required score, they lose.
                        elif day == 3 or day == 4:
                            scene = 'game_over-2'
                            total_score += score
                        else:
                            scene = 'game_over'
                            total_score += score                        pygame.mixer.music.stop()

            # Checks if the scene is in the pause menu
            if scene == 'pause_menu':
                # Checks if the player pressed the escape button
                if event.type == pygame.KEYDOWN and event == pygame.K_ESCAPE and not key_refresh:
                    scene = 'in_game'
                    key_refresh = True

            # Looks to see if the player made a mouse or key input
            if scene == 'end_day_1' or scene == 'end_day_2' or scene == 'end_day_3':
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not mouse_refresh:
                    scene = 'in_game'
                    countdown = 60
                    mouse_refresh = True
                elif event.type == pygame.KEYDOWN and not key_refresh:
                    scene = 'in_game'
                    countdown = 60
                    key_refresh = True

            # Looks to see if the user made a key input
            if scene == 'end_day_4':
                if event.type == pygame.KEYDOWN and not key_refresh:
                    scene = 'main_menu'
                    mouse_refresh = True

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
            game_display.fill(WHITE)

            # To prevent negative score
            if score < 0:
                score = 0

            # Diner's Table
            pygame.draw.rect(game_display,
                             BLUE, pygame.Rect(0, DISPLAY_HEIGHT * 0.4, DISPLAY_WIDTH, DISPLAY_HEIGHT / 8))

            # Loads the player's sprite
            player.load_sprite()

            # Serving Table
            pygame.draw.rect(game_display, BLUE, pygame.Rect(0, 500, DISPLAY_WIDTH, DISPLAY_HEIGHT / 6))

            # Timer Box
            pygame.draw.rect(game_display, BLUE,
                             pygame.Rect(DISPLAY_WIDTH * 0.8, 0, DISPLAY_HEIGHT * 0.4, DISPLAY_HEIGHT / 12))

            # Score Box
            pygame.draw.rect(game_display, BLUE,
                             pygame.Rect(0, 0, DISPLAY_HEIGHT * 0.4, DISPLAY_HEIGHT / 12))
            pygame.draw.rect(game_display, BLACK, pygame.Rect(500, 510, 80, 80))
            timer = my_font.render('Score: ' + str(score), True, BLACK)
            for food in range(0, len(serving_table)):
                game_display.blit(serving_table[food], (110 * food, 500))
            game_display.blit(timer, (DISPLAY_WIDTH * 0.8 + 10, 15))

            # Player Controls
            keys = pygame.key.get_pressed()
            if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and pygame.KEYDOWN and player.x > 0:
                player.x -= 10

            elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and pygame.KEYDOWN and player.x < DISPLAY_WIDTH:
                player.x += 10

            if keys[pygame.K_UP] and pygame.KEYDOWN and not key_refresh:
                # Customer1 food ordered logic
                if 0 <= player.x <= 200 and not customer01.order_taken:
                    if customer01.food_order == sprites.pudding:
                        serving_table.append(sprites.pudding)
                    elif customer01.food_order == sprites.spaghetti:
                        serving_table.append(sprites.spaghetti)
                    elif customer01.food_order == sprites.rice_bowl:
                        serving_table.append(sprites.rice_bowl)
                    elif customer01.food_order == sprites.hamburger:
                        serving_table.append(sprites.hamburger)
                    customer01.order_taken = True
                    customer01.patience += 3
                    key_refresh = True
                elif player.item_held == customer01.food_order and 0 <= player.x <= 200 and customer01.order_taken:
                    customer01.leave_restaurant()
                    customer01.set_delay()
                    player.item_held = 'Nothing'
                    score += (customer01.patience * 100) + 500
                    key_refresh = True
                    plates_clacking.play()

                # Customer2 Food Ordered Logic
                if 200 <= player.x <= 400 and not customer02.order_taken:
                    if customer02.food_order == sprites.pudding:
                        serving_table.append(sprites.pudding)
                    elif customer02.food_order == sprites.spaghetti:
                        serving_table.append(sprites.spaghetti)
                    elif customer02.food_order == sprites.rice_bowl:
                        serving_table.append(sprites.rice_bowl)
                    elif customer02.food_order == sprites.hamburger:
                        serving_table.append(sprites.hamburger)
                    customer02.order_taken = True
                    customer02.patience += 3
                    key_refresh = True
                elif player.item_held == customer02.food_order and 200 <= player.x <= 400 and customer02.order_taken:
                    customer02.leave_restaurant()
                    customer02.set_delay()
                    player.item_held = 'Nothing'
                    score += (customer02.patience * 100) + 500
                    key_refresh = True
                    plates_clacking.play()

                    # Customer3 Food Order Logic
                    if 400 <= player.x <= 600 and not customer03.order_taken:
                        if customer03.food_order == sprites.pudding:
                            serving_table.append(sprites.pudding)
                        elif customer03.food_order == sprites.spaghetti:
                            serving_table.append(sprites.spaghetti)
                        elif customer03.food_order == sprites.rice_bowl:
                            serving_table.append(sprites.rice_bowl)
                        elif customer03.food_order == sprites.hamburger:
                            serving_table.append(sprites.hamburger)
                        customer03.order_taken = True
                        customer03.patience += 3
                        key_refresh = True
                    elif player.item_held == customer03.food_order and 400 <= player.x <= 600 and customer03.order_taken:
                        customer03.leave_restaurant()
                        customer03.set_delay()
                        player.item_held = 'Nothing'
                        score += (customer03.patience * 100) + 500
                        key_refresh = True
                        plates_clacking.play()

                    # Customer4 Food Ordered Logic
                    if 620 <= player.x <= 800 and not customer04.order_taken:
                        if customer04.food_order == sprites.pudding:
                            serving_table.append(sprites.pudding)
                        elif customer04.food_order == sprites.spaghetti:
                            serving_table.append(sprites.spaghetti)
                        elif customer04.food_order == sprites.rice_bowl:
                            serving_table.append(sprites.rice_bowl)
                        elif customer04.food_order == sprites.hamburger:
                            serving_table.append(sprites.hamburger)
                        customer04.order_taken = True
                        customer04.patience += 3
                        key_refresh = True
                    elif player.item_held == customer04.food_order and 200 <= player.x <= 400 and customer04.order_taken:
                        customer04.leave_restaurant()
                        customer04.set_delay()
                        player.item_held = 'Nothing'
                        score += (customer04.patience * 100) + 500
                        key_refresh = True
                        plates_clacking.play()

            # Checks if the player can grab food, if so, it removes it depending on the location of food
            elif keys[pygame.K_DOWN] and pygame.KEYDOWN and not key_refresh and player.item_held == 'Nothing':
                if 0 <= player.x < 100 and len(serving_table) > 0:
                    player.item_held = serving_table[0]
                    serving_table.remove(serving_table[0])
                    key_refresh = True
                elif 100 < player.x < 200 and len(serving_table) > 1:
                    player.item_held = serving_table[1]
                    serving_table.remove(serving_table[1])
                    key_refresh = True
                elif 200 < player.x < 300 and len(serving_table) > 2:
                    player.item_held = serving_table[2]
                    serving_table.remove(serving_table[2])
                    key_refresh = True
                elif 300 <= player.x < 400 and len(serving_table) > 3:
                    player.item_held = serving_table[3]
                    serving_table.remove(serving_table[3])
                    key_refresh = True

            # Checks if the player is near the trash bin
            elif keys[pygame.K_DOWN] and pygame.KEYDOWN and not key_refresh and 470 <= player.x < 550 and \
                    player.item_held != 'Nothing':
                if customer01.food_order == player.item_held:
                    customer01.order_taken = False
                elif customer02.food_order == player.item_held:
                    customer02.order_taken = False
                elif customer03.food_order == player.item_held:
                    customer03.order_taken = False
                elif customer04.food_order == player.item_held:
                    customer04.order_taken = False
                player.item_held = 'Nothing'
                score -= 200
                key_refresh = True

            # Checks if player paused
            elif keys[pygame.K_ESCAPE] and pygame.KEYDOWN and not key_refresh:
                scene = 'pause_menu'

            # Checks for a key refresh
            if pygame.KEYUP and key_refresh:
                key_refresh = False

            # Game Starts off with a set number of customers dependant on day
            if day == 0:
                # Updates the customer sprite
                customer01.enter_restaurant()
                customer01.update()
            elif day == 1:
                if not game_setup:
                    customer01.pause = 5
                    customer02.pause = 10
                    pygame.mixer.music.load(baccano)
                    pygame.mixer.music.play(-1)
                game_setup = True
                customer01.update()
                customer01.enter_restaurant()
                customer02.update()
                customer02.enter_restaurant()
            elif day == 2:
                if not game_setup:
                    customer01.pause = 3
                    customer02.pause = 5
                    pygame.mixer.music.load(baccano)
                    pygame.mixer.music.play(-1)
                game_setup = True
                customer01.update()
                customer01.enter_restaurant()
                customer02.update()
                customer02.enter_restaurant()
                customer03.update()
                customer03.enter_restaurant()
            elif day == 3:
                if not game_setup:
                    customer01.pause = 3
                    customer02.pause = 5
                    customer03.pause = 10
                    pygame.mixer.music.load(baccano)
                    pygame.mixer.music.play(-1)
                game_setup = True
                customer01.update()
                customer01.enter_restaurant()
                customer02.update()
                customer02.enter_restaurant()
                customer03.update()
                customer03.enter_restaurant()
            elif day == 4:
                if not game_setup:
                    customer01.pause = 3
                    customer02.pause = 4
                    customer03.pause = 8
                    customer04.pause = 12
                    pygame.mixer.music.load(baccano)
                    pygame.mixer.music.play(-1)
                game_setup = True
                customer01.update()
                customer01.enter_restaurant()
                customer02.update()
                customer02.enter_restaurant()
                customer03.update()
                customer03.enter_restaurant()
                customer04.update()
                customer04.enter_restaurant()

        elif scene == 'pause_menu':
            pause = title_font.render('PAUSED', 1, BLACK)
            game_display.blit(pause, (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2))

        elif scene == 'game_over':
            game_display.blit(sprites.game_over_screen, (0, 0))
            game_over_title = title_font.render('GAME OVER', 1, WHITE)
            game_display.blit(game_over_title, (255, 400))

        elif scene == 'game_over-2':
            game_display.blit(sprites.game_over2_screen, (0, 0))

        elif scene == 'end_day_1':
            game_display.blit(sprites.day1_complete, (0, 0))

        elif scene == 'end_day_2':
            game_display.blit(sprites.day2_complete, (0, 0))

        elif scene == 'end_day_3':
            game_display.blit(sprites.day3_complete, (0, 0))

        elif scene == 'end_day_4':
            game_display.fill(WHITE)
            game_display.blit(my_font.render('Thanks for Playing!', 1, BLACK), (50, 10))
            game_display.blit(my_font.render('Total Score: ' + str(total_score), 1, BLACK), (50, 110))

        elif scene == 'instructions':
            game_display.fill(WHITE)
            game_display.blit(my_font.render('Use the left/right or a/d keys to move', 1, BLACK), (50, 10))
            game_display.blit(my_font.render('Use the up key to grab a customer\'s order or serve them', 1, BLACK),
                              (50, 60))
            game_display.blit(my_font.render('Use the down key to grab food off the table or dump food', 1, BLACK),
                              (50, 110))
            game_display.blit(my_font.render('in the black square on the bottom right corner', 1, BLACK),
                              (50, 160))
            game_display.blit(my_font.render('Press escape to pause. Have fun!', 1, BLACK), (50, 210))

        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
