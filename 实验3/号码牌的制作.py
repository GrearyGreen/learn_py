s = input()
c1 = s[0]
c2 = s[1]
c3 = s[2]
x = s[3:]
k = len(x)
print('{}{}{}'.format(c1,c2*k,c1))
print('{}{}{}'.format(c3,x,c3))
print('{}{}{}'.format(c1,c2*k,c1))