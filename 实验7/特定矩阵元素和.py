n = int(input())
x = 0
y = n-1
s = 0
for i in range(n):
    t = list(map(float,input().split()))
    s += t[x]
    if x != y:
        s += t[y]
    x += 1
    y -= 1
print(f'{s:.2f}')