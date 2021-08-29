for _ in range(int(input())):
    l1 = list(map(int,input().strip().split()))
    l2 = list(map(int,input().strip().split()))
    ans = 0
    for i in range(3):
        if l1[i]>l2[i] : ans += 1
        else:ans -=1
    print("A" if ans>0 else "B")