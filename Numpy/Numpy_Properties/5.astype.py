# array ===>>> checking
# syntax ==>> astype()
# changing the type str to int, float to int
# array.astype(new_type) any of them int, float, str

import numpy as np

# arr = np.array([1.2, 5.9, 4.5])
# int_arr = arr.astype(str)
# int_arr = arr.astype(int)
# print(int_arr)
# print(int_arr.dtype)

# output =>>> 
# <U32
# ['1.2' '5.9' '4.5']
# <U32


arr = np.array([45.5, 66.5, 78.4])
print(arr.dtype) # float
int_arr = arr.astype(int) # convert float into int
print(int_arr) # print data in integer
print(int_arr.dtype) # int

# output =>>>
# float64
# [45 66 78]
# int64