import sys
words = sys.argv[1].split(" ")
vowels = "AEIOUaeiou"
for w in words:
    vcount = 0;
    for c in w:
        if c in vowels:
            vcount+=1
    if vcount >= 3:
        print(w, end=' ')
