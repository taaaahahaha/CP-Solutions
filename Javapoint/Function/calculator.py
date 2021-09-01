def add(n1,n2):
    return n1+n2
def diff(n1,n2):
    return n1-n2
def mult(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
print('''Enter the choices:
Add = 1
Substract = 2
Divide = 3
Multiply = 4''')
c = input()
if(c=="1"):print(add(n1,n2))
elif(c=="2"):print(diff(n1,n2))
elif(c=="4"):print(mult(n1,n2))
elif(c=="3"):print(div(n1,n2))
else:print("Wrong input")