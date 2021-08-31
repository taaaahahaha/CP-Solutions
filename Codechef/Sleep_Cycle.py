# Taaha Multani @ https://github.com/taaaahahaha

for _ in range(int(input())):
    l,h = map(int,input().strip().split())
    s = input()
    str = s.split('1')
    str.sort(reverse=True)
    flag = 0
    for x in str:
        l = len(x)
        h = h-l
        if h<=0:
            flag=1
            break
        else: 
            h = 2*h

    if flag==0:print("NO")
    else:print("YES")
