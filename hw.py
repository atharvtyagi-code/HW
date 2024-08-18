import numpy as np

Array2D = np.random.randint(1, 100, size=(7, 7))
sorted = np.sort(Array2D, axis=0)  #'axis = 0' helps get the numbers in ascending order vertically.
print(Array2D)
print(sorted)

print(Array2D[2:5, 2:5])
print(Array2D[4:7, 4:7])

Array2D += 1  #Numbers will increase by 1 in Array2D
print(Array2D)