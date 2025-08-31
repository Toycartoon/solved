x, y, c = map(int, input().split())
dist = ((x ** 2) + (y ** 2)) ** 0.5
ans = 0
while 2 * c < dist:
    ans += 1
    dist -= c

if dist % c == 0:
    ans += dist // c
else:
    ans += 2

print(int(ans))
