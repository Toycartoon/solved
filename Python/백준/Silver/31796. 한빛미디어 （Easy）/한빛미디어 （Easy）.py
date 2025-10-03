n = int(input())
s = list(map(int, input().split()))
s.sort()

ans = 1
v = s[0]
for i in range(1, n):
    if v * 2 <= s[i]:
        ans += 1
        v = s[i]
print(ans)
