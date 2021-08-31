def isPrime(n):
    for i in range(2,n):
        if n%i==0:return False
    return True


for _ in range(int(input())):
    d = int(input())
    ans = 1
    i = 0
    fact = (1+d)
    while i<2:
        if isPrime(fact):
            ans *= fact
            fact += d
            i+=1
        else:
            fact += 1
    print(ans)
    
