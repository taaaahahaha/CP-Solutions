n,m = map(int,input().split())
c=0
n,m = min(n,m),min(n,m)
while n>0 and m>0:
    c+=1
    n-=1
    m-+1

if c%2==0:
    print("Malvika")
else:
    print("Akshat")