arr = [1, 2, 8, 3, 2, 2, 2, 5, 1];
ans = [0]*len(arr)

for i in range(len(arr)):
    count = 1
    for j in range(i+1,len(arr)):
        if arr[i] == arr[j]:
            count += 1
            ans[j] = -1
    if ans[i] != -1:
        ans[i] = count
for k in range(len(ans)):
    if ans[k] != -1:
        print(f"Element {arr[k]} = Frequency {ans[k]}")


