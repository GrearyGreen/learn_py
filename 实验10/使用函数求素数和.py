def prime(p):
    if p == 1:
        return False
    if p == 2:
        return True
    else:
        for i in range(2,p):
            if p%i == 0:
                return False
        return True
def PrimeSum(m,n):
    sum = 0
    for i in range(m,n):
        if prime(i):
            sum = sum + i
            #print(sum)
    return sum

m,n=input().split()
m=int(m)
n=int(n)
print(PrimeSum(m,n))