n = int(input())
a = list(map(int, input().split()))

e, p = 0, 0
for i in range(1, n):
    v = a[i-1] - a[i]
    if v < 0:
        p += -v
    elif v > 0:
        e += v

print(e, p)
