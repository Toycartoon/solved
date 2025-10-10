n, m = map(int, input().split())
a = []
for i in range(m):
    a.append(int(input()))
a.sort()

ans = 0
for i in a:
    if n-i < 0:
        break
    else:
        n -= i
        ans += 1
print(ans)
