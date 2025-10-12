n = int(input())
a = list(enumerate(map(int, input().split())))

ans = [0 for _ in range(n)]
a.sort(key=lambda x: x[1])
for i in range(n):
    ans[a[i][0]] = i+1
print(*ans)
