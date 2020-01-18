import sys
str = sys.argv[1]
str2 = ""

for x in range(len(str)):
  if x%2==0:
    str2+=str[x]

print(str2)
