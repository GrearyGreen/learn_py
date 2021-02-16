def function1(n):
    for i in range(n):
        print('{}{}'.format('+ ',4*'- '),end='')
    if n>0:
        print('+')
def function2(n):
    for i in range(n):
        print('{:<10}'.format('|'),end='')
    if n>0:
        print('|')
n = int(input())
for i in range(n):
    function1(n)
    for j in range(4):
        function2(n)
function1(n)