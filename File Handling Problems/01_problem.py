
#     CHAPTER 9 - PRACTICE SET
# 1. Write a program to read the text from a given file "poems.txt' and find out whether it
# contains the word 'twinkle'.

# Using with statement (recommended)
poem = open("Chapter_09_File_(I-O)/poems.txt")

if("twinkle" in poem.read().lower()):
    print("twinkle is present in poem")
else:
    print("twinkle is not present in poem")

poem.close()