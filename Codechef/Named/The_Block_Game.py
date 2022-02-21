ii = lambda: int(input())
imi = lambda: [int(i) for i in input().split()]

for _ in range(ii()):
    x = input()
    if x == x[::-1]:print("wins")
    else:print("loses")