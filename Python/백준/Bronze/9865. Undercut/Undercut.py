for t in range(int(input())):
    n = int(input())
    v = []
    while len(v) < n * 2:
        v.extend(list(map(int, input().split())))
    sa, sb = 0, 0
    for i in range(0, n * 2, 2):
        if v[i] == v[i+1]:
            continue

        if v[i] < v[i+1]:
            if v[i+1]-v[i] == 1:
                if v[i] == 1:
                    sa += 6
                else:
                    sa += v[i] + v[i+1]
            else:
                sb += v[i+1]
        elif v[i] > v[i+1]:
            if v[i] - v[i+1] == 1:
                if v[i+1] == 1:
                    sb += 6
                else:
                    sb += v[i] + v[i+1]
            else:
                sa += v[i]
    print(f"Game {t+1}: Tessa {sa} Danny {sb}")
