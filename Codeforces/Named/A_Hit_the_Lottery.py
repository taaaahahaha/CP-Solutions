li = [100,20,10,5,1]
n = int(input())
c=0
for i in li:
    notes = n//i
    c+=notes
    n-=(notes*i)
print(c)