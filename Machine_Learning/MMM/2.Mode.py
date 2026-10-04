from scipy import stats

speed = [23.4,43.65,56.3,45.8,67.0,908.5,34.3,555.6,908.2]

mode1 = stats.mode(speed)

print(mode1)