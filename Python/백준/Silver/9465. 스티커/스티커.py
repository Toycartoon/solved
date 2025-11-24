for t in range(int(input())):
    n = int(input())
    a = []
    for _ in range(2):
        a.append(list(map(int, input().split())))

    dp = [[0] * n, [0] * n]
    dp[0][0] = a[0][0]
    dp[1][0] = a[1][0]
    for i in range(1, n):
        if i == 1:
            dp[0][i] = a[0][i] + dp[1][i-1]
            dp[1][i] = a[1][i] + dp[0][i-1]
        else:
            dp[0][i] = a[0][i] + max(dp[1][i-1], dp[1][i-2], dp[0][i-2])
            dp[1][i] = a[1][i] + max(dp[0][i-1], dp[1][i-2], dp[0][i-2])
    print(max(dp[0][-1], dp[1][-1]))
