import sys
import time

subHexagons = {1: {0, 1, 2, 6, 7, 8}, 2: {2, 3, 4, 8, 9, 10}, 3: {5, 6, 7, 12, 13, 14}, 4: {7, 8, 9, 14, 15, 16},
5: {9, 10, 11, 16, 17, 18}, 6: {13, 14, 15, 19, 20, 21}, 7: {15, 16, 17, 21, 22, 23}}

letters = ['A', 'B', 'C', 'D', 'E', 'F']               #{'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0}

def isInvalid(puz):
    fivetimes = False
    for letter in letters:
        if fivetimes and puz.count(letter) >= 5:
            return 1
        if puz.count(letter) >= 5:
            fivetimes = True
    for hexagons in subHexagons.keys():
        subPuz = ""
        for triangle in subHexagons[hexagons]:
            subPuz += puz[triangle]
        for char in subPuz:
            if char != '.' and subPuz.count(char) > 1:
                    return 1
    if '.' in puz:
        return 0
    return 2

def bruteForce(pzl):
    booleanish = isInvalid(pzl)
    if booleanish == 1: return ""
    if booleanish == 2: return pzl
    index = pzl.find('.')
    for possible in letters:
        subPzl = pzl[0:index] + str(possible) + pzl[index+1:]
        bF = bruteForce(subPzl)
        if bF: return bF
    return ""


root = '.' * 24
print(bruteForce(root))
