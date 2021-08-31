n = int(input())
c=0
ans = 0
i=1
while True:
    ans += ((i*(i+1))//2)
    if ans<=n:
        c+=1
    else:
        print(c)
        break
    i+=1




