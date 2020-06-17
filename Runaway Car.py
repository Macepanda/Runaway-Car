'''
This is a game where a car has 5 lanes and is trying to avoid the obstacles.
'''
import pygame
import random

## initalising the game and variables
pygame.init()
carImage = pygame.image.load("racecar.png")
gameIcon = pygame.image.load("gameicon.png")
pause = False
highScore = 0

# the dimensions of the game display and car
display_height = 600
display_width = 560
car_width = 50
## x coordinate for block lanes
blockLanes = [10, 120, 230, 340, 450]

## initialising colours
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (200, 0, 0)
bright_red = (255, 0, 0)
green = (0, 200, 0)
bright_green = (0, 255, 0)
block_colour = (255, 165, 0) ## orange
yellow = (255, 255, 0)
road_grey = (136, 140, 141)

## creating game name and icon
pygame.display.set_caption("Runaway Car")
pygame.display.set_icon(gameIcon)
clock = pygame.time.Clock()

def gameDesign():
    global gameDisplay

    ## game display
    gameDisplay = pygame.display.set_mode((display_width,display_height))

    ## road colour
    gameDisplay.fill(road_grey)
    
    ## left barrier
    pygame.draw.rect(gameDisplay, yellow, [0, 0, 10, 600])
    pygame.draw.rect(gameDisplay, black, [0, 60, 10, 60])
    pygame.draw.rect(gameDisplay, black, [0, 180, 10, 60])
    pygame.draw.rect(gameDisplay, black, [0, 300, 10, 60])
    pygame.draw.rect(gameDisplay, black, [0, 420, 10, 60])
    pygame.draw.rect(gameDisplay, black, [0, 540, 10, 60])

    ## right barrier
    pygame.draw.rect(gameDisplay, yellow, [550, 0, 10, 600])
    pygame.draw.rect(gameDisplay, black, [550, 60, 10, 60])
    pygame.draw.rect(gameDisplay, black, [550, 180, 10, 60])
    pygame.draw.rect(gameDisplay, black, [550, 300, 10, 60])
    pygame.draw.rect(gameDisplay, black, [550, 420, 10, 60])
    pygame.draw.rect(gameDisplay, black, [550, 540, 10, 60])

    ## lane1 marker
    pygame.draw.rect(gameDisplay, white, [110, 0, 10, 30])
    pygame.draw.rect(gameDisplay, white, [110, 80, 10, 90])
    pygame.draw.rect(gameDisplay, white, [110, 240, 10, 90])
    pygame.draw.rect(gameDisplay, white, [110, 400, 10, 90])
    pygame.draw.rect(gameDisplay, white, [110, 560, 10, 90])

    ## lane2 marker
    pygame.draw.rect(gameDisplay, white, [220, 0, 10, 90])
    pygame.draw.rect(gameDisplay, white, [220, 160, 10, 90])
    pygame.draw.rect(gameDisplay, white, [220, 320, 10, 90])
    pygame.draw.rect(gameDisplay, white, [220, 480, 10, 90])

    ## lane3 marker
    pygame.draw.rect(gameDisplay, white, [330, 0, 10, 30])
    pygame.draw.rect(gameDisplay, white, [330, 80, 10, 90])
    pygame.draw.rect(gameDisplay, white, [330, 240, 10, 90])
    pygame.draw.rect(gameDisplay, white, [330, 400, 10, 90])
    pygame.draw.rect(gameDisplay, white, [330, 560, 10, 90])

    ## lane4 marker
    pygame.draw.rect(gameDisplay, white, [440, 0, 10, 90])
    pygame.draw.rect(gameDisplay, white, [440, 160, 10, 90])
    pygame.draw.rect(gameDisplay, white, [440, 320, 10, 90])
    pygame.draw.rect(gameDisplay, white, [440, 480, 10, 90])
    

def score(dodged, high_score):
    global gameDisplay
    font = pygame.font.SysFont("comicsansms", 20)
    text = font.render("Dodged: " + str(dodged), True, black)
    text2 = font.render("High Score: " + str(high_score), True, black)
    gameDisplay.blit(text, (13,2))
    gameDisplay.blit(text2, (13,24))

## defining the function to display the car
def car(lane):
    global gameDisplay
    gameDisplay.blit(carImage,(lane[0], lane[1]))

## defining the function to create obstacles
def blocks(block_x, block_y, lane_width, block_colour):
    global gameDisplay
    pygame.draw.rect(gameDisplay, block_colour, [block_x, block_y, lane_width, lane_width])

def blocks2(block_x, block_y, lane_width, block_colour):
    global gameDisplay
    pygame.draw.rect(gameDisplay, block_colour, [block_x, block_y, lane_width, lane_width])

def blocks3(block_x, block_y, lane_width, block_colour):
    global gameDisplay
    pygame.draw.rect(gameDisplay, block_colour, [block_x, block_y, lane_width, lane_width])

def blocks4(block_x, block_y, lane_width, block_colour):
    global gameDisplay
    pygame.draw.rect(gameDisplay, block_colour, [block_x, block_y, lane_width, lane_width])

## defining the functions to create text objects
def text_object(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

## defining the function for something to happen during a crash
def crash():
    global gameDisplay
    largeText = pygame.font.SysFont("comicsansms", 70)
    TextSurf, TextRect = text_object("You Crashed", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        ## buttons to continue and quit
        button("Play Again", 120, 450, 100, 50, green, bright_green, game_loop)
        button("Quit", 340, 450, 100, 50, red, bright_red, quitgame)

        # updates the display
        pygame.display.update()
        clock.tick(15)

## defining the function to display buttons
def button(message, x, y, width, height, inactiveColour, activeColour, action = None):
    global gameDisplay
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(gameDisplay, activeColour, [x, y, width, height])
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, inactiveColour, [x, y, width, height])
    smallText = pygame.font.SysFont("comicsansms", 15)
    TextSurf, TextRect = text_object(message, smallText)
    TextRect.center = ((x + (width/2) , y + (height /2)))
    gameDisplay.blit(TextSurf, TextRect)
    
## defining the function to quitgame
def quitgame():
    pygame.quit()
    quit()

## defining the function to unpause
def unpause():
    global pause
    pause = False
    
## defining the function to pause
def paused():
    global gameDisplay
    global pause
    largeText = pygame.font.SysFont("comicsansms", 70)
    TextSurf, TextRect = text_object("Paused", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        button("Continue", 120, 450, 100, 50, green, bright_green, unpause)
        button("Quit", 340, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)   

## defining the game intro
def game_intro():
    global gameDisplay
                
    gameDesign()
    largeText = pygame.font.SysFont("comicsansm", 70)
    textSurf, textRect = text_object("Runaway Car", largeText)
    textRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(textSurf, textRect)

    intro = True
        
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        ## buttons to continue and quit
        button("Start Game", 120, 450, 100, 50, green, bright_green, game_loop)
        button("Quit", 340, 450, 100, 50, red, bright_red, quitgame)

        # updates the display
        pygame.display.update()
        clock.tick(15)
        
## defining the main game function
def game_loop():
    global pause
    global highScore
    global gameDisplay
    
    ## initialising variables
    quitGame = False
    ## lanes for the cars to move
    lane1 = ((display_width * 0.5 - car_width * 0.5) - 220, display_height * 0.8)
    lane2 = ((display_width * 0.5 - car_width * 0.5) - 110, display_height * 0.8)
    lane3 = (display_width * 0.5 - car_width * 0.5, display_height * 0.8)
    lane4 = ((display_width * 0.5 - car_width * 0.5) + 110, display_height * 0.8)
    lane5 = ((display_width * 0.5 - car_width * 0.5) + 220, display_height * 0.8)
    lane_no = lane3
    lane_width = 100
    ## block dimensions
    block_startx = 230
    block_starty = - display_height
    block_speed = 5
    dodged = 0

    ## runs this loop as long as the game is running
    while not quitGame:
        
        ## finds out the events happening within the game display
        for event in pygame.event.get():
            
            ## finds out if user is trying to exit the game by clicking the red X on the top right
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            ## finds out if user is pressing down any keys
            if event.type == pygame.KEYDOWN:

                ## finds out if the user wants to move left
                if event.key == pygame.K_LEFT:
                    if lane_no == lane5:
                        lane_no = lane4
                    elif lane_no == lane4:
                        lane_no = lane3
                    elif lane_no == lane3:
                        lane_no = lane2
                    elif lane_no == lane2:
                        lane_no = lane1
                        
                ## finds out if the user wants to move right    
                elif event.key == pygame.K_RIGHT:
                    if lane_no == lane1:
                        lane_no = lane2
                    elif lane_no == lane2:
                        lane_no = lane3
                    elif lane_no == lane3:
                        lane_no = lane4
                    elif lane_no == lane4:
                        lane_no = lane5

                ## finds out if the user wants to pause
                elif event.key == pygame.K_p:
                    pause = True
                    paused()

        ## fills the display with white
        gameDesign()

        ## displays the obstacles, car and score
        if dodged >= 30:
            blocks(block_startx, block_starty, lane_width, block_colour)
            blocks2(block_2x, block_starty, lane_width, block_colour)
            blocks3(block_3x, block_starty, lane_width, block_colour)  
            blocks4(block_4x, block_starty, lane_width, block_colour)  
        elif dodged >= 20:
            blocks(block_startx, block_starty, lane_width, block_colour)
            blocks2(block_2x, block_starty, lane_width, block_colour)
            blocks3(block_3x, block_starty, lane_width, block_colour)  
        elif dodged >= 10:
            blocks(block_startx, block_starty, lane_width, block_colour)
            blocks2(block_2x, block_starty, lane_width, block_colour)
        else:
            blocks(block_startx, block_starty, lane_width, block_colour)
        block_starty += block_speed
        car(lane_no)
        score(dodged, highScore)

        ## checks if the block has passed and creates a new one, as well as adds the score
        if block_starty > display_height:
            block_starty = 0 - 100
            dodged += 1
            highScore = max(highScore, dodged)
            for b in blockLanes:
                if dodged >= 30:
                    block_startx = blockLanes[random.randint(0,4)]
                    block_2x = blockLanes[random.randint(0,4)]
                    block_3x = blockLanes[random.randint(0,4)]                    
                    block_4x = blockLanes[random.randint(0,4)]
                elif dodged >= 20:
                    block_startx = blockLanes[random.randint(0,4)]
                    block_2x = blockLanes[random.randint(0,4)]
                    block_3x = blockLanes[random.randint(0,4)]
                elif dodged >= 10:
                    block_startx = blockLanes[random.randint(0,4)]
                    block_2x = blockLanes[random.randint(0,4)]
                else:
                    block_startx = blockLanes[random.randint(0,4)]
                    
                break
            
            if dodged >=30:
                block_speed = 8
                block_speed += 1
                
            block_speed += 1/4
            
        ## checks for a crash. lane1[1] refers to the y coordinate of the car, since it never changes lane1 is just an example, you can use any lane.
        if lane1[1] < block_starty + 100:

            ## crash occurs if it also clashes with the x coordinate.
            if dodged >= 30:
                if lane_no[0] > block_startx and lane_no[0] < block_startx + 100 or \
                   lane_no[0] > block_2x and lane_no[0] < block_2x + 100 or \
                   lane_no[0] > block_3x and lane_no[0] < block_3x + 100 or \
                   lane_no[0] > block_4x and lane_no[0] < block_4x + 100:
                    crash()
            elif dodged >= 20:
                if lane_no[0] > block_startx and lane_no[0] < block_startx + 100 or \
                   lane_no[0] > block_2x and lane_no[0] < block_2x + 100 or \
                   lane_no[0] > block_3x and lane_no[0] < block_3x + 100:
                    crash()                
            elif dodged >= 10:
                if lane_no[0] > block_startx and lane_no[0] < block_startx + 100 or \
                   lane_no[0] > block_2x and lane_no[0] < block_2x + 100:
                    crash()                
            else:
                if lane_no[0] > block_startx and lane_no[0] < block_startx + 100:
                    crash()
        
        ## updates the display and sets the frames/second
        pygame.display.update()
        clock.tick(60)

## runs the game
game_intro()
game_loop()
quitgame()

