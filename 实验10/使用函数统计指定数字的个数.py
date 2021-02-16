def CountDigit(number,digit ):
    n = 0
    if number<0:
        number = abs(number)
    num = str(number)
    for i in num:
        if int(i) == digit:
            n = n+1
    return n

number,digit=input().split()
number=int(number)
digit=int(digit)
count=CountDigit(number,digit )
print("Number of digit 2 in "+str(number)+":",count)