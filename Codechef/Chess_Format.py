for _ in range(int(input())):
    a,b = map(int,input().strip().split())
    r = a+b
    if r<3:print(1)
    elif r<11:print(2)
    elif r<61:print(3)
    else:print(4)