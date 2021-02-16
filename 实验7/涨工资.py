t = list(map(eval,input().split()))
s = [i*1.5 if i<5000 else i for i in t]
print(*s)