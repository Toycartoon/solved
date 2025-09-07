p = list(map(int, input().split()))
c1, c2, c3 = map(int, input().split())

s = sum(p)
if c2 < c3:
    c2, c3 = c3, c2

a = sum(p) - (sum(p) * (c1 * 0.01))
p.sort(reverse=True)
p[0] -= p[0] * (c2 * 0.01)
p[1] -= p[1] * (c3 * 0.01)
b = sum(p)

if a < b:
    print(f"one {s - a:.02f}")
else:
    print(f"two {s - b:.02f}")
