d = {'6':0,'7':0,'8':0,'9':0,'10':0}
l = []
x = list(input().split(','))
for i in d:
    for j in x:
        if i == j:
            d[i] = d[i]+1
for i in d:
    if d[i] == 0:
        l.append(i)
print(*l)