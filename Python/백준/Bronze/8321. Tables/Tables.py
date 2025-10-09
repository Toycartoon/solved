n, k, s = map(int, input().split())
a = list(map(int, input().split()))

v = k * s
a.sort(reverse=True)
for i in range(n):
    v -= a[i]
    if v <= 0:
        print(i+1)
        break
