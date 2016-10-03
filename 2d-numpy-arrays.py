import numpy as np

np_height = np.array([1.73, 1.68, 1.82])

np_weight = np.array([65.4, 58.2, 70.3])

print (type(np_height))
print (type(np_weight))

np_2d = np.array([[1.73, 1.68, 1.82],
                  [65.4, 58.2, 70.3]])

print (np_2d)
print (np_2d.shape)

np_2d[0][1]
print (np_2d)

np_2d[0, 1]
print(np_2d)

print (np_2d[:, 1:3])

print (np_2d[1, :])


