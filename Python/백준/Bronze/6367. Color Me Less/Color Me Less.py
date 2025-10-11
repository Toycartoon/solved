a = []
for i in range(16):
    r, g, b = map(int, input().split())
    a.append((r, g, b))

while True:
    r, g, b = map(int, input().split())
    if r == g == b == -1:
        break

    dist = float('inf')
    ans = ()
    for dr, dg, db in a:
        d = ((r-dr) ** 2 + (g-dg) ** 2 + (b-db) ** 2) ** 0.5
        if dist > d:
            dist = d
            ans = (dr, dg, db)
    print(f"({r},{g},{b}) maps to ({ans[0]},{ans[1]},{ans[2]})")
