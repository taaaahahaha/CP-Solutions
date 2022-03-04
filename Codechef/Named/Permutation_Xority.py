for _ in range(int(input())):
    n = int(input())
    if n%2!=0:
        # print('odd',n)
        print(' '.join([str(i) for i in range(1,n+1)]))
    else:
        if n==2:
            print(-1)
        elif n==4:
            print("1 4 2 3")
        else:
            # print("even")
            li = [str(n-1),str(n),str(n-3),str(n-2),str(n-4)] + [str(i) for i in range(n-5,0,-1)]
            print(' '.join(li))
