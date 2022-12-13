import sys
import pygame
import os
from random import randint


balls = pygame.sprite.Group() # вместо списка группа спрайтов (пока пустая)
fps = 60
DELTA = 5 # Скорость шариков (можно менять)
COUNT_BALLS = 5 # Количество шариков на поле (можно менять)
SIZE = W, H = 800, 600 # Размер поля (можно менять)


# универсальная функция подгрузки изображения
def load_image(name, colorkey=None):
    # картинки находятся в папке "data"
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f'Файл с изображением "{fullname}" не найден')
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        # Для повышения производительности обычно
        # целесообразно преобразовать изображение
        # в тот же формат пикселей, что и экран.
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        # если изображение содержит прозрачность
        # (альфа-значение указано явно: 0 - 255)
        image = image.convert_alpha()
    return image


# класс шара наследуем от группы спрайтов
class Ball(pygame.sprite.Sprite):
    def __init__(self, mouse_pos):
        # ВАЖНО вызвать конструктор родительского класса Sprite
        pygame.sprite.Sprite.__init__(self)
        self.x = mouse_pos[0]
        self.y = mouse_pos[1]
        # подгружаем в спрайт изображение мяча
        img = load_image("ball.png")
        # приводим к нужному размеру
        self.image = pygame.transform.scale(img, (50, 50))
        # делаем копию для вращения
        self.img_copy = self.image.copy()
        # вычисляем tick на момент создания экземпляра
        self.last_update = pygame.time.get_ticks()
        # угол вращения
        self.angle = 0
        # получаем прямоугольник изображения
        self.rect = self.image.get_rect()
        # центрируем мяч относительно курсора мыши
        self.rect.x = self.x - self.rect.w // 2
        self.rect.y = self.y - self.rect.h // 2
        self.deltaX = DELTA
        self.deltaY = DELTA

    # перемещение, управление прямо в классе  
    def update(self):
        self.rotate() # вращаем в полёте
        self.rect.x -= self.deltaX
        self.rect.y -= self.deltaY
        if self.rect.x <= 0 or self.rect.x + self.rect.w >= W:
            self.deltaX = -self.deltaX
        if self.rect.y <= 0 or self.rect.y + self.rect.h >= H:
            self.deltaY = -self.deltaY

    # вращение
    def rotate(self):
        # текущий tick
        now = pygame.time.get_ticks()
        # на каждую половину tick-ов
        if now - self.last_update > fps // 2:
            # обновляем tick для следующего поворота
            self.last_update = now
            # смещаемся на 1/2 от fps
            self.angle = (self.angle + (fps // 2)) % 360
            # прорисовываем повернутое изображение
            new_image = pygame.transform.rotate(self.img_copy, self.angle)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center
        

pygame.init()
pygame.display.set_caption('Шарики')
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
screen.fill((0, 0, 0))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # создаём экземпляр мяча
            ball = Ball(event.pos)
            # и добавляем его в группу
            balls.add(ball)
    screen.fill((0, 0, 0))
    if len(balls) > COUNT_BALLS:
        balls.remove(ball)
    # вызываем метод update для всей группы
    balls.update()
    # прорисовываем все мячи
    balls.draw(screen)
    # обновляем экран, всё, как обычно
    pygame.display.update()
    clock.tick(fps)
pygame.display.quit()
pygame.quit()
sys.exit()
