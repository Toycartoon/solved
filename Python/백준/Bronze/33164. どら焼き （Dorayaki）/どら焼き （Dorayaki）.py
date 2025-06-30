n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0
for i in a:
    for j in b:
        ans += (i + j) * max(i, j)

print(ans)
