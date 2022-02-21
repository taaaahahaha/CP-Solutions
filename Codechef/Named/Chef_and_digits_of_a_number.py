for _ in range(int(input())):
    n = input()
    n1 = n.count('0')
    n2 = n.count('1')
    if abs(n1-n2)<2:print("Yes")
    else:print("No")
