for _ in range(int(input())):
    c = 1
    n = input()
    for i in n:
        if int(i) > 1:
            c += (int(i)-1)
    print(c)