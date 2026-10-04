import numpy 
speed_1 = [99,86,87,88,111,86,103,87,94,78,77,85,86]
# speed_2 = [77, 78, 85, 86, 86, 86, 87, 87, 88, 94, 99, 103, 111]
speed_2 = [67, 68]


x = numpy.mean(speed_1)
y = numpy.median(speed_2)


print("mean : " , x)
print("median : " , y)