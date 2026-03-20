n = int(input())
a = list(map(int, input().split()))

idx = [-1 for _ in range(n)]
for i in range(n):
    idx[a[i]-1] = i

mx = 0
mn = 0
for i in range(1, n):
    v = abs(a[i]-a[i-1])
    mx = max(mx, v)

for i in range(n-1):
    v = abs(idx[i]-idx[i+1])
    mn = max(mn, v)

print(f"{mx}/1")
print(f"1/{mn}")
