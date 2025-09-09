r, s, n = map(int, input().split())
a = list(map(int, input().split()))
v = 0
for k in range(n):
    if v % s == r % s:
        print(k)
        exit()
    v += a[k]

if v % s == r % s:
    print(n)
else:
    print(-1)
