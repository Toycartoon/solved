while True:
    a, *l = map(int, input().split())

    if a == 0:
        break

    ans = l[0]
    for i in range(1, len(l)):
        if i % 2 == 1:
            ans -= l[i]
        else:
            ans *= l[i]
    print(ans)
