for _ in range(int(input())):
    n = int(input())
    li = [int(i) for i in input().split()]
    max_num = max(li)
    min_num = min(li)
    li = sorted(list(set(li)))
    arr = [i for i in range(min_num,max_num+1)]
    if li==arr:print("YES")
    else:print("NO")