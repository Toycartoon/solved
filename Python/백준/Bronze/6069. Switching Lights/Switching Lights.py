n, m = map(int, input().split())
a = [False for _ in range(n)]
for _ in range(m):
    com, l, r = map(int, input().split())
    if com == 0:
        for i in range(l-1, r):
            a[i] = not a[i]
    elif com == 1:
        ans = 0
        for i in range(l-1, r):
            if a[i]:
                ans += 1
        print(ans)
