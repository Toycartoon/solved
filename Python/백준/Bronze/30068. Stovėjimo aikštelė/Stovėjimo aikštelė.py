w = {}
for i in range(int(input())):
    t, n = map(int, input().split())

    if n in w:
        print(n, t-w[n])
    else:
        w[n] = t
