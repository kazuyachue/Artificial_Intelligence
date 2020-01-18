import sys
from collections import OrderedDict
foo = sys.argv[1]
print ("".join(OrderedDict.fromkeys(foo)))
