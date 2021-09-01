def pronic(n):
    for i in range(n+1):
        if i==n+1:
            return False
        else:
            if i * (i+1) == n:
                return True
    

l = int(input("Enter lower bound : "))
h = int(input("Enter upper bound : "))

for n in range(l,h+1):
    if(pronic(n)):print(n)
