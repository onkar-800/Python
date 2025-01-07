# 1. Write a program using functions to find greatest of three numbers.

def greatest_amon_three(a,b,c):
    if(a>b and b>c): return a
    if(b>c): return b
    return c

print(greatest_amon_three(12,12,3))