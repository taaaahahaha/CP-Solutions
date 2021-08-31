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
    li = iil()
    lenli = len(li)
    i=0
    l = []
    while i<lenli:
        if i%2==0:
            l.append(str(li.pop(0)))
        else:
            l.append(str(li.pop()))


        i+=1
    print(' '.join(l))