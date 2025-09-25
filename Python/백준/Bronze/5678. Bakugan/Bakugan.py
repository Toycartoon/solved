while True:
    r = int(input())
    if r == 0:
        break

    m = list(map(int, input().split()))
    l = list(map(int, input().split()))

    mark, leti = sum(m), sum(l)
    for i in range(2, r):
        if m[i-2] == m[i-1] == m[i]:
            if not l[i-2] == l[i-1] == l[i]:
                mark += 30
            break
        elif l[i-2] == l[i-1] == l[i]:
            if not m[i-2] == m[i-1] == m[i]:
                leti += 30
            break

    if mark > leti:
        print("M")
    elif mark < leti:
        print("L")
    else:
        print("T")
