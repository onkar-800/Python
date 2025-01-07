# 8. Write a python function to print multiplication table of a given number.

def multi_table(num):
    for i in range(1,11):
        print(f"{num} X {i} = {num*i}")
    
print(multi_table(5))