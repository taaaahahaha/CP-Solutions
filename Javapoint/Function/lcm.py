def lcm(n1,n2):
    greater = max(n1,n2)
    while True:
        if greater%n1==0 and greater%n2==0:
            return greater
        else: greater+=1

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
print(f"Lcm of the numbers {n1} and {n2} are {lcm(n1,n2)}")

