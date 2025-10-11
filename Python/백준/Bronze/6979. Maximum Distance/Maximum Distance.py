for t in range(int(input())):
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        for j in range(i, n):
            if x[i] == y[j]:
                ans = max(ans, j-i)
    print(f"The maximum distance is {ans}")
    print()
