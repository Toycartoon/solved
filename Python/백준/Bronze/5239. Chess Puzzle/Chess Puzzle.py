for t in range(int(input())):
    x = [0 for _ in range(9)]
    y = [0 for _ in range(9)]

    n, *a = map(int, input().split())
    for i in range(1, len(a)+1, 2):
        x[a[i-1]] += 1
        y[a[i]] += 1

    if max(x) > 1 or max(y) > 1:
        print("NOT SAFE")
    else:
        print("SAFE")
