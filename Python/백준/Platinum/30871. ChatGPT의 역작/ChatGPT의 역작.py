# Opened Editorial, Thanks to: ohwphil

def f(x, l, r):
    v = x
    for i in range(n):
        if l[i] <= x <= r[i]:
            v = v^((x | l[i]) + (x & r[i]) * (l[i] ^ r[i])) % (2 ** 64)
    return v >= 0x123456789ABCDEF

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

l, r = 0, 10 ** 18 + 1
while l + 1 < r:
    mid = (l + r) // 2

    if f(mid, a, b):
        r = mid
    else:
        l = mid

print(l)
