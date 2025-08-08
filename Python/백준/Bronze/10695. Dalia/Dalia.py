for t in range(int(input())):
    n, r1, c1, r2, c2 = map(int, input().split())

    pos = [(-1, 2), (-1, -2), (1, 2), (1, -2), (-2, 1), (-2, -1), (2, 1), (2, -1)]
    f = False
    for dx, dy in pos:
        if 1 <= r1 + dx <= n and 1 <= c1 + dy <= n and r1 + dx == r2 and c1 + dy == c2:
            f = True
            break

    print(f"Case {t+1}:", "YES" if f else "NO")
