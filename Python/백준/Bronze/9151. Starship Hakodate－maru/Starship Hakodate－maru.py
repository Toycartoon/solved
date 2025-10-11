while True:
    n = int(input())
    if n == 0:
        break

    ans = 0
    i = 0
    while i ** 3 <= n:
        j = 0
        while i ** 3 + j * (j + 1) * (j + 2) // 6 <= n:
            ans = max(ans, i ** 3 + j * (j + 1) * (j + 2) // 6)
            j += 1
        i += 1
    print(ans)
