a = []
for i in range(16):
    r, g, b = map(int, input().split())
    a.append((r, g, b))

while True:
    try:
        r, g, b = map(int, input().split())
    
        dist = float('inf')
        ans = ()
        for dr, dg, db in a:
            d = ((r-dr) ** 2 + (g-dg) ** 2 + (b-db) ** 2) ** 0.5
            if dist > d:
                dist = d
                ans = (dr, dg, db)
        print(f"{str(r).rjust(3)} {str(g).rjust(3)} {str(b).rjust(3)} maps to {str(ans[0]).rjust(3)} {str(ans[1]).rjust(3)} {str(ans[2]).rjust(3)}")
    except EOFError:
        break
