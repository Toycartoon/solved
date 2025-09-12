for z in range(int(input())):
    n, m, l = map(int, input().split())
    l -= 1
    ans = 0
    for i in range(n):
        if l % m == 0:
            ans += 1
        l += 1
    print(ans)
