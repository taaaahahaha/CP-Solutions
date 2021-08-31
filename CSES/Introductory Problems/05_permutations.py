# Taaha Multani @ https://github.com/taaaahahaha

n = int(input())

if(n==2 or n==3):print("NO SOLUTION")
elif(n==4):print("2 4 1 3")
else:
    if n%2==0:
        for k in range(n,0,-2):print(k,end=" ")
        for k in range(n-1,0,-2):print(k,end=" ")
    else:
        for k in range(n-1,0,-2):print(k,end=" ")
        for k in range(n,0,-2):print(k,end=" ")