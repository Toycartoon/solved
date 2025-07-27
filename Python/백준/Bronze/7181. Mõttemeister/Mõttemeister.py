n = input()
for i in range(int(input())):
    x = input()
    a, b = 0, 0
    for v in range(len(x)):
        if x[v] in n:
            a += 1
        if x[v] == n[v]:
            b += 1

    print(a, b)
