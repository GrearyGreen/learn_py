t = eval(input())
x = list(set(t))
x.sort(key = t.index)
print(*x)