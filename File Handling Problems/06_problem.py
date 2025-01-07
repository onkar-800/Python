# 6. Write a program to mine a log file and find out whether it contains 'python'.


with open("Chapter_09_File_(I-O)/log.txt") as log:
    flag = False
    for line in log:
        if("python" in line.lower()):
            flag = True
            break
    if(flag): print("Python is present in file")
    else: print("Python is Not present in file")

    