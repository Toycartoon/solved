n = int(input())
s = list(map(int, input().split()))

fruit = [0 for _ in range(10)]
l = 0
ans = 0
for r in range(len(s)):
    fruit[s[r]] += 1
    while fruit.count(0) < 8:
        fruit[s[l]] -= 1
        l += 1
    ans = max(ans, r-l+1)
print(ans)
