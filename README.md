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

## Sorting Algorithms

The sorting directory contains implementations of various sorting algorithms with visual representation.

### Features

- **Interactive Visualization**: Watch the sorting process in real-time with animated bars
- **Multiple Algorithms**:
  - **Selection Sort**: Repeatedly selects the smallest element from the unsorted portion
  - **Binary Insertion**: Uses binary search to find the insertion position, making it more efficient
  - **Bubble Sort**: Repeatedly steps through the list, compares adjacent elements, and swaps them if needed
  - **Merge Sort**: Divides the array into smaller subarrays, sorts, and merges them
  - **Quick Sort**: Picks a pivot element and partitions the array around the pivot
  - **Heap Sort**: Uses a binary heap data structure for efficient sorting
  - **Counting Sort**: Non-comparison based sorting algorithm for positive integers

### How to Run

```bash
cd sorting
python run.py
```

You can choose which sorting algorithm to run by uncommenting the relevant line in run.py:

```python
# sorting.selection_sort()
sorting.binary_insertion()
# sorting.bubble_sort()
# sorting.merge_sort()
```

### Project Structure

- visual.py: Handles the visualization using pygame
- algorithms.py: Contains sorting algorithm implementations
- run.py: Entry point to run the application

### Visualization

- Bar heights represent the values in the array
- Smooth animations show the movement of elements during sorting
- Color transitions indicate comparisons and swaps
- Final green color indicates that sorting is complete

## Searching Algorithms

The searching directory contains implementations of various search algorithms.

### Features

- **Traditional Binary Search**: Efficiently finds elements in a sorted array
- **Conditional Binary Search**: Finds the point of change in a boolean array

## Reinforcement Learning

The repository also includes an implementation of Deep Q-Learning for reinforcement learning.

### Features

- **Deep Q-Network (DQN)**: Implementation using TensorFlow and Keras
- **Experience Replay**: Uses a memory buffer to store and sample past experiences
- **CartPole Environment**: Trains an agent to balance a pole on a moving cart

### How to Run

```bash
cd test
python deepreinforcement.py
```

### Implementation Details

- **Neural Network**: A simple feed-forward network with two hidden layers
- **Exploration Strategy**: Epsilon-greedy policy with decay
- **Training Process**: Collects experiences and learns from batches
- **Testing**: Visualizes the trained agent's performance

## Upcoming Additions

- Graph algorithms
- Dynamic programming examples
- Neural network implementations
- And more...