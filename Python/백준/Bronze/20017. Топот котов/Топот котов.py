n, m, a = map(int, input().split())
b = list(map(int, input().split()))

ans = 0
for i in range(m * (n-1)):
    if 2 * b[i] < b[i+m]:
        ans += a

print(ans)
