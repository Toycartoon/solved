from math import trunc

for t in range(int(input())):
    c, p = map(int, input().split())
    w = {}
    for i in range(c):
        n, s, m, l = input().split()
        w[n] = {"small": int(s), "medium": int(m), "large": int(l)}

    for i in range(p):
        name, size, coffee = input().split()
        cost = w[coffee][size] + trunc(100 / p)
        if cost % 5 == 1:
            cost -= 1
        elif cost % 5 == 4:
            cost += 1

        print(name, cost)
