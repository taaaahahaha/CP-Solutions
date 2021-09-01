def hcf(n1,n2):
    for i in range(min(n1,n2),0,-1):
        if n1%i==0 and n2%i==0:
            return i

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
print(f"HCF of the numbers {n1} and {n2} are {hcf(n1,n2)}")