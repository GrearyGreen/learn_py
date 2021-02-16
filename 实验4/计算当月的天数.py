a,b = input().split()
a = eval(a)
if b in ['1','3','5','7','8','10','12'] :
    print(31)
elif b in ['4','6','9','11'] :
    print(30)
elif b == '2' :
    if a % 100 == 0 :
        if a % 400 == 0 :
            print(29)
        else :
            print(28)
    elif a % 4  == 0 :
        print(29)
    else :
        print(28)
else :
    print("Error")