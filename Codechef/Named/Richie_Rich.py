for _ in range(int(input())):
    a,b,x=map(int,input().strip().split())
    c=0
    while(a<b):
        c+=1
        a+=x
    print(c)