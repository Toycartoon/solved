for t in range(int(input())):
    n = int(input())
    h = list(map(int, input().split()))

    ans = 0
    for i in range(1, n-1):
        if h[i-1] < h[i] > h[i+1]:
            ans += 1

    print(f"Case #{t+1}: {ans}")
