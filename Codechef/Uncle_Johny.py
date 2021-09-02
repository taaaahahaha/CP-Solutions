for _ in range(int(input())):
    n = int(input())
    li = [int(i) for i in input().split()]
    k = int(input())
    num = li[k-1]
    li.sort()
    print(li.index(num)+1)