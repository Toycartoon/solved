n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(int(input()))

v = [0 for _ in range(n)]
for i in range(m):
    x = int(input())
    for k in range(n):
        if a[k] <= x:
            v[k] += 1
            break

print(v.index(max(v))+1)
