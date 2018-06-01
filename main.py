import pygame
import time

pygame.init()

title_font = pygame.font.SysFont('Arial', 48)
my_font = pygame.font.SysFont('Consolas', 24)
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

# GRAPHICS
main_character = pygame.image.load('main character.png')
customer1 = pygame.image.load('patrons-3.png')
customer1 = pygame.transform.scale(customer1, (200, 200))
pudding = pygame.image.load('food copy 3.png')

# COLOR PALATE
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('A NEET Cafe')
clock = pygame.time.Clock()

game_running = True
scene = 'main_menu'


def text_objects(text, font):
    text_surface = font.render(text, True, BLACK)
    return text_surface, text_surface.get_rect()


def message_display(text):
    large_text = pygame.font.Font('freesansbold.ttf', 115)
    text_surf, text_rect = text_objects(text, large_text)
    text_rect.center = ((DISPLAY_WIDTH / 2), (DISPLAY_HEIGHT / 2))
    game_display.blit(text_surf, text_rect)
    time.sleep(2)
    pygame.display.update()
    game_loop()


def get_mouse_coordinates():
    for event in pygame.event.get():
        if pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            print(mouse_x, mouse_y)


class PlayerCharacter:
    def __init__(self):
        self.img = main_character

    def load_sprite(self):
        game_display.blit(self.img, (400, 300))


def customer():
    game_display.blit(customer1, (50, 0))


def game_loop():
    global scene
    key_refresh = False
    countdown = 60
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    while game_running:
        # Event Logic Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if scene == 'main_menu':
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not key_refresh:
                    # Checks mouse x and y coodinates
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    # Condition, if the cursor is within the button when clicked
                    if 300 < mouse_x < 500 and 300 < mouse_y < 380:
                        # Enters the Game
                        scene = 'in_game'
                        key_refresh = True

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and scene == 'game_over' and not key_refresh:
                scene = 'main_menu'
                key_refresh = True

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                key_refresh = False

            if event.type == pygame.USEREVENT and scene == 'in_game':
                countdown -= 1
                if countdown == 0:
                    scene = 'game_over'

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and scene == 'in_game' and not key_refresh:
                scene = 'pause_menu'
                key_refresh = True

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and scene == 'pause_menu' and not key_refresh:
                scene = 'in_game'
                key_refresh = True

        # Scene Logic Loop
        if scene == 'main_menu':
            game_display.fill(WHITE)
            game_title = title_font.render('A NEET Cafe', 1, BLACK)
            game_display.blit(game_title, (255, 200))

            # Start Button
            pygame.draw.rect(game_display, BLACK, pygame.Rect(300, 300, 200, 80))
            start_button = title_font.render('START', 1, WHITE)
            game_display.blit(start_button, (320, 300))


        elif scene == 'in_game':
            game_display.fill(WHITE)
            pygame.draw.rect(game_display, BLUE, pygame.Rect(0, 200, DISPLAY_WIDTH, 100))
            player = PlayerCharacter()
            player.load_sprite()
            customer()
            pygame.draw.rect(game_display, BLUE, pygame.Rect(0, 500, DISPLAY_WIDTH, 100))
            pygame.draw.rect(game_display, BLUE, pygame.Rect(700, 0, 100, 50))
            timer = my_font.render('Timer: ' + str(countdown), True, BLACK)
            game_display.blit(pudding, (0, 500))
            game_display.blit(timer, (DISPLAY_WIDTH - 85, 15))

        elif scene == 'pause_menu':
            pause = title_font.render('PAUSED', 1, BLACK)
            game_display.blit(pause, (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2))

        elif scene == 'game_over':
            game_display.fill(BLACK)
            game_over_title = my_font.render('GAME OVER', 1, WHITE)
            game_over_title2 = title_font.render('GAME OVER', 1, WHITE)
            game_display.blit(game_over_title, (255, 200))
            game_display.blit(game_over_title2, (255, 400))

        pygame.display.update()
        clock.tick(50)


game_loop()
pygame.quit()
quit()
