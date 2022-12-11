import pandas as pd
import numpy as np

# 1 What are the similarities and differences between pandas and numpy?
# Include some type of example with code.
'''
Pandas and Numpy are both used to house objects of large data sets. However,
they differ in the types of data they are used for and the application that follows.
Numpy can only handle data of the same type and any dimension but Pandas can mix many
data types but is really intended for tabular 2D data. As a result numpy is often used
in scientific computations and pandas is used for data analysis.
'''
# this would throw an error np.array([1,2, "example"])
# pandas has no problem with this mixed data
print(pd.DataFrame([1,2, "example"]))

# 2. What is the ndarray in numPy?
# ndarray is the basic data type for a numpy array

# 3. Create a 1D array of numbers from 0 to 9 
array_1d = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(array_1d)

# 4. Extract all odd numbers from array1 

array1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(array1[array1 % 2 == 1])

# 5. Get the common items between a and b

#input
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

# Desired Output: array([2, 4])
print(np.intersect1d(a, b))

# 6. From array a remove all items present in array b 

#Input:

a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])

#Desired Output: array([1,2,3,4])
test = np.intersect1d(a, b)
mask = np.isin(a, test, invert=True)
print(a[mask])

# 7. Find out if iris has any missing values. 

# Input
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
print(True in np.equal(iris, None))
# There are no missing values
