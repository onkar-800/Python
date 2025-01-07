# 8. Write a program to make a copy of a text file "poems. txt"


with open("Chapter_09_File_(I-O)/poems.txt") as file:
    content = file.read()
    with open("Chapter_09_File_(I-O)/poems_copy.txt",'w') as copy:
        copy.write(content)
