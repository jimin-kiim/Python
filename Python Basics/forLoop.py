# when the number of iterations is fixed.
# for loop has cleaner and shorter syntax, making it a better choice in most cases.
days=["mon","tue","wed","thu","fri","sat","sun"]
for day in days:
    print(day+"!")
    i=0
    for word in day:
        print(" "*i+word)
        i+=1

# iterate over a given sequence, such as lists or strings.
    # string, list, tuple, range()
string="How many 'i' is in this question ?"
count=0
for char in string:
    if char=='i':
        count+=1
print(count)


for i in range(5):
    print("*"*i)
