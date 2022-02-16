user_input=input()
# input() function : return what the user entered ❗️ as a string.❗️
print(user_input)

name=input("Enter your name: ")
# prompt message
print('Hello, '+name)

age=int(input("Enter your age: "))
print("Next year, "+ name+"'s age is : "+str(age+1))
# int() function, str() function
"""
int(), str(), bool(), float()
"""

age+=3
# in-place operator
name+=" kim"
print("In 2025, "+ name+"'s age is : "+str(age))

print(hello:=input("Say Hello ! "))
print(name+"'s fav is "+ str(fav:=input("What do you like the most?")))
# Walrus operator :=