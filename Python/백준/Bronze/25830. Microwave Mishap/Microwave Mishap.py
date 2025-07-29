a, b = map(int, input().split(":"))
h, m, s = a, b, 0

m -= a
s -= b
if s < 0:
    s += 60
    m -= 1
if m < 0:
    h -= 1
    m += 60

print(f"{str(h).zfill(2)}:{str(m).zfill(2)}:{str(s).zfill(2)}")
