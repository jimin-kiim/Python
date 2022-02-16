def multiply(x,y):
    """
    Docstrings
    They are created by putting a multiline string containing an explanation of the function below the function's first line
    """
    return x*y
    print(x+y)

# Once you return a value from a function, it immediately stops being executed.
# Any code after the return statement will never happen.

operation=multiply
print(operation(2,4))
# functions are just like any other kind of value.
    # They can be assigned and reassigned to variables, and later referenced by those names.

def multiply_twice(func,x,y):
    return func(func(x,y),func(x,y))
print(multiply_twice(multiply,2,4))
# Functions can also be used as arguments of other functions.

def plus(x,y=0):
    # can assign a default value
    print(x+y)
plus(1,3)
# postional argument
plus(y=4, x=0)
# keyword argument
    #it's useful when it's hard to remember the order of the parameters
plus(5)


def say_hello(name="anonymous"):
    print("Hello "+name)
    print("Hello",name)
    print(f"Hello {name}")
    # when the string is wordy and contains a lot of variables, this way is more pertinent
    print("Hello {0}".format(name))
say_hello()
say_hello("jimin")