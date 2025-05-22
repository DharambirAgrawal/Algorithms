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

        def recursive(arr):
            n = len(arr)

            if n <= 1:
                return arr
            m = n // 2

            L = arr[:m]
            R = arr[m:]

            L = recursive(L)
            R = recursive(R)

            l , r = 0,0 
            res = []

            while  l < len(L) and r < len(R):

                if L[l] < R[r]:
                    res.append(L[l])
                    l = l+1
                else:
                    res.append(R[r])
                    r = r+1
            
            res.extend(L[l:])
            res.extend(R[r:])
            return res

        
        

    def quick_sort(arr):
        n = len(arr)
        
        if n <= 1:
            return arr
            
        piv = arr[-1]
        
        L = [arr[i] for i in range(len(arr)-1) if arr[i] <= piv]
        
        R = [arr[i] for i in range(len(arr)-1) if arr[i] > piv]
        
    
        
        L = quick_sort(L)
        R = quick_sort(R)
        
        return L + [piv] + R
    
   

    def heap_sort(self):
        arr= self.array
        n = len(arr)
        heapq.heapify(arr)

        res = [0] * n

        for i in range(n):
            min = heapq.hippop(arr)
            arr[i] = min

    return res
            

    def counting_sort_positive(self):
        # only for positive number
        
        maxx = max(self.array)

        counts = [0] * (maxx+1)
        res = []
        for i in self.array:
            counts[i] = counts[i] +1

        for i in range(len(counts):
            res = res + [i] * counts[i]

        return res

    def counting_sort(self):
        arr = self.array
        maxx = max(arr)
        minn = min(arr)
        res = []

        if minn < 0:
            maxx = maxx - minn
        
        counts = [0] * (maxx + 1)

        for val in arr:
            counts[val-minn] += 1 
        
        for i in range(len(counts)):
            res = res + [i + minn] * counts[i]

        return res

# radix_sort(A)
            

        


            



if __name__ == "__main__":

    sorting = SortingAlgorithms([1,23,6,2,7,256,4,7])
    print(sorting.selection_sort())
            
            
            
            