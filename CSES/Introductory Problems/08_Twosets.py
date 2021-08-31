# Taaha Multani @ https://github.com/taaaahahaha

# import math                                   #Use pypy3 for submission
# n = int(input())
# sum = n*(n+1)/2
# if(sum%2!=0 or n==2):print("NO")
# else:
#     print("YES")
#     if(n%2==0):
#         print(n//2)
#         a = []
#         for i in range(1,n+1): a.append(i)
#         for i in range(n//4):
#             print(a[i],end=" ")
#         for i in range((3*n)//4,n):
#             print(a[i],end=" ")
#         print("")
#         print(n//2)
#         for i in range(n//4,(3*n)//4):
#             print(a[i],end=" ")
#     else:
#         a = [1,2]
#         b = [3]
#         r = (n-3)//2
#         for i in range(1,r+1):
#             a2 = n-(3*i)
#             a.append(a2)
#             a.append(a2+3)
#             b.append(a2+1)
#             b.append(a2+2)
#         print(math.ceil(n/2))
#         for i in range(math.ceil(n/2)):
#             print(a[i],end=" ")
#         print(" ")
#         print(math.floor(n/2))
#         for i in range(math.floor(n/2)):
#             print(b[i],end=" ")                                       



n = int(input())
if ((n*(n+1)//2)%2!=0):
    print('NO')
else:
    arr1 = []
    arr2 = []
    j = n
    if (n%2 == 0):
        i = 1
    else:
        arr1.append(1)
        arr1.append(2)
        arr2.append(3)
        i = 4
    while (i < j):
        arr1.append(i)
        i += 1
        arr2.append(i)
        i += 1
        arr1.append(j)
        j -= 1
        arr2.append(j)
        j -= 1
    print('YES')
    print(len(arr1))
    for a1 in arr1:
        print(a1, end=" ")
    print(" ")
    print(len(arr2))
    for a2 in arr2:
        print(a2, end=" ")
    print()