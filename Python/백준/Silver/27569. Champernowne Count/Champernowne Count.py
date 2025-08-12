n, k = map(int, input().split())
a = 0
ans = 0
for i in range(1, n+1):
    a = a * (10 ** (len(str(i)))) + i
    if a % k == 0:
        ans += 1

    a %= k

print(ans)
