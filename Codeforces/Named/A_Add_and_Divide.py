def xd(a,b):
    c = 0
    while a!=0:
        a = a//b
        c+=1
    return c

for _ in range(int(input())):
    a,b = map(int,input().split())
    c = 0
    while a!=0:
        if a==b or b==1 or xd(a,b+1)<xd(a,b):
            b+=1
        else:
            a=a//b
        c+=1
        
        
    print(c)

    668.5
