#
# BREAKOUT GAME 
#

import pygame, time

#
# definitions 
#

FPS = 30 # Frames Per Second
SCREEN_WIDTH = 1280  * 0.8   # screensize in x-direction
SCREEN_HEIGHT = 720 * 0.8   # screensize in y-direction
BALL_WIDTH = 16       # ballsize in x-direction in pixels
BALL_HEIGHT = 16      # ballsize in y-direction in pixels
PADDLE_WIDTH = 144
PADDLE_HEIGHT = 32

ball_x = 0            # x-position of ball in pixels
ball_y = 0
ball_speed_x = 6      # speed of ball in x-direction in pixels per frame
ball_speed_y = 6
paddle_x = SCREEN_WIDTH / 2 - PADDLE_WIDTH / 2 
paddle_y = SCREEN_HEIGHT - PADDLE_HEIGHT
paddle_speed_right = 10
paddle_speed_left = -1 * paddle_speed_right
game_status_msg = "Controls: A and D"
#
# init game
#

# Initializes the pygame modules (e.g. 'font' or 'display')
pygame.init()         

# Sets the font that is default to my system
font = pygame.font.SysFont('default', 64)

# This initializes the display and returns a 'Surface' which can be drawn on. 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Creates the object that track time and control the games framerate.
fps_clock = pygame.time.Clock()

#
# read images
#

# Loads the image and preserves the alpha (transparancy) values
spritesheet = pygame.image.load('Breakout_Tile_Free.png').convert_alpha()   

# Creates a new surface for the ball of 64 by 64 pixels. The format will include the alpha values
ball_img = pygame.Surface((64, 64), pygame.SRCALPHA)  
paddle_img = pygame.Surface((243, 64), pygame.SRCALPHA)


# draws the ball from the specific coordinates of the spritesheet on the created surface, with a width and height of 64 pixels
ball_img.blit(spritesheet, (0, 0), (1403, 652, 64, 64))
paddle_img.blit(spritesheet, (0, 0), (1158, 396, 243, 64))

# Scales the surface to the desired width and height
ball_img = pygame.transform.scale(ball_img, (BALL_WIDTH, BALL_HEIGHT))  
paddle_img = pygame.transform.scale(paddle_img, (PADDLE_WIDTH, PADDLE_HEIGHT))

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
    ball_y = ball_y + ball_speed_y

    # bounce ball
    if ball_x < 0 :                           # If the ball is at the left edge of the screen:
      ball_speed_x = abs(ball_speed_x)        # Make the ballspeed positive (moving to the right)
    if ball_x + BALL_WIDTH > SCREEN_WIDTH:    # If the right side of the ball exceeds the right of the screen:
      ball_speed_x = abs(ball_speed_x) * -1   # Make the ballspeed negative (moving to the left)

    if ball_y < 0:
       ball_speed_y = abs(ball_speed_y)
    if ball_y + BALL_HEIGHT > SCREEN_HEIGHT:
       ball_speed_y = abs(ball_speed_y) * -1

    # bounce off paddle
    if (ball_x + BALL_WIDTH > paddle_x and
        ball_x < paddle_x + PADDLE_WIDTH and
        ball_y + PADDLE_HEIGHT > paddle_y and
        ball_y < paddle_y + PADDLE_HEIGHT):
       ball_speed_y = abs(ball_speed_y) * -1
       

    # move paddle
    if keys[pygame.K_d] and paddle_x <= SCREEN_WIDTH - PADDLE_WIDTH:
       paddle_x += paddle_speed_right
    if keys[pygame.K_a] and paddle_x >= 0:
       paddle_x += paddle_speed_left
       

    # 
    # handle collisions
    #
    if ball_y + BALL_HEIGHT >= SCREEN_HEIGHT:
       ball_speed_x = 0
       ball_speed_y = 0
       game_status_msg = "You lost!"



    # 
    # draw everything
    #

    # clear screen
    screen.fill(pygame.Color(0, 154, 166))  # Makes the background greenish
    screen.set_alpha(0)                     # Makes the background fully transparant 

    # draw ball
    screen.blit(ball_img, (ball_x, ball_y))      # draws the ball on the screen surface on the current coordinates of the ball
    screen.blit(paddle_img, (paddle_x, paddle_y))
    game_status_img = font.render(game_status_msg, True, 'green')
    screen.blit(game_status_img, (SCREEN_WIDTH / 2 - game_status_img.get_width() / 2, 0))
    
    # show screen
    pygame.display.flip() 

    # 
    # wait until next frame
    #

    fps_clock.tick(FPS) # Sleep the remaining time of this frame

print('mygame stopt running')
