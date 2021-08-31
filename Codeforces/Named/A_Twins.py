n = int(input())
li = [int(i) for i in input().split()]
li.sort(reverse = True)
st = sum(li)
s = 0
c = 0
for i in li:
    s+=i
    c+=1
    if s>st-s:break
print(c)
