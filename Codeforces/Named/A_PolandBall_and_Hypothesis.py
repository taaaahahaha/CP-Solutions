def isPrime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

n = int(input())
for i in range(1,1001):
    if not isPrime(n*i + 1):
        print(i)
        break
