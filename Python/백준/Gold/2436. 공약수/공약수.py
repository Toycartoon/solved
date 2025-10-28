from math import lcm

a, b = map(int, input().split())
v = b // a

s = float('inf')
ans = (-1, -1)
for i in range(1, v + 1):
    if v % i == 0:
        if s > (v // i * a) + (i * a) and lcm(v // i * a, i * a) == b:
            s = (v // i * a) + (i * a)
            ans = (i * a, v // i * a)
print(*ans)
