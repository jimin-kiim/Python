'''
r: default. open in read mode.
w: open in write mode. rewriting the contents of a file.
a: open in append mode. adding new content to the end of the file.
adding b: open in binary mode. non-text files.(image, sound files)
rb, wb, ab
'''
try:
    f=open("./Python Basics/practice.txt","w")
    amount_written=f.write("This has been written to a file.")
    print(amount_written)
finally: 
    f.close()
    # making sure that files are always closed after they have been used.

with open("./Python Basics/practice.txt","r") as file:
    cont = file.read(16)
    # the number of bytes that should be read.
    
    print("16 bytes of the content: ",cont)
    print("length of 16 bytes of the content: ", len(cont))
    print(file.readlines())
    for line in file:
        print(line)
    # reading starts at the point where the previous readind ended 
    print(file.read())
    print(len(open("./Python Basics/practice.txt").readlines()))
    # file.close()
    # with 'with statement': file is automatically closed. 
