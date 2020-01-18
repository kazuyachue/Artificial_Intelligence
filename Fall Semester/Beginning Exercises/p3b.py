import sys
my_list = []

for i in range(1, len(sys.argv)):
  if(int(sys.argv[i])%3==0):
      my_list.append(sys.argv[i])

print(my_list)
