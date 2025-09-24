n = int(input())
a = list(map(int, input().split()))

g = []
v = a[0]
for i in range(1, n):
    if a[i-1] > a[i]:
        g.append(a[i-1]-v)
        v = a[i]

g.append(a[-1]-v)
print(max(g))
