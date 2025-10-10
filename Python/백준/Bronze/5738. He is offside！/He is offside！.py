while True:
    a, d = map(int, input().split())
    if a == d == 0:
        break

    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    c.sort()

    if min(b) < c[1]:
        print("Y")
    else:
        print("N")
