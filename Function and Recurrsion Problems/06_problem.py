# 5. Write a python function to print first n lines of the following pattern:
# ***
# **
# *
# - for n =3

def pattern1(n=3):
    if(n==1):
        print("*")
        return
    print("*"*n)
    pattern1(n-1)

def pattern(n=3):
    for i in range(n,0,-1):
        print("*"*i)

def pyramid(n=3):
    if(n==0):
        return
    pyramid(n-1)
    print("*"*n)

pattern1(5)
pyramid(5)