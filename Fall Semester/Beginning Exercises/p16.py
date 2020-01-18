import sys
word = sys.argv[1]
maxdiff = 0;
l = []

for i in range(len(word)-1):
    if abs(ord(word[i+1])-ord(word[i])) > maxdiff:
        maxdiff = abs(ord(word[i+1])-ord(word[i]))
        l = [word[i], word[i+1]]
print(l)
