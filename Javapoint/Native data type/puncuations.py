punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
s = input("Enter the string")
ans = ""
for char in s:
    if char not in punc:
        ans += char
print(ans)
