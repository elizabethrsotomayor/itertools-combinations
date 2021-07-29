from itertools import combinations

S, k = input().split()

for i in range(1,int(k)+1):
    c = list(combinations(S, i))
    o = []
    for j in c:
        lst = sorted(j)
        t = ''.join(lst)
        o.append(t)
        o.sort()

    for i in o:
        print(i)