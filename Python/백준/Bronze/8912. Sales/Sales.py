for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    for i in range(1, n):
        for j in range(i):
            if a[j] <= a[i]:
                ans += 1
    print(ans)
