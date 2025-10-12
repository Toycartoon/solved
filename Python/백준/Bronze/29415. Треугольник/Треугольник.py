from math import isqrt

n = int(input())
ans = 0
for i in range(1, n+1):
    for j in range(i, n+1):
        if i * j == n * 2 and isqrt((i ** 2) + (j ** 2)) ** 2 == i ** 2 + j ** 2:
            ans += 1
print(ans)
