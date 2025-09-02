while True:
    a = list(map(int, input().split()))
    if a[0] == -1:
        break

    ans = 0
    for i in range(len(a)-1):
        if a[i] * 2 in a:
            ans += 1

    print(ans)
