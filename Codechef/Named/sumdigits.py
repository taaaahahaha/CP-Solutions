# Taaha Multani @ https://github.com/taaaahahaha

for _ in range(int(input())):
    n = int(input())
    sum=0
    while(n!=0):
        r = n%10
        sum+=r
        n//=10
    print(sum)
