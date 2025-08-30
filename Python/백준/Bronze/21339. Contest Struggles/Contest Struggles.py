n, k = map(int, input().split())
d, s = map(int, input().split())

v = (d * n - k * s) / (n - k)
if v > 100 or 0 > v:
    print("impossible")
else:
    print(v)
