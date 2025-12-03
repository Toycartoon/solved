n, m = map(int, input().split())
a = list(map(int, input().split()))

for j in range(m):
    l, h = map(int, input().split())
    if a[h-1] == max(a):
        continue
    a[l-1] -= 1
print(*a)
