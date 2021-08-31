for _ in range(int(input())):
    n = int(input())
    li1 = [int(i) for i in input().split()]
    li2 = [int(i) for i in input().split()]
    lid = [li1[i]-li2[i] for i in range(n)]
    # print(lid)
    d = {}
    if sum(lid)!=0:print(-1)
    else:
        c = 0
        i=0
        while i<n or lid[i] >0:
        
            
            for j in range(n):
                if lid[j]<0:
                    d[i+1] = [j+1]
                    c+=1
                    lid[i] -= 1
                    lid[j] += 1
                    break
            i+=1
        print(c)
        print(d.items)