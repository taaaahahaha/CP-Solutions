n,m = map(int,input().strip().split())
if n*m>=2:
    if (n*m)%2==0:
        print((n*m)//2)
    else:
        print((n*m-1)//2)
else:
    print("0")