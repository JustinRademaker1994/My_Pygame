#
# BREAKOUT GAME 
#

import pygame, time

#
# definitions 
#

FPS = 30 # Frames Per Second
SCREEN_WIDTH = 1280   # screensize in x-direction
SCREEN_HEIGHT = 720   # screensize in y-direction
BALL_WIDTH = 16       # ballsize in x-direction in pixels
BALL_HEIGHT = 16      # ballsize in y-direction in pixels

ball_x = 0            # x-position of ball in pixels
ball_speed_x = 6      # speed of ball in x-direction in pixels per frame

#
# init game
#

# Initializes the pygame modules (e.g. 'font' or 'display')
pygame.init()         

# Sets the font that is default to my system
font = pygame.font.SysFont('default', 64)

# This initializes the display and returns a 'Surface' which can be drawn on. 
screen = pygame.display.set_mode((SCREEN_WIDTH * 0.8, SCREEN_HEIGHT * 0.8))

# Creates the object that track time and control the games framerate.
fps_clock = pygame.time.Clock()

#
# read images
#

# Loads the image and preserves the alpha (transparancy) values
spritesheet = pygame.image.load('Breakout_Tile_Free.png').convert_alpha()   

# Creates a new surface for the ball of 64 by 64 pixels. The format will include the alpha values
ball_img = pygame.Surface((64, 64), pygame.SRCALPHA)  

# draws the ball from the specific coordinates of the spritesheet on the created surface, with a width and height of 64 pixels
ball_img.blit(spritesheet, (0, 0), (1403, 652, 64, 64))

# Scales the surface to the desired width and height
ball_img = pygame.transform.scale(ball_img, (BALL_WIDTH, BALL_HEIGHT))  

#
# game loop
#

print('mygame is running')
running = True
while running:
    #
    # read events
    # 
    for event in pygame.event.get(): 
        # The 'quit' event represents when the X is pressed on the top right corner
        if event.type == pygame.QUIT:  
            running = False

    # stores an object that has a constant value for every key and a boolean indication if the key is pressed
    keys = pygame.key.get_pressed() 
            
    # 
    # move everything
    #

    # move ball
    ball_x = ball_x + ball_speed_x

    # bounce ball
    if ball_x < 0 :                           # If the ball is at the left edge of the screen:
      ball_speed_x = abs(ball_speed_x)        # Make the ballspeed positive (moving to the right)
    if ball_x + BALL_WIDTH > SCREEN_WIDTH:    # If the right side of the ball exceeds the right of the screen:
      ball_speed_x = abs(ball_speed_x) * -1   # Make the ballspeed negative (moving to the left)

    # 
    # handle collisions
    #
    
    # 
    # draw everything
    #

    # clear screen
    screen.fill(pygame.Color(0, 154, 166))  # Makes the background greenish
    screen.set_alpha(0)                     # Makes the background fully transparant 

    # draw ball
    screen.blit(ball_img, (ball_x, 0))      # draws the ball on the screen surface on the current coordinates of the ball
    
    # show screen
    pygame.display.flip() 

    # 
    # wait until next frame
    #

    fps_clock.tick(FPS) # Sleep the remaining time of this frame

print('mygame stopt running')
