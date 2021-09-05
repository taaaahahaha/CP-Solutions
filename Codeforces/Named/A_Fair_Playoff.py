for _ in range(int(input())):
    li = [int(i) for i in input().split()]
    temp = li.copy()
    max_1 = li.pop(li.index(max(li)))
    max_2 = li.pop(li.index(max(li)))
    xx = [max_1,max_2]
    m1,m2 = (max(temp[0],temp[1]),max(temp[2],temp[3]))
    max_li = [m1,m2]
    
    # print(xx,max_li)
    xx.sort()
    max_li.sort()

    if xx == max_li:print("YES")
    else:print("NO")