for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
   
    a[a.index(max(a))] = min(a)

    i = min(a)
    while(True):
        c=0
        for x in a:
            if x%i!=0:c=1
        if c==0 : 
            for o in a:
                c+= o//i
            print(c)
            break
        i-=1
    
