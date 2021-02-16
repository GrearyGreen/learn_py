x = int(input())
n = 0
for i in range(x,x+4):
    for j in range(x,x+4):
        if(i == j):
            continue
        for k in range(x,x+4):
            if(k == i):
                continue
            if(k == j):
                continue
            n = n+1
            if n%6 == 0:
                print("{:<3}".format(i*100+j*10+k))
            else:
                print("{:<4}".format(i*100+j*10+k),end = '')