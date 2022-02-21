ii = lambda: int(input())
imi = lambda: [int(i) for i in input().split()]

for _ in range(ii()):
    a,b,c=map(float,input().split())
    hardness = a>50
    carbon_content = b<0.7
    tensile_strength = c>5600

    if hardness and carbon_content and tensile_strength:
        print("10")
    elif hardness and carbon_content:
        print('9')
    elif carbon_content and tensile_strength:
        print('8')
    elif hardness and tensile_strength:
        print('7')
    elif hardness or carbon_content or tensile_strength:
        print('6')
    else:
        print('5')