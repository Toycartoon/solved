for t in range(int(input())):
    n, m, p = map(int, input().split())
    s = []

    for i in range(n):
        s.append(list(map(int, input().split())))

    ans = 0
    for i in range(m):
        ans += max(list(zip(*s))[i]) - s[p-1][i]

    print(f"Case #{t+1}: {ans}")
