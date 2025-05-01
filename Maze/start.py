from mazeCreate import MazeeGenerator
from visual import MazeVisualizer
from algorithms import search_algorithm
import time



if __name__ == "__main__":
    maze1 = MazeeGenerator(15,15)
    maze,start, goal, _=maze1.get_maze()

    vis = MazeVisualizer(maze,"maze (A*)", max_window_size=700)
    vis.draw_maze()


    time.sleep(5)
    search= search_algorithm(maze,start, goal,vis)
    # search.bfs()
    search.greedy_best_first()
    # search.a_star()



    vis.wait_for_exit()