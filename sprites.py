import pygame

# Load the graphics into the program
# Character Sprites
main_character = pygame.image.load('pictures/main character.png')
grandparents = pygame.image.load('pictures/grandparents.png')
mohawk_customer = pygame.image.load('pictures/patrons.png')
blond_female_customer = pygame.image.load('pictures/patrons-3.png')
orange_hair_customer = pygame.image.load('pictures/patrons-4.png')
glasses_customer = pygame.image.load('pictures/patrons-5.png')
sunglasses_customer = pygame.image.load('pictures/patrons-6.png')
blond_male_customer = pygame.image.load('pictures/patrons-7.png')
baseball_hat_customer = pygame.image.load('pictures/patrons-8.png')
old_man_customer = pygame.image.load('pictures/patrons-9.png')

# Food Sprites
pudding = pygame.image.load('pictures/pudding.png')
hamburger = pygame.image.load('pictures/hamburger.png')
spaghetti = pygame.image.load('pictures/spaghetti.png')
rice_bowl = pygame.image.load('pictures/rice bowl.png')

# Screens
title_screen = pygame.image.load('pictures/title screen.png')
house_screen = pygame.image.load('pictures/home with text.png')
game_over_screen = pygame.image.load('pictures/cg-you failed.png')

# Other Sprites
cloud = pygame.image.load('pictures/cloud.png')
cook_scene_1 = pygame.image.load('pictures/1.png')
cook_scene_2 = pygame.image.load('pictures/2.png')
cook_scene_3 = pygame.image.load('pictures/3.png')
cook_scene_4 = pygame.image.load('pictures/4.png')

# Scales the sprites to fit the display rather than using it purely at its original size
mohawk_customer = pygame.transform.scale(mohawk_customer, (200, 200))
blond_female_customer = pygame.transform.scale(blond_female_customer, (200, 200))
orange_hair_customer = pygame.transform.scale(orange_hair_customer, (200, 200))
glasses_customer = pygame.transform.scale(glasses_customer, (200, 200))
sunglasses_customer = pygame.transform.scale(sunglasses_customer, (200, 200))
blond_male_customer = pygame.transform.scale(blond_male_customer, (200, 200))
baseball_hat_customer = pygame.transform.scale(baseball_hat_customer, (200, 200))
old_man_customer = pygame.transform.scale(old_man_customer, (200, 200))

# Sprite List
food_list = ('Pudding', 'Spaghetti', 'Hamburger', 'Rice Bowl')
customer_list = (mohawk_customer, blond_female_customer, orange_hair_customer, glasses_customer, sunglasses_customer,
                 blond_male_customer, baseball_hat_customer, old_man_customer)


