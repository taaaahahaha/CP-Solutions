for _ in range(int(input())):
    n = int(input())
    li = [int(i) for i in input().split()]
    s1 , s2 = 0,0
    f=0
    l=n-1
    while f<=l:
        if s1>s2:
            s2 += li[l]
            l -= 1
        else:
            s1 += li[f]
            f += 1
    
    print(max(s1,s2))
