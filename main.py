import pygame
import random

pygame.init()

#colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
#size of screen
displayWidth = 600
displayHight = 400
#snake variables
snakeSize = 10
snakeSpeed = 15

#create game screen
gameScreen = pygame.display.set_mode((displayWidth, displayHight))
pygame.display.set_caption('Snake Game in Python')

clock = pygame.time.Clock()

#set fonts
gameOverFont = pygame.font.SysFont(None, 25)
scoreFont = pygame.font.SysFont(None, 35)


def getScore(score):
    value = scoreFont.render("Score: " + str(score), True, white)
    gameScreen.blit(value, [0, 0])


def getSnake(snakeSize, snakeList):
    for x in snakeList:
        pygame.draw.rect(gameScreen, green, [x[0], x[1], snakeSize, snakeSize])


def getMessage(msg, color):
    mesg = gameOverFont.render(msg, True, color)
    gameScreen.blit(mesg, [displayWidth / 6, displayHight / 3])


def gameLoop():

    game_over = False
    game_close = False

    x1 = displayWidth / 2
    y1 = displayHight / 2

    xFutureMove = 0
    yFutureMove = 0

    snakeList = []
    snakeLenght = 1

    foodx = round(random.randrange(0, displayWidth - snakeSize) / 10.0) * 10.0
    foody = round(random.randrange(0, displayHight - snakeSize) / 10.0) * 10.0

    while not game_over:

        #if snake dies display
        while game_close == True:
            gameScreen.fill(black)
            getMessage("You Lost! Press A to Play Again or Q to Quit", red)
            getScore(snakeLenght - 1)
            pygame.display.update()

            #get input für death screen
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_a:
                        gameLoop()

        #get user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xFutureMove = -snakeSize
                    yFutureMove = 0
                elif event.key == pygame.K_RIGHT:
                    xFutureMove = snakeSize
                    yFutureMove = 0
                elif event.key == pygame.K_UP:
                    yFutureMove = -snakeSize
                    xFutureMove = 0
                elif event.key == pygame.K_DOWN:
                    yFutureMove = snakeSize
                    xFutureMove = 0

        #check if player is outside of the map
        if x1 >= displayWidth or x1 < 0 or y1 >= displayHight or y1 < 0:
            game_close = True
        #set change
        x1 += xFutureMove
        y1 += yFutureMove
        #set background color
        gameScreen.fill(black)
        #draw snake and food
        pygame.draw.rect(gameScreen, blue, [foodx, foody, snakeSize, snakeSize])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snakeList.append(snake_Head)

        #reset snake lenght
        if len(snakeList) > snakeLenght:
            del snakeList[0]
        #check if snake goes into itself
        for x in snakeList[:-1]:
            if x == snake_Head:
                game_close = True

        #set score and snake
        getSnake(snakeSize, snakeList)
        getScore(snakeLenght - 1)
        #update game
        pygame.display.update()

        #if snake eats food add length to snake
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, displayWidth - snakeSize) / 10.0) * 10.0
            foody = round(random.randrange(0, displayHight - snakeSize) / 10.0) * 10.0
            snakeLenght += 1

        clock.tick(snakeSpeed)

    pygame.quit()
    quit()


gameLoop()