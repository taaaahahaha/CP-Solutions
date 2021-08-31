import math
n = int(input())
li = [int(i) for i in input().split()]
c = 0
c_3 = 0
c_1 = 0
c_2 =0
for i in range(len(li)):
    if li[i] == 4:
        c+=1
        li[i] == 0
    elif li[i]==3:
        c_3+=1
    elif li[i]==1:
        c_1+=1
    else:
        c_2+=1
    if c_1 > 0 and c_3>0:
            c_3-=1
            c_1-=1
            c+=1
    if c_2 >=2 :
        c+=1
        c_2-=2
c += c_3
if c_2>0:
    if c_1>0:
        c_2 -= 1 
        c_1 -= 2
        c+=1 
    else:
        c_2 -= 1 
        c+=1 
c+=math.ceil(c_1/4)
print(c)