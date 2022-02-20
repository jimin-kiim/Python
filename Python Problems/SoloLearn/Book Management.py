"""
Read the title one by one and output the code for each book on a separate line.
The code is equal to the first letter of the book, followed by the number of characters in the title.

❗️ remember that all lines, except the last one, contain a \n at the end.
"""

'''
# Python >= 3.9.0

✔️ removesuffix()

file = open("./Python Problems/SoloLearn/books.txt", "r")
lines=file.readlines()
for line in lines:
    line.removesuffix('\n')
    print(line[0]+str(len(line)))
file.close()
'''

def removesuffix(str,target):
    if target in str:
        return str.strip(target)
    return str

file = open("./Python Problems/SoloLearn/books.txt", "r")

lines=file.readlines()
for line in lines:
    line=removesuffix(line,'\n')
    print(line[0].capitalize()+str(len(line)),line)
file.close()
