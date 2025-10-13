n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(n):
    for j in range(i+1, n):
        v = str(a[i] * a[j])
        f = True
        for k in range(1, len(v)):
            if int(v[k-1]) + 1 != int(v[k]):
                f = False
                break
        if f:
            ans = max(ans, int(v))

if ans == 0:
    print(-1)
else:
    print(ans)
