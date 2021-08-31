import math
import sys

ii = lambda: int(sys.stdin.readline())
imi = lambda: map(int,sys.stdin.readline().strip().split())
iil = lambda: [int(i) for i in sys.stdin.readline().split()]
istr = lambda: sys.stdin.readline()
ims = lambda: sys.stdin.readline().split()
isl = lambda: [(i) for i in sys.stdin.readline().split()]

MOD = 1000000007

n,k = imi()
n = int(str(n)[-1])
t = n
if n==k or n==0:
    print(1)
else:
    c=0
    i=1
    while str(n)[-1]!='0' and str(n)[-1]!=str(k):
        n = t * i
        i+=1
        c+=1
    print(c)
