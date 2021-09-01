lower_r = int(input("Enter lower range: "))
upper_r = int(input("Enter Upper range: "))
for i in range(lower_r,upper_r+1):
    temp=i
    sum=0
    while(temp!=0):
        rem=temp%10
        sum+=(rem**3)
        temp//=10
        if(i==sum):print(i)
        