import pygame
import sys

class MazeVisualizer:
    def __init__(self, maze, name, max_window_size=700):
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])

        # Calculate appropriate cell size
        self.cell_size = min(max_window_size // self.cols, max_window_size // self.rows)
        self.width = self.cols * self.cell_size
        self.height = self.rows * self.cell_size

        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(name)

        self.colors = {
            '#': (0, 0, 0),       # Wall - Black
            ' ': (255, 255, 255), # Path - White
            'S': (0, 255, 0),     # Start - Green
            'G': (255, 0, 0),     # Goal - Red
            '*': (30, 144, 255)   # Solution - Dodger Blue
        }

    def draw_maze(self):
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.maze[row][col]
                color = self.colors.get(cell, (128, 128, 128))
                pygame.draw.rect(self.screen, color, 
                                 (col * self.cell_size, row * self.cell_size, 
                                  self.cell_size, self.cell_size))
        pygame.display.flip()

    def highlight_cell(self, row, col, color):
        pygame.draw.rect(self.screen, color, 
                         (col * self.cell_size, row * self.cell_size, 
                          self.cell_size, self.cell_size))
        pygame.display.flip()

    def wait_for_exit(self, fps=30):
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            clock.tick(fps)
        pygame.quit()
        sys.exit()

