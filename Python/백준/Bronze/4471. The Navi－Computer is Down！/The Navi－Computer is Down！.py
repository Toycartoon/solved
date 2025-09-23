for t in range(int(input())):
    s = input()
    sx, sy, sz = map(float, input().split())
    e = input()
    ex, ey, ez = map(float, input().split())

    print(f"{s} to {e}: {((sx - ex) ** 2 + (sy - ey) ** 2 + (sz - ez) ** 2) ** 0.5:.02f}")
