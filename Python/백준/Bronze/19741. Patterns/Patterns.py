n, k = map(int, input().split())
for i in range(1, n ** 2 + 1):
    v = 0
    for j in range(1, i+1):
        if i % j == 0:
            v += 1

    if v <= k:
        print("*", end="")
    else:
        print(".", end="")

    if i % n == 0:
        print()
