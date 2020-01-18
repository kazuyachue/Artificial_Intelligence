import sys

s = sys.argv[1].lower()
vowels = "aeiou"

for c in vowels:
    print(c+":"+str(s.count(c)),end=" ")
