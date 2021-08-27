def iil():
    return [int(i) for i in input().split()]
def imi():
    return map(int,input().strip().split())
def ii():
    return int(input())


def subs(l1,l2):
    li = []
    for i in l1+l2:
        if not(i in l1 and i in l2):
            li.append(i)
        if i in l1 and i not in l1:
            li.append(i)
    return li



for _ in range(ii()):
    n,m = imi()
    done = iil()
    total = list(range(1,n+1))
    rem = subs(total,done)
    rem.sort()
    chef = []
    ass = []
    for i in range(0,len(rem)):
        if i%2==0:
            chef.append(rem[i])
        else:
            ass.append(rem[i])
    
    print(' '.join([str(i) for i in chef]))
    print(' '.join([str(i) for i in ass]))


# for _ in range(int(input())):
    

#     n,m=map(int,input().split())
#     st = set([str(i) for i in range(1,n+1)])
    
#     li = [i for i in input().split()]
#     li.sort()
#     s = set(li)
#     d_s = list(st.difference(s))
    
#     chef = []
#     ass = []
#     for x in range(len(d_s)):
#         if x%2==0:chef.append(d_s[x])
#         else:ass.append(d_s[x])
#     print(' '.join(sorted(chef)))
#     print(' '.join(sorted(ass)))


