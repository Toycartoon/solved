while True:
    n = int(input())
    if n == 0:
        break

    a = []
    s = input()
    for i in range(n, len(s) + n, n):
        if i % (2 * n) == 0:
            a.append([*s[i-n:i]][::-1])
        else:
            a.append([*s[i-n:i]])

    for i in zip(*a):
        print(*i, sep="", end="")
    print()
