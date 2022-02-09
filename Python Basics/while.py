# when the number of iterations is not known and depends on some calculations and conditions in the code block of the loop.
i=0
while i<5:
    i+=1
    if i==3:
        print("Skipping 3")
        continue
    # continue jumps back to the top of the loop
    print(i)