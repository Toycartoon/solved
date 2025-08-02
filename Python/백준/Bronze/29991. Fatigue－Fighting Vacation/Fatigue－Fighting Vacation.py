import sys

input = sys.stdin.readline

d, c, r = map(int, input().split())
a = []
b = []
for i in range(c):
    a.append(int(input()))

for i in range(r):
    b.append(int(input()))

ans = 0
x = 0
y = 0
while x < c:
    if d >= a[x]:
        d -= a[x]
        x += 1
        ans += 1
    else:
        if y < r:
            d += b[y]
            y += 1
            ans += 1
        else:
            break

ans += r-y
print(ans)
