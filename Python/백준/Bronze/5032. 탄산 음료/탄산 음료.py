e, f, c = map(int, input().split())
ans = (e + f) // c
x = (e + f) % c + ans
while x >= c:
    ans += x // c
    x = x % c + (x // c)

print(ans)
