# 3. Write a program to generate multiplication tables from 2 to 20 and write it to the
# different files. Place these files in a folder for a 13 - year old.

def generatrTable(n):
    table = ""
    for j in range(1,21):
        table += str(f"{n} X {j} = {n*j}\n")
    with open (f"Chapter_09_File_(I-O)/Tables/table_of_{n}.txt",'w') as f:
        f.write(table)


def tables():    
    for i in range(1,21):
        generatrTable(i)

tables()