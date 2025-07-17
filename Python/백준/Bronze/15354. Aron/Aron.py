n = int(input())
a = []

for i in range(n):
    a.append(input())

ans = n+1
for i in range(1, n):
    if a[i-1] == a[i]:
        ans -= 1

print(ans)
