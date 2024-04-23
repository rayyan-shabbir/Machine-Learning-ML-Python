import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# # %matplotlib inline

x = [1, 2, 3, 4]
y = [1, 2, 3, 4]

plt.plot(x, y)

plt.xlabel('x numbers')
plt.ylabel('y numbers')

plt.show()

# data = pd.read_csv('trainRegression.csv')
# data.head()

# print (data['X'])
# plt.plot(data['X'], data['Y'])

# type(data)

# # to convert data into Numpy Array
# numpydata = data.as_matrix()
# type(numpydata)