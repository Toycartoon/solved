n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

ans = 0
for i in range(n-1, 0, -1):
    for j in range(i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            ans += 1
print(ans)
