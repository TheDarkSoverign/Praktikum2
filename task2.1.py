import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
screen.fill((255, 255, 255))  # белый фон
pygame.display.set_caption('Тимчук Никита Викторович')

# Создание кругов
pygame.draw.circle(screen, 'red', (100, 100), 30, width=0)
pygame.draw.circle(screen, (255, 154, 13), (100, 400), 50, width=15)
pygame.draw.circle(screen, '#FFEE54', (300, 100), 100, width=5)

# Создание прямоугольников
pygame.draw.rect(screen, 'yellow', (400, 20, 300, 200), 0)
for i in range(5):
    top = random.randint(50, 700)
    left = random.randint(50, 500)
    w = random.randint(10, 200)
    h = random.randint(10, 200)
    color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    pygame.draw.rect(screen, color, [top, left, w, h], 4)

# Создание произвольной фигуры из линий
dots = [[221, 432], [225, 331], [133, 342], [141, 310],
        [51, 230], [74, 217], [58, 153], [114, 164],
        [230, 287], [249, 193], [301, 193],
        [320, 281], [351, 190], [301, 177], [248, 190],
        [473, 432], [497, 386], [386, 217],
        [337, 310], [327, 342], [233, 331]]
pygame.draw.lines(screen, 'green', True, dots, 2)

# Загрузка и отображение изображения яблока
apple = pygame.image.load('apple.png')
screen.blit(apple, (400, 450))
pygame.display.flip()

# Перемещение изображения яблока
pygame.time.delay(2000)
pygame.draw.rect(screen, 'white', (400, 450, 100, 100))
screen.blit(apple, (600, 450))

# Создание домика из линий
house_x = 400  # центр экрана
house_y = 300
house_width = 200
house_height = 150
roof_height = 100

# Основа дома
pygame.draw.line(screen, 'black', (house_x - house_width // 2, house_y), (house_x - house_width // 2, house_y + house_height), 2)
pygame.draw.line(screen, 'black', (house_x + house_width // 2, house_y), (house_x + house_width // 2, house_y + house_height), 2)
pygame.draw.line(screen, 'black', (house_x - house_width // 2, house_y + house_height), (house_x + house_width // 2, house_y + house_height), 2)
pygame.draw.line(screen, 'black', (house_x - house_width // 2, house_y), (house_x + house_width // 2, house_y), 2)

# Крыша
pygame.draw.line(screen, 'black', (house_x, house_y - roof_height), (house_x - house_width // 2, house_y), 2)
pygame.draw.line(screen, 'black', (house_x, house_y - roof_height), (house_x + house_width // 2, house_y), 2)

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
