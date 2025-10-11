for z in range(int(input())):
    n, k = map(int, input().split())
    q = 1
    while q < n:
        q -= 1
        q += k
    print(q-n)
