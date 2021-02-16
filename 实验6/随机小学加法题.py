import random as r
x,y = input().split()
r.seed(int(x))
for i in range(1,int(y)+1):
    a = r.randint(1,9)
    b = r.randint(1,9)
    print("{}+{}=".format(a,b))