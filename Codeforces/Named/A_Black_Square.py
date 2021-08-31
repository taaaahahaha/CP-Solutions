li = [int(i) for i in input().split()]
l = [int(i) for i in input()]

s=0

for i in l:
    s+=li[i-1]

print(s)