import sys, csv
import numpy as np

with open("data.csv", 'r') as f:
    reader = csv.reader(f)
    rows = list(reader)
    rows = rows[50:194]
    velocity = [float(li[3]) for li in rows]
    acceleration = [float(li[5]) for li in rows]

g = 9.8

alpha_11 = sum(i*i for i in velocity)
alpha_12 = sum(i**3 for i in velocity)
alpha_21 = alpha_12
alpha_22 = sum(i**4 for i in velocity)

beta1 = sum((g - y) * x for x,y in zip(velocity, acceleration))
beta2 = sum((g - y) * x * x for x,y in zip(velocity, acceleration))

alpha = np.array([[alpha_11, alpha_12], [alpha_21, alpha_22]])
beta = np.array([[beta1], [beta2]])

alpha_inverse = np.linalg.inv(alpha)
c = np.dot(alpha_inverse, beta)
print(c)
