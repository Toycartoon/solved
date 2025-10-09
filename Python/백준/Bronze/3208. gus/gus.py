m, n = map(int, input().split())
ans = 1 if m > n else 0
ans += 2 * min(m-1, n-1)
print(ans)
