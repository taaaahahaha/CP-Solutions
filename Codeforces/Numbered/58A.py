s = list(input())
h = "hello"
x=0
for i in s:
    if i==h[x]:
        x+=1
    if x==5:
        print("YES")
        break
else:print("NO")