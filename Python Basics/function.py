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