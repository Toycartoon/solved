r, g, b = map(int, input().split())
cr, cg, cb = map(int, input().split())
crg, cgb = map(int, input().split())

r = max(0, r-cr)
g = max(0, g-cg)
b = max(0, b-cb)

if r > crg or b > cgb:
    print(-1)
    exit()

ans = r + b
crg -= r
cgb -= b
if g > (crg+cgb):
    print(-1)
    exit()

ans += g
print(ans)
