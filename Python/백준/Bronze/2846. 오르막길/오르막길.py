n = int(input())
p = list(map(int, input().split()))

ans = []
mn = p[0]
for i in range(1, n):
    if p[i-1] >= p[i]:
        ans.append(p[i-1] - mn)
        mn = p[i]

ans.append(p[-1]-mn)
print(max(ans))
