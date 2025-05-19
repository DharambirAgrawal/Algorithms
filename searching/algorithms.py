

class Searching:
    def __init__(self,data, visualizer):
        self.array = data

    def traditional_binary_search(self,target):

        """
        M = (L+R) // 2  
        or
        M = L + (R-L) // 2  --> prevents overflow
        """


