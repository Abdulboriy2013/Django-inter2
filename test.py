import pygame
import random
import time

# O'yin o'lchamlarini belgilash
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Ranglar
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Pygame ni ishga tushirish
pygame.init()

# Ekran va o'yin nomini yaratish
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Car Racing Game")

# Avtomobilni yaratish
car_width = 50
car_height = 100
car_image = pygame.image.load('car.png')  # Bu yerda o'z avtotransport rasmi kerak
car_image = pygame.transform.scale(car_image, (car_width, car_height))

# To'siqlarni yaratish
block_width = 70
block_height = 70

# O'yin tugmasi
clock = pygame.time.Clock()
game_over = False

# Avtomobilni ekranda harakatlantirish funksiyasi
def car(x, y):
    screen.blit(car_image, (x, y))

# To'siqni yaratish
def draw_block(block_x, block_y):
    pygame.draw.rect(screen, RED, [block_x, block_y, block_width, block_height])

# O'yin holati
def game_loop():
    x = SCREEN_WIDTH // 2 - car_width // 2
    y = SCREEN_HEIGHT - car_height - 10
    x_change = 0
    y_change = 0
    block_x = random.randint(0, SCREEN_WIDTH - block_width)
    block_y = -block_height
    block_speed = 7
    score = 0

    global game_over

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        if x < 0:
            x = 0
        elif x > SCREEN_WIDTH - car_width:
            x = SCREEN_WIDTH - car_width

        # To'siqni harakatlantirish
        block_y += block_speed
        if block_y > SCREEN_HEIGHT:
            block_y = -block_height
            block_x = random.randint(0, SCREEN_WIDTH - block_width)
            score += 1

        # To'siq va avtomobilning to'qnashishini tekshirish
        if y < block_y + block_height and y + car_height > block_y:
            if x + car_width > block_x and x < block_x + block_width:
                game_over = True

        # Ekranni tozalash
        screen.fill(WHITE)

        # Avtomobilni va to'siqni chizish
        car(x, y)
        draw_block(block_x, block_y)

        # O'yin ballini ko'rsatish
        font = pygame.font.SysFont("comicsansms", 30)
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, [10, 10])

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

# O'yinni boshlash
game_loop()
