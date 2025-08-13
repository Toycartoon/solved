ans = float('inf')

n = int(input())
a = list(map(int, input().split()))

l = a[0]
r = sum(a)-a[0]
for i in range(1, n):
    ans = min(abs(l-r), ans)
    l += a[i]
    r -= a[i]

print(ans)
