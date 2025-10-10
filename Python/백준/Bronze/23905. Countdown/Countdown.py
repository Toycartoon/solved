for t in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    ans = 0
    for i in range(k-1, n):
        if a[i] != 1:
            continue
        v = k
        for j in range(i-k+1, i+1):
            if a[j] != v:
                break
            v -= 1
        if v == 0:
            ans += 1
    print(f"Case #{t+1}: {ans}")
