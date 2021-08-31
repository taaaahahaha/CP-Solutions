n = int(input())
li = [int(i) for i in input().split()]
print(' '.join([str(i) for i in sorted(li)]))