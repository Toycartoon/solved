while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break

    v = []
    for i in range(n):
        a, b = map(int, input().split())
        if m < a:
            continue
        v.append((b / a, a, b))
    v.sort(key=lambda x: (x[0], -x[1]))
    if len(v) == 0:
        print("No suitable tickets offered")
    else:
        print(f"Buy {v[0][1]} tickets for ${v[0][2]}")
