n, m = map(int, input().split())
w = {}
for i in range(n):
    k = int(input())
    a = list(map(int, input().split()))

    for v in a:
        if v in w:
            w[v] += 1
        else:
            w[v] = 1

ans = 0
for i in w:
    if w[i] >= m:
        ans += 1

print(ans)
