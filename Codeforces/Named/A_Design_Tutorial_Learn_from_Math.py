import math
import sys

ii = lambda: int(sys.stdin.readline())
imi = lambda: map(int,sys.stdin.readline().strip().split())
iil = lambda: [int(i) for i in sys.stdin.readline().split()]
istr = lambda: sys.stdin.readline()
ims = lambda: sys.stdin.readline().split()
isl = lambda: [(i) for i in sys.stdin.readline().split()]

MOD = 1000000007

def SOE(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
                for i in range(p * 2, n + 1, p):
                    prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    li = []
    for p in range(n + 1):
        if prime[p]:
            li.append(p),
    return li


n = ii()
li = SOE(n)
a=4
b=n-4
while a in li or b in li:
    a+=1
    b-=1
print(a,b)