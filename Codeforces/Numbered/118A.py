s = list(input())
sn = []
for i in s:
    if i=="A" or i=='a' or i=="E" or i=="Y" or i=='y' or i =="e" or i=="I" or i=='i' or i=="o" or i=="O" or i=="u" or i=="U":continue
    elif i>='A' and i<="Z": sn+= "."+i.lower()
    else:sn+="."+i
print(''.join(sn))