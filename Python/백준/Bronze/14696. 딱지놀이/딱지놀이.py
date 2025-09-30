for t in range(int(input())):
    n, *a = map(int, input().split())
    m, *b = map(int, input().split())

    x = []
    y = []
    for i in range(4, 0, -1):
        x.append(a.count(i))
        y.append(b.count(i))

    if x > y:
        print("A")
    elif x < y:
        print("B")
    else:
        print("D")
