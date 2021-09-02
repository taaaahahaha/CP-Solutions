n = int(input())
t = 0

for i in range(1,n+1):
    li = []
    if t%2==0:
        for x in range(i*5-4,i*5+1):
            li.append(x)
    else:
        for x in range(i*5,i*5-5,-1):
            li.append(x)
    print(" ".join([str(i) for i in li]))
    t+=1