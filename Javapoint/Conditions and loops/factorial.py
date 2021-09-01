n=int(input())
f=1
for i in range(1,n+1):
    f=f*i
if(n>0):print(f)
elif(n==0):print("1")
else:print("Factorial does not exist")