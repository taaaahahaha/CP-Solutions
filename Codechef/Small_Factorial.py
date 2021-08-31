# Taaha Multani @ https://github.com/taaaahahaha

def fact(n):
    if n<=1:return 1
    else:return n*fact(n-1)
for _ in range(int(input())):
    print(fact(int(input())))