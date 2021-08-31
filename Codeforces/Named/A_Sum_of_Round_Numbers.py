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
    s = str(n)
    li = []
    
    for i in range(len(s)):
        if s[i]!='0':
            li.append(str(s[i])+(len(s)-(i+1))*'0')
    
    print(len(li))
    print(' '.join(li))

#output can be given in any order
    
