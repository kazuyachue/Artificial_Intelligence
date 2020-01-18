import sys
temp = sys.argv[1].split(" ")
find = temp.pop(0)
repl = temp.pop(0)
word = " ".join(temp)
print(word.replace(find, repl))
