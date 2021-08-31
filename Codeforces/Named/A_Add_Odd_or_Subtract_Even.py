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
    a,b = imi()
    if a==b:
        print(0)
    elif a<b:
        if (b-a)%2!=0:
            print(1)
        else:
            print(2)
    else:
        if (a-b)%2==0:
            print(1)
        else:
            print(2)