import sys
import re
words = sys.argv[1].split(' ')
find = words.pop(0)
word = " ".join(words)
matches = re.findall(f'(?={find})', word)
print(len(matches))
