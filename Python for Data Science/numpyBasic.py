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

z=np.arange(2,10,3)
print(z)
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

