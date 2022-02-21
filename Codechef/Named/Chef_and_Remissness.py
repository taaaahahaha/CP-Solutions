ii = lambda: int(input())
imi = lambda: [int(i) for i in input().split()]

for _ in range(ii()):
    a,b=map(int,input().split())
    print(max(a,b),a+b)