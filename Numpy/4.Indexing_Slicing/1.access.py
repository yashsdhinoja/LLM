"""

array[index] #1d array
array[row, column] #2d array

"""
import numpy as np
            #   0   1  2  3  4  5  6  7  8  9
arr = np.array([10,20,30,40,50,60,70,80,90,100])
arr_alpha = np.array(["Yash","Car"])

print(arr[0])
print(arr[2])
print(arr[-2])

print(arr_alpha[0])
print(arr_alpha[-1])