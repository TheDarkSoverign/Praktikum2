import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
screen.fill((255, 255, 255))  # белый фон
pygame.display.set_caption('Первая программа в pygame')

# Создание кругов
pygame.draw.circle(screen, 'red', (100, 100), 30, width=0)
pygame.draw.circle(screen, (255, 154, 13), (100, 400), 50, width=15)
pygame.draw.circle(screen, '#FFE54', (300, 100), 100, width=5)

# Создание прямоугольников
pygame.draw.rect(screen, 'yellow', (400, 20, 300, 200), 0)
for i in range(5):
    top = random.randint(50, 700)
    left = random.randint(50, 500)
    w = random.randint(10, 200)
    h = random.randint(10, 200)
    color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    pygame.draw.rect(screen, color, [top, left, w, h], 4)

# Создание домика
house_x = 400  # центр экрана
house_y = 300
house_width = 200
house_height = 150
roof_height = 100

# Основа дома
pygame.draw.rect(screen, 'brown', (house_x - house_width // 2, house_y, house_width, house_height))

# Крыша
roof_points = [(house_x, house_y - roof_height),  # верхушка крыши
               (house_x - house_width // 2, house_y),
               (house_x + house_width // 2, house_y)]
pygame.draw.polygon(screen, 'red', roof_points)

# Окно в доме
pygame.draw.rect(screen, 'blue', (house_x - 30, house_y + 40, 60, 60))
pygame.draw.line(screen, 'black', (house_x, house_y + 40), (house_x, house_y + 100), 2)
pygame.draw.line(screen, 'black', (house_x - 30, house_y + 70), (house_x + 30, house_y + 70), 2)

# Дверь
pygame.draw.rect(screen, 'black', (house_x - 25, house_y + 80, 50, 70))

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
