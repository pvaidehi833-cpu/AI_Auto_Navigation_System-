import pygame
from path_planning import astar

WIDTH = 600
ROWS = 20

class Simulation:
    def __init__(self):
        pygame.init()
        self.win = pygame.display.set_mode((WIDTH, WIDTH))
        pygame.display.set_caption("Autonomous Navigation")

        self.grid = [[0 for _ in range(ROWS)] for _ in range(ROWS)]

        self.start = (2, 2)
        self.end = (18, 18)

        self.path = astar(self.grid, self.start, self.end)

    def draw(self):
        gap = WIDTH // ROWS
        for i in range(ROWS):
            for j in range(ROWS):
                rect = pygame.Rect(j*gap, i*gap, gap, gap)

                if self.grid[i][j] == 1:
                    pygame.draw.rect(self.win, (0,0,0), rect)
                elif (i,j) == self.start:
                    pygame.draw.rect(self.win, (0,255,0), rect)
                elif (i,j) == self.end:
                    pygame.draw.rect(self.win, (255,0,0), rect)
                elif (i,j) in self.path:
                    pygame.draw.rect(self.win, (0,0,255), rect)
                else:
                    pygame.draw.rect(self.win, (255,255,255), rect)

    def run(self):
        run = True
        clock = pygame.time.Clock()

        path_index = 0
        current_pos = self.start

        while run:
            clock.tick(5)

            self.win.fill((255,255,255))

            # 🖱️ Mouse se obstacle draw
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                gap = WIDTH // ROWS
                row = pos[1] // gap
                col = pos[0] // gap

                if (row, col) != self.start and (row, col) != self.end:
                    self.grid[row][col] = 1

            # 🔁 Path update
            self.path = astar(self.grid, self.start, self.end)

            self.draw()

            # 🤖 Robot movement
            if path_index < len(self.path):
                current_pos = self.path[path_index]
                path_index += 1

            gap = WIDTH // ROWS
            rect = pygame.Rect(current_pos[1]*gap, current_pos[0]*gap, gap, gap)
            pygame.draw.rect(self.win, (255, 165, 0), rect)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

        pygame.quit()