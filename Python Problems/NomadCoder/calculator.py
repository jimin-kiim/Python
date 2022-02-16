def plus(x,y):
    print(f"the result of {x}+{y}={float(x)+float(y)}")

def minus(x,y):
    print(f"the result of {x}-{y}={float(x)-float(y)}")

def multiply(x,y):
    print(f"the result of {x}*{y}={float(x)*float(y)}")

def divide(x,y):
    print(f"the result of {x}/{y}={float(x)/float(y)}")

def mod(x,y):
    print(f"the result of {x}//{y}={float(x)//float(y)}")

def power(x,y):
    print(f"the result of {x}*{y}={float(x)**float(y)}")

menu_input=float(input("""What are you going to do?\n
1 : plus, 2 : minus, 3 : multiply, 4 : divide, 5 : mod, 6 : power"""))
a=float(input("input the first number to calculate"))
b=float(input("input the second number to calculate"))
if(menu_input==1):
    plus(a,b)
elif(menu_input==2):
    minus(a,b)
elif(menu_input==3):
    multiply(a,b)
elif(menu_input==4):
    divide(a,b)
elif(menu_input==5):
    mod(a,b)
elif(menu_input==6):
    power(a,b)
