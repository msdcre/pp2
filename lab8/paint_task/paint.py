import pygame
import sys
import pygame.draw
import pygame.freetype

pygame.init()

screen_width, screen_height = 900, 700
screen = pygame.display.set_mode((screen_width, screen_height))

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
current_color = BLACK

font_size = 24
font = pygame.freetype.SysFont("Arial", font_size)

tool = None
drawing = False  

def draw_text(text, position, color):
    font.render_to(screen, position, text, color)

screen.fill(WHITE)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                tool = 'rectangle'
            elif event.key == pygame.K_c:
                tool = 'circle'
            elif event.key == pygame.K_e:
                tool = 'eraser'
            elif event.key == pygame.K_s:
                current_color = WHITE if current_color == BLACK else BLACK
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                start_pos = event.pos
                if tool in ['rectangle', 'circle']:
                    shape_start = event.pos
        
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
                if tool == 'rectangle':
                    pygame.draw.rect(screen, current_color, pygame.Rect(shape_start, (event.pos[0] - shape_start[0], event.pos[1] - shape_start[1])))
                elif tool == 'circle':
                    radius = int(((event.pos[0] - shape_start[0]) ** 2 + (event.pos[1] - shape_start[1]) ** 2) ** 0.5)
                    pygame.draw.circle(screen, current_color, shape_start, radius)
                pygame.display.flip()
        
        elif event.type == pygame.MOUSEMOTION and drawing:
            if tool == 'eraser':
                pygame.draw.rect(screen, WHITE, pygame.Rect(event.pos[0], event.pos[1], 10, 10))
                pygame.display.flip()

    draw_text("R: Rectangle, C: Circle, E: Eraser, S: Switch Color", (10, 40), BLACK)

    if drawing and tool not in ['rectangle', 'circle', 'eraser']:
        pygame.draw.circle(screen, current_color, event.pos, 5)
        pygame.display.flip()