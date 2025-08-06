t = 1
while True:
    n = int(input())
    if n == 0:
        break

    a = [list(map(int, input().split())) for _ in range(n)]
    ans = a[0][0] + (sum(a[-1]) if n != 1 else 0)
    for i in range(1, n-1):
        ans += a[i][0] + a[i][-1]

    print(f"Case #{t}:{ans}")
    t += 1
