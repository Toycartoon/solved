for t in range(int(input())):
    n, *a = map(int, input().split())
    d = a[1] - a[0]
    f = True
    for i in range(1, n):
        if a[i] - a[i-1] != d:
            f = False
            break

    if f:
        print(f"The next 5 numbers after {a} are: {list(range(a[-1]+d, a[-1]+5*d + (d // abs(d)), d))}")
    else:
        print(f"The sequence {a} is not an arithmetic sequence.")
