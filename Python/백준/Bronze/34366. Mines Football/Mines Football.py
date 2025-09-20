mx = -1
mn = 1001
tmx = -1
tmn = 10 ** 9
for i in range(int(input())):
    s, *a = map(int, input().split())
    mx = max(mx, max(a))
    mn = min(mn, min(a))
    tmx = max(tmx, sum(a))
    tmn = min(tmn, sum(a))

print(mx)
print(mn)
print(tmx)
print(tmn)
