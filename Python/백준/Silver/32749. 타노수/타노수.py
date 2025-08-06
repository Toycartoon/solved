n, t = map(int, input().split())
s = input()

ans = 0
v = 2 ** (n - t)
for i in range(v, len(s)+1, v):
    ans = max(ans, int(s[i-v:i]))

print(ans)
