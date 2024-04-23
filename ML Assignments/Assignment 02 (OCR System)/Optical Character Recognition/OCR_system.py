import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
# %matplotlib inline


Train_X = np.array([[0, 0, 0, 1],
            [0, 1, 1, 1], 
            [1, 0, 1, 0], 
            [1, 0, 0, 1], 
            [0, 1, 0, 0], 
            [1, 0, 1, 1]])

print(Train_X.shape)

Train_X2 = Train_X[:3]
Train_X4 = Train_X[3:]

print(Train_X2)
print("\n")
print(Train_X4)
print("\n")


print(Train_X2.shape)

prob_Xone_2 = (np.sum(Train_X2, axis=0)) / Train_X2.shape[0]
prob_Xzero_2 =  1 - prob_Xone_2

prob_Xone_4 = (np.sum(Train_X4, axis=0)) / Train_X4.shape[0]
prob_Xzero_4 =  1 - prob_Xone_4

prob_2 = 3/6
print(prob_2)

print("Xone_2")
print(prob_Xone_2)
print("Xzero_2")
print(prob_Xzero_2)

prob_4 = 3/6
print(prob_4)

print("Xone_4")
print(prob_Xone_4)
print("Xzero_4")
print(prob_Xzero_4)


Test_X = np.array([1, 1, 0, 1])

print(type(Test_X))

product_x_2 = 1
product_x_4 = 1
j = 0
print("\n")

for i in range(0, len(Test_X)):
    # print(Test_X[i])
    if Test_X[i] == 1:
        product_x_2 = product_x_2*prob_Xone_2[j] 
        product_x_4 = product_x_4*prob_Xone_4[j] 
        # print(prob_Xone_2[j])
    elif Test_X[i]== 0:
        product_x_2 = product_x_2*prob_Xzero_2[j]
        product_x_4 = product_x_4*prob_Xzero_4[j] 
        # print(prob_Xzero_2[j])
    j = j + 1

product_x_2 = product_x_2*prob_2
product_x_4 = product_x_4*prob_4

print("2|X", product_x_2)
print("2|X", product_x_4)

if product_x_2 > product_x_4:
    print("your input is digit 2")
else:
    print("your input is digit 4")