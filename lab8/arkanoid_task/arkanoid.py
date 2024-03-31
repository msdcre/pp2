import pygame
import random

pygame.init()

W, H = 1200, 800
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
bg = (0, 0, 0)

paddleW = 150
paddleH = 25
paddleSpeed = 20
paddleShrinkRate = 0.1
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)

ballRadius = 20
ballSpeed = 6
ballSpeedIncrease = 0.01 
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

collision_sound = pygame.mixer.Sound('catch.mp3')

block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50) for i in range(10) for j in range(5)] 
color_list = [(0, 0, 255) for _ in range(len(block_list))]  

bonus_blocks = random.sample(range(len(block_list) - 10, len(block_list) - 1), 3)

def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    elif delta_x > delta_y:
        dy = -dy
    else:
        dx = -dx
    return dx, dy

def game_over_screen():
    font = pygame.font.SysFont('comicsansms', 60)
    game_over_text = font.render('Game Over', True, (255, 0, 0))
    game_over_rect = game_over_text.get_rect(center=(W // 2, H // 2))
    screen.blit(game_over_text, game_over_rect)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return True

        clock.tick(FPS)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddleSpeed
    if key[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += paddleSpeed

    screen.fill(bg)
    for color, block in zip(color_list, block_list):
        pygame.draw.rect(screen, color, block)
    pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)

    ball.x += ballSpeed * dx
    ball.y += ballSpeed * dy

    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
        dx = -dx
    if ball.centery < ballRadius + 50:
        dy = -dy
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)
    
    hitIndex = ball.collidelist(block_list)
    if hitIndex != -1:
        if hitIndex < len(block_list) - 10:
            hitRect = block_list.pop(hitIndex)
            color_list.pop(hitIndex)
            dx, dy = detect_collision(dx, dy, ball, hitRect)
            game_score += 1
            collision_sound.play()
            if hitIndex in bonus_blocks:
                paddleW += 30
                paddle.width = paddleW
        else:
            dx, dy = detect_collision(dx, dy, ball, block_list[hitIndex])

    if ball.bottom > H:
        if not game_over_screen():
            done = True
        else:
            ball.center = (random.randrange(ball_rect, W - ball_rect), H // 2)
            dx, dy = 1, -1
            game_score = 0
            paddleW = 150
            paddle.width = paddleW
            block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50) for i in range(10) for j in range(5)]
            color_list = [(0, 0, 255) for _ in range(len(block_list))] 
            bonus_blocks = random.sample(range(len(block_list) - 10, len(block_list) - 1), 3)

    game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
    screen.blit(game_score_text, game_score_rect)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()