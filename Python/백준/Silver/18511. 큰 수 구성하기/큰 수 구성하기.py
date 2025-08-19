from itertools import product as prod

n, k = map(int, input().split())
a = list(input().split())

ans = 0
for v in range(1, 10):
    for i in prod(a, repeat=v):
        if int("".join(i)) <= n:
            ans = max(ans, int("".join(i)))

print(ans)
