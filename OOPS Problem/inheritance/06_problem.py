# Write str() method to print the vector as follows:
# 71+8i+10k
# Assume vector of dimension 3 for this problem.

class Vector:
    def __init__(self,i,j,k):
        self.i  = i 
        self.j  = j
        self.k  = k

    def __add__(self,v1):
        return Vector(self.i+v1.i,self.j+v1.j,self.k+v1.k)

    def __mul__(self,v1):
        return Vector(self.i*v1.i,self.j*v1.j,self.k*v1.k)

    def __str__(self):
        return f"{self.i}+{self.j}i+{self.k}k"

v1 = Vector(4,5,6)
v2 = Vector(1,2,3)
print(v1+v2)
print(v1*v2)