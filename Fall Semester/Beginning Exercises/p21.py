import sys
allowed = "1234567890abcdefABCDEF"
word = sys.argv[1]
b = True
for letter in word:
    if letter not in allowed:
        b = False
if b:
    print(int(word, 16))
