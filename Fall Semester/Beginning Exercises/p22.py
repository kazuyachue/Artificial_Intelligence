import sys

words = sys.argv[1].split(" ")
newwords = []
for w in words:
    newwords.append(w[::-1])
print(" ".join(newwords))
