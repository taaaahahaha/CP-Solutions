ii = lambda: int(input())
imi = lambda: [int(i) for i in input().split()]

for _ in range(ii()):
    q,p=map(int,input().split())
    if (q>1000):
        ans = q*p*0.9
    else:
        ans = q*p*1.0
    print("%.6f"%ans)
    