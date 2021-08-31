# Taaha Multani @ https://github.com/taaaahahaha


#Method1

n = int(input())
while(n!=1):
    print(n,end=' ')
    if(n%2==0): n = n//2
    else: n = 3*n+1
 
print("1")

#Method2
# def fun(n):
#     if(n==1):
#         print("1")
#         return
#     if(n%2==0):
#         print(n,end=' ')
#         return fun(n//2)
#     else:
#         print(n,end=' ')
#         return fun(3*n+1)

# n = int(input())
# fun(n)