n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
g = zip(*g)

ans = 0
for i in g:
    ans += max(i)
print(ans)
