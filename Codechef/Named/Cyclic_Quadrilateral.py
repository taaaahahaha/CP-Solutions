for _ in range(int(input())):
    a,b,c,d = map(int,input().strip().split())
    if a+c==b+d==180:print("YES")
    else:print("NO")