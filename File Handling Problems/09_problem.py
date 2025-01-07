# 9. Write a program to find out whether a file is identical & matches the content of
# another file.

def are_identical(file1_path, file2_path):
    try:
        with open(file1_path) as file1:        
            with open(file2_path) as file2:
                # print(file1.read(),file2.read())
                return file1.read() == file2.read()
    except FileNotFoundError:
        print("One or both files could not be found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Example usage
file1 = "Chapter_09_File_(I-O)/poems.txt"
file2 = "Chapter_09_File_(I-O)/poems_copy.txt"
print(f"Are the files identical? {are_identical(file1, file2)}")