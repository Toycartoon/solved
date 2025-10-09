n, k = map(int, input().split())
a = []
for i in range(n):
    a.append(int(input()))

a.sort()
ans = 0
for i in range(n):
    x = 1
    for j in range(i+1, n):
        if a[j] > a[i] + k:
            break
        x += 1
    ans = max(ans, x)
print(ans)
