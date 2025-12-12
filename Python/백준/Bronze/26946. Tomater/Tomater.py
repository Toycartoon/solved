n, d = map(int, input().split())
t = list(map(int, input().split()))

ans = 0
for i in range(1, n+1):
    f = False
    for v in t:
        if abs(i-v) <= d:
            f = True
            break

    if f:
        ans += 1
print(ans)
