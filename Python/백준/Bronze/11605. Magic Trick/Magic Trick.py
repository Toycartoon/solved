a = []
for i in range(int(input())):
    a.append(input().split())

ans = 0
for i in range(1, 101):
    n = i
    for c, x in a:
        if c == "ADD":
            n += int(x)
        elif c == "SUBTRACT":
            n -= int(x)
            if n < 0:
                ans += 1
                break
        elif c == "MULTIPLY":
            n *= int(x)
        elif c == "DIVIDE":
            if n % int(x) != 0:
                ans += 1
                break
            n //= int(x)
print(ans)
