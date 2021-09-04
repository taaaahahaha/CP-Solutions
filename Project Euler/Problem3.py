# Copyright ⒸTaaha Multani @https://github.com/taaaahahaha
# https://projecteuler.net/problem=3


def SOE(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
                for i in range(p * 2, n + 1, p):
                    prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    li = []
    for p in range(n + 1):
        if prime[p]:
            li.append(p),
    return li[-1]




n = 600851475143
print(SOE(n))
