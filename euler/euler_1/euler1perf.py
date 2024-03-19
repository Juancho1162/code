import numpy as np

numbers = np.arange(1000)

condition = (numbers % 5 == 0) | (numbers % 3 == 0)
a = numbers[condition]
print(sum(a))
