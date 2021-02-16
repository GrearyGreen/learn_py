x = input().split()
m = int(x[0])
n = int(x[1])
def funcation(n):
    s = 1
    for i in range(2,n+1):
        s *= i
    return s
s = int(funcation(n)/funcation(m)/funcation(n-m))
print('result = {}'.format(s))