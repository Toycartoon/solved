for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    for i in range(n-1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                ans += 1
    print(f"Optimal train swapping takes {ans} swaps.")
