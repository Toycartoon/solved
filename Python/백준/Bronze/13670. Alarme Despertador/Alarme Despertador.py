while True:
    h1, m1, h2, m2 = map(int, input().split())

    if h1 == m1 == h2 == m2 == 0:
        break

    t = m2 - m1
    if t < 0:
        t += 60
        h2 -= 1

    t += (h2 - h1) * 60 if h2 - h1 >= 0 else (24 + (h2 - h1)) * 60
    print(t)
