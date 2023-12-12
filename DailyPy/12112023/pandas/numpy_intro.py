#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 21:27:38 2023

@author: zhihaowang
"""

import numpy as np


# Creating NumPy arrays
arr1 = np.array([1,2,3,4,5])
arr2 = np.arange(1, 6)
arr3 = np.linspace(1,5,5)

# Displaying the arrays
print("Array 1:", arr1)
print("Array 2:", arr2)
print("Array 3:", arr3)

# Basic array operations
sum_result = arr1 + arr2
product_result = arr1 * arr2

# Displaying the results
print("\nSum of arrays 1 and 2:", sum_result)
print("Product of arrays 1 and 2:", product_result)

# Array manipulation
reshaped_arr = arr1.reshape(5, 1)

# Displaying the reshaped array
print("\nReshaped Array:")
print(reshaped_arr)

# Create a NumPy array
original_array = np.array([1, 2, 3, 4, 5, 6])

# Reshape the array into a 2x3 matrix
reshaped_array = np.reshape(original_array, (2, 3))

print("Original Array:")
print(original_array)

print("\nReshaped Array:")
print(reshaped_array)

random_data = np.random.randn(1000)

mean_value = np.mean(random_data)
median_value = np.median(random_data)
std_deviation = np.std(random_data)

# Display the results
print("Mean:", mean_value)
print("Median:", median_value)
print("Standard Deviation:", std_deviation)
print(random_data)

# Generate a 2D array with dimensions 2x3
random_2d_array = np.random.randn(2, 3)

# Generate a 3D array with dimensions 2x3x4
random_3d_array = np.random.randn(2, 3, 4)

print("Random 2D Array:")
print(random_2d_array)

print("\nRandom 3D Array:")
print(random_3d_array)


