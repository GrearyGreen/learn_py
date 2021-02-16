#ren min bi zhuan huan qi
t = input()
if t[0] in ['$']:
    f = eval(t[1:])
    c = f*7
    print("￥{:.2f}".format(c))
elif t[0] in ['￥']:
    c = eval(t[1:])
    f = c/7
    print("${:.2f}".format(f))
else:
    print("输入格式错误")