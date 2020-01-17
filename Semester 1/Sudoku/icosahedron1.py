import sys, time

lookupTable = {0:{1,4,6}, 1:{0,2,8}, 2:{1,3,10}, 3:{2,4,12}, 4:{3,0,14}, 5:{6,14,15},
6:{0,5,7},7:{6,8,16}, 8:{1,7,9}, 9:{8,10,17}, 10:{2,9,11}, 11:{10,12,18}, 12:{3,11,13},
13:{12,14,19}, 14:{4,5,13}, 15:{5,16,19}, 16:{7,15,17}, 17:{9,16,18}, 18:{11,17,19}, 19:{13,15,18}}

def isInvalid(puz,size):
    count = 0
    for triangles in lookupTable.keys():
        if puz[triangles] == 'E':
            count += 1
            for neighbors in lookupTable[triangles]:
                if puz[neighbors] == 'E':
                    return 1
    if count >= int(size):
        return 2
    elif count + puz.count('*') == 20:
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

root = '.' * 20
print(bruteForce(root,sys.argv[1]))
