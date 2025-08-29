n = int(input())

ans = 0
x = 1
while True:
    if x ** 2 <= n:
        ans += 1
    else:
        break
    x += 1

print(ans)
