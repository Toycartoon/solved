n, l, d = map(int, input().split())
ans = 0
a = 0
for i in range(n):
    a += l
    while ans < a:
        ans += d
    if a <= ans < a + 5:
        break
    a += 5
print(ans)
