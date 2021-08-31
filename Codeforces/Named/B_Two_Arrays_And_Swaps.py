import math
import sys

ii = lambda: int(sys.stdin.readline())
imi = lambda: map(int,sys.stdin.readline().strip().split())
iil = lambda: [int(i) for i in sys.stdin.readline().split()]
istr = lambda: sys.stdin.readline()
ims = lambda: sys.stdin.readline().split()
isl = lambda: [(i) for i in sys.stdin.readline().split()]

MOD = 1000000007

for _ in range(int(ii())):
    n,k=imi()
    lia = iil()
    lib = iil()

    i=0
    while i<k and max(lib)>min(lia):
        temp = min(lia)
        lia[lia.index(min(lia))]=max(lib)
        lib[lib.index(max(lib))]=temp

        i+=1

    print(sum(lia))

