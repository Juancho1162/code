# Faster implementation of the Euler 1 problem with numpy
import numpy as np

numbers = np.arange(1000)

condition = (numbers % 5 == 0) | (numbers % 3 == 0)
a = numbers[condition]
print(sum(a))
