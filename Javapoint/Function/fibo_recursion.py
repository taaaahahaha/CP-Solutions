def recursion(n):
    if n<=1:
        return 1
    else:
        return (recursion(n-1)+recursion(n-2))




n=int(input("Enter a digit greater than 0"))
for i in range(n):
    print(recursion(i))