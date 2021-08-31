n = int(input())
li = [int(i) for i in input().split()]
max = max(li)
min = min(li)
c = 0
max_ind = li.index(max)
min_ind = n-(li[::-1].index(min))-1
# print(max_ind,min_ind)
if max_ind>min_ind:print(max_ind+(n-min_ind-1-1))
else:print(max_ind+(n-min_ind-1))