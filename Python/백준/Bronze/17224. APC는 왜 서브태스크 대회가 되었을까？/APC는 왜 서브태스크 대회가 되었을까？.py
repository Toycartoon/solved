n, l, k = map(int, input().split())
a = []
for i in range(n):
    sub1, sub2 = map(int, input().split())
    a.append((sub1, sub2))
a.sort(key=lambda x: (x[1], x[0]))

ans = 0
for i in range(n):
    if k <= 0:
        break

    if a[i][1] <= l:
        ans += 140
        k -= 1
    elif a[i][0] <= l:
        ans += 100
        k -= 1
print(ans)
