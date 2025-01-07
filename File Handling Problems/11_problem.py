# 11 Write a python program to rename a file to “renamed_by_python.txt.”

import os
current_file = "Chapter_09_File_(I-O)/poems_copy.txt"
new_file = "Chapter_09_File_(I-O)/renamed_by_python.txt"
try:
    os.rename(current_file,new_file)
    print("File renamed successful")
except FileNotFoundError:
    print("file not found error")
except Exception as e:
    print(e)
