# Write a class "calculator" capable of finding square, cube and square root of a number.
# Add a static method in problem 2, to greet the user with hello.

class Calculator:
    def __init__(self,number) -> None:
        self.number = number
    
    def square_root(self):
        return self.number ** 0.5 

    def square(self):
        return self.number ** 2
    
    def cube(self):
        return self.number ** 3
    
    @staticmethod
    def greet():
        print("Hello")
    
c1 = Calculator(3)
print(c1.square())
print(c1.square_root())
print(c1.cube())
c1.greet()
