import sys
word = sys.argv[1]

for c in word:
    if word.count(c)==1:
        print(c)
        break
