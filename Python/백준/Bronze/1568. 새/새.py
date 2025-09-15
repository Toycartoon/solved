n = int(input())
ans = 0
v = 1
while n > 0:
    if n < v:
        v = 1
    ans += 1
    n -= v
    v += 1

print(ans)
