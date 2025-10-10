n, k = map(int, input().split())
ans = 0
for i in range(n):
    s = input().split()
    ans += k - len(set(s))
print(ans)
