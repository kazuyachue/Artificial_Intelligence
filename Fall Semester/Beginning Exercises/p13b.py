import sys
import collections

s = sys.argv[1]
myset = set()
d = {}
for c in s:
    myset.add(c)
for x in myset:
    d[x]=s.count(x)
max_count = 0
for i in d:
    if d[i]>max_count:
        max_count = d[i]
for j in d:
    if d[j] == max_count:
        print(j, end = ' ')
print(str(max_count) + " times.")
