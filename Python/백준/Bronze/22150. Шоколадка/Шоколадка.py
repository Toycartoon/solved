for t in range(int(input())):
    n, *a = map(int, input().split())
    f = True
    for i in range(0, len(a), 2):
        if a[i] + a[i+1] != n:
            f = False
            break

    if f:
        print("no")
    else:
        print("yes")
