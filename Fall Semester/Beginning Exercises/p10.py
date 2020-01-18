import sys

my_list = [int(num) for num in sys.argv[1:]]
my_set = set(my_list)
lst = sorted(list(my_set))
if not isArithmetic(lst):
    print("No")
else:
    if repeated(my_list, lst):
        print("Yes")
    else:
        print("No")

def repeated(lst1, lst2):
    ctr = 0
    while lst1[0]!=lst2[0] and ctr<len(lst2):
        lst2.append(lst2.pop(0))
        ctr+=1
    for i in lst1:
        if lst1[i]!=lst2[0]:
            return False
        lst2.append(lst2.pop(0))
    return True

def isArithmetic(l):
    if len(l)<2:
        return False
    elif len(l)==2:
        return True
    else:
        dif = lst[1]-lst[0]
        b = True
        for j in range(0, len(lst)-1):
            if lst[j+1]-lst[j]!=dif:
                b = False
        return b

"""
lst = []
for i in range(1, len(sys.argv)):
    lst.append(int(sys.argv[i]))

if len(lst)<2:
    print("No")
elif len(lst)==2:
    print("Yes")
else:
    dif = lst[1]-lst[0]
    s = "Yes"
    ptrn = []
    for j in range(0, len(lst)-1):
        ptrn.append(lst[j])
        if lst[j+1]-lst[j]!=dif:
            if ptrn[0]!=lst[j+1]:
                s = "No"
    print(s)
"""
