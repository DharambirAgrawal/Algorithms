
import random

class MazeeGenerator:

    def __init__(self, rows, cols, add_loops=True, loop_chance=0.1):
        self.rows = rows
        self.cols = cols
        self.grid = [[{'N': True, 'E': True, 'S': True, 'W': True, 'visited': False} for _ in range(cols)] for _ in range(rows)]
        self.DIRS = {
            'N': (-1, 0, 'S'),
            'S': (1, 0, 'N'),
            'E': (0, 1, 'W'),
            'W': (0, -1, 'E')
        }
        self.generate_maze_prims()
        if add_loops:
            self.add_random_loops(chance=loop_chance)

    def generate_maze_prims(self):
        frontier = []
        start_y, start_x = random.randint(0, self.rows - 1), random.randint(0, self.cols - 1)
        self.grid[start_y][start_x]['visited'] = True

        def add_frontiers(y, x):
            for direction, (dy, dx, _) in self.DIRS.items():
                ny, nx = y + dy, x + dx
                if 0 <= ny < self.rows and 0 <= nx < self.cols and not self.grid[ny][nx]['visited']:
                    frontier.append((ny, nx, y, x))

        add_frontiers(start_y, start_x)

        while frontier:
            idx = random.randint(0, len(frontier) - 1)
            y, x, py, px = frontier.pop(idx)

            if not self.grid[y][x]['visited']:
                direction = None
                for dir, (dy, dx, opposite) in self.DIRS.items():
                    if y - dy == py and x - dx == px:
                        direction = dir
                        break

                if direction:
                    self.grid[y][x]['visited'] = True
                    self.grid[y][x][self.DIRS[direction][2]] = False
                    self.grid[py][px][direction] = False
                    add_frontiers(y, x)

    def add_random_loops(self, chance=0.1):
        for y in range(self.rows):
            for x in range(self.cols):
                for direction, (dy, dx, opposite) in self.DIRS.items():
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < self.rows and 0 <= nx < self.cols and self.grid[ny][nx]['visited']:
                        if self.grid[y][x][direction] and random.random() < chance:
                            self.grid[y][x][direction] = False
                            self.grid[ny][nx][opposite] = False

    def get_maze(self):
        maze_height = self.rows * 2 + 1
        maze_width = self.cols * 2 + 1
        maze_map = [['#' for _ in range(maze_width)] for _ in range(maze_height)]

        for y in range(self.rows):
            for x in range(self.cols):
                cx, cy = x * 2 + 1, y * 2 + 1
                maze_map[cy][cx] = ' '
                if not self.grid[y][x]['N']:
                    maze_map[cy - 1][cx] = ' '
                if not self.grid[y][x]['S']:
                    maze_map[cy + 1][cx] = ' '
                if not self.grid[y][x]['E']:
                    maze_map[cy][cx + 1] = ' '
                if not self.grid[y][x]['W']:
                    maze_map[cy][cx - 1] = ' '

        start = (1, 1)
        goal = (maze_height - 2, maze_width - 2)
        maze_map[start[0]][start[1]] = 'S'
        maze_map[goal[0]][goal[1]] = 'G'
        return maze_map, start, goal, (self.rows, self.cols)

    def __repr__(self):
        maze, _, _, _ = self.get_maze()
        for row in maze:
            print(''.join(row))
        return ''

# Example usage:
if __name__ == "__main__":
    maze = HardMazeGenerator(20, 40, add_loops=True, loop_chance=0.15)
    print(maze)
