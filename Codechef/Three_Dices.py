for _ in range(int(input())):
    a,b = map(int,input().strip().split())
    if a+b>=6 : print("0")
    else:
        
        ans = str((6-(a+b))/6)

        print(ans[:8])