n, q = map(int, input().split())
a = []
for i in range(n):
    a.append(int(input()))

for i in range(q):
    l, r = map(int, input().split())
    print(sum(a[l-1:r]))
