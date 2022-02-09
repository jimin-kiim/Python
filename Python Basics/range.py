# range() function returns a sequence of numbers.
numbers=list(range(10))
print(numbers)
# In order to output the range as a list, 
#   we need to explicitly convert it to a list, using the list() function.
numbers2=list(range(3,8))
print(numbers2)
print(len(numbers2))

print(range(5)==range(0,5))

numbers3=list(range(2,10,2))
print(numbers3)
numbers3=list(range(2,10,-2))
print(numbers3)
numbers3=list(range(10,2,-2))
print(numbers3)
# step