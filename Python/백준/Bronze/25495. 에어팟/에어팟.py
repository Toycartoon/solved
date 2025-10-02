n = int(input())
a = list(map(int, input().split()))

v = 2
p = 2
for i in range(1, n):
    if a[i-1] == a[i]:
        p *= 2
        v += p
    else:
        v += 2
        p = 2

    if v >= 100:
        v = 0
        p = 1
print(v)
