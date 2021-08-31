n = int(input())
s = input()
alphabets = "abcdefghijklmnopqrstuvwxyz"
s = ''.join(sorted(list(set((s.lower())))))
print("YES" if s==alphabets else "NO")