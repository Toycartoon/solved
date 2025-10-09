while True:
    n = int(input())
    if n == 0:
        break

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    sa, sb = 0, 0
    for i in range(n):
        if a[i] == b[i]:
            continue

        if a[i] < b[i]:
            if b[i]-a[i] == 1:
                if a[i] == 1:
                    sa += 6
                else:
                    sa += a[i] + b[i]
            else:
                sb += b[i]
        elif a[i] > b[i]:
            if a[i] - b[i] == 1:
                if b[i] == 1:
                    sb += 6
                else:
                    sb += a[i] + b[i]
            else:
                sa += a[i]
    print(f"A has {sa} points. B has {sb} points.")
    print()
