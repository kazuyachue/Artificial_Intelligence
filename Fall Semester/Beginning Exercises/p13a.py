import sys
import collections

s = sys.argv[1]
print(collections.Counter(s).most_common(1)[0])
