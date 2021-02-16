x,z = input().split()
x = eval(x)
if ((x/2)*10)%10 <= 4:
    y = x//2
else:
    y = x//2 + 1

for i in range(y):
    print(z*x)