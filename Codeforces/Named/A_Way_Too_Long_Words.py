for i in range(int(input())):
    w = input()
    li = list(w)
    nw = li[0] + str(len(w)-2) +li[-1]
    if (len(w)>10):print(nw)
    else:print