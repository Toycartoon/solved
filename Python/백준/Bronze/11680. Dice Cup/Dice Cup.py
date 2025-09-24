n, m = map(int, input().split())
a = [0 for _ in range(n+m+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        a[i+j] += 1

mx = max(a)
for i in range(n+m):
    if a[i] == mx:
        print(i)
