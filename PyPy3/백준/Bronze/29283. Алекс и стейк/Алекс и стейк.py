n = int(input())
x = 30
ans = 0
while n > 0:
    if n >= 5:
        ans += x * 5
        x += 30
        n -= 5
    else:
        ans += x * n
        n = 0

print(ans)
