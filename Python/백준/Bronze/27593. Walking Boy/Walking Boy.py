for t in range(int(input())):
    n = int(input())
    a = [0] + list(map(int, input().split())) + [1440]

    v = 0
    for i in range(1, n+2):
        v += (a[i]-a[i-1]) // 120
    print("YES" if v >= 2 else "NO")
