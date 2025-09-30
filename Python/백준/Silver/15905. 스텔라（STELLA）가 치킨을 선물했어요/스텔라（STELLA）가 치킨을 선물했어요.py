a = []
for i in range(int(input())):
    s, p = map(int, input().split())
    a.append((s, p))

a.sort(key=lambda x: (-x[0], x[1]))
f = a[4][0]
ans = 0
for i in range(5, len(a)):
    if f == a[i][0]:
        ans += 1

print(ans)
