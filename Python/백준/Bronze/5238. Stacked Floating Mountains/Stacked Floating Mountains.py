for t in range(int(input())):
    n, *a = map(int, input().split())
    f = True
    for i in range(2, n):
        if a[i-2] + a[i-1] != a[i]:
            f = False
            break

    print("YES" if f else "NO")
