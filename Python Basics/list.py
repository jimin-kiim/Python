words=["Hello","world","!",]
print(words[0]+words[1])
# print(words[3])   IndexError: list index out of range
# square brackets, commas

empty_list=[]

things=["string",0,[1,2,True,"number"],5.7]
# it is also possible to include several different types.
print(things[0]+things[2][3])
print(things[1]+things[3]-things[2][0])
print(things)
things[1]=False
# reasigning the item at a certain index
print(things)
# ['string', False, [1, 2, True, 'number'], 5.7] 
#   is printed. don't need to iterate each item like in C.

nums=[0,1,2]
print(nums*2+things)
# list operations
str="Hello"
# print(str[1]+nums)
# TypeError: can only concatenate str (not "list") to str
#   we can access the string like a list but cannot concatenate to the list not a str.

days=["lundi","mardi","thursday","friday","samedi"]
print("jeudi"in days)
print("e"in str)
# The 'in' operator is also used to determine whether or not a string is a substring of another string.
print(not "a" in str)
print("a" not in str)
# both of them above mean the same thing.

days.append("dimanche")
print(days)
# The append method adds an item to the end of an existing list.
# append is a method of the list class.
print("length of 'Hello' is:",len(str))
print("length of array is:",len(days))
# print("length of array is:"+len(days))
#   TypeError: can only concatenate str (not "int") to str 
#   len() returns integer, no a string.
print(1,2,3)
# printing several items in a row which are not a string, we use ',' not '+'
# '+' means concatenation, which can be only used with lists and strings

days.insert(2,"wednesday")
print(days)
# The 'insert method' allows us to insert a new item at any position in the list
# Elements, that are after the inserted item, are shifted to the right.

days[5]="friday"
print(days.index('friday'))
# The 'index method' finds the first occurrence of a list item and returns its index.

numbers=[3,4,5,5,5,2,3,1,7]
print("list:",numbers)
print("maximum number of the list:",max(numbers),"\n",
"minimum number of the list:",min(numbers),"\n",
"the number of times '5' occurs in the list:",numbers.count(5),"\n")
numbers.remove(5)
print("list:",numbers)
# finds the first occurrence of a list item and removes it.
numbers.reverse()
print("list:",numbers)

list=[1,3,5,2,6,3,4]
print(list[list[2]])