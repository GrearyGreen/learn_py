import math
n=eval(input())
if n<0:
    s=abs(n+1)
elif 0<=n<=5:
    s=2*n+1
else:
    s=math.sin(n)+5
print(f"x={n:.2f},y={s:.2f}")