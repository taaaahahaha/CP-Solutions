# Taaha Multani @ https://github.com/taaaahahaha

# #TLE exceeded

# a = int(input())
# n = list(map(int,input().strip().split()))
# count = 0
# for i in range(1,a):
#     while (n[i]<n[i-1]):
#         count+=1
#         n[i] += 1
# print(count)

a = int(input())
n = list(map(int,input().strip().split()))
count = 0
for i in range(1,a):
    while (n[i]<n[i-1]):
        count+= n[i-1] - n[i]
        n[i] = n [i-1]
print(count)