n=int(input())
temp=n
sum=0
while(temp!=0):
    rem=temp%10
    sum+=(rem**3)
    temp//=10
if(n==sum):print("Armstrong number")
else:print("Not an armstrong number")