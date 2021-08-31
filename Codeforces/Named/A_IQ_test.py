n = int(input())
li = [int(i)%2 for i in input().split()]
c0 = li.count(0)
c1 = li.count(1)
if c0==1:
    print(li.index(0)+1)
else:
    print(li.index(1)+1)
    