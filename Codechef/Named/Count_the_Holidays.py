for _ in range(int(input())):
    n = int(input())
    li = [int(i) for i in input().split()]
    holidays = [6,7,13,14,20,21,27,28]
    for i in li:
        if i not in holidays:
            holidays.append(i)
    print(len(holidays))