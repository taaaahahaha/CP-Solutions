import math
import sys

ii = lambda: int(sys.stdin.readline())
imi = lambda: map(int,sys.stdin.readline().strip().split())
iil = lambda: [int(i) for i in sys.stdin.readline().split()]
istr = lambda: sys.stdin.readline()
ims = lambda: sys.stdin.readline().split()
isl = lambda: [(i) for i in sys.stdin.readline().split()]

MOD = 1000000007

for _ in range(ii()):
    n = ii()
    if n%4!=0:
        print('NO')
    else:
        print("YES")
        li = []
        for i in range(2,n+1,2):
            li.append(i)
        i=0
        for j in range(n//2-1):
            li.append(li[j]-1)
            i+=1
        li.append(li[n//2-1]+i)
        print(' '.join([str(i) for i in li]))
