# Ch04 NumPy Foundations

## Getting Started wiht NumPy

### NumPy Array

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

[[i + 1 for i in row] for row in matrix]

# First, let's import NumPy
import numpy as np

# Constructing an array with a simple list results in a 1d array
array1 = np.array([10, 100, 1000.])

# Constructing an array with a nested list results in a 2d array
array2 = np.array([[1., 2., 3.],
                   [4., 5., 6.]])

array1.dtype

float(array1[0])

### Vectorization and Broadcasting

array2 + 1

array2 * array2

array2 * array1

array2 @ array2.T  # array2.T is a shortcut for array2.transpose()

### Universal Functions (ufunc)

import math

math.sqrt(array2)  # This will raise en Error

np.array([[math.sqrt(i) for i in row] for row in array2])

np.sqrt(array2)

array2.sum(axis=0)  # Returns a 1d array

array2.sum()

## Creating and Manipulation Arrays

### Getting and Setting Array Elements

array1[2]  # Returns a scalar

array2[0, 0]  # Returns a scalar

array2[:, 1:]  # Returns a 2d array

array2[:, 1]  # Returns a 1d array

array2[1, :2]  # Returns a 1d array

### Useful Array Constructors

np.arange(2 * 5).reshape(2, 5)  # 2 rows, 5 columns

np.random.randn(2, 3)  # 2 rows, 3 columns

### View vs. Copy

array2

subset = array2[:, :2]
subset

subset[0, 0] = 1000

subset

array2