x = eval(input())
y = map(int,input().split())
y = sorted(y)
del  y[0]
del  y[0]
del  y[-1]
del  y[-1]
z = sum(y)/(x-4)
print("aver={:.2f}".format(z))