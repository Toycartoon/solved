n, m = map(int, input().split())
t = list(map(int, input().split()))
a = []
for i in range(n):
    s = list(map(int, input().split()))

    solved = 0
    for v in range(m):
        if s[v] == t[v]:
            solved += 1
    a.append((solved, i+1))

a.sort(key=lambda x: (-x[0], x[1]))
print(a[0][1])
