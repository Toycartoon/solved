n, k = map(int, input().split())
a = list(map(int, input().split()))
for i in range(1, n):
    a[i] = max(a[i-1] + k, a[i])
print(*a)
