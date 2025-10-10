for t in range(int(input())):
    m, n = map(int, input().split())
    g = [list(map(int, input().split())) for _ in range(m)]

    ans = 0
    for i in zip(*g):
        idx = i.count(1)
        for v in range(m):
            if i[v] == 1:
                ans += (m-v)-idx
                idx -= 1
    print(ans)
