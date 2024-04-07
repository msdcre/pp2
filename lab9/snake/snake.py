import pygame
import sys
import random
import time

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_SIZE = 20
FPS = 10

GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Snake:
    def __init__(self):
        self.body = [(5, 5)]
        self.direction = RIGHT
        self.grow_pending = False  

    def move(self):
        head = self.body[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        self.body.insert(0, new_head)
        if not self.grow_pending:
            self.body.pop() 
        else:
            self.grow_pending = False

    def turn(self, direction):
        if self.direction != (-direction[0], -direction[1]):
            self.direction = direction

    def grow(self):
        self.grow_pending = True 

    def check_collision(self):
        head = self.body[0]
        return head in self.body[1:] or head[0] < 0 or head[0] >= SCREEN_WIDTH // CELL_SIZE or head[1] < 0 or head[
            1] >= SCREEN_HEIGHT // CELL_SIZE

class Food:
    def __init__(self):
        self.position = (
        random.randint(0, SCREEN_WIDTH // CELL_SIZE - 1), random.randint(0, SCREEN_HEIGHT // CELL_SIZE - 1))

    def generate(self, snake):
        while True:
            self.position = (
            random.randint(0, SCREEN_WIDTH // CELL_SIZE - 1), random.randint(0, SCREEN_HEIGHT // CELL_SIZE - 1))
            if self.position not in snake.body:
                break

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

snake = Snake()
food = Food()
score = 0
level = 1
level_threshold = 3
speed = 5
start_time = time.time()
counter = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.turn(UP)
            elif event.key == pygame.K_DOWN:
                snake.turn(DOWN)
            elif event.key == pygame.K_LEFT:
                snake.turn(LEFT)
            elif event.key == pygame.K_RIGHT:
                snake.turn(RIGHT)

    snake.move()

    if snake.check_collision():
        pygame.quit()
        sys.exit()
    if snake.body[0] == food.position:
        snake.grow()
        score += 1
        if score % level_threshold == 0:
            level += 1
            speed += 1
        food.generate(snake)
        counter += 1
        start_time = time.time()
    end_time = time.time()
    if end_time - start_time > 5:  
        food.generate(snake)
        start_time = time.time()
    screen.fill(GREEN)
    for segment in snake.body:
        pygame.draw.rect(screen, BLACK,
                         pygame.Rect(segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    if counter % 3 == 0:
        pygame.draw.rect(screen, RED,
                         pygame.Rect(food.position[0] * 30, food.position[1] * 30, 30, 30))
    else:
        ...
    pygame.draw.rect(screen, RED,
                     pygame.Rect(food.position[0] * CELL_SIZE, food.position[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}  Level: {level}", True, BLACK)
    screen.blit(text, (10, 10))

    pygame.display.flip()

    clock.tick(speed)