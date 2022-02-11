#LeetCode Array-Introduction #3 (#977)
# Squares of a Sorted Array
nums = [-4,-1,0,3,10]
new=[]
for num in nums:
    new.append(num**2)
new.sort()
print(new)