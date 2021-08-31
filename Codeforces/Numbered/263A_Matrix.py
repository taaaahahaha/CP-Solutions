matrix = []

for i in range(5):
    matrix.append([int(i) for i in input().split()])

for r in range(5):
    for c in range(5):
        if matrix[r][c] == 1 :
            x,y = r+1,c+1

print(abs(3-x)+abs(3-y))