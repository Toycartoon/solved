n, m = map(int, input().split())
ans = 0
t = 0
for i in range(m):
    c, v = input().split()
    if c == "leave":
        t -= int(v)
    elif c == "enter":
        if t + int(v) > n:
            ans += 1
        else:
            t += int(v)
print(ans)
