n, k = map(int, input().split())
ans = 0

p = 0
for i in range(n):
    a, b = map(int, input().split())
    p += a - b
    ans = max(ans, p - k)

print(ans)
