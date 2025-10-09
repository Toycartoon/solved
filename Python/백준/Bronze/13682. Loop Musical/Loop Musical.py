while True:
    n = int(input())
    if n == 0:
        break

    a = list(map(int, input().split()))
    a *= 2

    ans = 0
    for i in range(n):
        if a[i-1] < a[i] > a[i+1] or a[i-1] > a[i] < a[i+1]:
            ans += 1
    print(ans)
