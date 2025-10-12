n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort(reverse=True)
b.sort(reverse=True)
ans = 0
for i in range(min(n, m)):
    ans += a[i] * b[i]
print(min(n, m), ans)
