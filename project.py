from ast import Return
import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)

width = 600
height = 400
snake_size = 10
snake_speed = 10


WINDOW = pygame.display.set_mode((width, height))
pygame.display.set_caption('Automated Snake Game')

clock = pygame.time.Clock()

font_style = pygame.font.SysFont("freesansbold.ttf", 32)


def display_score(score):
    pygame.display.set_caption("Score:  " + str(score))


def display_snake(snake_size, snake_list):
    for coordinates in snake_list:
        pygame.draw.rect(
            WINDOW, black, [coordinates[0], coordinates[1], snake_size, snake_size])


def display_msg(msg, color):
    message = font_style.render(msg, True, color)
    WINDOW.blit(message, [width / 2, height / 2])


def algorithm(head, food, prev):
    head_x = head[0]
    head_y = head[1]

    food_x = food[0]
    food_y = food[1]

    if food_x == head_x and food_y < head_y:
        if prev != 'down':
            return 'up'
        else:
            return 'right'

    if food_x == head_x and food_y > head_y:
        if prev != 'up':
            return 'down'
        else:
            return 'left'

    if food_y == head_y and food_x < head_x:
        if prev != 'right':
            return 'left'
        else:
            return 'up'

    if food_y == head_y and food_x < head_x:
        if prev != 'left':
            return 'right'
        else:
            return 'down'

    if food_x < head_x and food_y < head_y:
        if prev != 'right':
            return 'left'
        else:
            return 'up'

    if food_x < head_x and food_y > head_y:
        if prev != 'up':
            return 'down'
        else:
            return 'left'

    if food_x > head_x and food_y > head_y:
        if prev != 'up':
            return 'down'
        else:
            return 'right'

    if food_x > head_x and food_y < head_y:
        if prev != 'left':
            return 'right'
        else:
            return 'up'

    return 'down'


def gameLoop_player():
    finish_flag = False
    lost_flag = False

    x_coordinate = width / 2
    y_coordinate = height / 2

    changeX = 0
    changeY = 0

    snake_List = []
    score = 1

    foodx = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_size) / 10.0) * 10.0

    while not finish_flag:

        while lost_flag == True:
            WINDOW.fill(white)
            display_msg("You Lost! Press P to Play Again or Q to Quit", red)
            display_score(score - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        finish_flag = True
                        lost_flag = False
                    if event.key == pygame.K_p:
                        gameLoop_player()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish_flag = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    changeX = -snake_size
                    changeY = 0
                elif event.key == pygame.K_RIGHT:
                    changeX = snake_size
                    changeY = 0
                elif event.key == pygame.K_UP:
                    changeY = -snake_size
                    changeX = 0
                elif event.key == pygame.K_DOWN:
                    changeY = snake_size
                    changeX = 0

        if x_coordinate >= width or x_coordinate < 0 or y_coordinate >= height or y_coordinate < 0:
            game_close = True

        x_coordinate += changeX
        y_coordinate += changeY
        WINDOW.fill(white)
        pygame.draw.rect(WINDOW, red, [foodx, foody, snake_size, snake_size])
        snake_List.append((x_coordinate, y_coordinate))
        if len(snake_List) > score:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == (x_coordinate, y_coordinate):
                lost_flag = True

        display_snake(snake_size, snake_List)
        display_score(score - 1)

        pygame.display.update()

        if x_coordinate == foodx and y_coordinate == foody:
            foodx = round(random.randrange(
                0, width - snake_size) / 10.0) * 10.0
            foody = round(random.randrange(
                0, height - snake_size) / 10.0) * 10.0
            score += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


move = 'right'


def gameLoop_automated(move):
    finish_flag = False
    lost_flag = False

    x_coordinate = width / 2
    y_coordinate = height / 2

    changeX = 0
    changeY = 0

    snake_List = []
    score = 1

    foodx = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_size) / 10.0) * 10.0

    while not finish_flag:

        while lost_flag == True:
            WINDOW.fill(white)
            display_msg("You Lost! Press P to Play Again or Q to Quit", red)
            display_score(score - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        finish_flag = True
                        lost_flag = False
                    if event.key == pygame.K_c:
                        gameLoop_automated()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish_flag = True

        move = algorithm((x_coordinate, y_coordinate), (foodx, foody), move)
        if move == 'left':
            changeX = -snake_size
            changeY = 0
        elif move == 'right':
            changeX = snake_size
            changeY = 0
        elif move == 'up':
            changeY = -snake_size
            changeX = 0
        elif move == 'down':
            changeY = snake_size
            changeX = 0

        """if x1 >= width:
            x1 = 0

        if x1 < 0:
            x1 = width

        if y1 >= height:
            y1 = 0

        if y1 < 0:
            y1 = height"""

        if x_coordinate >= width or x_coordinate < 0 or y_coordinate >= height or y_coordinate < 0:
            lost_flag = True

        x_coordinate += changeX
        y_coordinate += changeY
        WINDOW.fill(white)
        pygame.draw.rect(WINDOW, red, [foodx, foody, snake_size, snake_size])
        snake_List.append((x_coordinate, y_coordinate))
        if len(snake_List) > score:
            del snake_List[0]

        """for x in snake_List[:-1]:
            if x == (x1, y1):
                game_close = True"""

        display_snake(snake_size, snake_List)
        display_score(score - 1)

        pygame.display.update()

        if x_coordinate == foodx and y_coordinate == foody:
            foodx = round(random.randrange(
                0, width - snake_size) / 10.0) * 10.0
            foody = round(random.randrange(
                0, height - snake_size) / 10.0) * 10.0
            score += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


print("1. Automated Snake Game")
print("2. Single Player Snake Game")
print("3. Quit")
option = int(input())
if option == 1:
    gameLoop_automated(move)
if option == 2:
    gameLoop_player()
if option == 3:
    Return
