# 7. Write a python function to remove a given word from a list ad strip it at the same
# time.

def rem_and_strip(lst,word):
    n = []
    if(word in lst): lst.remove(word)
    for item in lst:
        if word in item:
            n.append(item.strip(word))
        else:
            n.append(item)
    return n

print(rem_and_strip(["hello","hi","applehi","banana"],'he'))