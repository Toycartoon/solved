for t in range(int(input())):
    c, n = map(int, input().split())
    m = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for i in b:
        m[i-1] -= 1

    print(f"Data Set {t+1}:")
    print(max(m))
    print()
