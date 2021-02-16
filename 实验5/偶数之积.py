y = input()
y = eval(y)
sum = 1
for i in range(2,y+1,2):
    sum *= i
print(sum)