n, m = map(int, input().split())
a = list(map(int, input().split()))

s = sum(a)
if s < m:
    print(-1)
    exit()

for i in range(n):
    s -= a[i]
    if s < m:
        print(i+1)
        break
