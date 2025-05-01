import time
import pygame

class search_algorithm:

    def __init__(self,maze,start, goal,vis):
        self.maze = maze
        self.start = start
        self.goal = goal
        self.vis = vis
        self.rows = len(maze)
        self.cols = len(maze[0])

        x, y = self.goal
        self.heuristic = [[(abs(x - i) + abs(y - j)) for i in range(self.rows)] for j in range(self.cols)]

    def dfs(self):
        stack = [[self.start]]  # stack stores paths
        visited = set()

        while stack:
            pygame.event.pump() 
            path = stack.pop()
            current = path[-1]

            if current == self.goal:
                print("Goal found!")
                # mark the path on the maze
                for r, c in path:
                    if self.maze[r][c] == ' ':
                        self.maze[r][c] = '*'
                        self.vis.highlight_cell(r, c, (200, 200, 0))
                self.vis.highlight_cell(self.goal[0], self.goal[1],(200, 200, 0))
                pygame.time.delay(50)
                return self.maze

            if current in visited:
                continue
            visited.add(current)

            row, col = current
            self.vis.highlight_cell(row, col, (30, 144, 255))
            pygame.time.delay(50)
            time.sleep(0.1)

            # 4 directions
            for dr, dc in [(0,1), (1,0), (-1,0), (0,-1)]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < self.rows and 0 <= nc < self.cols:
                    if self.maze[nr][nc] != '#' and (nr, nc) not in visited:
                        stack.append(path + [(nr, nc)])

        print("No path found.")
        return self.maze
        
    def bfs(self):
        queue = [[self.start]]  # stack stores paths
        visited = set()

        while queue:
            pygame.event.pump()
            path = queue.pop(0)
            current = path[-1]

            if current == self.goal:
                print("Goal found!")
                # mark the path on the maze
                for r, c in path:
                    if self.maze[r][c] == ' ':
                        self.maze[r][c] = '*'
                        self.vis.highlight_cell(r, c, (0, 255, 0))
                self.vis.highlight_cell(self.goal[0], self.goal[1], (0, 255, 0))
                # pygame.time.delay(50)
               
                return self.maze

            if current in visited:
                continue
            visited.add(current)

            row, col = current
            self.vis.highlight_cell(row, col, (30, 144, 255))
            pygame.time.delay(50)
            time.sleep(0.1)

            # 4 directions
            for dr, dc in [(0,1), (1,0), (-1,0), (0,-1)]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < self.rows and 0 <= nc < self.cols:
                    if self.maze[nr][nc] != '#' and (nr, nc) not in visited:
                        queue.append(path + [(nr, nc)])
                        
                        

        print("No path found.")
        return self.maze


    def greedy_best_first(self):
        start_x, start_y = self.start
        visited= set()
        dequeue = [[self.heuristic[start_x][start_y],[self.start] ]]
        
        while dequeue:
            min_index = min(range(len(dequeue)), key=lambda i: dequeue[i][0])

            path = dequeue.pop(min_index)
            current =path[1][-1]

            
            if current == self.goal:
                print("Goal found!")
                
                for r,c in path[1]:
                    if self.maze[r][c] != '#':
                        self.maze[r][c] = '*'
                        self.vis.highlight_cell(r, c, (0, 255, 0))
                pygame.time.delay(50)
                return self.maze
            
            if current in visited:
                continue
            visited.add(current)
    
            row, col = current
            self.vis.highlight_cell(row, col, (30, 144, 255))
            time.sleep(0.1)
            pygame.time.delay(50)
            
            for dr, dc in [(1,0), (0,1), (-1,0), (0,-1)]:
                nr, nc = dr + row, dc + col
                
                if 0 <= nr < self.rows and 0 <= nc < self.cols:
                    if self.maze[nr][nc] != "#":
                        dequeue.append([self.heuristic[nr][nc],path[1]+ [(nr, nc)]])
                        
        
        print("No path found")
        return self.maze

    def a_star(self):
        start_x, start_y = self.start
        visited= set()
        dequeue = [[self.heuristic[start_x][start_y],[self.start] ]]
        cost_so_far = {self.start: 0}
        
        while dequeue:
            min_index = min(range(len(dequeue)), key=lambda i: dequeue[i][0])

            path = dequeue.pop(min_index)
            current =path[1][-1]

            
            if current == self.goal:
                print("Goal found!")
                
                for r,c in path[1]:
                    if self.maze[r][c] != '#':
                        self.maze[r][c] = '*'
                        self.vis.highlight_cell(r, c, (0, 255, 0))
                pygame.time.delay(50)
                return self.maze
            
            if current in visited:
                continue
            visited.add(current)
    
            row, col = current
            self.vis.highlight_cell(row, col, (30, 144, 255))
            time.sleep(0.1)
            pygame.time.delay(50)
            
            for dr, dc in [(1,0), (0,1), (-1,0), (0,-1)]:
                nr, nc = dr + row, dc + col
                
                if 0 <= nr < self.rows and 0 <= nc < self.cols and self.maze[nr][nc] != "#":
                    
                    # basically the cost we are adding for the path to 1
                    new_cost = cost_so_far[current] + 1
                    if (nr, nc) not in cost_so_far or new_cost < cost_so_far[(nr, nc)]:
                        cost_so_far[(nr, nc)] = new_cost
                        priority = new_cost + self.heuristic[nr][nc]  
                        dequeue.append([priority, path[1] + [(nr, nc)]])

                    # dequeue.append([self.heuristic[nr][nc] ,path[1]+ [(nr, nc)]])
                        
        
        print("No path found")
        return self.maze
                      
          


        
