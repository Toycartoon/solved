n = int(input())

print(n - 1 + n ** 2)
ans = []
for i in range(-1, -n-1, -1):
    ans.append(i)

ans.append(0)
for i in range(n, 0, -1):
    ans.append(i)

print(*ans)
