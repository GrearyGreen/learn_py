y = list(input().split())
y.reverse()
x = len(y)
try:
    z = x - y.index('250')
except ValueError:
    z = 0
print(z)