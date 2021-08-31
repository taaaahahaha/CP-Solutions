n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
a.pop(0)
b.pop(0)
ans = set(a+b)
ans.discard(0)
if n==len(ans):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")

