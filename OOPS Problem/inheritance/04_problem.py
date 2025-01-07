# Write a class 'Complex' to represent complex numbers, along with overloaded operators '+' and '*' which adds and multiplies them.
class Complex:
    def __init__(self,r,i):
        self.r = r
        self.i = i

    def __add__(self,c2):
        return Complex(self.r + c2.r,self.i+c2.i)

    def __mul__(self,num):
        real = self.r*num.r - self.i*num.i 
        imaginary = self.r*num.i + self.i * num.r 
        return Complex(real,imaginary)

    def __str__(self):
        return f"{self.r} + {self.i}i"
    
c = Complex(10,11)
d = Complex(10,12)
print(c+d)
print(c*d)