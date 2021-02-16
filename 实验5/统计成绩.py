sum = 0
count = 0
n = 0
while 1 :
    x = eval(input())
    if x<0 :
        break
    count = count + 1
    sum = sum + x
    if x<60 :
        n = n+1
if count == 0 :
    print("没有学生")
else :
    evage = sum / count
    print("平均分={:.2f},不及格人数={}".format(evage,n))
    