s = list(input())
y = list(input().split())
for i in range(len(s)-1,-1,-1):
    if s[i] == y[0]:
        print(i,s[i])
    if s[i] == y[1]:
        print(i,s[i])