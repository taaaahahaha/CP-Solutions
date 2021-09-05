for _ in range(int(input())):
    k = int(input())

    if k==1:print(1)
    elif k==2:print(2)
    else:
        k-=2
        n=3
        while k!=0:
            n+=1
            if n%10!=3 and n%3!=0:k-=1

        print(n)
