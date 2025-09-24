n, m = map(int, input().split())
a = [i for i in range(1, n+1)]
for i in range(m):
    x, y = map(int, input().split())
    a[x-1] = y

for i in a:
    print(i)
