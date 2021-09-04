# Copyright ⒸTaaha Multani @https://github.com/taaaahahaha
# https://projecteuler.net/problem=2

def fibo(n,memo={}):
    if n<=2:return 1
    else:
        if n in memo.keys():return memo[n]
        else: 
            memo[n] = fibo(n-1,memo) + fibo(n-2,memo)
            return memo[n]

sum = 0
for i in range(1,50):
    x = fibo(i)
    if x%2==0:
        sum+=x
    if x>4000000:
        break
print(sum)

