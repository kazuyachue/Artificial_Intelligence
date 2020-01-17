import sys

s = set({i for i in range(9, 100, 10)} | {i for i in range(0, 100, 10)})
print(s)

n = 10
d = {i : {j for j in range(n) if ((i + j)**0.5)**2==(i+j)} for i in range(n)}
print(d)
