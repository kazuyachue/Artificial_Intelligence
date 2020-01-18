import sys

for i in range(int(sys.argv[1]), int(sys.argv[2])):
    print(i**2-3*i+2, end=", ")
print(int(sys.argv[2])**2-3*int(sys.argv[2])+2)
