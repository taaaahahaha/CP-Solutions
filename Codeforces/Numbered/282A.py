count  = 0
for _ in range(int(input())):
    x = input()
    if x == "++X" or x == "X++" : count += 1
    else: count -= 1
print(count)  