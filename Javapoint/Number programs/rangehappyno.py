def happy(n):
    sum = 0
    while(n!=0):
        rem = n%10
        sum += (rem**2)
        n//=10
    return sum

l = int(input("Enter lower bound : "))
h = int(input("Enter upper bound : "))

for n in range(l,h+1):
    temp=n

    while(n!=1 and n!=4):
        n = happy(n)

    if n==1: print(temp)
