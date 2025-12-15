for t in range(int(input())):
    n = int(input())
    ans = 0
    while n > 1:
        if n % 2:
            ans += 1
            n += 1
        n //= 2
    print(ans)
