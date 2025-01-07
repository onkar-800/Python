# 5. Repeat program 4 for a list of such words to be censored.

words = ["donkey","monkey","cat"]
with open("Chapter_09_File_(I-O)/animals.txt","r") as f:
    content = f.read()

for word in words:
    content = content.replace(word,"#####")

with open("Chapter_09_File_(I-O)/animals.txt","w") as f:
    f.write(content)