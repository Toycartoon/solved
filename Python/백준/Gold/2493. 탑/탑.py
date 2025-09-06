n = int(input())
a = list(map(int, input().split()))

ans = []
q = []
for i in range(n):
    f = True
    while q:
        x, idx = q.pop()
        if x >= a[i]:
            f = False
            q.append((x, idx))
            ans.append(idx)
            break

    q.append((a[i], i+1))
    if f:
        ans.append(0)

print(*ans)
