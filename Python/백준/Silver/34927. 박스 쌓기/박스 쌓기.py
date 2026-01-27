n = int(input())
w = list(map(int, input().split()))

w.sort()
ans = 1
tmp = w[0]
for i in range(1, n):
    if w[i] >= tmp:
        ans += 1
        tmp += w[i]
print(ans)
