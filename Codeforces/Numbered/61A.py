n1 = list(input())
n2 = list(input())
ans = ""
for i in range(len(n1)):
    if n1[i]==n2[i]: ans+="0"
    else : ans+="1"
print(ans)