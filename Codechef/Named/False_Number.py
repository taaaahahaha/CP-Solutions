for _ in range(int(input())):
    n = input()
    l = list(n)
    l1 = l.copy()
    l2 = l.copy()
    l1.insert(1,'0')
    n1 = int(''.join(l1))
    l2.insert(0,'1')
    n2 = int(''.join(l2))
    print(n1 if n1<n2 else n2)
    




