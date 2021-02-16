k = 'a'
d = {'a':0}
x = list(input())
for i in x:
    d[i] = 0
for i in x:
    d[i] += 1
    if(d[i] >= d[k]):
        k = i
print("('{}', {})".format(k,d[k]))