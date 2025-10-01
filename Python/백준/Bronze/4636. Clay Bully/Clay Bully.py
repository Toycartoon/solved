while True:
    n = int(input())
    if n == -1:
        break

    a = []
    for i in range(n):
        x, y, z, s = input().split()
        a.append((int(x) * int(y) * int(z), s))
    print(f"{max(a)[1]} took clay from {min(a)[1]}.")
