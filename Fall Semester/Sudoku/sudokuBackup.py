import sys,time
start = time.clock()

lookupTable = {}

possibleTable = {}
notAssigned = set()
backupTable = {}

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

def bruteForce(pzl, index):
    booleanish = isInvalid(pzl, index)
    if booleanish == 1: return ""
    if booleanish == 2 or len(notAssigned)==0: return pzl

    index = next(iter(notAssigned))
    for i in notAssigned:
        if len(possibleTable[i]) < len(possibleTable[index]): index = i
    #print(notAssigned)
    #print(index)
    #print(pzl)
    notAssigned.remove(index)
    for possible in possibleTable[index]:
        subPzl = pzl[0:index] + possible + pzl[index+1:]
        backupTable = possibleTable
        for neighbors in lookupTable[index]:
            possibleTable[neighbors] -= {possible}
        bF = bruteForce(subPzl, index)
        if bF: return bF
        possibleTable = backupTable
        backupTable.clear()
    return ""

count = 0
with open("puzzles.txt","r") as f:
    for line in f:
        notAssigned.clear()
        possibleTable.clear()
        backupTable.clear()
        print(f"COUNT: {count}")
        if count >= 51: break
        puzzle = line.strip()
        for i in range(81):
            if puzzle[i] == '.': notAssigned.add(i)
            possibleTable[i] = {str(j) for j in range(1,10)}
            for neighbors in lookupTable[i]:
                possibleTable[i] -= set(puzzle[neighbors])
        print(bruteForce(puzzle, -1))
        count += 1

print("Total time: " + str(time.clock() - start))
