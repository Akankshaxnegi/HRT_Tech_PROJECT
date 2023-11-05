
"""PROJECT : SNAKE GAME USING PYTHON
   NAME    : AKANKSHA NEGI
   DOMAIN  : PYTHON PROGRAMMING"""

# ********************************************  SNAKE  GAME  ALGORITHM *********************************************************
"""1. set the initial coordinates or start coordinates of the snake
   2. The body of the snake should be a number of rectangles arranged consecutively their coordinates would be saved in a list
   3. Also define the food position which would be randomly picked everytime the snake eats the food
   4. To randomly pick a spot for the food we would import the random module
   5. Keep track of the score and increase size of the snake everytime it eats the food
   6. Define a game over function to end the game
   7. Handle movement of the snake using key inputs (use key module)"""

# Import libraries necessary to create the snake game 
import pygame as pg
import time
import random

#initialise the module
pg.init()

# Constants
WIDTH, HEIGHT = 600, 500
SNAKE_SIZE = 10
FPS = 15

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Fonts
font = pg.font.SysFont('calibri', 25)

# Screen setup
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Snake Game")

# Object to set framrate later
clock = pg.time.Clock()

# initial score is zero
# to create a function to display the score just like a text with no calculation
def show_score(score):
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, [10, 10])
    
# To show the game over text and so to quit automatically when the game is over
def game_over():
    game_over_text = font.render("Game Over", True, RED)
    screen.blit(game_over_text, [WIDTH / 2 - 80, HEIGHT / 2 - 50])
    show_score(score)
    pg.display.flip()
    time.sleep(2)
    pg.quit()
    quit()

def snake(snake_size, snake_list):
    for block in snake_list:
        pg.draw.rect(screen, GREEN, [block[0], block[1], snake_size, snake_size])

def game_loop():
    global direction
    global change_to
    global snake_pos
    global snake_list
    global score

    direction = 'RIGHT'
    change_to = direction
    snake_pos = [100, 50]
    snake_list = [[100, 50], [90, 50], [80, 50]]
    score = 0

    food_x, food_y = random.randrange(0, WIDTH - SNAKE_SIZE, SNAKE_SIZE), random.randrange(0, HEIGHT - SNAKE_SIZE, SNAKE_SIZE)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT and not direction == 'RIGHT':
                    change_to = 'LEFT'
                elif event.key == pg.K_RIGHT and not direction == 'LEFT':
                    change_to = 'RIGHT'
                elif event.key == pg.K_UP and not direction == 'DOWN':
                    change_to = 'UP'
                elif event.key == pg.K_DOWN and not direction == 'UP':
                    change_to = 'DOWN'

        # Change direction
        if change_to == 'LEFT' and not direction == 'RIGHT':
            direction = 'LEFT'
        elif change_to == 'RIGHT' and not direction == 'LEFT':
            direction = 'RIGHT'
        elif change_to == 'UP' and not direction == 'DOWN':
            direction = 'UP'
        elif change_to == 'DOWN' and not direction == 'UP':
            direction = 'DOWN'

        # Move the snake
        if direction == 'UP':
            snake_pos[1] -= SNAKE_SIZE
        elif direction == 'DOWN':
            snake_pos[1] += SNAKE_SIZE
        elif direction == 'LEFT':
            snake_pos[0] -= SNAKE_SIZE
        elif direction == 'RIGHT':
            snake_pos[0] += SNAKE_SIZE

        # Check if the snake has eaten the food
        if snake_pos[0] == food_x and snake_pos[1] == food_y:
            food_x, food_y = random.randrange(0, WIDTH - SNAKE_SIZE, SNAKE_SIZE), random.randrange(0, HEIGHT - SNAKE_SIZE, SNAKE_SIZE)
            score += 10
            snake_list.append([])

        # Check if the snake collided with the screen edges
        if snake_pos[0] < 0 or snake_pos[0] >= WIDTH or snake_pos[1] < 0 or snake_pos[1] >= HEIGHT:
            game_over()

        # Check if the snake collided with itself
        for block in snake_list[1:]:
            if len(block) >= 2 and snake_pos[0] == block[0] and snake_pos[1] == block[1]:
                game_over()


        # Update snake body
        snake_list.insert(0, list(snake_pos))
        if len(snake_list) > score / 10 + 3:  # Adjust snake speed based on score
            snake_list.pop()

        # Drawing the screen
        screen.fill(BLACK)
        pg.draw.rect(screen, RED, [food_x, food_y, SNAKE_SIZE, SNAKE_SIZE])
        snake(SNAKE_SIZE, snake_list)
        show_score(score)

        pg.display.flip()

        # Set the speed of the game
        clock.tick(FPS)

game_loop()

# CONCLUSION :-
"""Implemented the classic Snake game where the player controls a snake that grows longer as it eats food. 
   The game ends if the snake collides with itself or the screen edges."""
