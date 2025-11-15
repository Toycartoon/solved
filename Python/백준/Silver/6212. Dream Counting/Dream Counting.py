m, n = map(int, input().split())
a = [0 for _ in range(10)]

for i in range(m, n+1):
    for v in str(i):
        a[int(v)] += 1
print(*a)
