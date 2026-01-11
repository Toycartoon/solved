n, m = map(int, input().split())

p, q = [], []
for _ in range(n):
    x, y = map(int, input().split())
    p.append((x, y))

for _ in range(m):
    x, y = map(int, input().split())
    q.append((x, y))

ans = 0
for qx, qy in q:
    r = 0
    for px, py in p:
        r = max(r, (px-qx) ** 2 + (py-qy) ** 2)
    ans = max(r, ans)
print(ans)
