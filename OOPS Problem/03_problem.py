# Create a class with a class attribute a; create an object from it and set 'a' directly using object.a = 0. Does this change the class attribute?
class A:
    a = 0
a = A()
a.a = 10
print(a.a)
print(A.a)