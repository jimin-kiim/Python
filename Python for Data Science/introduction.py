# Measures of Central Tendency
'''
mean : the average value of the dataset. 
median : the middle value of an ordered dataset.
        If our dataset had an even number of values, 
        we would take the two values in the middle and calculate their average value.
'''

vac_nums = [0,0,0,0,0,
            1,1,1,1,1,1,1,1,
            2,2,2,2,
            3,3,3
            ]

count=0
for num in vac_nums:
    count+=num

print(count/len(vac_nums))

# Standard Deviation
'''
 Variance : the average of the squared differences from the mean.
 Standard Deviation (std) : the square root of the Variance

 A low standard deviation indicates that the values tend to be close to the mean of the set, 
 while a high standard deviation indicates that the values are spread out over a wider range.
 '''

players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]

def mean(list):
    total=0
    for item in list:
        total+=item
    mean=total/len(list)
    print("mean :",mean)
    return mean

def std(list, mean):
    total=0
    for item in list:
        total+=(item-mean)**2
    std=(total/len(list))**0.5
    print("std :",std)
    return std

def count_in_range(list, mean, std):
    count=0
    for item in list:
        if mean-std<item<mean+std:
            count+=1
    return count

m=mean(players)
s=std(players,m)
print("the number of players in the range of one standard deviation from the mean :",count_in_range(players,m,s))