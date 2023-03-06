# File created by: Liam McKeown

# editors notes: My RPS game's base components work with two issues which I could not resolve
# the cpu images, lose screen, win screen, tie screen, and restart screen constantly flicker; engine issue?
# the reset screen will work for less than a second when spacebar is pressed but will then return to result of previous bout

# Libraries; outside python code to be used for this specific code
from time import sleep
from random import randint
import pygame as pg
import os

# Accesses the game folder
game_folder = os.path.dirname(__file__)
print(game_folder)

# Sets the width, height, and frames per second for the pygame window
WIDTH = 860
HEIGHT = 680
FPS = 30

# Defines the colors; colors defined by Red/Green/Blue values with 255 = white and 0 = black
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# List of three strings
# List because of brackets; Tuple uses parenthesis
# Tuples can't be changed; Lists can be changed
objects = ["rock", "paper", "scissors"]

# "def" is a module that stores multiple lines of code and functions # Best used when multiple lines of code have to be used multiple times
# "screen" is a pygame exclusive variable that displays images or defined colors on screen
# "pg.display.flip()" updates the display with "screen" images


def start_screen():
    screen.fill(BLACK)
    screen.blit(octagon_image, octagon_image_rect)
    screen.blit(rock_image, rock_image_rect)
    screen.blit(paper_image, paper_image_rect)
    screen.blit(scissors_image, scissors_image_rect)
    pg.display.flip()

# "def" is a module that stores multiple lines of code and functions # Best used when multiple lines of code have to be used multiple times
# "rect" loads in the image
# no "rect" defines the image
# to treat an image as if it doesn't exist, I defined the location far outside the height and width such as -2050


def reset():
    screen.blit(rock_image, rock_image_rect)
    rock_image_rect.x = 0
    rock_image_rect.y = 10
    screen.blit(paper_image, paper_image_rect)
    paper_image_rect.x = 250
    paper_image_rect.y = 400
    screen.blit(scissors_image, scissors_image_rect)
    scissors_image_rect.x = 0
    scissors_image_rect.y = 400
    screen.blit(cpu_rock_image, cpu_rock_image_rect)
    cpu_rock_image_rect.x = -500
    cpu_rock_image_rect.y = -500
    screen.blit(cpu_scissors_image, cpu_scissors_image_rect)
    cpu_scissors_image_rect.x = -600
    cpu_scissors_image_rect.y = -600
    screen.blit(cpu_paper_image, cpu_scissors_image_rect)
    cpu_paper_image_rect.x = -700
    cpu_paper_image_rect.y = -700
    screen.blit(win_image, win_image_rect)
    win_image_rect.x = -2050
    screen.blit(lose_image, lose_image_rect)
    lose_image_rect.x = -2050
    screen.blit(tie_image, tie_image_rect)
    tie_image_rect.x = -2050
    screen.blit(restart_image, restart_image_rect)
    restart_image_rect.x = -2050

# "def" is a module that stores multiple lines of code and functions # Best used when multiple lines of code have to be used multiple times
# "screen" is a pygame exclusive variable that displays images or defined colors on screen
# "pg.display.flip()" updates the display with "screen" images
# "rect" loads in the image
# no "rect" defines the image


def win_screen():
    screen.blit(win_image, win_image_rect)
    win_image_rect.x = 325
    win_image_rect.y = 400
    pg.display.flip()

# "def" is a module that stores multiple lines of code and functions # Best used when multiple lines of code have to be used multiple times
# "screen" is a pygame exclusive variable that displays images or defined colors on screen
# "pg.display.flip()" updates the display with "screen" images
# "rect" loads in the image
# no "rect" defines the image


def tie_screen():
    screen.blit(tie_image, tie_image_rect)
    tie_image_rect.x = 400
    tie_image_rect.y = 400
    pg.display.flip()

# "def" is a module that stores multiple lines of code and functions # Best used when multiple lines of code have to be used multiple times
# "screen" is a pygame exclusive variable that displays images or defined colors on screen
# "pg.display.flip()" updates the display with "screen" images
# "rect" loads in the image
# no "rect" defines the image


def lose_screen():
    screen.blit(lose_image, lose_image_rect)
    lose_image_rect.x = 300
    lose_image_rect.y = 400
    pg.display.flip()

# "def" is a module that stores multiple lines of code and functions # Best used when multiple lines of code have to be used multiple times
# "screen" is a pygame exclusive variable that displays images or defined colors on screen
# "pg.display.flip()" updates the display with "screen" images
# "rect" loads in the image
# no "rect" defines the image


def restart_button():
    screen.blit(restart_image, restart_image_rect)
    restart_image_rect.x = 5
    restart_image_rect.y = 475
    pg.display.flip()

# "def" is a module that stores multiple lines of code and functions # Best used when multiple lines of code have to be used multiple times
# "screen" is a pygame exclusive variable that displays images or defined colors on screen
# "pg.display.flip()" updates the display with "screen" images
# "rect" loads in the image
# no "rect" defines the image


def cpu_randchoice():
    choice = objects[randint(0, 2)]
    print("The computer chose " + choice)
    return choice

# "def" is a module that stores multiple lines of code and functions # Best used when multiple lines of code have to be used multiple times
# "screen" is a pygame exclusive variable that displays images or defined colors on screen
# "pg.display.flip()" updates the display with "screen" images
# "rect" loads in the image
# no "rect" defines the image


def cpu_rock():
    screen.blit(cpu_rock_image, cpu_rock_image_rect)
    cpu_rock_image_rect.x = 500
    cpu_rock_image_rect.y = 50
    pg.display.flip()

# "def" is a module that stores multiple lines of code and functions # Best used when multiple lines of code have to be used multiple times
# "screen" is a pygame exclusive variable that displays images or defined colors on screen
# "pg.display.flip()" updates the display with "screen" images
# "rect" loads in the image
# no "rect" defines the image


def cpu_paper():
    screen.blit(cpu_paper_image, cpu_paper_image_rect)
    cpu_paper_image_rect.x = 500
    cpu_paper_image_rect.y = 150
    pg.display.flip()

# "def" is a module that stores multiple lines of code and functions # Best used when multiple lines of code have to be used multiple times
# "screen" is a pygame exclusive variable that displays images or defined colors on screen
# "pg.display.flip()" updates the display with "screen" images
# "rect" loads in the image
# no "rect" defines the image


def cpu_scissors():
    screen.blit(cpu_scissors_image, cpu_scissors_image_rect)
    cpu_scissors_image_rect.x = 500
    cpu_scissors_image_rect.y = 150
    pg.display.flip()

# "def" is a module that stores multiple lines of code and functions # Best used when multiple lines of code have to be used multiple times
# "screen" is a pygame exclusive variable that displays images or defined colors on screen
# "pg.display.flip()" updates the display with "screen" images
# "rect" loads in the image
# no "rect" defines the image


def player_rock():
    screen.blit(rock_image, rock_image_rect)
    rock_image_rect.x = 150
    rock_image_rect.y = 50
    paper_image_rect.x = -500
    scissors_image_rect.x = -500
    pg.display.flip

# "def" is a module that stores multiple lines of code and functions
# Best used when multiple lines of code have to be used multiple times
# "screen" is a pygame exclusive variable that displays images or defined colors on screen
# "pg.display.flip()" updates the display with "screen" images
# "rect" loads in the image
# no "rect" defines the image


def player_scissors():
    screen.blit(scissors_image, scissors_image_rect)
    scissors_image_rect.x = 250
    scissors_image_rect.y = 150
    rock_image_rect.x = -500
    paper_image_rect.x = -500
    pg.display.flip

# "def" is a module that stores multiple lines of code and functions # Best used when multiple lines of code have to be used multiple times
# "screen" is a pygame exclusive variable that displays images or defined colors on screen
# "pg.display.flip()" updates the display with "screen" images
# "rect" loads in the image
# No "rect" defines the image


def player_paper():
    screen.blit(paper_image, paper_image_rect)
    paper_image_rect.x = 250
    paper_image_rect.y = 150
    scissors_image_rect.x = -500
    rock_image_rect.x = -500
    pg.display.flip


# "init" initializes the pygame modules; get's everything started
pg.init()

# "screen" is defined with the Width and Height
# "set_caption" displays text in the window bar
# "time.clock" tracks amount of time
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Rock, Paper, Scissors")
clock = pg.time.Clock()

# First two lines loads in the image
# "image_rect" defines the image in pygame
# Last lines define either the x-value, y-value, or both
win_image = pg.image.load(os.path.join(
    game_folder, 'youwin.png')).convert()
win_image_rect = win_image.get_rect()
win_image_rect.x = -2050

# First two lines loads in the image
# "image_rect" defines the image in pygame
# Last lines define either the x-value, y-value, or both
lose_image = pg.image.load(os.path.join(
    game_folder, 'youlose.png')).convert()
lose_image_rect = lose_image.get_rect()
lose_image_rect.x = -2050

# First two lines loads in the image
# "image_rect" defines the image in pygame
# Last lines define either the x-value, y-value, or both
tie_image = pg.image.load(os.path.join(
    game_folder, 'youtie.png')).convert()
tie_image_rect = tie_image.get_rect()
tie_image_rect.x = -2050

# First two lines loads in the image
# "image_rect" defines the image in pygame
# Last lines define either the x-value, y-value, or both
restart_image = pg.image.load(os.path.join(
    game_folder, 'spacerestart.png')).convert()
restart_image_rect = restart_image.get_rect()
restart_image_rect.x = -2050

# First two lines loads in the image
# "image_rect" defines the image in pygame
# Last lines define either the x-value, y-value, or both
# "octagon_image_rect.x" uses the modulus operator
# "octagon_image_rect.y" uses the exponentiation operator
octagon_image = pg.image.load(os.path.join(
    game_folder, 'octagon.jpg')).convert()
octagon_image_rect = octagon_image.get_rect()
octagon_image_rect.x = (100 % 10)
octagon_image_rect.y = (500 ** 0)

# First two lines loads in the image
# "image_rect" defines the image in pygame
# Last lines define either the x-value, y-value, or both
# "rock_image_rect.x" uses the subtraction operator
# "rock_image_rect.y" uses the addition operator
rock_image = pg.image.load(os.path.join(game_folder, 'therock.jpg')).convert()
rock_image_rect = rock_image.get_rect()
rock_image_rect.x = (5 - 5)
rock_image_rect.y = (0 + 10)

# First two lines loads in the image
# "image_rect" defines the image in pygame
# Last lines define either the x-value, y-value, or both
# "scissors_image_rect.x" uses the subtraction operator
# "scissors_image_rect.y" uses the addition operator
scissors_image = pg.image.load(os.path.join(
    game_folder, 'scissors.jpg')).convert()
scissors_image_rect = scissors_image.get_rect()
scissors_image_rect.x = (5000000000000000 - 5000000000000000)
scissors_image_rect.y = (200 + 200)

# First two lines loads in the image
# "image_rect" defines the image in pygame
# Last lines define either the x-value, y-value, or both
# "paper_image_rect.x" uses the division operator
# "paper_image_rect.y" uses the multiplication operator
paper_image = pg.image.load(os.path.join(game_folder, 'paper.jpg')).convert()
paper_image_rect = paper_image.get_rect()
paper_image_rect.x = (500 / 2)
paper_image_rect.y = (200 * 2)

# First two lines loads in the image
# "image_rect" defines the image in pygame
# Last lines define either the x-value, y-value, or both
cpu_rock_image = pg.image.load(os.path.join(
    game_folder, 'therock.jpg')).convert()
cpu_rock_image_rect = cpu_rock_image.get_rect()
cpu_rock_image_rect.x = -500
cpu_rock_image_rect.y = -500

# First two lines loads in the image
# "image_rect" defines the image in pygame
# Last lines define either the x-value, y-value, or both
cpu_scissors_image = pg.image.load(os.path.join(
    game_folder, 'scissors.jpg')).convert()
cpu_scissors_image_rect = cpu_scissors_image.get_rect()
cpu_scissors_image_rect.x = -600
cpu_scissors_image_rect.y = -600

# First two lines loads in the image
# "image_rect" defines the image in pygame
# Last lines define either the x-value, y-value, or both
cpu_paper_image = pg.image.load(
    os.path.join(game_folder, 'paper.jpg')).convert()
cpu_paper_image_rect = cpu_paper_image.get_rect()
cpu_paper_image_rect.x = -700
cpu_paper_image_rect.y = -700

# "running" is the pygame engine displaying its function
# "player_choice" is the option that the user chooses
# "cpu_choice" is the option the computer chooses
running = True
player_choice = ""
cpu_choice = ""

# while loop; program runs infinitely
# for loop; program runs for limited amount of time
# if statement; defines a variable's function and what will occur if variable is used
# else statement; anything else that occurs besides the variable's function will lead to a defined statement
# elif statement; specific else statement, if "if" statment does not occur, specific alternative is defined
# specific pygame
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYUP:
            if event.key == pg.K_SPACE:
                reset()
        if event.type == pg.MOUSEBUTTONUP:
            mouse_coords = pg.mouse.get_pos()
            if rock_image_rect.collidepoint(mouse_coords):
                print("You chose rock")
                player_choice = "rock"
                cpu_choice = cpu_randchoice()
            elif paper_image_rect.collidepoint(mouse_coords):
                print("You chose paper")
                player_choice = "paper"
                cpu_choice = cpu_randchoice()
            elif scissors_image_rect.collidepoint(mouse_coords):
                print("You chose scissors")
                player_choice = "scissors"
                cpu_choice = cpu_randchoice()
            else:
                print("You chose nothing")

# Defined function in which I made the start screen
    start_screen()

# "if" statement; defines a variable's function and what will occur if variable is used
# Multiple defined functions occur if certain "if" combinations occur
    if player_choice == "rock":
        if cpu_choice == "rock":
            cpu_rock()
            player_rock()
            tie_screen()
            restart_button()
        if cpu_choice == "paper":
            cpu_paper()
            player_rock()
            lose_screen()
            restart_button()
        if cpu_choice == "scissors":
            cpu_scissors()
            player_rock()
            win_screen()
            restart_button()
    if player_choice == "paper":
        if cpu_choice == "rock":
            cpu_rock()
            player_paper()
            win_screen()
            restart_button()
        if cpu_choice == "paper":
            cpu_paper()
            player_paper()
            tie_screen()
            restart_button()
        if cpu_choice == "scissors":
            cpu_scissors()
            player_paper()
            lose_screen()
            restart_button()
    if player_choice == "scissors":
        if cpu_choice == "rock":
            cpu_rock()
            player_scissors()
            lose_screen()
            restart_button()
        if cpu_choice == "paper":
            cpu_paper()
            player_scissors()
            win_screen()
            restart_button()
        if cpu_choice == "scissors":
            cpu_scissors()
            player_scissors()
            tie_screen()
            restart_button()

# pygame stops running and exits
pg.quit
