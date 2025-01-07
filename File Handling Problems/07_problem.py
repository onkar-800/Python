# 7. Write a program to find out the line number where python is present from ques 6.


with open("Chapter_09_File_(I-O)/log.txt") as log:
    for lineNo,line in enumerate(log,1):
        if("python" in line.lower()):
            print(f"Python is present at line no. {lineNo}")
        

# with open("Chapter_09_File_(I-O)/log.txt") as log:
#     line = log.readline()
#     lineNo = 1
#     while(line != ""):
#         if("python" in line.lower()):
#             print(f"Python is present at line no. {lineNo}")
#         lineNo+=1
#         line = log.readline()

    