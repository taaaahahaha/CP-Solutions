for _ in range(int(input())):
    a,b = map(int,input().split())
    diff = max(a,b)-min(a,b)
    # print(diff)
    if diff%10==0:
        print(diff//10)
    else:
        print(diff//10 + 1)