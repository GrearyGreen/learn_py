x = 0
y = 0
n = int(input())
for i in range(n):
    l = list(input().split())
    s = set(l)
    if len(l) != len(s):
        y += 1
    else:
        x += 1
print('True={}, False={}'.format(y,x))