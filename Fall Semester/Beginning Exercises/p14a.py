import sys
words = sys.argv[1].split(" ")
vowels = "AEIOUaeiou"
for w in words:
    if w[0] in vowels and w[-1] in vowels:
        print(w, end=' ')
