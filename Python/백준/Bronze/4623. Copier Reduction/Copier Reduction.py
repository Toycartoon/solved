while True:
    a, b, c, d = map(int, input().split())
    if a == b == c == d == 0:
        break
    print(min(100, int(100 * min(max(c, d) / max(a, b), min(c, d) / min(a, b)))), "%", sep="")
