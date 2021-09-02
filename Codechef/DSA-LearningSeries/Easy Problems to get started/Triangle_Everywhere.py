
a,b,c = map(int,input().strip().split())

if ((a+b)>c and (a+c)>b and (b+c)>a):
    ans=True
else:ans=False

if ans:
    if a==b and a==c and b==c:
        print("1")
    elif a==b or a==c or b==c:
        print("2")
    else:
        print("3")

else:
    print("-1")