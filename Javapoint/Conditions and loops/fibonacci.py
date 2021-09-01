n=int(input())
a,b=0,1
print("0,1",end=',')
for i in range(n-2):
    t=b
    b=a+b
    a=t
    print(b,end=",")