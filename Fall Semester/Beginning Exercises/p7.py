import sys
import string

s = sys.argv[1]
s = ''.join(s.split())
translator = str.maketrans('', '', string.punctuation)
print(s.translate(translator))
