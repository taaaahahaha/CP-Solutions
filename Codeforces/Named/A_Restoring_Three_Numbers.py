import math
import sys

ii = lambda: int(sys.stdin.readline())
imi = lambda: map(int,sys.stdin.readline().strip().split())
iil = lambda: [int(i) for i in sys.stdin.readline().split()]
istr = lambda: sys.stdin.readline()
ims = lambda: sys.stdin.readline().split()
isl = lambda: [(i) for i in sys.stdin.readline().split()]

MOD = 1000000007

li = iil()
maxnum = max(li)
li.remove(maxnum)
l = []
for i in li:
    l.append(str(maxnum-i))
print(' '.join(l))
 

#  Output in any order