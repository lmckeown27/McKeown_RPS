# File created by: Liam McKeown

# import libraries

from time import sleep

from random import randint
# thorough game library
import pygame as pg
# library that allows one to get directory and manage folders
import os

# where to find files
game_folder = os.path.dirname(__file__)
print(game_folder)

# game settings; capitalized because their constant/cannot change
WIDTH = 360
HEIGHT = 480
FPS = 30

# define colors
# rgb values
# tuples cannot change
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# makes the gameover false
GAMEOVER = False

# initializes pygame
pg.init()
pg.mixer.init()

# opens up pygame and describes its location
screen = pg.display.set_mode((WIDTH, HEIGHT))
# when display is opened, sets text display
pg.display.set_caption("Rock, Paper, Scissors...")
# sets the FPS
clock = pg.time.Clock()

# loads in the image
rock_image = pg.image.load(os.path.join(game_folder, 'therock.jpg')).convert()
# storing the location/dimensions of pixels and allows user to access/change pixels
rock_image_rect = rock_image.get_rect()

# loads in the image
scissors_image = pg.image.load(os.path.join(
    game_folder, 'scissors.jpg')).convert()
# storing the location/dimensions of pixels and allows user to access/change pixels
scissors_image_rect = scissors_image.get_rect()
scissors_image_rect.y = 300
scissors_image_rect.x = -30

# loads in the image
paper_image = pg.image.load(os.path.join(game_folder, 'paper.jpg')).convert()
# storing the location/dimensions of pixels and allows user to access/change pixels
paper_image_rect = paper_image.get_rect()
paper_image_rect.x = 180
paper_image_rect.y = 100

# defines the variable as a true statement
running = True

# repeats the function as long as the code is running
while running:
    # sets the frame rate
    clock.tick(FPS)
    # sets up the variables to be defined
    # event is whenever an action occurs
    for event in pg.event.get():
        # flow loop: iterates over a sequence such as making a true statement become false
        if event.type == pg.QUIT:
            running = False
        # sets up the events for mouse button input is released
        if event.type == pg.MOUSEBUTTONUP:
            # displays the coordinates to be clicked
            # 0 is x-coordinate
            # print(pg.mouse.get_pos()[0])
            # 1 is y-coordinate
            # print(pg.mouse.get_pos()[1])
            # gets the coordinates and stores it for use
            mouse_coords = pg.mouse.get_pos()
            if pg.mouse.get_pos()[0] <= rock_image_rect.width and pg.mouse.get_pos()[1] < rock_image_rect.height:
                print("I chose the rock")
            else:
                print("no rock")
            # returning the true/false datatypes
            print(rock_image_rect.collidepoint(mouse_coords))
            if rock_image_rect.collidepoint(mouse_coords):
                print("you clicked on rock")
            elif paper_image_rect.collidepoint(mouse_coords):
                print("you clicked on paper")
                if GAMEOVER == False:
                    GAMEOVER = True
                else:
                    GAMEOVER = False
            elif scissors_image_rect.collidepoint(mouse_coords):
                print("you clicked on scissors")
                if GAMEOVER == False:
                    GAMEOVER = True
                else:
                    GAMEOVER = False
            else:
                print("you did not click on anything")

    # get user input
    # HCI - human computer interaction...
    # keyboard, mouse, controller, vr headset
    # update
    # rock_image_rect.x += 1

    # draw
    screen.fill(BLACK)

    if not GAMEOVER:
        screen.blit(rock_image, rock_image_rect)
        screen.blit(paper_image, paper_image_rect)
        screen.blit(scissors_image, scissors_image_rect)
    else:
        screen.blit(rock_image, rock_image_rect)

    pg.display.flip()

pg.quit
