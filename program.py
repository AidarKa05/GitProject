import pygame


pygame.init()
w, h = 800, 600
size = (w, h)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Жёлтый круг')
screen.fill((0, 100, 255))

fps = 1
clock = pygame.time.Clock()

running = True
drawing = False
r = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            coord = event.pos
            r = 0
    while r != 1:
        pygame.draw.circle(screen, (255, 255, 0), coord, r)
        pygame.display.flip()
        r += 10
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                r = 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                screen.fill((0, 0, 255))
                pygame.display.flip()
                coord = event.pos
                r = 0
pygame.quit()
