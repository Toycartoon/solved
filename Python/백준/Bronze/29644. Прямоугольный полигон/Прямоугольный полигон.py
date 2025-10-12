s, p = map(int, input().split())
ans = [-1]
for a in range(1, p // 2):
    b = (p - 2 * a) // 2
    if a >= b and a * b == s:
        ans = (a, b)
        break
print(*ans)
