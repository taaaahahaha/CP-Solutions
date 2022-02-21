def gcd(a,b):
    if a==0:
        return b

    return gcd(b%a,a)

ii = lambda: int(input())
imi = lambda: [int(i) for i in input().split()]

for _ in range(ii()):
    a,b=map(int,input().split())
    x=gcd(a,b)
    y=(a*b)//x
    print(x,y)

