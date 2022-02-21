ii = lambda: int(input())
imi = lambda: [int(i) for i in input().split()]

for _ in range(ii()):
    n = ii()
    x = input()
    # INDIAN
    # NOT INDIAN
    # NOT SURE
    set_x = set(list(x))
    if "I" in set_x:
        print("INDIAN")
    elif "N" in set_x and len(set_x)==1:
        print("NOT SURE")
    else:
        print("NOT INDIAN")
