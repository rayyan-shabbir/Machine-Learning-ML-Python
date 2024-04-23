# Importing important libraries related assignment....
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# % matplotlib inline

# Getting Training and Testing data
Trn_data = pd.read_csv('trainRegression.csv')
Test_data = pd.read_csv('testRegression.csv')


# Printing Training data
print("TRAIN DATA")
# Trn_data.head()
print(Trn_data)

# Printing Testing data
print("\nTEST DATA")
# Test_data.head()
print(Test_data)



print("\n\n")
print(Trn_data['X'])

# plt.plot(Trn_data['X'], Trn_data['R'], '*')

print(type(Trn_data))

plt.show()


x = np.array(Trn_data)
# x = Trn_data.as_matrix()

print("\n\n")
print(x)

A1 = Trn_data.shape[0]
print(A1)

A2 = np.sum(Trn_data['X'])
print(A2)

A4 = np.sum(np.dot(Trn_data['X'], Trn_data['X']))
print(A4)

B1 = np.sum(Trn_data['R'])
print(B1)

B2 = np.sum(np.dot(Trn_data['X'], Trn_data['R']))
print(B2)



A = np.array([[A1, A2], [A2, A4]])
B = np.array([[B1] , [B2]])

print(type(A))

A_inv = np.linalg.inv(A)

print(type(A_inv))
print(type(B))

Q = np.dot(A_inv, B)

print(Q)