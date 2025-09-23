n = int(input())
ans = 1
while True:
    if ans * (2 * ans ** 2 + 1) // 3 <= n:
        ans += 1
    else:
        print(ans-1)
        break
