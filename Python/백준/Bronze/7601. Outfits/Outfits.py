t = 1
while True:
    n, d = map(int, input().split())
    if n == d == 0:
        break

    bec = [i+1 for i in range(n)]
    cas = [i for i in range(n, 0, -1)]

    r = int(input())
    if r != 0:
        del bec[r-1]
    r = int(input())
    if r != 0:
        del cas[r-1]

    print(f"Scenario {t}")
    for i in range(d):
        a, b = map(int, input().split())
        if bec[a-1] == cas[b-1]:
            print(f"Day {i+1} ALERT")
        else:
            print(f"Day {i+1} OK")
    t += 1
