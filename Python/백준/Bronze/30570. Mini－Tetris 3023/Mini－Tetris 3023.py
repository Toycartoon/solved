a, b, c = map(int, input().split())
ans = 2 * a
if b > 0 and c >= 2:
    c -= 2
    ans += 3 * b - (b-1) + 2
if c > 0:
    ans += 3 * (c // 2)
print(ans)
