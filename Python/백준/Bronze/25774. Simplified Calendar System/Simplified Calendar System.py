d, m, y, n = map(int, input().split())
s_dt = 360 * (y-1) + 30 * (m-1) + d

d, m, y = map(int, input().split())
dt = 360 * (y-1) + 30 * (m-1) + d

a = [0 for _ in range(7)]
for i in range(s_dt % 7, 7):
    a[i] = n
    n = (n + 1) % 7 if n != 6 else 7

for i in range(s_dt % 7):
    a[i] = n
    n = (n + 1) % 7 if n != 6 else 7

print(a[dt % 7])
