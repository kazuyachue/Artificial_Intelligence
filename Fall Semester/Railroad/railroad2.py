import sys
import time
from math import *
from heapq import heappush, heappop
import tkinter

start_time = time.clock()
global smallest_longitude
smallest_longitude = sys.float_info.max
global biggest_latitude
biggest_latitude = 0
global scale
global offset

#haversine distance
def distance(x, y):
    lat1 = radians(x[0])
    lat2 = radians(y[0])
    long1 = radians(x[1])
    long2 = radians(y[1])
    delta_latitutude = lat1 - lat2
    delta_longitude = long1 - long2
    a = sin(delta_latitutude/2) ** 2 + cos(lat1) * cos(lat2) * sin(delta_longitude/2) ** 2
    c = 2 * atan2(a**0.5, (1-a)**0.5)
    return 6371 * c

def printPath(c, d, dist):
    l = []
    while not c == "":
        l.append(c)
        c = d[c]
    for x in l[::-1]:
        if x in key_city:
            print(key_city[x])
        else:
            print(x)
    print(f"Total distance travelled: {dist}km")

def drawPath(c, d, canvas, root):
    count = 0
    city = c
    while not d[city] == "":
        city2 = d[city]
        #print(scale * (key_location[city][1] - smallest_longitude) + offset, scale * (biggest_latitude - key_location[city][0]), scale * (key_location[city2][1]-smallest_longitude) + offset, scale * (biggest_latitude - key_location[city2][0]))
        canvas.create_line(scale * (key_location[city][1] - smallest_longitude) + offset, scale * (biggest_latitude - key_location[city][0]), scale * (key_location[city2][1]-smallest_longitude) + offset, scale * (biggest_latitude - key_location[city2][0]), fill = "red")
        if count%10 == 0:
             root.update()
        city = city2
        count+=1

key_city = {}
city_key = {}
key_location = {}
edges_dict = {}

with open("rrNodeCity.txt","r") as f:
    for line in f:
        l = line.strip().split(" ")
        key_city[l[0]] = ' '.join(l[1:])
        city_key[' '.join(l[1:])] = l[0]

with open("rrNodes.txt","r") as f:
    for line in f:
        l = line.strip().split(" ")
        key_location[l[0]] = (float(l[1]), float(l[2]))
        if float(l[1]) > biggest_latitude:
            biggest_latitude = float(l[1])
        if float(l[2]) < smallest_longitude:
            smallest_longitude = float(l[2])

with open("rrEdges.txt") as f:
    for line in f:
        l = line.strip().split(" ")
        if l[0] not in edges_dict:
            edges_dict[l[0]] = []
        edges_dict[l[0]].append(l[1])
        if l[1] not in edges_dict:
            edges_dict[l[1]] = []
        edges_dict[l[1]].append(l[0])

root = tkinter.Tk()
canvas = tkinter.Canvas(root, width = 1000, height=500)
canvas.pack()
scale = 11
offset = 100
for city in edges_dict.keys():
    for city2 in edges_dict[city]:
        canvas.create_line(scale * (key_location[city][1] - smallest_longitude) + offset, scale * (biggest_latitude - key_location[city][0]), scale * (key_location[city2][1]-smallest_longitude) + offset, scale * (biggest_latitude - key_location[city2][0]))

s = sys.argv[1].split(" ")
if s[0] in city_key:
    start = city_key[s[0]]
    goal = city_key[' '.join(s[1:])]
else:
    start = city_key[' '.join(s[0:2])]
    goal = city_key[' '.join(s[2:])]

closedSet = {start: ""}
openSet = list()
parentDict = {start: ""}
open_counter = 0
closed_counter = 0
done = False

heuristic = distance(key_location[start], key_location[goal])
heappush(openSet, (heuristic, start, 0))
while len(openSet) > 0:
    if done:
        break
    tup = heappop(openSet)
    current_city = tup[1]
    for city in edges_dict[current_city]:
        dist = tup[2] + distance(key_location[current_city], key_location[city])
        if city == goal:
            closedSet[city] = current_city
            closedSet[current_city] = parentDict[current_city]
            done = True
            printPath(city, closedSet, dist)
            drawPath(city, closedSet, canvas, root)
            break
        if city in closedSet:
            continue
        heuristic = distance(key_location[city], key_location[goal]) + dist
        heappush(openSet, (heuristic, city, dist))
        canvas.create_line(scale * (key_location[current_city][1] - smallest_longitude) + offset, scale * (biggest_latitude - key_location[current_city][0]), scale * (key_location[city][1]-smallest_longitude) + offset, scale * (biggest_latitude - key_location[city][0]), fill = "blue")
        if open_counter % 10000 == 0:
            root.update()
        open_counter+=1
        if city not in parentDict.keys():
            parentDict[city] = current_city
    closedSet[current_city] = parentDict[current_city]
    if closedSet[current_city] != "":
        canvas.create_line(scale * (key_location[current_city][1] - smallest_longitude) + offset, scale * (biggest_latitude - key_location[current_city][0]), scale * (key_location[closedSet[current_city]][1]-smallest_longitude) + offset, scale * (biggest_latitude - key_location[closedSet[current_city]][0]), fill = "green")
    if closed_counter % 5000 == 0:
        root.update()
    closed_counter+=1

root.mainloop()

print("Total time: {}".format(time.clock()-start_time))
