import sys

def isPrime(i):
    for j in range(2,int(i**(1/2))+1):
        if i%j==0:
            return "not prime"
    return "prime"

print(isPrime(int(sys.argv[1])))
