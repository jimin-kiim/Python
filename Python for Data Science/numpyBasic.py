'''
NumPy(Numerical Python): a Python library used to work with numerical data.

np.array() : NumPy provides an array structure for performing operations with data.
NumPy arrays are homogeneous, meaning they can contain only a single data type, while lists can contain multiple different types of data.

'ndarrays' stands for "N-dimensional array"
ndim :  returns the number of dimensions of the array.
size : returns the total number of elements of the array.
shape : returns a tuple of integers that indicate the number of elements stored along each dimension of the array.
'''
import numpy as np 

x=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(x)
print(x.ndim)
print(x.size)
print(x.shape)
# to the number of rows and columns in the array.

x=np.append(x,4)
print(x)

x=np.delete(x,0)
print(x)
# np.delete(array, index)

y=np.sort(x)
print(y)

'''
arange & reshape
'''
z=np.arange(2,10,3)
print("z=np.arange(2,10,3)", z)
#  create an array that contains a range of evenly spaced intervals (similar to a Python range)

z=np.arange(1,7)
print(z)
# 1-dimensional array
z=z.reshape(3,2)
print(z)
# 2-dimensional array
    # 3-row 2-col

x=np.array([[1,2],[3,4],[5,6]])
print(x)
# 2-dimensional array
x=x.reshape(6)
print(x)
# 1-dimensional array (flat array)

x=np.array([[1,2],[3,4],[5,6]])
print(x)
# 2-dimensional array
x=x.flatten()
print(x)
# 1-dimensional array (flat array)

x = np.arange(1, 8, 3)
z = x.reshape(3, 1)
print(z[1][0])

'''
Indexing & Slicing
'''
x=np.arange(1,10)
print(x)
print("x[0:2]", x[0:2])
print("x[5:]",x[5:])
print("x[:2]",x[:2])
print("x[-3:]",x[-3:])

'''
Condition
'''

x=np.arange(1,10)
print("x[x<4]",x[x<4])
print("x[(x>5) & (x%2==0)]",x[(x>5) & (x%2==0)])

'''
Array Operation
'''
x=np.arange(1,10)
print("x.sum()",x.sum())
print("x.min()",x.min())
print("x.max()",x.max())

y=2*x
# broadcasting
print(y)

print("np.mean(x)", np.mean(x))
print("np.median(x)", np.median(x))
print("np.var(x)", np.var(x))
print("np.std(x)", np.std(x))

print("x[x>np.mean(x)]",x[x>np.mean(x)])

"""
# House Prices Problem

' You are given an array that represents house prices.
Calculate and output the percentage of houses that are within one standard deviation from the mean. ' 

"""
data = np.array([150000, 125000, 320000, 540000, 200000, 120000, 160000, 230000, 280000, 290000, 300000, 500000, 420000, 100000, 150000, 280000])

mean=np.mean(data)
std=np.std(data)
# print(data[mean-std<data<mean+std]) : Value Error
num=len(data[(mean-std<data)& (data<mean+std)])
percentage= num/len(data)*100
print(percentage)