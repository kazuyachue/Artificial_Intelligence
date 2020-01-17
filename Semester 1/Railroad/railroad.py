import sys
import time
from math import *
import tkinter

start_time = time.clock()
smallest_longitude = sys.float_info.max
biggest_latitude = 0
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

letter_name = {}
letter_location = {}
edges_dict = {}

with open("romFullNames.txt","r") as f:
    for line in f:
        line = line.strip()
        letter_name[line[0]] = line

with open("romNodes.txt","r") as f:
    for line in f:
        l = line.strip().split(" ")
        letter_location[l[0]] = (float(l[1]), float(l[2]))
        if float(l[1]) > biggest_latitude:
            biggest_latitude = float(l[1])
        if float(l[2]) < smallest_longitude:
            smallest_longitude = float(l[2])

with open("romEdges.txt") as f:
    for line in f:
        l = line.strip().split(" ")
        try:
            edges_dict[l[0]].add(l[1])
        except KeyError:
            edges_dict[l[0]] = set(l[1])

root = tkinter.Tk()
canvas = tkinter.Canvas(root, width = 1000, height=500)
canvas.pack()
scale = 100
offset = 30
total_distance = 0
for city in edges_dict.keys():
    for city2 in edges_dict[city]:
        canvas.create_line(scale * (letter_location[city][1] - smallest_longitude) + offset, scale * (biggest_latitude - letter_location[city][0]) + offset, scale * (letter_location[city2][1]-smallest_longitude) + offset, scale * (biggest_latitude - letter_location[city2][0]) + offset)
        total_distance += distance(letter_location[city], letter_location[city2])

root.mainloop()

print(f"Total distance: {total_distance}km")
print("Total time: {}".format(time.clock()-start_time))
