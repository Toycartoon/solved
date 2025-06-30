n, m = map(int, input().split())
ans = 0
for i in range(int(input())):
    a, b = map(int, input().split())
    ans += max(a * n, b * m)

print(ans)
