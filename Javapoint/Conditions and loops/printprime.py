n1=int(input("Lower range"))
n2=int(input("Upper range"))
for i in range(n1,n2+1):
    c=0
    for j in range(1,i+1):
        if i%j==0:c+=1
    if c==2:print(i)