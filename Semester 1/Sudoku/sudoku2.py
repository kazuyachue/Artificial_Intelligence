import sys,time
start = time.clock()

lookupTable = {}
symbolSet = {'1', '3', '9', '2', '4', '6', '5', '8', '7'}

for i in range(81):
    lookupTable[i] = set()
    row_start = i // 9
    column_start = i % 9
    top_corner = i - (column_start % 3) - (row_start % 3) * 9
    square_loc = top_corner
    for j in range(9):
        if j == 3 or j == 6:
            square_loc += 6
        lookupTable[i].add(9 * row_start + j)
        lookupTable[i].add(column_start + j * 9)
        lookupTable[i].add(square_loc)
        square_loc += 1
    lookupTable[i].remove(i)

def isInvalid(puz, index):
    if index == -1:
        return 0
    number = puz[index]
    for neighbors in lookupTable[index]:
        if puz[neighbors] == number:
            return 1
    if '.' in puz:
        return 0
    return 2

def possible(puz, index):
    possibleTable = set()
    for neighbors in lookupTable[index]:
        if puz[neighbors] != '.':
            possibleTable.add(puz[neighbors])
    return possibleTable

def bruteForce(pzl, index):
    booleanish = isInvalid(pzl, index)
    if booleanish == 1: return ""
    if booleanish == 2: return pzl

    minimum = 10
    for i in range(len(pzl)):
        if pzl[i] == '.':
            p = possible(pzl, i)
            numPoss = 9 - len(p)
            if numPoss == 0:
                return ""
            elif numPoss == 1:
                index = i
                impossibleSet = p
                break
            elif numPoss < minimum:
                minimum = numPoss
                index = i
                impossibleSet = p
    possibleSet = symbolSet - impossibleSet
    for j in possibleSet:
        subPzl = pzl[0:index] + j + pzl[index+1:]
        bF = bruteForce(subPzl, index)
        if bF: return bF
    return ""

count = 1
with open("puzzles.txt","r") as f:
    for line in f:
        print(f"COUNT: {count}")
        #if count >= 128: break
        puzzle = line.strip()
        print(bruteForce(puzzle, -1))
        count += 1

print("Total time: " + str(time.clock() - start))
