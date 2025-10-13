k, n = map(int, input().split())
a = []
for i in range(k):
    a.append(list(map(int, input().split())))

ans = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            continue
        f = True
        for l in a:
            if l.index(i) > l.index(j):
                f = False
                break
        if f:
            ans += 1
print(ans)
