for t in range(int(input())):
    project, paper, midterm = map(int, input().split())
    f = False
    for i in range(101):
        if project * 0.15 + paper * 0.2 + midterm * 0.25 + i * 0.4 >= 90:
            print(i)
            f = True
            break

    if not f:
        print("impossible")
