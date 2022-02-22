ii = lambda: int(input())
imi = lambda: [int(i) for i in input().split()]

for _ in range(ii()):
    n , k =map(int,input().split())
    li = [str(i) for i in range(1,n+1)]
    lians = [str(n-k+1)] + [str(i) for i in range(1,n-k+1)] + [str(i) for i in range(n-k+2,n+1)]
    print(' '.join(lians))

