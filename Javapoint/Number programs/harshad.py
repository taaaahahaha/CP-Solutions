def sum(n):
    sum=0
    while(n!=0):
        sum += n%10
        n //=10
    return sum

n = int(input())
temp = n
if temp%sum(n)==0:print("Harshad number")
else:print("Not a harshad number")
