l = int(input("Enter lower bound : "))
h = int(input("Enter upper bound : "))
for n in range(l,h+1):
    temp = n
    len=0
    sum = 0
    while(n!=0):
        n //= 10
        len += 1
    n = temp
    while(n!=0):
        sum  += (n%10)**len
        len -= 1
        n//=10
    if(sum == temp): print(temp,end=" ")
    

