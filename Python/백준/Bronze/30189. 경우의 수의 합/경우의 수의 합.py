n, m = map(int, input().split())
ans = 0
for a in range(n+1):
    for b in range(m+1):
        for c in range(n+m+1):
            if a + b == c:
                ans += 1
print(ans)
