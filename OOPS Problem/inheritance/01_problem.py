# Create a class (2-D vector) and use it to create another class representing a 3-D vector.

class TwoDVector:
    def __init__(self,i,j):
        self.i = i
        self.j = j
        print(f"This is 2D vector {self.i}i + {self.j}j")

class ThreeDVector(TwoDVector):
    def __init__(self,k):
        super().__init__(5,6)
        self.k = k
        print(f"This is 2D vector {self.i}i + {self.j}j + {self.k}k")
    
d2 = TwoDVector(2,3)
d3 = ThreeDVector(5)
