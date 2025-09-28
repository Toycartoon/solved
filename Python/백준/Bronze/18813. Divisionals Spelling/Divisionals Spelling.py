n, m = map(int, input().split())
ans = 0
for i in range(n):
    s = [*input()]
    if len(s) == len(set(s)) and ord(max(s)) <= 64 + m:
        ans += 1
print(ans)
