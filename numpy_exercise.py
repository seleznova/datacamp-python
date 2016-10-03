import numpy as np

height = [1.73, 1.68, 1.71, 1.89, 1.79]

np_height = np.array(height)

weight = [65.4, 59.2, 63.6, 88.4, 68.8]

np_weight = np.array(weight)

bmi = np_weight / np_height ** 2

print (bmi)

print (bmi[1])

print (bmi > 20)