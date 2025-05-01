This repository contains implementations of various algorithms. Currently, it includes:

## Maze Algorithms

The Maze directory contains a complete set of maze generation and solving algorithms with visualization.

### Features

- **Maze Generation**: Using Prim's algorithm with optional loop addition
- **Path Finding Algorithms**:
  - **BFS** (Breadth-First Search): Explores all nodes at the present depth before moving to nodes at the next depth level
  - **DFS** (Depth-First Search): Explores as far as possible along each branch before backtracking
  - **Greedy Best-First Search**: Uses a heuristic to always choose the path that appears best
  - **A\* Search**: Combines the strengths of Dijkstra's algorithm and Greedy Best-First Search

### How to Run

```bash
cd Maze
python start.py
```

You can modify start.py to choose which path-finding algorithm to use by uncommenting the relevant line:

```python
# search.bfs()
search.greedy_best_first()  # Currently active
# search.a_star()
# search.dfs()
```

### Project Structure

- mazeCreate.py: Implements maze generation using Prim's algorithm
- algorithms.py: Contains all path-finding algorithms (BFS, DFS, Greedy Best-First, A*)
- visual.py: Handles visualization using pygame
- start.py: Entry point to run the application

### Visualization

The program provides a visual representation of:
- Maze structure with walls, paths, start, and goal points
- Algorithm exploration process with blue cells showing explored areas
- Final path found marked in green or yellow (depending on the algorithm)

## Upcoming Additions

- Sorting algorithms
- Graph algorithms
- Dynamic programming examples
- And more...