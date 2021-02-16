s = input()
x = 'Dang'
shi = int(s[:2])
fen = int(s[3:])
if 0 <= shi < 12 :
    print("Only {:0>2}:{:0>2}.  Too early to Dang.".format(shi,fen))
elif shi == 12 and fen == 0 :
    print("Only {:0>2}:{:0>2}.  Too early to Dang.".format(shi,fen))
else :
    if fen == 0 :
        print(x*(shi - 12))
    else :
        print(x*(shi - 11))