from math import factorial as f

n = int(input())
ans = 0
for i in range(n+1):
    ans += 1 / f(i)

print(ans)
