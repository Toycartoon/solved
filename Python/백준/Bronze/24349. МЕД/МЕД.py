n, a, b, c = map(int, input().split())
n -= 1

ans = 0
p = "r"
while n > 0:
    if p == "r":
        if a < b:
            ans += a
            p = "o"
        else:
            ans += b
            p = "i"
    elif p == "o":
        if a < c:
            ans += a
            p = "r"
        else:
            ans += c
            p = "i"
    elif p == "i":
        if b < c:
            ans += b
            p = "r"
        else:
            ans += c
            p = "o"
    n -= 1

print(ans // 100, ans % 100)
