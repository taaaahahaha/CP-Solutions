# Taaha Multani @ https://github.com/taaaahahaha

for _ in range(int(input())):
    e,k = map(int,input().strip().split())
    c = -1
    while e:
        c+=1
        e = round(e/k)
    if k==2:   #*
        c+=1
    print(c)

# In python 3.x the function round(2.5) gives 2
# https://stackoverflow.com/questions/10825926/python-3-x-rounding-behavior

#* A bug if E=1 and K=2 It becomes an Infinite loop
# round(0.5)==1 and 1/2=0.5