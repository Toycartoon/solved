while True:
    n = int(input())
    if n == 0:
        break

    a = [input() for _ in range(n)]
    idx = 0
    x = 0
    while idx < n:
        try:
            if a[idx][x] == " ":
                idx += 1
                continue
            x += 1
        except IndexError:
            idx += 1
            continue
    print(x+1)
