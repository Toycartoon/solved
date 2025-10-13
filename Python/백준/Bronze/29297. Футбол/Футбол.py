for t in range(int(input())):
    a, b = map(int, input().split(":"))

    lag, dcu = 0, 0
    for i in range(10):
        for j in range(10):
            if a + i > b + j:
                lag += 1
            elif a + i < b + j:
                dcu += 1
            else:
                if i < b:
                    dcu += 1
                elif i > b:
                    lag += 1
    print(lag, dcu)
