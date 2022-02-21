ii = lambda: int(input())
imi = lambda: [int(i) for i in input().split()]
def summ(n):
    return n*(n+1)//2
for _ in range(ii()):
    d,n=map(int,input().split())
    while d>0:
        n=summ(n)
        d-=1
    print(n)