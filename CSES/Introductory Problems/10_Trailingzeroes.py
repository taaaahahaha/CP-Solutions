# Taaha Multani @ https://github.com/taaaahahaha

n = int(input())
count = 0
i = 5
while (n/i > 0):
    count += n//i
    i *= 5
print(count)