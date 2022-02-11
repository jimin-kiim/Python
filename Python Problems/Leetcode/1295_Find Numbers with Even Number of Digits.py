#LeetCode Array-Introduction #2, (#1295)
# Find Numbers with Even Number of Digits
nums = [12,345,2,6,7896]
count=0
for num in nums:
    if len(str(num))%2==0:
        count+=1
print(count)

# to use len(), num should be turned into string using str()