import sys
import time

def isEdge(s1, s2):
    numDiff = 0;
    for i in range(0,6):
        if s1[i]!=s2[i]:
            numDiff+=1
    if numDiff == 1:
        return True
    else:
        return False


myDict = dict()
numVertices = 0
numEdges = 0
start_time = time.clock()
with open("sixletterwords.txt","r") as f:
    for line in f:
        line = line.strip()
        myDict[line] = set()
        numVertices+=1
        for s in myDict:
            if s!=line and isEdge(s, line):
                myDict[s].add(line)
                myDict[line].add(s)
                numEdges+=1

print("Time taken to create graph: {}".format(time.clock()-start_time))
print(f"Number of vertices: {numVertices}")
print(f"Number of edges: {numEdges}")

if len(sys.argv) > 1:
    word = sys.argv[1]
    neighbors = set()
    for s in myDict:
        if isEdge(word, s):
            neighbors.add(s)
    print(neighbors)

max_neighbors = 0
max_set = set()
for w in myDict:
    if len(myDict[w]) > max_neighbors:
        max_neighbors = len(myDict[w])
        max_set.clear()
        max_set.add(w)
    elif len(myDict[w]) == max_neighbors:
        max_set.add(w)
print(f"The words with the most amount of neighbors ({max_neighbors} neighbors): {max_set}")

connected_max = 0;
connected = 0;
parse_set = set()
parsed_set = set()
connected_set = set()
while len(myDict)>0:
   if len(parse_set) == 0:
       if len(connected_set)>connected_max:
           connected_max = len(connected_set)
       connected+=1
       connected_set.clear()
       key = next(iter(myDict))
       parse_set.add(key)
   else:
       nodes = parse_set.pop()
       if nodes not in parsed_set:
           parsed_set.add(nodes)
           connected_set.add(nodes)
           s = myDict.pop(nodes)
           for x in s:
               parse_set.add(x)

print(f"Number of connected components: {connected}")
print(f"Max number of connected items: {connected_max}")

print("Time taken to finish running: {}".format(time.clock()-start_time))
