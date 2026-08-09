n = int(input())
a = [True for _ in range(n+1)]

ans = 0
for i in range(int(input())):
    k = int(input())
    for v in range(k, n+1, k):
        a[v] = not a[v]
    ans = max(ans, a[1:].count(False))
print(ans)
