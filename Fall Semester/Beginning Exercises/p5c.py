import sys

def isPrime(i):
    for j in range(2,int(i**(1/2))+1):
        if i%j==0:
            return False
    return True

if len(sys.argv)==2:
    print(isPrime(int(sys.argv[1])))
else:
    for i in range(int(sys.argv[1])+1, int(sys.argv[2])):
        if isPrime(i):
            print(i,end=' ')
