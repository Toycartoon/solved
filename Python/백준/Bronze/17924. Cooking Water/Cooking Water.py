l, r = -1, 1001
for i in range(int(input())):
    a, b = map(int, input().split())
    l = max(l, a)
    r = min(r, b)

if l > r:
    print("edward is right")
else:
    print("gunilla has a point")
