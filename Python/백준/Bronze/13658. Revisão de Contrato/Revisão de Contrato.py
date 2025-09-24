while True:
    d, n = input().split()
    if d == n == "0":
        break

    s = n.replace(d, "")
    if len(s) == 0:
        print(0)
    else:
        print(int(s))
