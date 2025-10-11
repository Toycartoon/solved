h, w, n = map(int, input().split())
a = list(map(int, input().split()))

f = True
l, d = 0, 0
for i in a:
    l += i
    if l >= w:
        if l > w:
            f = False
            break
        l = 0
        d += 1
        if d == h:
            break

if d < h or not f:
    print("NO")
else:
    print("YES")
