import sys
import string

def punc(s):
    s = ''.join(s.split())
    translator = str.maketrans('', '', string.punctuation)
    return s.translate(translator)

s = sys.argv[1]
s=s.lower()
s=punc(s)

if str(s) == str(s)[::-1]:
    print("Yes")
else:
    print("No")
