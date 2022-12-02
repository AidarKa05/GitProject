import pygame

white = (255, 255, 255)
lw = 1


class Board:
    def __init__(self, width, height):
        self.w = width
        self.h = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 50

    def set_view(self, left, top, sell_size):
        self.left = left
        self.top = top
        self.cell_size = sell_size

    def render(self, screen):
        for i in range(self.h):
            for j in range(self.w):
                if self.board[i][j] == 0:
                    pygame.draw.rect(screen, white, (self.left + self.cell_size * j, self.top + self.cell_size * i,
                                                     self.cell_size, self.cell_size), lw)
                else:
                    pygame.draw.rect(screen, white, (self.left + self.cell_size * j, self.top + self.cell_size * i,
                                                     self.cell_size, self.cell_size))

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def on_click(self, cell_coords):
        x = cell_coords[0]
        y = cell_coords[1]
        if x == -1 or y == -1:
            return
        if self.board[y][x] == 1:
            self.board[y][x] = 0
        else:
            self.board[y][x] = 1

    def get_cell(self, mouse_pos):
        x = (mouse_pos[0] - self.left) // self.cell_size
        y = (mouse_pos[1] - self.top) // self.cell_size
        if mouse_pos[0] < self.left or mouse_pos[0] > self.w * self.cell_size + self.left:
            x = -1
        if mouse_pos[1] < self.top or mouse_pos[1] > self.h * self.cell_size + self.top:
            y = -1
        # print(f'({x}, {y})')
        # if x < 0 or y < 0:
        # print('None')
        return x, y


if __name__ == '__main__':
    pygame.init()
    size = width, height = 500, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Координаты клетки")

    board = Board(5, 7)
    board.set_view(80, 80, 50)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)

        screen.fill((0, 0, 0))
        board.render(screen)

        pygame.display.flip()
    pygame.quit()
