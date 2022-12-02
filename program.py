import pygame

WHITE = (255, 255, 255)
LW = 1


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == 0:
                    pygame.draw.rect(screen, WHITE, (self.left + self.cell_size * j, self.top + self.cell_size * i,
                                                     self.cell_size, self.cell_size), LW)
                else:
                    pygame.draw.rect(screen, WHITE, (self.left + self.cell_size * j, self.top + self.cell_size * i,
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
        # print(mouse_pos[0], mouse_pos[1])
        if mouse_pos[0] < self.left or mouse_pos[0] > self.width * self.cell_size + self.left:
            x = -1
        if mouse_pos[1] < self.top or mouse_pos[1] > self.height * self.cell_size + self.top:
            y = -1
        # print(x, y)
        return x, y

# реализация класса Board
if __name__ == '__main__':
    pygame.init()
    size = width, height = 400, 400 # окно 400 х 400
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Клетки")


    board = Board(8, 8) # доска 8 х 8, можно и другие значения
    # положение левого верхнего угла X = 0, Y = 0
    # размеры клетки 50 х 50
    board.set_view(0, 0, 50) 

    running = True
    while running:
        # внутри игрового цикла ещё один цикл
        # приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)

        screen.fill((0, 0, 0))
        board.render(screen)

        pygame.display.flip()
    pygame.quit()
