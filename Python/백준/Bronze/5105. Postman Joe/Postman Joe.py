while True:
    n, *a = input().split()
    if n == "#":
        break

    arr = [False for _ in range(21)]
    n = int(n)
    arr[n] = True
    arr[0] = True
    f = True
    for i in a:
        if i[0] == "U":
            n += int(i[1])
            if n > 20:
                f = False
                break
        elif i[0] == "D":
            n -= int(i[1])
            if n < 1:
                f = False
                break

        if arr[n]:
            f = False
            break
        arr[n] = True

    if not f:
        print("illegal")
    elif arr.count(True) == len(arr):
        print("none")
    else:
        for i in range(1, 21):
            if not arr[i]:
                print(i, end=" ")
        print()
