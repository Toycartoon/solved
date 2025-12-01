n, k = map(int, input().split())
a = list(map(int, input().split()))

f = True
mx = a[0]
for i in range(1, n):
    if mx-a[i] > k:
        f = False
        break
    mx = max(a[i], mx)

if f:
    print("YES")
else:
    print("NO")
