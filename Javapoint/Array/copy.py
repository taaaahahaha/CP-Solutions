# a = input().strip().split()
# a2=a.copy()
# print(a2)

a = [1,2,3,4,5]
s2 = [None]*len(a);
for i in range(len(a)):
    s2[i]=a[i]
for i in range(len(s2)):
    print(s2[i])