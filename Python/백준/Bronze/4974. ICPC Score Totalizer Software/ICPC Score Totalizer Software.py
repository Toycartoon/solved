while True:
    n = int(input())
    if n == 0:
        break

    a = []
    for i in range(n):
        a.append(int(input()))
    a.sort()
    print(sum(a[1:-1]) // (n-2))
