import random
from visual import Visualizer
from algorithms import SortingAlgorithms
vis = Visualizer()

# Initial array

arr = [random.randint(1, 1000) for _ in range(50)]

vis.update_array(arr)

# Change values after some delay
import time
time.sleep(2)

sorting = SortingAlgorithms(arr, vis)

# sorting.selection_sort()
sorting.binary_insertion()

# Keep window open
vis.run_forever()


# import time
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
# import numpy as np


# class ArrayVisualizer:
#     """Visualizer for sorting algorithms using matplotlib animations."""
    
#     def __init__(self, data, algorithm_name="Sorting Algorithm"):
#         self.data = data.copy()
#         self.algorithm_name = algorithm_name
        
#         # Set up the figure and axis
#         plt.style.use('seaborn-v0_8-darkgrid')
#         self.fig, self.ax = plt.subplots(figsize=(12, 6))
#         self.fig.canvas.manager.set_window_title(f"{algorithm_name} Visualization")
        
#         # Initial bar colors (blue for unsorted)
#         self.colors = ['#3498db'] * len(data)
        
#         # Create the initial bar chart
#         self.bars = self.ax.bar(range(len(data)), data, color=self.colors, alpha=0.8, edgecolor='black')
        
#         # Add labels and title
#         self.ax.set_xlabel('Index')
#         self.ax.set_ylabel('Value')
#         self.title = self.ax.set_title(f"{self.algorithm_name}: Unsorted Array", fontsize=14)
        
#         # Add text annotation for steps
#         self.step_text = self.ax.text(0.02, 0.95, "Step: 0", transform=self.ax.transAxes, 
#                                      fontsize=12, verticalalignment='top')
        
#         # Add text for current operation
#         self.operation_text = self.ax.text(0.02, 0.90, "", transform=self.ax.transAxes,
#                                          fontsize=12, verticalalignment='top')
        
#         # Counter for steps
#         self.step_count = 0
        
#         # Adjust axis limits
#         self.ax.set_xlim(-0.5, len(data) - 0.5)
#         max_val = max(data) * 1.1
#         self.ax.set_ylim(0, max_val)
        
#         # Show the initial state
#         plt.tight_layout()
#         plt.ion()  # Turn on interactive mode
#         plt.show(block=False)
#         self.fig.canvas.draw()
        
#     def update_array(self, array, current_index=None, comparison_index=None, swapped=False):
#         """Update the visualization with current state of the array."""
#         # Update step count
#         self.step_count += 1
        
#         # Reset colors
#         self.colors = ['#3498db'] * len(array)
        
#         # Color current index (the one we're trying to place) in red
#         if current_index is not None:
#             self.colors[current_index] = '#e74c3c'  # Red
            
#         # Color comparison index in yellow
#         if comparison_index is not None:
#             self.colors[comparison_index] = '#f1c40f'  # Yellow
            
#         # Color already sorted elements in green
#         for i in range(current_index if current_index is not None else 0):
#             self.colors[i] = '#2ecc71'  # Green
            
#         # Update operation text
#         if current_index is not None and comparison_index is not None:
#             if swapped:
#                 op_text = f"Swapping elements at indices {current_index} and {comparison_index}"
#             else:
#                 op_text = f"Comparing elements at indices {current_index} and {comparison_index}"
#             self.operation_text.set_text(op_text)
        
#         # Update the bars with new data and colors
#         for bar, height, color in zip(self.bars, array, self.colors):
#             bar.set_height(height)
#             bar.set_color(color)
            
#         # Update step text
#         self.step_text.set_text(f"Step: {self.step_count}")
        
#         # Update title
#         if current_index is not None and current_index == len(array) - 1:
#             self.title.set_text(f"{self.algorithm_name}: Sorting Complete!")
#         else:
#             self.title.set_text(f"{self.algorithm_name}: In Progress")
            
#         # Redraw the figure
#         self.fig.canvas.draw()
#         plt.pause(0.5)  # Pause to show the current state
        
#     def finish_animation(self):
#         """Final state of the visualization."""
#         # Color all bars green to indicate sorting is complete
#         for bar in self.bars:
#             bar.set_color('#2ecc71')
            
#         self.title.set_text(f"{self.algorithm_name}: Sorting Complete!")
#         self.operation_text.set_text("Array is now sorted!")
        
#         # Redraw the figure
#         self.fig.canvas.draw()
#         plt.pause(2)  # Give some time to see the final state
        
#         # Keep the plot open until closed by user if running in interactive mode
#         if plt.isinteractive():
#             plt.ioff()
#             plt.show()


# class SortingAlgorithms:
#     def __init__(self, data, visualizer=None):
#         self.array = data
#         self.visualizer = visualizer
    
#     def selection_sort(self):
#         """Selection sort with enhanced visualization."""
#         arr_copy = self.array.copy()
#         n = len(arr_copy)
        
#         for i in range(n):
#             # Find the minimum element in the unsorted part
#             min_index = i
            
#             # Initial visualization for this step
#             if self.visualizer:
#                 self.visualizer.update_array(arr_copy, current_index=i)
                
#             for j in range(i + 1, n):
#                 # Show comparison
#                 if self.visualizer:
#                     self.visualizer.update_array(arr_copy, current_index=i, comparison_index=j)
                
#                 if arr_copy[j] < arr_copy[min_index]:
#                     min_index = j
#                     # Show new minimum found
#                     if self.visualizer:
#                         self.visualizer.update_array(arr_copy, current_index=i, comparison_index=min_index)
            
#             # Swap elements if needed
#             if min_index != i:
#                 if self.visualizer:
#                     # Show before swap
#                     self.visualizer.update_array(arr_copy, current_index=i, comparison_index=min_index, swapped=True)
                    
#                 # Perform swap
#                 arr_copy[i], arr_copy[min_index] = arr_copy[min_index], arr_copy[i]
                
#                 # Show after swap
#                 if self.visualizer:
#                     self.visualizer.update_array(arr_copy, current_index=i)
            
#         # Finish animation when sorting is complete
#         if self.visualizer:
#             self.visualizer.finish_animation()
            
#         return arr_copy
    
#     def bubble_sort(self):
#         """Bubble sort with visualization."""
#         arr_copy = self.array.copy()
#         n = len(arr_copy)
        
#         for i in range(n):
#             swapped = False
            
#             for j in range(0, n - i - 1):
#                 # Show comparison
#                 if self.visualizer:
#                     self.visualizer.update_array(arr_copy, current_index=j, comparison_index=j+1)
                
#                 if arr_copy[j] > arr_copy[j + 1]:
#                     # Show swap
#                     if self.visualizer:
#                         self.visualizer.update_array(arr_copy, current_index=j, comparison_index=j+1, swapped=True)
                        
#                     # Perform swap
#                     arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
#                     swapped = True
                    
#                     # Show after swap
#                     if self.visualizer:
#                         self.visualizer.update_array(arr_copy, current_index=j+1)
            
#             # If no swap occurred in this pass, array is sorted
#             if not swapped:
#                 break
                
#         # Finish animation
#         if self.visualizer:
#             self.visualizer.finish_animation()
            
#         return arr_copy
    
#     def insertion_sort(self):
#         """Insertion sort with visualization."""
#         arr_copy = self.array.copy()
#         n = len(arr_copy)
        
#         for i in range(1, n):
#             key = arr_copy[i]
#             j = i - 1
            
#             # Show element to insert
#             if self.visualizer:
#                 self.visualizer.update_array(arr_copy, current_index=i)
            
#             while j >= 0 and arr_copy[j] > key:
#                 # Show comparison
#                 if self.visualizer:
#                     self.visualizer.update_array(arr_copy, current_index=i, comparison_index=j)
                
#                 # Move elements one position ahead
#                 arr_copy[j + 1] = arr_copy[j]
#                 j -= 1
                
#                 # Show movement
#                 if self.visualizer:
#                     arr_copy[j + 1] = key  # Temporarily place key for visualization
#                     self.visualizer.update_array(arr_copy, current_index=j+1)
#                     arr_copy[j + 1] = arr_copy[j]  # Restore for correct algorithm operation
            
#             # Place the key in its correct position
#             arr_copy[j + 1] = key
            
#             # Show after insertion
#             if self.visualizer:
#                 self.visualizer.update_array(arr_copy, current_index=j+1)
                
#         # Finish animation
#         if self.visualizer:
#             self.visualizer.finish_animation()
            
#         return arr_copy


# if __name__ == "__main__":
#     # Example data with more variation to better visualize the sorting
#     data = [42, 23, 74, 11, 65, 58, 94, 36, 99, 87]
    
#     # Create visualizer
#     visualizer = ArrayVisualizer(data, "Selection Sort")
    
#     # Create sorting instance
#     sorting = SortingAlgorithms(data, visualizer)
    
#     # Run the sorting algorithm (uncomment the one you want to use)
#     sorted_array = sorting.selection_sort()
#     # sorted_array = sorting.bubble_sort()
#     # sorted_array = sorting.insertion_sort()
    
#     print("Original array:", data)
#     print("Sorted array:", sorted_array)