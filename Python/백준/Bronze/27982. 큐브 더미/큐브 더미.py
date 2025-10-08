n, m = map(int, input().split())
a = []
for _ in range(m):
    i, j, k = map(int, input().split())
    a.append((i, j, k))

ans = 0
for i, j, k in a:
    if (i+1, j, k) in a and (i-1, j, k) in a and (i, j+1, k) in a and (i, j-1, k) in a and (i, j, k+1) in a and (i, j, k-1) in a:
        ans += 1
print(ans)
