import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Тимчук Никита Викторович')
clock = pygame.time.Clock()

# Начальные координаты и скорости
square_x, square_y, square_dx = 100, 200, 3
rect_x, rect_y, rect_dx = 200, 300, 4
circle_x, circle_y, circle_dx = 300, 400, 2
triangle_x, triangle_y, triangle_dx = 400, 500, 5

# Случайные цвета
square_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
rect_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
circle_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
triangle_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            if square_x <= mx <= square_x + 50 and square_y <= my <= square_y + 50:
                square_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            if rect_x <= mx <= rect_x + 80 and rect_y <= my <= rect_y + 40:
                rect_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            if (mx - circle_x) ** 2 + (my - circle_y) ** 2 <= 30 ** 2:
                circle_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            if triangle_x - 50 <= mx <= triangle_x + 50 and triangle_y - 50 <= my <= triangle_y + 50:
                triangle_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Движение фигур
    square_x += square_dx
    rect_x += rect_dx
    circle_x += circle_dx
    triangle_x += triangle_dx

    # Отражение от границ и смена цвета
    if square_x <= 0 or square_x + 50 >= WIDTH:
        square_dx = -square_dx
        square_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    if rect_x <= 0 or rect_x + 80 >= WIDTH:
        rect_dx = -rect_dx
        rect_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    if circle_x - 30 <= 0 or circle_x + 30 >= WIDTH:
        circle_dx = -circle_dx
        circle_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    if triangle_x - 50 <= 0 or triangle_x + 50 >= WIDTH:
        triangle_dx = -triangle_dx
        triangle_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Отрисовка фигур
    pygame.draw.rect(screen, square_color, (square_x, square_y, 50, 50))
    pygame.draw.rect(screen, rect_color, (rect_x, rect_y, 80, 40))
    pygame.draw.circle(screen, circle_color, (circle_x, circle_y), 30)
    pygame.draw.polygon(screen, triangle_color, [(triangle_x, triangle_y - 50), (triangle_x - 50, triangle_y + 50),
                                                 (triangle_x + 50, triangle_y + 50)])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
