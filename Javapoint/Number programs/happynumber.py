def happy(n):
    sum = 0
    while(n!=0):
        rem = n%10
        sum += (rem**2)
        n//=10
    return sum

n = int(input())

while(n!=1 and n!=4):
    n = happy(n)

if n==4: print("Not a Happy number")
elif n==1: print("Happy Number")
