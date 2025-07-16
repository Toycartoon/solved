n, m = map(int, input().split())
ans = n + 10 * m

mx = 0
for i in range(5):
    a, b = map(int, input().split())
    mx = max(mx, a + 10 * b)

print(max(mx - ans + 1, 0))
