while True:
    n = int(input())
    if n == 0:
        break

    v = list(map(int, input().split()))

    ans = 0
    for i in range(1, n-1):
        if v[i-1] < v[i] > v[i+1]:
            ans += 1

    print(ans)
