n, m = map(int, input().split())
x, y = map(int, input().split())
k = int(input())

ans = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if x == i and y == j:
            continue
        if abs(x-i) + abs(j-y) <= k:
            ans += 1
print(ans)
