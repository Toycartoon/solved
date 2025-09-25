for t in range(int(input())):
    a = list(map(int, input().split()))[:-1]
    ans = 0
    for i in range(1, len(a)):
        if a[i-1] * 2 < a[i]:
            ans += a[i] - (a[i-1] * 2)
    print(ans)
