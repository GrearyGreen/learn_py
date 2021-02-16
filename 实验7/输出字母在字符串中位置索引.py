s = input()
t = input().split()
n = len(s)
for i in range(n-1,-1,-1):
    if s[i] in t:
        print(i,s[i])