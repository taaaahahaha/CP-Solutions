for _ in range(int(input())):
    n = int(input())
    i=1
    c=0
    while(n>=(5**i)):
        c += n//(5**i)
        i+=1
    print(c)