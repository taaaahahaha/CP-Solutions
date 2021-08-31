for _ in range(int(input())):
    n = int(input())
    c = 0
    t = 1
    while t<=n:
        for i in range(1,10):
            if t*i<=n:
                c+=1
        t = t*10 + 1

    print(c)
    


        


