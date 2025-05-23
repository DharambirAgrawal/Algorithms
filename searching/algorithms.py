

class Searching:
    def __init__(self,data, visualizer):
        self.array = data

    def traditional_binary_search(self,target):

        """
        M = (L+R) // 2  
        or
        M = L + (R-L) // 2  --> prevents overflow
        """
        arr = self.array[:].sort()
        

        def binary_search(arr, target):
            L = 0
            R = len(arr) - 1

            while R >= L:
                M = L + (R-L) // 2
                if arr[M] == target:
                    return True
                
                elif arr[M] < target:
                    L = M + 1
                else:
                    R = M - 1
            return False



    def conditional_binary_search(self,target):
        """
                 | searching this point of change
                 V
        [T,T,T,T,F,F,F]
        """


