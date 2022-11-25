import pygame


pygame.init()
a, n = [int(el) for el in input().split()]
if a % n == 0:
    width = a / n
    size = (a, a)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Шахматная клетка')
    screen.fill((0, 0, 0))
    for x in range(n):
        for y in range(n):
            if x % 2 == 0 and y % 2 == 0:
                screen.fill((255, 255, 255), pygame.Rect(x * width, y * width, x * width + width, y * width + width))

    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.flip()

    pygame.quit()
else:
    print('Неправильный формат ввода')
