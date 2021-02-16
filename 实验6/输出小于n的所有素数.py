import math as m
x = int(input())
n = 0
if x<3:
    print("NONE")
else:
    for i in range(2,x) :
        for j in range(2,int(m.sqrt(i))+1):
            if(i%j == 0):
                break;
        else:
            print("{0:>6}".format(i),end = '')
            n = n+1
            if n%10 == 0:
                print()
