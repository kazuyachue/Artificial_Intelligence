import sys, time

lookupTable = {1: {2,3,4,5,6}, 2: {1,3,6,8,9}, 3:{1,2,4,9,10}, 4:{1,3,5,10,11}, 5:{1,4,6,7,11}, 6:{1,2,5,7,8},
7:{5,6,8,11,12}, 8:{2,6,7,9,12}, 9:{2,3,8,10,12}, 10:{3,4,5,9,12}, 11:{4,5,7,10,12}, 12:{7,8,9,10,11}}

def isInvalid(puz,size):
    count = 0
    for pentagons in lookupTable.keys():
        if puz[pentagons-1] == 'E':
            count += 1
            for neighbors in lookupTable[pentagons]:
                if puz[neighbors-1] == 'E':
                    return 1
    if count >= int(size):
        return 2
    elif count + puz.count('*') == 12:
        return 1
    return 0

def bruteForce(pzl,size):
    booleanish = isInvalid(pzl,size)
    if booleanish == 1: return ""
    if booleanish == 2: return pzl

    index = pzl.find('.')
    for char in ['E', '*']:
        subPzl = pzl[0:index] + char + pzl[index+1:]
        bF = bruteForce(subPzl,size)
        if bF: return bF
    return ""

root = '.' * 12
print(bruteForce(root,sys.argv[1]))
