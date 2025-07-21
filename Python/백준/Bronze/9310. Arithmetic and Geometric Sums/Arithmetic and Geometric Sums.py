while True:
    n = int(input())
    if n == 0:
        break

    a1, a2, a3 = map(int, input().split())
    if a3-a2 == a2-a1:
        print(n * (2 * a1 + (n - 1) * (a3-a2)) // 2)
    elif a3 // a2 == a2 // a1:
        print(a1 * ((a3 // a2) ** n - 1) // (a3 // a2 - 1))
