# SoloLearn Python Core '30 code Project'
number=int(input("Enter a number ! :"))
for i in range(number):
    if (i%3==0)and(i%5==0):
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)