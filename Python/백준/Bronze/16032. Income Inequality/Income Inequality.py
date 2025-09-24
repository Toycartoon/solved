while True:
    n = int(input())
    if n == 0:
        break

    a = list(map(int, input().split()))
    s = sum(a) / n

    ans = 0
    for i in a:
        if i <= s:
            ans += 1
    print(ans)
