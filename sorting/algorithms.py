import time
import heapq

class SortingAlgorithms:

    def __init__(self, data, visualizer):
        self.array = data
        self.visualizer = visualizer

    def selection_sort(self):
        
        arr_copy= self.array.copy()
        for i in range(len(self.array)):
            min_index =  i
            for j in range(i+1, len(arr_copy)):
                if arr_copy[j] < arr_copy[min_index]:
                    min_index=  j
                    
            arr_copy[i],arr_copy[min_index] = arr_copy[min_index], arr_copy[i]

            # just part of animation -->
            self.visualizer.update_array(arr_copy)
            time.sleep(0.5)
        # Animation part ends here <---
        self.visualizer.finish_animation()
        return arr_copy

    def binary_insertion(self):
        arr = []

        for i in range(len(self.array)):
            num = self.array[i]
            if not arr:
                arr.append(num)
                continue

            left = 0
            right = len(arr) - 1
            insert_idx = len(arr)  # Default to insert at the end

            while left <= right:
                mid = (left + right) // 2
                if arr[mid] < num:
                    left = mid + 1
                else:
                    insert_idx = mid
                    right = mid - 1

            arr.insert(insert_idx, num)
            self.visualizer.update_array(arr)
            time.sleep(0.5)
        self.visualizer.finish_animation()
        return arr

        
    def bubble_sort(self):
        # Here is bubble sort Algorithm

        arr = self.array.copy()
        self.visualizer.update_array(arr)
        changed = True
        
        while changed:
            changed= False
            pass_num = 0
            for i in range(len(arr)-1 - pass_num):
                a,b = self.array[i], self.array[i+1]

                if a>b:
                    arr[i], arr[i+1] = b,a
                    self.visualizer.update_array(arr)
                    time.sleep(0.01)
                    changed = True
            pass_num += 1
        
        self.visualizer.finish_animation()

    def merge_sort(self):
        pass

    def quick_sort(self):
        pass
   

    def heap_sort(self):
        arr= self.array
        n = len(arr)
        heapq.heapify(arr)

        res = [0] * n

        for i in range(n):
            min = heapq.hippop(arr)
            arr[i] = min

    return res
            

    def radix_sort(self):
        pass
            

        


            



if __name__ == "__main__":

    sorting = SortingAlgorithms([1,23,6,2,7,256,4,7])
    print(sorting.selection_sort())
            
            
            
            