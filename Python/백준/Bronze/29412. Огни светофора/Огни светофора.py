a = list(map(int, input().split()))
t = int(input())

r, y, g = 0, 0, 0
idx = 0
while t > 0:
    if idx == 0:
        g += min(t, a[idx])
    elif idx == 1:
        g += min(t, a[idx]) // 2
    elif idx == 2:
        y += min(t, a[idx])
    elif idx == 3:
        r += min(t, a[idx])
    elif idx == 4:
        r += min(t, a[idx])
        y += min(t, a[idx])
    t -= a[idx]
    idx = (idx + 1) % 5

print(r, y, g)
