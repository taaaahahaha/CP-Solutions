# Taaha Multani @ https://github.com/taaaahahaha

n,no_q = map(int,input().strip().split())
Ai = [int(i) for i in input().split()]
for i in range(no_q):
    li = [int(x) for x in input().split()]
    if li[0]==1 : 
    	for i in range(li[1],li[2]+1):
        	Ai[i-1]  += (li[3]+i-li[1])**2
    elif li[0]==2 : print(Ai[li[1]-1])