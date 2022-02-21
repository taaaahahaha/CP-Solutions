ii = lambda: int(input())
imi = lambda: [int(i) for i in input().split()]

for _ in range(ii()):
    a = input().upper()
    if a=="B":print("BattleShip")
    elif a=='C':print("Cruiser")
    elif a=='F':
        print("Frigate")
    else:
        print("Destroyer")