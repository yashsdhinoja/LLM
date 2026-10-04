import numpy 
from scipy import stats

scores = [85, 90, 78, 90, 92, 88, 78, 90, 95, 82]

scores__1 = numpy.mean(scores)
scores__2 = numpy.median(scores)
scores__3 = stats.mode(scores)

print(scores__1)
print(scores__2)
print(scores__3)