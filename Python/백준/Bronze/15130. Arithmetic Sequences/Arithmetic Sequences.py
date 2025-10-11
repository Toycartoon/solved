a = list(map(int, input().split()))
l, r = -1, -1
for i in range(10):
    if a[i] != 0:
        if l == -1:
            l = i
        else:
            r = i
            break

if (a[r] - a[l]) % (r - l) != 0:
    print(-1)
else:
    d = (a[r] - a[l]) // (r - l)
    for i in range(10):
        a[i] = a[l] + (i - l) * d
    print(*a)
