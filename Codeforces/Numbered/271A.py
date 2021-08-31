n = int(input()) + 1
n=str(n) 
t=int(n)
c = 0
while len(set(n))!=4:
    t += 1
    n = str(t)
print(n)
