# Taaha Multani @ https://github.com/taaaahahaha

#2x3 in nxn = (n-1)(n-2)
t = int(input())
for n in range(1,t+1):
    print(((n**2)*(n**2-1)//2) - (4*(n-1)*(n-2)))