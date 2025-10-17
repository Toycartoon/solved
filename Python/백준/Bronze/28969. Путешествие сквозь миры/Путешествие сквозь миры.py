l, r = map(int, input().split())
ans = 0
for i in range(1, 10):
    s = 0
    while s <= r:
        s = s * 10 + i
        if l <= s <= r:
            ans += 1
print(ans)
