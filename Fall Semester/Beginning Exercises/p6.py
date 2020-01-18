import sys

lst = [int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])]

s = (lst[0]+lst[1]+lst[2])/2
area = (s*(s-lst[0])*(s-lst[1])*(s-lst[2]))**(1/2)

print(area)
