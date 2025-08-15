a, b, n = map(int, input().split())
ans = []
s = b + a * n
for i in range(n, 0, -1):
    ans.append(s)
    s += b

print(*sorted(ans))
