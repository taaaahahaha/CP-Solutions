ii = lambda: int(input())
imi = lambda: [int(i) for i in input().split()]

for _ in range(ii()):
    n,k = map(int,input().split())
    li = imi()
    li.sort()
    lians = ['x' for i in range(n)]
    # print(lians,len(lians))
    liansfin = []
    c = 1
    m = 0
    for i in li:
        minilist = lians[m:i]
        m=i
        # print(minilist)
        # lians[i-1] = c
        # c += 1
        minilist[-1] = str(c)
        c += 1
        for i in range(len(minilist)):
            if minilist[i] == 'x':
                minilist[i] = str(c)
                c+=1
        liansfin += minilist
    
    print(' '.join(liansfin))
    