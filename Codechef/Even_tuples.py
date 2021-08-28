import sys
sys.setrecursionlimit(10**6)


def fact(n):
    if n<=1: return 1
    else: return n*fact(n-1)
    

for _ in range(int(input())):
    n,q = map(int,input().strip().split())
    li_A = [int(i) for i in input().split()] 
    for _ in range(q):
        c_odd,c_even = 0,0
        l,r = map(int,input().strip().split())
        for x in range(l,r+1):
            if x%2==0:c_even+=1
            else:c_odd+=1
        ans = (fact(c_odd)//(2*fact(c_odd-2))*c_even) + (fact(c_even)//(fact(3)*fact(c_even-3)))
        print(ans)
        