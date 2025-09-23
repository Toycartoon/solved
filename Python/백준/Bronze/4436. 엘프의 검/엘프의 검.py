while True:
    try:
        n = int(input())
        k = 1
        v = {*range(10)} - set(map(int, [*str(n)]))

        a = n
        while v:
            k += 1
            a = str(n * k)
            v -= set(map(int, [*a]))
        print(k)
    except EOFError:
        break
