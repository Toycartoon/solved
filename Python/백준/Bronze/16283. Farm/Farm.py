a, b, n, w = map(int, input().split())
s, g = 0, 0
for i in range(1, n):
    if i * a + (n-i) * b == w:
        if s == g == 0:
            s, g = i, n-i
        else:
            s, g = -1, -1

if s <= 0:
    print(-1)
else:
    print(s, g)
