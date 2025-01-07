# Override the len() method on vector of problem 5 to display the dimension of the vector.

class Vector:
    def __init__(self,lst):
        self.lst = lst
    
    def __len__(self):
        return len(self.lst)

v1 = Vector([4,5,6,7,8,9])
print(len(v1))
