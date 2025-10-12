for t in range(int(input())):
    m = int(input())
    p = list(map(int, input().split()))

    ans = 0
    idx = (0, 1)
    for i in range(12):
        for j in range(i+1, 12):
            if m // p[i] * (p[j] - p[i]) > ans or (m // p[i] * (p[j] - p[i]) == ans and p[idx[0]] >= p[i]):
                idx = (i, j)
                ans = m // p[i] * (p[j] - p[i])

    if ans > 0:
        print(f"Case #{t+1}: {idx[0]+1} {idx[1]+1} {ans}")
    else:
        print(f"Case #{t+1}: IMPOSSIBLE")
