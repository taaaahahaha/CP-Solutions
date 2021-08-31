a = input()
b = input()
c = input()
d = a+b
d = ''.join(sorted(d))
c = ''.join(sorted(c))
print("YES" if d==c else "NO")