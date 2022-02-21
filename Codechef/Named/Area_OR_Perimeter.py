l = int(input())
b = int(input())

area = l*b
peri = 2*(l+b)

if area==peri:
    print("Eq")
    print(area)
elif area>peri:
    print('Area')
    print(area)
else:
    print('Peri')
    print(peri)