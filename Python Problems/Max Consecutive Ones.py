#LeetCode Array-Introduction #1 (#485)
# nums=[1,1,0,1,1,1]
nums=[1,0,1,1,0,1]
count=[0]
i=0
for num in nums:
    if num==1:
        count[i]+=1
    else:
        count.append(0)
        i+=1
print(max(count))