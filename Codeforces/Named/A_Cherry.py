for _ in range(int(input())):
    n = int(input())
    li = [int(i) for i in input().split()]
    ans = 0
    for i in range(len(li)):
        l = []
        l.append(li[i])
        for j in range(i+1,len(li)):
            l.append(li[j])
            soln = max(l)*min(l)
            if soln>ans:ans=soln
    print(ans)

    # l = [li[0],li[1]]
    # ans = l[0]*l[1]
    # if len(li) == 2:
    #     print(ans)
    # else:
    #     if li[1]>li[0]:
    #         ma = li[1]
    #         mi = li[0]
    #     else:
    #         ma = li[0]
    #         mi = li[1]
        
    #     for i in range(3,len(l)):
    #         if li[i]>ma:
    #             mi=li[i]
    #             temp = ma
    #             ma = mi
    #             mi = temp


    #         elif li[i]>mi and li[i]<ma:
                
    #             mi=li[i]
    #     print(mi*ma)