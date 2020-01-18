import sys
digits = "1234567890"
word = sys.argv[1]
b = True
for letter in word:
    if letter not in digits:
        b = False
if b:
    print("only digits")
else:
    print("not only digits")
