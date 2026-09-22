import numpy as np

arr_1d = np.array([10, 20, 30])
arr_2d = np.array([2.3, 5.7, 6.7])

print(arr_1d + 5)
print(arr_1d - 6)
print(arr_1d / 3)
print(arr_1d * 3)
print(arr_1d ** 2)
print(arr_1d // 2)
print(arr_1d % 2)

# print(arr_2d + 5)
# print(arr_2d - 6)
# print(arr_2d / 3)
# print(arr_2d * 3)
# print(arr_2d ** 2)
# print(arr_2d // 2)
# print(arr_2d % 3)

int_arr = arr_1d.astype(str) # convert float to str
print(int_arr) # print data in str
print(int_arr.dtype) # str