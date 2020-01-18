import sys
num = int(sys.argv[1])

def fib(x):
    if x==0 or x==1:
        return 1
    else:
        return fib(x-1)+fib(x-2)

for i in range(num-1):
    print(fib(i), end=',')
print(fib(num-1))
