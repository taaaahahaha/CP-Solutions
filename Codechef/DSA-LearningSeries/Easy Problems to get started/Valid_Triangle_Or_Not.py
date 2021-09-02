a,b,c = map(int,input().split())
# c = "NO"
if (a+b)>=c and (a+c)>=b and (b+c)>=a:
    print("YES")
else:print("NO")