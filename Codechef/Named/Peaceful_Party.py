ii = lambda: int(input())
imi = lambda: [int(i) for i in input().split()]

for _ in range(ii()):
    a,b,c = map(int,input().split())
    print(max((a+c),b))